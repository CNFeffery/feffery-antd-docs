import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdLayout(
        [
            fac.AntdSider(
                id='sider-custom-trigger-demo',
                collapsible=True,
                trigger=None,
                style={'backgroundColor': 'rgb(240, 242, 245)'},
            ),
            fac.AntdContent(
                fac.AntdButton(
                    '折叠/展开',
                    id='sider-custom-trigger-button-demo',
                    type='primary',
                ),
                style={'backgroundColor': 'white'},
            ),
        ],
        style={'height': '100vh'},
    )

    return demo_contents


app.clientside_callback(
    """(nClicks, collapsed) => !collapsed""",
    Output('sider-custom-trigger-demo', 'collapsed'),
    Input('sider-custom-trigger-button-demo', 'nClicks'),
    State('sider-custom-trigger-demo', 'collapsed'),
    prevent_initial_call=True,
)


code_string = [
    {
        'code': '''
fac.AntdLayout(
    [
        fac.AntdSider(
            id='sider-custom-trigger-demo',
            collapsible=True,
            trigger=None,
            style={'backgroundColor': 'rgb(240, 242, 245)'},
        ),
        fac.AntdContent(
            fac.AntdButton(
                '折叠/展开',
                id='sider-custom-trigger-button-demo',
                type='primary',
            ),
            style={'backgroundColor': 'white'},
        ),
    ],
    style={'height': '100vh'},
)

...

app.clientside_callback(
    """(nClicks, collapsed) => !collapsed""",
    Output('sider-custom-trigger-demo', 'collapsed'),
    Input('sider-custom-trigger-button-demo', 'nClicks'),
    State('sider-custom-trigger-demo', 'collapsed'),
    prevent_initial_call=True,
)
'''
    }
]
