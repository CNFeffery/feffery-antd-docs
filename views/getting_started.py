from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

from server import app

code_demo = '''
import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdRow(
            [
                fac.AntdCol(
                    fac.AntdDatePicker(
                        id='getting-started-date-picker-demo',
                        placeholder='选择日期'
                    )
                ),
                fac.AntdCol(
                    fac.AntdSelect(
                        id='getting-started-select-demo',
                        placeholder='选择你所熟悉的编程语言',
                        options=[
                            {
                                'label': 'Python',
                                'value': 'Python'
                            },
                            {
                                'label': 'R',
                                'value': 'R'
                            },
                            {
                                'label': 'Julia',
                                'value': 'Julia'
                            },
                            {
                                'label': 'JavaScript',
                                'value': 'JavaScript'
                            },
                            {
                                'label': 'Java',
                                'value': 'Java'
                            },
                            {
                                'label': 'Scala',
                                'value': 'Scala'
                            }
                        ],
                        maxTagCount=2,
                        mode='multiple',
                        style={
                            'width': '17rem'
                        }
                    )
                ),
                fac.AntdCol(
                    fac.AntdButton(
                        '提交内容',
                        id='getting-started-button-demo',
                        type='primary'
                    )
                ),
            ],
            gutter=15,
            justify='center'
        ),

        html.Div(id='getting-started-notification-demo')
    ],
    style={
        'height': '500px',
        'display': 'flex',
        'alignItems': 'center',
        'justifyContent': 'center',
        'backgroundColor': 'rgba(241, 241, 241, 0.4)'
    }
)


@app.callback(
    Output('getting-started-notification-demo', 'children'),
    Input('getting-started-button-demo', 'nClicks'),
    [State('getting-started-date-picker-demo', 'selectedDate'),
     State('getting-started-select-demo', 'value')],
    prevent_initial_call=True
)
def getting_started_callback_demo(nClicks, selectedDate, select_value):
    # 若按钮被点击
    if nClicks:
        # 若两个输入组件均有值输入
        if selectedDate and select_value:
            return fac.AntdNotification(
                message='提交成功',
                description='已提交日期：{}，已提交选项值：{}'.format(
                    selectedDate,
                    '、'.join(select_value)
                ),
                type='success',
                duration=3
            )

        return fac.AntdNotification(
            message='提交失败',
            description='信息提交不完整！',
            type='error',
            duration=3
        )


if __name__ == '__main__':
    app.run_server(debug=True)

'''

docs_content = html.Div(
    [
        fac.AntdParagraph(
            [
                fac.AntdText('用fac开发一个简单的Dash应用',
                             strong=True,
                             style={'fontSize': '30px'}),
                fac.AntdText('😋', style={'fontSize': '30px'})
            ]
        ),

        fac.AntdParagraph(
            [
                fac.AntdText('　　作为基于'),
                fac.AntdText('Dash', italic=True),
                fac.AntdText('的UI组件库，'),
                fac.AntdText('要想顺畅地使用'),
                fac.AntdText('fac', strong=True),
                fac.AntdText('来构建你的web应用，你需要对'),
                fac.AntdText('Dash', italic=True),
                fac.AntdText('有一定的知识储备，零基础的开发者可以移步我撰写的'),
                html.A('Dash基础教程',
                       target='_blank',
                       href='https://www.cnblogs.com/feffery/tag/Dash/'),
                fac.AntdText('进行学习。')
            ]
        ),

        fac.AntdDivider(),

        fac.AntdParagraph(
            [
                fac.AntdText('　　在完成对'),
                fac.AntdText('fac', strong=True),
                fac.AntdText('的安装之后，推荐按照'),
                fac.AntdText('import feffery_antd_components as fac',
                             keyboard=True,
                             copyable=True),
                fac.AntdText('的方式进行'),
                fac.AntdText('fac', strong=True),
                fac.AntdText('的导入，'),
                fac.AntdText('之后使用'),
                fac.AntdText('fac.组件名称', strong=True),
                fac.AntdText('的方式调用各种功能丰富的组件即可，'),
                fac.AntdText('下面是基于'),
                fac.AntdText('fac', strong=True),
                fac.AntdText('的一些组件构建一个简单表单提交应用的例子：'),
            ]
        ),

        html.Div(
            [
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            fac.AntdDatePicker(
                                id='getting-started-date-picker-demo',
                                placeholder='选择日期'
                            )
                        ),
                        fac.AntdCol(
                            fac.AntdSelect(
                                id='getting-started-select-demo',
                                placeholder='选择你所熟悉的编程语言',
                                options=[
                                    {
                                        'label': 'Python',
                                        'value': 'Python'
                                    },
                                    {
                                        'label': 'R',
                                        'value': 'R'
                                    },
                                    {
                                        'label': 'Julia',
                                        'value': 'Julia'
                                    },
                                    {
                                        'label': 'JavaScript',
                                        'value': 'JavaScript'
                                    },
                                    {
                                        'label': 'Java',
                                        'value': 'Java'
                                    },
                                    {
                                        'label': 'Scala',
                                        'value': 'Scala'
                                    }
                                ],
                                maxTagCount=2,
                                mode='multiple',
                                style={
                                    'width': '17rem'
                                }
                            )
                        ),
                        fac.AntdCol(
                            fac.AntdButton(
                                '提交内容',
                                id='getting-started-button-demo',
                                type='primary'
                            )
                        ),
                    ],
                    gutter=15,
                    justify='center'
                ),

                html.Div(id='getting-started-notification-demo')
            ],
            style={
                'height': '500px',
                'display': 'flex',
                'alignItems': 'center',
                'justifyContent': 'center',
                'backgroundColor': 'rgba(241, 241, 241, 0.4)'
            }
        ),

        html.Div(
            html.Span(
                '源码',
                id='源码',
                style={
                    'borderLeft': '4px solid grey',
                    'padding': '3px 0 3px 10px',
                    'backgroundColor': '#f5f5f5',
                    'fontWeight': 'bold',
                    'fontSize': '1rem'
                }
            ),
            style={
                'marginBottom': '10px',
                'marginTop': '10px'
            }
        ),

        html.Div(
            [
                fuc.FefferySyntaxHighlighter(
                    showLineNumbers=True,
                    showInlineLineNumbers=True,
                    language='python',
                    codeStyle='coy-without-shadows',
                    codeString=code_demo
                )
            ],
            style={
                'backgroundColor': 'rgba(250, 250, 250, 1)'
            }
        ),

        fac.AntdDivider(),

        fac.AntdParagraph(
            [
                fac.AntdText('　　阅读你感兴趣的其他组件文档页，充分运用'),
                fac.AntdText('fac', strong=True),
                fac.AntdText('的能力吧！'),
            ]
        ),

        html.Div(
            style={
                'height': '100px'
            }
        )

    ]
)


@app.callback(
    Output('getting-started-notification-demo', 'children'),
    Input('getting-started-button-demo', 'nClicks'),
    [State('getting-started-date-picker-demo', 'selectedDate'),
     State('getting-started-select-demo', 'value')],
    prevent_initial_call=True
)
def getting_started_callback_demo(nClicks, selectedDate, select_value):
    # 若按钮被点击
    if nClicks:
        # 若两个输入组件均有值输入
        if selectedDate and select_value:
            return fac.AntdNotification(
                message='提交成功',
                description='已提交日期：{}，已提交选项值：{}'.format(
                    selectedDate,
                    '、'.join(select_value)
                ),
                type='success',
                duration=3
            )

        return fac.AntdNotification(
            message='提交失败',
            description='信息提交不完整！',
            type='error',
            duration=3
        )
