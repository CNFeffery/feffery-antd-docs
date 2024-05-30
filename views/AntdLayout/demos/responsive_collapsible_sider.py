import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdLayout(
        [
            fac.AntdSider(
                breakpoint='xl',
                collapsible=True,
                style={'backgroundColor': 'rgb(240, 242, 245)'},
            ),
            fac.AntdContent(
                fac.AntdCenter(
                    fac.AntdTitle('内容区示例', level=2, style={'margin': '0'}),
                    style={
                        'height': '100%',
                    },
                ),
                style={'backgroundColor': 'white'},
            ),
        ],
        style={'height': '100vh'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdLayout(
    [
        fac.AntdSider(
            breakpoint='xl',
            collapsible=True,
            style={'backgroundColor': 'rgb(240, 242, 245)'},
        ),
        fac.AntdContent(
            fac.AntdCenter(
                fac.AntdTitle('内容区示例', level=2, style={'margin': '0'}),
                style={
                    'height': '100%',
                },
            ),
            style={'backgroundColor': 'white'},
        ),
    ],
    style={'height': '100vh'},
)
"""
    }
]
