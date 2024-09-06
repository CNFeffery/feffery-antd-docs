import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdLayout(
            [
                fac.AntdContent(
                    fac.AntdCenter(
                        fac.AntdTitle(
                            '内容区示例', level=2, style={'margin': '0'}
                        ),
                        style={'height': '100%'},
                    ),
                    style={'backgroundColor': 'white'},
                ),
                fac.AntdSider(
                    fac.AntdCenter(
                        fac.AntdTitle(
                            '右侧侧边栏', level=2, style={'margin': '0'}
                        ),
                        style={
                            'height': '100%',
                        },
                    ),
                    style={'backgroundColor': 'rgb(240, 242, 245)'},
                ),
            ],
            style={'height': '100vh'},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdLayout(
            [
                fac.AntdContent(
                    fac.AntdCenter(
                        fac.AntdTitle(
                            'Content Demo', level=2, style={'margin': '0'}
                        ),
                        style={'height': '100%'},
                    ),
                    style={'backgroundColor': 'white'},
                ),
                fac.AntdSider(
                    fac.AntdCenter(
                        fac.AntdTitle(
                            'Right Sider', level=2, style={'margin': '0'}
                        ),
                        style={
                            'height': '100%',
                        },
                    ),
                    style={'backgroundColor': 'rgb(240, 242, 245)'},
                ),
            ],
            style={'height': '100vh'},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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
    style={'height': '100vh'},
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdLayout(
    [
        fac.AntdContent(
            fac.AntdCenter(
                fac.AntdTitle(
                    'Content Demo', level=2, style={'margin': '0'}
                ),
                style={'height': '100%'},
            ),
            style={'backgroundColor': 'white'},
        ),
        fac.AntdSider(
            fac.AntdCenter(
                fac.AntdTitle(
                    'Right Sider', level=2, style={'margin': '0'}
                ),
                style={
                    'height': '100%',
                },
            ),
            style={'backgroundColor': 'rgb(240, 242, 245)'},
        ),
    ],
    style={'height': '100vh'},
)
"""
            }
        ]
