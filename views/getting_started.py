from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdTitle(
                    '环境搭建',
                    id='环境搭建',
                    level=3
                ),
                fac.AntdParagraph(
                    [
                        '在基于',
                        fac.AntdText(
                            'dash',
                            strong=True
                        ),
                        '和',
                        fac.AntdText(
                            'fac',
                            strong=True
                        ),
                        '进行应用开发之前，我们需要先搭建好所需的环境，推荐使用',
                        fac.AntdText(
                            'conda',
                            strong=True
                        ),
                        '作为环境管理工具，这里以Python 3.8版本为例，在终端执行下列命令进行相关环境的创建及激活：'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),
                fac.AntdTabs(
                    items=[
                        {
                            'label': '默认方式',
                            'key': '默认方式',
                            'children': html.Div(
                                [
                                    fmc.FefferySyntaxHighlighter(
                                        codeString='''conda create -n dash-apps python=3.8 -y
conda activate dash-apps''',
                                        language='bash',
                                        showCopyButton=True
                                    )
                                ]
                            )
                        },
                        {
                            'label': '国内使用镜像',
                            'key': '国内使用镜像',
                            'children': html.Div(
                                [
                                    fmc.FefferySyntaxHighlighter(
                                        codeString='''conda create -n dash-apps python=3.8 -c https://mirrors.aliyun.com/anaconda/pkgs/main/ -y
conda activate dash-apps''',
                                        language='bash',
                                        showCopyButton=True
                                    )
                                ]
                            )
                        }
                    ]
                ),
                fac.AntdParagraph(
                    [
                        '完成环境的创建及激活后，我们在对应环境中直接通过pip进行相关基础依赖库的安装即可：'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),
                fac.AntdTabs(
                    items=[
                        {
                            'label': '默认方式',
                            'key': '默认方式',
                            'children': html.Div(
                                [
                                    fmc.FefferySyntaxHighlighter(
                                        codeString='''pip install dash feffery-antd-components -U''',
                                        language='bash',
                                        showCopyButton=True
                                    )
                                ]
                            )
                        },
                        {
                            'label': '国内使用镜像',
                            'key': '国内使用镜像',
                            'children': html.Div(
                                [
                                    fmc.FefferySyntaxHighlighter(
                                        codeString='''pip install dash feffery-antd-components -U -i https://mirrors.aliyun.com/pypi/simple/''',
                                        language='bash',
                                        showCopyButton=True
                                    )
                                ]
                            )
                        }
                    ]
                ),
                fac.AntdTitle(
                    '构建示例应用',
                    id='构建示例应用',
                    level=3
                ),
                fac.AntdParagraph(
                    [
                        '完成前面所述的环境部署后，下面我们来开发一个简单的小应用，实现根据用户输入的目标值和实际值来生成对应的环形进度条，操作效果如下面动图所示：'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                html.Div(
                    fac.AntdImage(
                        src='assets/imgs/dash+fac上手示例应用.gif',
                        preview=False
                    ),
                    style={
                        'textAlign': 'center'
                    }
                ),

                fac.AntdParagraph(
                    [
                        '对应代码如下，在激活对应环境的前提下，终端执行',
                        fac.AntdText(
                            'python app.py',
                            code=True
                        ),
                        '即可启动该示例应用：'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                fac.AntdTabs(
                    items=[
                        {
                            'label': 'app.py',
                            'key': 'app.py',
                            'children': fmc.FefferySyntaxHighlighter(
                                codeString='''
import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output

# 实例化Dash应用对象
app = dash.Dash(__name__)

# 添加初始化页面内容
app.layout = html.Div(
    fac.AntdCard(
        [
            # 输入表单
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdInputNumber(
                            id='target-value',
                            style={
                                'width': '100%'
                            }
                        ),
                        label='目标值'
                    ),
                    fac.AntdFormItem(
                        fac.AntdInputNumber(
                            id='actual-value',
                            style={
                                'width': '100%'
                            }
                        ),
                        label='实际值'
                    )
                ],
                layout='inline',
                style={
                    'marginBottom': 25,
                    'width': '100%'
                }
            ),
            # 输出目标容器
            html.Div(
                id='output-container',
                style={
                    # 基于css中的flex布局实现水平垂直居中
                    'width': '100%',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            )
        ],
        title='dash+fac应用示例',
        hoverable=True,
        style={
            # 这里利用到css中的fixed布局
            'position': 'fixed',
            'top': '40%',
            'left': '50%',
            'transform': 'translate(-50%, -50%)',
            'width': 540,
            'height': 350
        }
    )
)

# 定义回调函数串起相关交互逻辑
@app.callback(
    Output('output-container', 'children'),
    [Input('target-value', 'value'),
     Input('actual-value', 'value')]
)
def handle_progress_render(target_value, actual_value):

    # 判断传入的目标值和实际值是否有效
    if target_value and actual_value:

        return fac.AntdProgress(
            percent=round(100 * actual_value / target_value, 2),
            type='dashboard'
        )

    return fac.AntdResult(
        subTitle='请输入有效的目标值和实际值',
        status='warning'
    )


if __name__ == '__main__':
    app.run(debug=False)
''',
                                language='python',
                                showCopyButton=True,
                                codeBlockStyle={
                                    'height': 600
                                }
                            )
                        }
                    ]
                ),

                fac.AntdDivider(
                    isDashed=True
                ),

                fac.AntdTitle(
                    '拓展阅读',
                    id='拓展阅读',
                    level=3
                ),

                fac.AntdSpace(
                    [
                        html.A(
                            fac.AntdCard(
                                title='10分钟极速入门dash应用开发',
                                coverImg={
                                    'src': 'assets/imgs/getting-started配图/cover_10分钟极速入门dash应用开发.png',
                                    'style': {
                                        'width': 265,
                                        'height': 325,
                                        'objectFit': 'cover'
                                    }
                                },
                                hoverable=True,
                                bodyStyle={
                                    'padding': 0
                                }
                            ),
                            href='https://mp.weixin.qq.com/s/BvGJT7DPHP2dYExZgifgiw',
                            target='_blank'
                        )
                    ]
                ),

                fac.AntdDivider(
                    isDashed=True
                ),

                fac.AntdTitle(
                    '更多dash专业知识',
                    id='更多dash专业知识',
                    level=3
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            'fac',
                            strong=True
                        ),
                        '中有将近100种具有不同功能特点的组件，你可以通过左侧菜单栏浏览它们各自的文档说明和使用示例，从而组合构建出具有任意功能的',
                        fac.AntdText(
                            'dash',
                            strong=True
                        ),
                        '应用✨。'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                fac.AntdParagraph(
                    [
                        '同时我也在持续运营名为',
                        fac.AntdText(
                            '玩转dash',
                            italic=True
                        ),
                        '的知识星球学习社区，目前已经更新了数套系统性的',
                        fac.AntdText(
                            'dash',
                            strong=True
                        ),
                        '应用开发教程，以及围绕',
                        fac.AntdText(
                            'dash',
                            strong=True
                        ),
                        '应用开发相关的各种前沿知识和使用技巧，是国内最专业的',
                        fac.AntdText(
                            'dash',
                            strong=True
                        ),
                        '应用知识社区，如果你对此感兴趣，欢迎扫描下方二维码加入我的学习社区：'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                html.Div(
                    fac.AntdImage(
                        src='assets/imgs/玩转dash星球二维码.jpg',
                        style={
                            'height': 450
                        }
                    ),
                    style={
                        'textAlign': 'center'
                    }
                )
            ],
            style={
                'flex': 'auto'
            }
        ),

        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '环境搭建', 'href': '#环境搭建'},
                    {'title': '构建示例应用', 'href': '#构建示例应用'},
                    {'title': '拓展阅读', 'href': '#拓展阅读'},
                    {'title': '更多dash专业知识', 'href': '#更多dash专业知识'}
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none'
            }
        )
    ],
    style={
        'display': 'flex',
        'padding': 25
    }
)
