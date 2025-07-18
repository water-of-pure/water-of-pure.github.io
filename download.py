import requests
from bs4 import BeautifulSoup
import markdownify
from datetime import datetime
import argparse
import re
from zoneinfo import ZoneInfo
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

class WebPageAnalyzer:
    """网页内容分析器，用于获取和处理网页内容"""
    
    def __init__(self, url: str, config: Optional[Dict[str, Any]] = None):
        """
        初始化网页分析器
        
        Args:
            url: 目标网页的URL
            config: 配置选项字典
        """
        self.url = url
        self.soup = None
        self.config = config or {}
        self.logger = logging.getLogger("WebPageAnalyzer")
        
        # 设置默认配置
        self.default_config = {
            'target_class': 'entry-content',
            'output_dir': './content/post',
            'preserve_code_language': True,
            'add_front_matter': True,
            'remove_hidden': True,
            'remove_copyright': True,
            'encoding': 'utf-8',
            'max_replacements': 100,
            'timeout': 10,
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        }
        
        # 合并用户配置和默认配置
        self.config = {**self.default_config, **self.config}
    
    def fetch_page(self) -> bool:
        """获取网页内容并解析"""
        try:
            self.logger.info(f"正在请求URL: {self.url}")
            response = requests.get(
                self.url, 
                headers=self.config['headers'],
                timeout=self.config['timeout']
            )
            response.raise_for_status()  # 检查请求是否成功
            
            self.logger.info(f"成功获取网页内容，状态码: {response.status_code}")
            self.soup = BeautifulSoup(response.text, 'html.parser')
            return True
        except requests.exceptions.RequestException as e:
            self.logger.error(f"请求错误: {e}")
            return False
        except Exception as e:
            self.logger.error(f"发生未知错误: {e}")
            return False
    
    def get_title(self) -> str:
        """获取页面标题"""
        if self.soup:
            title = self.soup.title
            return title.text.strip() if title else "无标题"
        return "页面未加载"
    
    def count_elements(self, tag_name: str) -> int:
        """计算指定标签的元素数量"""
        if self.soup:
            return len(self.soup.find_all(tag_name))
        return 0
    
    def find_links(self) -> List[Tuple[str, str]]:
        """查找所有链接"""
        links = []
        if self.soup:
            for link in self.soup.find_all('a'):
                href = link.get('href')
                text = link.get_text(strip=True)
                links.append((href, text))
        return links
    
    def get_meta_tags(self) -> List[Dict[str, str]]:
        """获取所有meta标签"""
        meta_tags = []
        if self.soup:
            for meta in self.soup.find_all('meta'):
                meta_tags.append(meta.attrs)
        return meta_tags
    
    def _remove_elements_by_condition(self, element, condition_func):
        """
        递归移除符合条件的子元素
        
        Args:
            element: BeautifulSoup元素对象
            condition_func: 判断元素是否应该被移除的函数
        """
        from bs4 import Tag
        
        if isinstance(element, Tag):
            # 复制子元素列表，避免在迭代时修改
            for child in list(element.children):
                if isinstance(child, Tag) and condition_func(child):
                    child.decompose()
                else:
                    self._remove_elements_by_condition(child, condition_func)
        
        return element
    
    def remove_hidden_elements(self, element):
        """递归移除元素中带有 style='display:none' 的子元素
        
        Args:
            element: BeautifulSoup元素对象
        """
        def is_hidden(el):
            return el.has_attr('style') and 'display:none' in el.get('style', '').lower().replace(' ', '')
        
        return self._remove_elements_by_condition(element, is_hidden)
    
    def remove_copyright_elements(self, element):
        """移除元素中 class 为 entry-copyright 的子元素
        
        Args:
            element: BeautifulSoup元素对象
        """
        def is_copyright(el):
            return el.has_attr('class') and 'entry-copyright' in el.get('class', [])
        
        return self._remove_elements_by_condition(element, is_copyright)
    
    def find_elements_by_class(self, class_name: str) -> List[Any]:
        """查找具有指定类的所有元素
        
        Args:
            class_name: 要查找的类名
        """
        elements = []
        if self.soup:
            elements = self.soup.find_all(class_=class_name)
            
            # 移除隐藏元素
            if self.config['remove_hidden'] and elements:
                elements = [self.remove_hidden_elements(el) for el in elements if el]
            
            # 移除版权元素
            if self.config['remove_copyright'] and elements:
                elements = [self.remove_copyright_elements(el) for el in elements if el]
        
        return elements
    
    def count_elements_by_class(self, class_name: str) -> int:
        """计算具有指定类的元素数量"""
        return len(self.find_elements_by_class(class_name))
    
    def get_class_elements_info(self, class_name: str) -> List[Dict[str, Any]]:
        """获取具有指定类的元素的信息"""
        elements_info = []
        for element in self.find_elements_by_class(class_name):
            if element:
                tag_name = element.name
                text = element.get_text(strip=True)
                attrs = dict(element.attrs)
                elements_info.append({
                    'tag': tag_name,
                    'text': text,
                    'attributes': attrs
                })
        return elements_info
    
    def extract_code_language(self, element) -> str:
        """从代码块元素及其子元素中提取语言信息
        
        Args:
            element: BeautifulSoup元素对象
        """
        # 常见的代码语言列表
        common_languages = [
            'bash', 'objectivec', 'python', 'java', 
            'javascript', 'html', 'css', 'php', 'sql', 
            'json', 'c', 'cpp', 'csharp', 'go', 'rust', 
            'swift', 'kotlin', 'ruby', 'perl', 'dart', 
            'scala', 'typescript'
        ]
        
        # 尝试从元素自身的class属性中提取语言
        if element.has_attr('class'):
            classes = element.get('class')
            for cls in classes:
                # 常见的代码语言标记前缀
                if cls.startswith(('language-', 'lang-')):
                    return cls.split('-', 1)[1]
                    
                # 直接匹配常见语言名称
                if cls.lower() in common_languages:
                    return cls.lower()
        
        # 尝试从data-language属性中提取
        if element.has_attr('data-language'):
            return element.get('data-language')
            
        # 尝试从父元素的class中提取
        parent = element.parent
        if parent and parent.has_attr('class'):
            classes = parent.get('class')
            for cls in classes:
                if cls.startswith(('language-', 'lang-')):
                    return cls.split('-', 1)[1]
        
        # 特别处理 <pre><code class="language-*">...</code></pre> 结构
        if element.name == 'pre':
            code_elements = element.find_all('code', recursive=False)
            for code in code_elements:
                if code.has_attr('class'):
                    classes = code.get('class')
                    for cls in classes:
                        if cls.startswith(('language-', 'lang-')):
                            return cls.split('-', 1)[1]
                            
                        if cls.lower() in common_languages:
                            return cls.lower()
                            
                # 尝试data-language属性
                if code.has_attr('data-language'):
                    return code.get('data-language')
        
        return "bash"  # 默认返回bash
    
    def html_to_markdown(self, html_content: Optional[str] = None) -> Optional[str]:
        """将HTML内容转换为Markdown格式
        
        Args:
            html_content: 可选的HTML内容，如果未提供则使用当前页面内容
        """
        if html_content is None:
            if self.soup is None:
                self.logger.error("错误：没有可用的HTML内容，请先调用fetch_page()或提供html_content参数")
                return None
            html_content = str(self.soup)
        
        try:
            # 设置代码语言提取回调函数
            if self.config['preserve_code_language']:
                markdown = markdownify.markdownify(
                    html_content, 
                    heading_style="ATX",
                    code_language_callback=self.extract_code_language
                )
            else:
                markdown = markdownify.markdownify(html_content, heading_style="ATX")
                
            return markdown
        except Exception as e:
            self.logger.error(f"HTML转Markdown失败: {e}")
            return None

    def get_element_markdown(self, element) -> Optional[str]:
        """将单个元素转换为Markdown格式"""
        try:
            # 设置代码语言提取回调函数
            if self.config['preserve_code_language']:
                return markdownify.markdownify(
                    str(element), 
                    heading_style="ATX",
                    code_language_callback=self.extract_code_language
                )
            else:
                return markdownify.markdownify(str(element), heading_style="ATX")
        except Exception as e:
            self.logger.error(f"元素转Markdown失败: {e}")
            return None

    def replace_keywords(self, text: str, replacements: Optional[Dict[str, str]] = None) -> str:
        """替换文本中的指定关键词
        
        Args:
            text: 要处理的文本
            replacements: 替换规则字典，默认为常见技术术语的规范化
        """
        if replacements is None:
            replacements = {
                'ios': 'iOS',
                'php': 'PHP',
                'html': 'HTML',
                'css': 'CSS',
                'javascript': 'JavaScript',
                'IOS': 'iOS',
                'sql': 'SQL',
                'mysql': 'MySQL',
                'mongodb': 'MongoDB',
                'yii': 'Yii'
            }
            
        # 限制替换的关键词数量
        if len(replacements) > self.config['max_replacements']:
            self.logger.warning(f"警告: 替换规则数量超过最大限制({self.config['max_replacements']})，只使用前{self.config['max_replacements']}个")
            replacements = {k: replacements[k] for k in list(replacements)[:self.config['max_replacements']]}
            
        # 使用正则表达式进行关键词替换
        pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in replacements.keys()) + r')\b', re.IGNORECASE)
        
        def replace(match):
            key = match.group(0)
            return replacements.get(key.lower(), key)
            
        res = pattern.sub(replace, text)

        # 定义要移除的后缀列表
        suffixes_to_remove = [
            " - 随笔 - Walkerfree",
            " - Walkerfree",
            " | Walkerfree",
            # 可以添加更多后缀...
        ]
        
        # 移除指定的后缀
        for suffix in suffixes_to_remove:
            if res.endswith(suffix):
                res = res[:-len(suffix)]

        return res

    def replace_empty_keywords(self, text: str, replacements: Optional[Dict[str, str]] = None) -> str:
        """替换文本中的指定字符
        
        Args:
            text: 要处理的文本
            replacements: 替换规则字典
        """
        if replacements is None:
            replacements = {
                ': ': '-',
                ':': '-',
                '、': '-',
                '）': '-',
                '（': '-',
                ')': '-',
                '(': '-',
                '，': '-',
                ',': '-',
                '&quot;': '-',
                '“': '-',
                '”': '-',
                ' ': '-',
                '/': '-',
                '#': '井'
            }
            
        # 限制替换的规则数量
        if len(replacements) > self.config['max_replacements']:
            self.logger.warning(f"警告: 替换规则数量超过最大限制({self.config['max_replacements']})，只使用前{self.config['max_replacements']}个")
            replacements = {k: replacements[k] for k in list(replacements)[:self.config['max_replacements']]}
        
        # 先处理空格，将连续空格合并为单个连字符
        if ' ' in replacements:
            text = text.replace(' ', replacements[' '])
            # 合并连续的连字符
            while replacements[' '] * 2 in text:
                text = text.replace(replacements[' '] * 2, replacements[' '])
        
        # 处理其他替换规则
        for old_char, new_char in replacements.items():
            if old_char != ' ':  # 跳过已处理的空格
                text = text.replace(old_char, new_char)
        
        return text

    def clean_title(self, title: str) -> str:
        """清理标题，移除末尾的连字符和多余空格
        
        Args:
            title: 原始标题字符串
        """
        # 移除末尾的所有连字符和空格
        cleaned_title = title.rstrip('- ').lstrip()
        
        # 如果标题为空，返回默认值
        return cleaned_title if cleaned_title else "未命名文章"

    def generate_front_matter(self, title: str, categories: Optional[List[str]] = None, 
                              tags: Optional[List[str]] = None) -> str:
        """生成Markdown文件的前置元数据
        
        Args:
            title: 文章标题
            categories: 文章分类列表
            tags: 文章标签列表
        """
        if categories is None:
            categories = ["技术"]
        if tags is None:
            tags = ["PHP"]
            
        # 获取当前时间并设置时区为东八区
        current_time = datetime.now(ZoneInfo('Asia/Shanghai')).isoformat()

        front_matter = f"""+++
date = '{current_time}'
draft = false
title = '{title}'
categories = [
{"".join([f'    "{cat}",\n' for cat in categories])}
]

tags = [
{"".join([f'    "{tag}",\n' for tag in tags])}
]
+++
"""
        return front_matter

    def remove_copyright_block(self, markdown_content: str) -> str:
        """移除Markdown内容中的版权声明区块
        
        Args:
            markdown_content: Markdown格式的文本内容
        """
        if not markdown_content:
            return ""
            
        # 移除永久链接
        permalink_pattern = re.compile(r'^本文永久链接：<[^>]+>$', re.MULTILINE)
        cleaned_content = permalink_pattern.sub('', markdown_content)
        
        # 移除可能残留的空行
        cleaned_content = re.sub(r'\n\s*\n', '\n\n', cleaned_content).strip()

        # 定义要移除的版权声明模式
        copyright_patterns = [
            r'#####\s*版权声明',
            r'本文首发于\s*!\[.*?\]\(.*?\)\s*\(.*?\)\s*博客\s*\(.*?\)\s*，版权所有，侵权必究。',
            r'本文首发于\s*\[.*?\]\(.*?\)\s*博客\s*\(.*?\)\s*，版权所有，侵权必究。',
            r'本文首发于\s*.*?，版权所有，侵权必究。',
            r'由\s*\[durban\].*?"创作共用保留署名-非商业-禁止演绎4\.0国际许可证。"\)'
            # 可以添加更多模式...
        ]
        
        # 替换所有匹配的版权声明
        for pattern in copyright_patterns:
            cleaned_content = re.sub(pattern, '', cleaned_content, flags=re.DOTALL)
        
        # 移除可能残留的空行
        cleaned_content = re.sub(r'\n\s*\n', '\n\n', cleaned_content).strip()
        
        # 检查是否移除了内容
        if cleaned_content != markdown_content:
            self.logger.info("已移除版权声明区块")
            
        return cleaned_content

    def save_markdown_to_file(self, markdown_content: str, file_path: str) -> bool:
        """将Markdown内容保存到文件
        
        Args:
            markdown_content: 要保存的Markdown内容
            file_path: 保存文件的路径
        """
        if not markdown_content:
            self.logger.error("错误：没有Markdown内容可保存")
            return False
            
        try:
            # 创建目录（如果不存在）
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            
            markdown_content = self.remove_copyright_block(markdown_content)

            # 如果需要添加前置元数据
            if self.config['add_front_matter']:
                # 获取页面标题作为文章标题
                page_title = self.get_title()
                # 规范化标题
                page_title = self.replace_keywords(page_title)
                # 生成前置元数据
                front_matter = self.generate_front_matter(title=page_title)
                # 合并前置元数据和Markdown内容
                content_to_save = front_matter + "\n" + markdown_content
            else:
                content_to_save = markdown_content
                
            with open(file_path, 'w', encoding=self.config['encoding']) as file:
                file.write(content_to_save)
            self.logger.info(f"Markdown内容已成功保存到 {file_path}")
            return True
        except Exception as e:
            self.logger.error(f"保存文件失败: {e}")
            return False

def main():
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='网页内容分析工具')
    
    # 添加必需的URL参数
    parser.add_argument('url', type=str, help='目标网页的URL')
    
    # 添加可选参数
    parser.add_argument('--target-class', type=str, default='entry-content', 
                        help='要提取的目标元素的类名')
    parser.add_argument('--output-dir', type=str, default='./content/post', 
                        help='输出文件的目录')
    parser.add_argument('--no-front-matter', action='store_true', 
                        help='不添加前置元数据')
    parser.add_argument('--timeout', type=int, default=10, 
                        help='请求超时时间（秒）')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    print(f"目标URL: {args.url}")
    
    # 配置选项
    config = {
        'target_class': args.target_class,
        'output_dir': args.output_dir,
        'add_front_matter': not args.no_front_matter,
        'timeout': args.timeout,
        'encoding': 'utf-8'  # 添加缺失的编码设置
    }
    
    analyzer = WebPageAnalyzer(args.url, config)
    if analyzer.fetch_page():
        title = analyzer.get_title().strip()
        print(f"原始页面标题: {title}")
        
        # 处理标题
        title = analyzer.replace_keywords(title)
        title = analyzer.replace_empty_keywords(title)
        title = analyzer.clean_title(title)
        print(f"处理后的标题: {title}")
        
        # 构建输出文件路径
        output_file = f"{config['output_dir']}/{title}.md"
        
        print(f"页面总链接数: {analyzer.count_elements('a')}")
        
        # 查找目标元素
        print(f"\n查找class为 '{config['target_class']}' 的元素:")
        elements = analyzer.find_elements_by_class(config['target_class'])
        
        if elements:
            print(f"找到 {len(elements)} 个匹配的元素")
            
            # 获取第一个匹配元素的Markdown格式
            first_element = elements[0]
            element_md = analyzer.get_element_markdown(first_element)
            
            if element_md:
                # 保存Markdown到文件
                if analyzer.save_markdown_to_file(element_md, output_file):
                    print(f"已将第一个匹配元素的Markdown内容保存到 {output_file}")
                    
                    # 显示保存的内容预览（包括前置元数据）
                    print("\n保存内容预览:")
                    with open(output_file, 'r', encoding=config['encoding']) as f:
                        preview = f.read(500)
                        print(preview + ("..." if len(preview) == 500 else ""))
            else:
                print("无法将元素转换为Markdown格式")
        else:
            print(f"未找到class为 '{config['target_class']}' 的元素")

if __name__ == "__main__":
    main()
