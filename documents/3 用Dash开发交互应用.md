　　在上一章节中，我们学习到使用`Dash`+`fac`开发静态应用的基础概念，而现代化的`web`应用需要与用户的操作建立起良好的互动，本章节中，我们就来学习`Dash`的精髓——交互式`web`应用的开发。

---

　　任何一个`Dash`组件都有`id`参数，在`Dash`中我们通过编写**回调函数**，可以赋予页面内所包含元素对应的`组件+属性`不同的**角色**，在`Dash`中常用的回调**角色**有3种：

- Input：**输入**类角色，其值的变化用于触发每一次回调函数逻辑的执行，并传入此刻的值进入回调函数进行运算；
- Output：**输出**类角色，对应回调函数中的返回值；
- State：**状态**类角色，其值的变化不会触发回调函数，主要用于在**输入**类角色触发回调函数时，顺便传递此刻的状态值进入回调函数逻辑进行运算；

　　而回调函数的书写基本格式如下，其中回调函数名自定义，回调函数中的传入参数名可自定义，但顺序需要按照`app.callback()`中从输入类角色到状态类角色的顺序：

```python
@app.callback(
	Output(id信息, 属性名), # 先罗列输出类角色，必填，有多个时写在列表中
    Input(id信息, 属性名), # 再罗列输入类角色，必填，有多个时写在列表中
    State(id信息, 属性名) # 最后罗列状态类角色，可选，有多个时写在列表中
)
def 回调函数名(输入类参数1, ..., 状态类参数1, ...):
    # 书写回调逻辑
    ...
    # 单个Output时返回单个对应结果，多个Output时返回多个对应结果按顺序构成的列表
    return ...
```

　　让我们通过实际的例子来好好理解如何书写回调函数：

- 单输入单输出

　　首先我们来学习最简单的单输入单输出型回调函数，下面的例子中，页面内的按钮每被点击一次（对应`AntdButton`的`nClicks`属性自增1），其后`AntdText`内的文字便随之更新（即`children`属性被更新），那么显而易见`nClicks`应当作为输入类角色，`children`应当作为输出类角色，理清楚这个逻辑关系后，配合各自对应的唯一`id`信息，构造回调函数非常简单：

```python
import dash
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入我们的主角fac框架
from dash.dependencies import Input, Output  # 从dash.dependencies导入所需的角色类

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdButton(
            '点我点我',
            id='input-demo'
        ),
        fac.AntdText(id='output-demo')
    ]
)


@app.callback(
    Output('output-demo', 'children'),
    Input('input-demo', 'nClicks')
)
def callback_demo1(nClicks_demo):
    return fac.AntdText(f'我被点击了{nClicks_demo}次', strong=True)


if __name__ == '__main__':
    app.run_server(debug=True)

```

<center><img src="./assets/imgs/getting-started配图/图7.gif"></img></center>
<center>图7</center>


- 单输入单输出单状态

　　而下面的例子中，我们引入状态类角色，用按钮的点击作为回调函数每次被触发的原因，从而避免每次输入框内的内容变化都引起回调函数的频繁触发：

```python
import dash
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入我们的主角fac框架
from dash.dependencies import Input, Output, State  # 从dash.dependencies导入所需的角色类

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdInput(
            id='state-demo',
            style={
                'width': '100px'
            }
        ),
        fac.AntdButton(
            '提交',
            id='input-demo'
        ),
        fac.AntdText(id='output-demo')
    ]
)


@app.callback(
    Output('output-demo', 'children'),
    Input('input-demo', 'nClicks'),
    State('state-demo', 'value')
)
def callback_demo1(nClicks_demo, input_value):
    return fac.AntdText(input_value, strong=True)


if __name__ == '__main__':
    app.run_server(debug=True)

```

<center><img src="./assets/imgs/getting-started配图/图8.gif"></img></center>
<center>图8</center>


- 多角色类回调

　　为了实现功能更加丰富的`Dash`应用，很多情况下我们的某个回调函数中可能就不止有单个输入、输出、状态类角色，这种情况下，用列表容纳某一类状态下的多个角色即可，多输出时回调函数内的返回值也需要返回一一对应的列表，譬如下面的例子：

```python
import dash
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入我们的主角fac框架
from dash.dependencies import Input, Output, State  # 从dash.dependencies导入所需的角色类

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdInput(
            placeholder='姓名',
            id='state-demo1',
            style={
                'width': '100px'
            }
        ),
        fac.AntdInput(
            placeholder='性别',
            id='state-demo2',
            style={
                'width': '100px'
            }
        ),
        fac.AntdButton(
            '提交',
            id='input-demo'
        ),
        fac.AntdSpace(
            [
                fac.AntdText(id='output-demo1'),
                fac.AntdText(id='output-demo2')
            ],
            size=20
        ),
    ]
)


@app.callback(
    [Output('output-demo1', 'children'),
     Output('output-demo2', 'children')],
    Input('input-demo', 'nClicks'),
    [State('state-demo1', 'value'),
     State('state-demo2', 'value')]
)
def callback_demo1(nClicks_demo, input_value1, input_value2):
    return [
        f'input_value1 = {input_value1}',
        f'input_value2 = {input_value2}'
    ]


if __name__ == '__main__':
    app.run_server(debug=True)

```

<center><img src="./assets/imgs/getting-started配图/图9.gif"></img></center>
<center>图9</center>


---

　　掌握了上述这些`Dash`+`fac`最基础的概念后，你可以阅读我较早之前撰写的`Dash`系列教程中的下列几篇以了解更多实用的`Dash`技术内容。

　　我先前在写作这些文章时还未开始开发`fac`，因此文章中涉及到`dash-bootstrap-components`、`dash-table`等颇为过时落后的组件库的相关概念，可略过改用`fac`中的相关功能进行替换，阅读时只需要理解`Dash`相关的技术要点即可：

- [（数据科学学习手札102）Python+Dash快速web应用开发——基础概念篇](https://www.cnblogs.com/feffery/p/14258438.html)
- [（数据科学学习手札104）Python+Dash快速web应用开发——回调交互篇（上）](https://www.cnblogs.com/feffery/p/14313103.html)
- [（数据科学学习手札105）Python+Dash快速web应用开发——回调交互篇（中）](https://www.cnblogs.com/feffery/p/14349206.html)
- [（数据科学学习手札106）Python+Dash快速web应用开发——回调交互篇（下）](https://www.cnblogs.com/feffery/p/14386458.html)
- [（数据科学学习手札119）Python+Dash快速web应用开发——多页面应用](https://www.cnblogs.com/feffery/p/14724140.html)
- [（数据科学学习手札120）Python+Dash快速web应用开发——整合数据库](https://www.cnblogs.com/feffery/p/14748675.html)
- [（数据科学学习手札121）Python+Dash快速web应用开发——项目结构篇](https://www.cnblogs.com/feffery/p/14773887.html)
- [（数据科学学习手札122）Python+Dash快速web应用开发——内网穿透篇](https://www.cnblogs.com/feffery/p/14775704.html)
- [（数据科学学习手札123）Python+Dash快速web应用开发——部署发布篇](https://www.cnblogs.com/feffery/p/14826195.html)

---

　　更多项目级`Dash`知识内容欢迎加入我的知识星球**玩转dash**：



