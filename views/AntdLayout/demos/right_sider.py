import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdLayout(
        [
            fac.AntdContent(
                fac.AntdCenter(
                    fac.AntdTitle('内容区示例', level=2, style={'margin': '0'}),
                    style={'height': '100%'},
                ),
                style={'backgroundColor': 'white'},
            ),
            fac.AntdSider(
                fac.AntdCenter(
                    fac.AntdTitle('右侧侧边栏', level=2, style={'margin': '0'}),
                    style={
                        'height': '100%',
                    },
                ),
                style={'backgroundColor': 'rgb(240, 242, 245)'},
            ),
        ],
        style={'height': 500},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdLayout(
    [
        fac.AntdContent(
            fac.AntdCenter(
                fac.AntdTitle('内容区示例', level=2, style={'margin': '0'}),
                style={'height': '100%'},
            ),
            style={'backgroundColor': 'white'},
        ),
        fac.AntdSider(
            fac.AntdCenter(
                fac.AntdTitle('右侧侧边栏', level=2, style={'margin': '0'}),
                style={
                    'height': '100%',
                },
            ),
            style={'backgroundColor': 'rgb(240, 242, 245)'},
        ),
    ],
    style={'height': 500},
)
"""
    }
]
