+++
date = '2025-07-30T11:44:11.827871+08:00'
draft = false
title = 'Python小技巧 - 下载抓取小视频'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

### 采集/下载小视频

操作流程

1. 分析页面
2. 抓取页面
3. 抓取小视频
4. 保存小视频

比如抓取pearvideo网站的视频

选取要抓取的页面`https://www.pearvideo.com/popular`，分析此页面的视频，通过点击页面的链接知道视频的页面`https://www.pearvideo.com/video_1707347`

然后抓取小视频，下载保存小视频

通过以上分析不难得出

1. 每一页的获取是通过`https://www.pearvideo.com/popular_loading.jsp?reqType=1&categoryId=&start=20&sort=15&mrd=0.24415926264194443`
2. 视频的获取是通过`https://www.pearvideo.com/video_1707347`页面的ajax请求`https://www.pearvideo.com/videoStatus.jsp`来获取视频的参数
3. 分析视频的参数获得视频的地址，这里注意一个地址的更换，假地址：`https://video.pearvideo.com/mp4/adshort/20201117/1605695463779-15486835_adpkg-ad_hd.mp4`真地址：`https://video.pearvideo.com/mp4/adshort/20201117/cont-1707347-15486835_adpkg-ad_hd.mp4`

最后示例代码如下

```python

import requests
import re
import os

def fetch_video_content(video_id):
    page_video_url = 'https://www.pearvideo.com/videoStatus.jsp'
    params = {
        'contId': video_id,
        'mrd': '0.9725183045235088'
    }

    headers = {
        'Referer': f'https://www.pearvideo.com/video_{video_id}',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/86.0.4240.193 Safari/537.36'
    }
    response = requests.get(page_video_url, params=params, headers=headers)

    data = response.json()

    video_url = re.sub(data['systemTime'],
                       f'cont-{video_id}',
                       data['videoInfo']['videos']['srcUrl'])

    video_content = requests.get(video_url)
    save_path = os.getcwd() + '/videos/video_' + str(video_id) + '.mp4'

    with open(save_path, mode='wb') as f:
        f.write(video_content.content)

def fetch_video():
    for page in range(10, 110, 10):
        page_web_page_url = f'https://www.pearvideo.com/popular_loading.jsp'
        params = {
            'reqType': 1,
            'start': page,
            'sort': 15,
            'mrd': '0.24415926264194443'
        }

        response = requests.get(page_web_page_url, params=params)

        titles = re.findall(
            '<h2 class="popularem-title">(.*?)</h2>', response.text)
        video_ids = re.findall(
            '<a href="video_(\d+)" class="popularembd actplay">',
            response.text)

        for video_id in video_ids:
            fetch_video_content(video_id)
```

### 知识点汇总

1. 正则的使用 `re.findall` `re.sub`
2. requests的使用，尤其是 `headers` `params`
3. requests的json处理，`response.json()`
4. request的二进制数据处理，`response.content`