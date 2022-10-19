　　在上一章节中，我们完成了`Dash`+`fac`基础开发环境的准备，在接下来这一章节中，我们来学习`Dash`的基础使用，并学习用`Dash`配合`fac`搭建**静态**的内容展示页面。

---

　　为了更方便地开发`Dash`应用，我们应该选择使用现代化的IDE软件，如`pycharm`、`vscode`等，以`pycharm`为例，在新建工程后，右下角选择`Add Interpreter`：

<center><img src="./assets/imgs/getting-started配图/图1.png"></img></center>
<center>图1</center>


　　如图2所示在`Conda Environment`-`Existing enviroment`里选择我们前面创建的`dash-dev-demo`环境（通常情况下这里会自动识别出最近创建的`conda`虚拟环境），点击`OK`完成解释器的配置。

<center><img src="./assets/imgs/getting-started配图/图2.png"></img></center>
<center>图2</center>


　　在当前工程下新建`app.py`文件，我们通常以`app`来命名我们的`Dash`应用入口`py`文件，你也可以换成其他你喜欢的名字。

　　文件最开始我们来导入一些必要的库：

```python
import dash
from dash import html # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac # 导入我们的主角fac框架
```

　　接着我们来实例化`Dash()`对象，推荐将也其命名为`app`：

```python
app = dash.Dash(__name__)
```

　　有了实例化的`Dash()`对象后，接下来我们需要让我们的`Dash`应用“看得见摸得着”，即为其构建网页中展示给用户的各个元素，这就涉及到其`layout`属性，其接受的输入值即为我们常说的“组件”。

　　下面是一个最简单的例子，我们用`html`中的`Div()`组件作为最外层元素，并将`'你好，Dash！'`作为其**第一个位置**上的参数传入：

```python
# 构建Dash应用网页内容的过程即为对layout属性赋值的过程
app.layout = html.Div(
	'你好，Dash！'
)
```

　　接下来我们在`app.py`最后补上下面这段代码，再运行`app.py`，在本机浏览器中访问[http://127.0.0.1:8050](http://127.0.0.1:8050)即可看到前面过程构建出的`Dash`应用：

```python
if __name__ == '__main__':
    app.run_server(debug=True)
```

　　其中右下角的蓝色控件是我们在`run_server()`中设置`debug=True`开启**调试模式**后的额外辅助功能，在调试模式下，我们实时修改代码中的内容，`ctrl+s`即刻保存后，浏览器中的`Dash`应用会随之自动刷新重载，这叫做**热重载**，大大方便了我们的开发过程：

<center><img src="./assets/imgs/getting-started配图/图3.png"></img></center>
<center>图3</center>


　　完整代码：

```python
import dash
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入我们的主角fac框架

app = dash.Dash(__name__)

# 构建Dash应用网页内容的过程即为对layout属性赋值的过程
app.layout = html.Div(
    '你好，Dash！'
)

if __name__ == '__main__':
    app.run_server(debug=True)

```

　　这就是最简单的一个`Dash`应用的示例，而像我所开发的`fac`这样的第三方组件库的意义，就在于将众多功能丰富、美观易用的组件引入`Dash`的世界中，帮助我们有能力组合出更加现代化的`web`应用，譬如我们将先前的`'你好，Dash！'`替换为`fac.AntdParagraph()`段落组件：

```python
app.layout = html.Div(
    fac.AntdParagraph(
        '段落示例1' * 100,
        copyable=True  # 开启可复制功能
    )
)
```

　　我们就获得了一段自带复制按钮功能的文字：

<center><img src="./assets/imgs/getting-started配图/图4.png"></img></center>
<center>图4</center>


　　每一个组件都有符合其功能设定的若干参数，我们先前向`html.Div()`中传入的第一个参数`'你好，Dash！'`就是其默认第一个位置的`children`参数，绝大多数组件的第一个位置参数都是`children`，通常都是用来传入向其内部嵌套的单个元素（单个字符串、单个数字、单个组件等），或由多个元素混合构成的**列表**，通过组件嵌套其他组件的层次关系，我们可以构建出很多丰富的页面功能，实现方便快捷的页面布局效果。

　　譬如我们可以使用`fac`中的`AntdRow()`与`AntdCol()`组件，用`AntdRow()`来嵌套`AntdCol()`，从而构建出网格布局效果，将前面例子中的`app.layout`属性替换为下面的例子，其中`style`参数用于为当前组件添加额外的`css`样式属性设定：

```python
app.layout = html.Div(
    # fac网格系统示例
    fac.AntdRow(
        [
            fac.AntdCol(
                html.Div(
                    fac.AntdStatistic(
                        title=f'指标{i}',
                        value=99999
                    ),
                    style={
                        'textAlign': 'center'  # 用于使Div内元素水平居中
                    }
                ),
                span=6
            )
            for i in range(1, 5)
        ],
        style={
            'marginTop': '100px'  # 用于在AntdRow()上方添加100像素留白
        }
    )
)
```

　　效果如下：

<center><img src="./assets/imgs/getting-started配图/图5.png"></img></center>
<center>图5</center>


　　搞懂了`Dash`中组件嵌套的“艺术”后，你就可以根据自己的需求，翻阅不同组件的文档页，了解其不同参数的功能，进而帮助你实现你的丰富构想，在下面这个进阶的静态应用例子中，我们就配合`fac`中的`AntdRow()`、`AntdCol()`、`AntdProgress()`、`AntdCard()`等若干组件，构建出一个美观的指标卡页面：

<center><img src="./assets/imgs/getting-started配图/图6.png"></img></center>
<center>图6</center>


　　完整代码如下，你可以通过这个例子，学习`Dash`应用构建中，层级嵌套代码书写的风格，养成好习惯提升代码的可读性，所使用到的各个组件的使用说明请自行前往对应文档页查看：

```python
import dash
import random
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入我们的主角fac框架

app = dash.Dash(__name__)

# 模拟数据
company2percent = {
    'A': 80,
    'B': 65,
    'C': 100,
    'D': 45
}

# 构建Dash应用网页内容的过程即为对layout属性赋值的过程
app.layout = html.Div(
    [
        fac.AntdTitle(
            '2022年第一季度各部门业务目标完成情况：',
            level=3
        ),
        fac.AntdText('示例中均为随机生成数据'),
        fac.AntdRow(
            [
                fac.AntdCol(
                    [
                        fac.AntdCard(
                            fac.AntdProgress(
                                percent=company2percent[apartment],
                                type='circle'
                            ),
                            title=f'部门{apartment}',
                            hoverable=True,
                            bodyStyle={
                                'display': 'flex',
                                'justifyContent': 'center'
                            }
                        ),
                        fac.AntdCard(
                            [
                                fac.AntdRow(
                                    [
                                        fac.AntdCol(
                                            fac.AntdText(
                                                f'员工{apartment}{i}：',
                                                strong=True
                                            ),
                                            flex='none'
                                        ),
                                        fac.AntdCol(
                                            fac.AntdProgress(
                                                percent=round(
                                                    random.uniform(20, 100), 1),
                                                strokeColor={
                                                    'from': '#00F5A0',
                                                    'to': '#00D9F5'
                                                }
                                            ),
                                            flex='auto'
                                        )
                                    ],
                                    style={
                                        'marginBottom': '10px',
                                        'width': '100%'
                                    }
                                )
                                for i in range(1, 10)
                            ],
                            title='各员工业绩目标完成情况',
                            hoverable=True,
                            style={
                                'textAlign': 'center',
                                'marginTop': '20px'
                            }
                        )
                    ],
                    span=6
                )
                for apartment in list('ABCD')
            ],
            gutter=20
        )
    ],
    style={
        'padding': '100px 200px'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)

```

