from dash import html
from functools import partial
import feffery_antd_components as fac
import feffery_markdown_components as fmc
from dash.dependencies import Component

from i18n import translator, get_current_locale
from utils.doc_renderer import MarkdownRenderer

md_renderer = MarkdownRenderer()


def render() -> Component:
    """渲染“Dash+fac快速上手”文档页"""

    t = partial(translator.t, locale_topic='getting_started')
    current_locale = get_current_locale()

    return html.Div(
        [
            fac.AntdBackTop(),
            html.Div(
                [
                    fac.AntdTitle(t('环境搭建'), id='环境搭建', level=3),
                    fac.AntdParagraph(
                        md_renderer.render(
                            t(
                                '在基于**Dash**和**fac**进行应用开发之前，我们需要先搭建好所需的环境，推荐使用**conda**或**mamba**作为环境管理工具，这里以Python 3.9版本为例，在终端执行下列命令进行相关环境的创建及激活：'
                            )
                        ),
                        style={'textIndent': '2rem'},
                    ),
                    (
                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '注：由于国内pypi相关镜像的更新延迟，通过其进行相关库的安装，版本可能滞后于原始pypi中的最新版本'
                                )
                            ],
                            style={'textIndent': '2rem'},
                        )
                        if current_locale == 'zh-cn'
                        else None
                    ),
                    fac.AntdTabs(
                        items=[
                            {
                                'label': t('默认方式'),
                                'key': t('默认方式'),
                                'children': html.Div(
                                    [
                                        fmc.FefferySyntaxHighlighter(
                                            codeString="""conda create -n dash-apps python=3.9 -y
conda activate dash-apps""",
                                            language='bash',
                                            showCopyButton=True,
                                        )
                                    ]
                                ),
                            },
                            *(
                                [
                                    {
                                        'label': '国内使用镜像',
                                        'key': '国内使用镜像',
                                        'children': html.Div(
                                            [
                                                fmc.FefferySyntaxHighlighter(
                                                    codeString="""conda create -n dash-apps python=3.9 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main -y
conda activate dash-apps""",
                                                    language='bash',
                                                    showCopyButton=True,
                                                )
                                            ]
                                        ),
                                    }
                                ]
                                if current_locale == 'zh-cn'
                                else []
                            ),
                        ]
                    ),
                    fac.AntdParagraph(
                        t(
                            '完成环境的创建及激活后，我们在对应环境中直接通过pip进行相关基础依赖库的安装即可：'
                        ),
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdTabs(
                        items=[
                            {
                                'label': t('默认方式'),
                                'key': t('默认方式'),
                                'children': html.Div(
                                    [
                                        fmc.FefferySyntaxHighlighter(
                                            codeString="""pip install dash feffery-antd-components -U""",
                                            language='bash',
                                            showCopyButton=True,
                                        )
                                    ]
                                ),
                            },
                            *(
                                [
                                    {
                                        'label': '国内使用镜像',
                                        'key': '国内使用镜像',
                                        'children': html.Div(
                                            [
                                                fmc.FefferySyntaxHighlighter(
                                                    codeString="""pip install dash feffery-antd-components -U -i https://pypi.tuna.tsinghua.edu.cn/simple""",
                                                    language='bash',
                                                    showCopyButton=True,
                                                )
                                            ]
                                        ),
                                    }
                                ]
                                if current_locale == 'zh-cn'
                                else []
                            ),
                        ]
                    ),
                    fac.AntdTitle(
                        t('构建示例应用'), id='构建示例应用', level=3
                    ),
                    fac.AntdParagraph(
                        t(
                            '完成前面所述的环境部署后，下面我们来开发一个简单的小应用，实现根据用户输入的目标值和实际值来生成对应的环形进度条，操作效果如下面动图所示：'
                        ),
                        style={'textIndent': '2rem'},
                    ),
                    html.Div(
                        fac.AntdImage(
                            src=(
                                'assets/imgs/getting_started/dash+fac上手示例应用.gif'
                                if current_locale == 'zh-cn'
                                else 'assets/imgs/getting_started/dash+fac上手示例应用_en-us.gif'
                            ),
                            preview=False,
                        ),
                        style={'textAlign': 'center'},
                    ),
                    fac.AntdParagraph(
                        md_renderer.render(
                            t(
                                '对应代码如下，在激活对应环境的前提下，终端执行`python app.py`即可启动该示例应用：'
                            )
                        ),
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdTabs(
                        items=[
                            {
                                'label': 'app.py',
                                'key': 'app.py',
                                'children': fmc.FefferySyntaxHighlighter(
                                    codeString=(
                                        """
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
                        fac.AntdInputNumber(id="target-value", style={"width": "100%"}),
                        label="目标值",
                    ),
                    fac.AntdFormItem(
                        fac.AntdInputNumber(id="actual-value", style={"width": "100%"}),
                        label="实际值",
                    ),
                ],
                layout="inline",
                style={"marginBottom": 25, "width": "100%"},
            ),
            # 输出目标容器
            html.Div(
                id="output-container",
                style={
                    # 基于css中的flex布局实现水平垂直居中
                    "width": "100%",
                    "display": "flex",
                    "justifyContent": "center",
                    "alignItems": "center",
                },
            ),
        ],
        title="dash+fac应用示例",
        hoverable=True,
        style={
            # 这里利用到css中的fixed布局
            "position": "fixed",
            "top": "40%",
            "left": "50%",
            "transform": "translate(-50%, -50%)",
            "width": 560,
            "height": 350,
        },
    )
)


# 定义回调函数串起相关交互逻辑
@app.callback(
    Output("output-container", "children"),
    [Input("target-value", "value"), Input("actual-value", "value")],
)
def handle_progress_render(target_value, actual_value):
    # 判断传入的目标值和实际值是否有效
    if target_value and actual_value:
        return fac.AntdProgress(
            percent=round(100 * actual_value / target_value, 2), type="dashboard"
        )

    return fac.AntdResult(subTitle="请输入有效的目标值和实际值", status="warning")


if __name__ == "__main__":
    app.run(debug=False)
"""
                                        if current_locale == 'zh-cn'
                                        else """
import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output

# Instantiate the Dash application object
app = dash.Dash(__name__)

# Add initial page content
app.layout = html.Div(
    fac.AntdCard(
        [
            # Input form
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdInputNumber(id="target-value", style={"width": "100%"}),
                        label="Target Value",
                    ),
                    fac.AntdFormItem(
                        fac.AntdInputNumber(id="actual-value", style={"width": "100%"}),
                        label="Actual Value",
                    ),
                ],
                layout="inline",
                style={"marginBottom": 25, "width": "100%"},
            ),
            # Output target container
            html.Div(
                id="output-container",
                style={
                    # Using flex layout from CSS for center alignment
                    "width": "100%",
                    "display": "flex",
                    "justifyContent": "center",
                    "alignItems": "center",
                },
            ),
        ],
        title="Dash + FAC Application Example",
        hoverable=True,
        style={
            # Using fixed layout from CSS
            "position": "fixed",
            "top": "40%",
            "left": "50%",
            "transform": "translate(-50%, -50%)",
            "width": 630,
            "height": 350,
        },
    )
)


# Define callback function to connect interaction logic
@app.callback(
    Output("output-container", "children"),
    [Input("target-value", "value"), Input("actual-value", "value")],
)
def handle_progress_render(target_value, actual_value):
    # Check if the input target and actual values are valid
    if target_value and actual_value:
        return fac.AntdProgress(
            percent=round(100 * actual_value / target_value, 2), type="dashboard"
        )

    return fac.AntdResult(
        subTitle="Please enter valid target and actual values", status="warning"
    )


if __name__ == "__main__":
    app.run(debug=False)
"""
                                    ),
                                    language='python',
                                    showCopyButton=True,
                                    codeBlockStyle={'height': 600},
                                ),
                            }
                        ]
                    ),
                    *(
                        [
                            fac.AntdDivider(isDashed=True),
                            fac.AntdTitle('拓展阅读', id='拓展阅读', level=3),
                            fac.AntdSpace(
                                [
                                    html.A(
                                        fac.AntdCard(
                                            title='10分钟极速入门dash应用开发',
                                            coverImg={
                                                'src': 'assets/imgs/getting_started/cover_10分钟极速入门dash应用开发.png',
                                                'style': {
                                                    'width': 275,
                                                    'height': 325,
                                                    'objectFit': 'cover',
                                                },
                                            },
                                            hoverable=True,
                                            bodyStyle={'padding': 0},
                                        ),
                                        href='https://mp.weixin.qq.com/s/BvGJT7DPHP2dYExZgifgiw',
                                        target='_blank',
                                    ),
                                    html.A(
                                        fac.AntdCard(
                                            title='Dash应用页面整体布局技巧',
                                            coverImg={
                                                'src': 'assets/imgs/getting_started/cover_Dash应用页面整体布局技巧.png',
                                                'style': {
                                                    'width': 275,
                                                    'height': 325,
                                                    'objectFit': 'cover',
                                                },
                                            },
                                            hoverable=True,
                                            bodyStyle={'padding': 0},
                                        ),
                                        href='https://mp.weixin.qq.com/s/6Ee1FpCyjlHU4W3JjoL8sQ',
                                        target='_blank',
                                    ),
                                    html.A(
                                        fac.AntdCard(
                                            title=fac.AntdText(
                                                '在Dash应用中更灵活地编写回调函数',
                                                style={'fontSize': '13px'},
                                            ),
                                            coverImg={
                                                'src': 'assets/imgs/getting_started/cover_在Dash应用中更灵活地编写回调函数.png',
                                                'style': {
                                                    'width': 275,
                                                    'height': 325,
                                                    'objectFit': 'cover',
                                                },
                                            },
                                            hoverable=True,
                                            bodyStyle={'padding': 0},
                                            style={'width': 275},
                                        ),
                                        href='https://mp.weixin.qq.com/s/IJGeAz5V8jqrtoVm3vHcUw',
                                        target='_blank',
                                    ),
                                    html.A(
                                        fac.AntdCard(
                                            title=fac.AntdText(
                                                'Dash应用浏览器端回调常用方法总结',
                                                style={'fontSize': '13px'},
                                            ),
                                            coverImg={
                                                'src': 'assets/imgs/getting_started/cover_Dash应用浏览器端回调常用方法总结.jpg',
                                                'style': {
                                                    'width': 275,
                                                    'height': 325,
                                                    'objectFit': 'cover',
                                                },
                                            },
                                            hoverable=True,
                                            bodyStyle={'padding': 0},
                                            style={'width': 275},
                                        ),
                                        href='https://mp.weixin.qq.com/s/WjhrxBuS_xL-kBkBEK2GCg',
                                        target='_blank',
                                    ),
                                ],
                                size='large',
                                wrap=True,
                            ),
                            fac.AntdDivider(isDashed=True),
                            fac.AntdTitle(
                                '更多dash专业知识',
                                id='更多dash专业知识',
                                level=3,
                            ),
                            fac.AntdParagraph(
                                [
                                    fac.AntdText('fac', strong=True),
                                    '中有超过100种具有不同功能特点的组件，你可以通过左侧菜单栏浏览它们各自的文档说明和使用示例，从而组合构建出具有任意功能的',
                                    fac.AntdText('dash', strong=True),
                                    '应用✨。',
                                ],
                                style={'textIndent': '2rem'},
                            ),
                            fac.AntdParagraph(
                                [
                                    '同时我也在持续运营名为',
                                    fac.AntdText('玩转dash', italic=True),
                                    '的知识星球学习社区，目前已经更新了数套系统性的',
                                    fac.AntdText('dash', strong=True),
                                    '应用开发教程，以及围绕',
                                    fac.AntdText('dash', strong=True),
                                    '应用开发相关的各种前沿知识和使用技巧，是国内最专业的',
                                    fac.AntdText('dash', strong=True),
                                    '应用知识社区，如果你对此感兴趣，欢迎扫描下方二维码加入我的学习社区：',
                                ],
                                style={'textIndent': '2rem'},
                            ),
                            html.Div(
                                fac.AntdImage(
                                    src='assets/imgs/index/玩转dash星球二维码.jpg',
                                    style={'height': 450},
                                ),
                                style={'textAlign': 'center'},
                            ),
                        ]
                        if current_locale == 'zh-cn'
                        else []
                    ),
                ],
                style={'flex': 'auto'},
            ),
            html.Div(
                fac.AntdAnchor(
                    linkDict=[
                        {'title': t('环境搭建'), 'href': '#环境搭建'},
                        {'title': t('构建示例应用'), 'href': '#构建示例应用'},
                        *(
                            [
                                {'title': '拓展阅读', 'href': '#拓展阅读'},
                                {
                                    'title': '更多dash专业知识',
                                    'href': '#更多dash专业知识',
                                },
                            ]
                            if current_locale == 'zh-cn'
                            else []
                        ),
                    ],
                    offsetTop=65,
                ),
                style={'flex': 'none'},
            ),
        ],
        style={'display': 'flex', 'padding': 25},
    )
