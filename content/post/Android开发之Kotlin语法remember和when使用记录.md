+++
date = '2025-07-30T11:44:33.051946+08:00'
draft = false
title = 'Android开发之Kotlin语法remember和when使用记录'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1603808282/walkerfree/Ju3ceiZzGSSQacR2juGN98.png'
categories = [
    "技术",

]

tags = [
    "Android",
    "Kotlin"
]
+++

kotlin语法remember使用记录

语法示例

```Kotlin

var currentStep by remember {
    mutableStateOf(1)
}
```

创建变量 currentStep 默认值为1

when使用记录

```Kotlin

val description = when (currentStep) {
    1 -> R.string.lemon_squeeze_title
    else -> R.string.lemon_drink_description
}
```

当currentStep变量被更改之后，description的值也会随着变化

在composble中，我理解为是变量的绑定，组件中通过更改currentStep会导致对应的变量和相应的逻辑发生变化

完整的代码示例

```Kotlin

@Composable
fun Lemon() {
    var currentStep by remember {
        mutableStateOf(1)
    }

    var squeezeCount by remember {
        mutableStateOf(0)
    }

    val imageResource = when (currentStep) {
        1 -> R.drawable.lemon_restart
        else -> R.drawable.lemon_drink
    }

    val description = when (currentStep) {
        1 -> R.string.lemon_squeeze_title
        else -> R.string.lemon_drink_description
    }

    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center,
        modifier = Modifier.fillMaxWidth()
    ) {
        Text(text = stringResource(description))
        Spacer(modifier = Modifier.height(32.dp))

        Button(
            onClick = {
                currentStep = when (currentStep) {
                    1 -> {
                        squeezeCount = (2..4).random()
                        2
                    }
                    2 -> {
                        squeezeCount--
                        if (squeezeCount == 0) {
                            3
                        } else {
                            2
                        }
                    }
                    3 -> 4
                    4 -> 1
                    else -> 1
                }
            },
            colors = ButtonDefaults.buttonColors(backgroundColor = Color.Magenta),
            shape = RoundedCornerShape(40.dp)
        ) {
            Image(
                painter = painterResource(id = imageResource),
                contentDescription = stringResource(description),
                modifier = Modifier.wrapContentSize()
            )
        }

    }

}
```
