from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdConfigProvider(
        html.Div(
            fac.Fragment(
                [
                    fuc.FefferyStyle(id='fragment-token-demo-dynamic-style'),
                    fac.AntdSpace(
                        [
                            fac.AntdCenter(
                                fac.AntdSwitch(
                                    id='fragment-token-demo-switch-algorithm',
                                    checked=True,
                                    checkedChildren='🌙',
                                    unCheckedChildren='☀️',
                                )
                            ),
                            fac.AntdText('Test' * 1000),
                        ],
                        direction='vertical',
                        style={'width': '100%'},
                    ),
                ],
                id='fragment-token-demo',
            ),
            style={'padding': 24},
        ),
        id='fragment-token-demo-config-provider',
    )

    return demo_contents


app.clientside_callback(
    '''(checked) => checked ? "dark" : "default"''',
    Output('fragment-token-demo-config-provider', 'algorithm'),
    Input('fragment-token-demo-switch-algorithm', 'checked'),
)

app.clientside_callback(
    """(token) => {
        let newStyle = `
body {
    background: ${token.colorBgBase} !important;
}`
        console.log(newStyle)
        return newStyle;
    }""",
    Output('fragment-token-demo-dynamic-style', 'rawStyle'),
    Input('fragment-token-demo', 'token'),
)


code_string = [
    {
        'code': """
fac.AntdConfigProvider(
    html.Div(
        fac.Fragment(
            [
                fuc.FefferyStyle(id='fragment-token-demo-dynamic-style'),
                fac.AntdSpace(
                    [
                        fac.AntdCenter(
                            fac.AntdSwitch(
                                id='fragment-token-demo-switch-algorithm',
                                checked=True,
                                checkedChildren='🌙',
                                unCheckedChildren='☀️',
                            )
                        ),
                        fac.AntdText('Test' * 1000),
                    ],
                    direction='vertical',
                    style={'width': '100%'},
                ),
            ],
            id='fragment-token-demo',
        ),
        style={'padding': 24},
    ),
    id='fragment-token-demo-config-provider',
)

...

app.clientside_callback(
    '''(checked) => checked ? "dark" : "default"''',
    Output('fragment-token-demo-config-provider', 'algorithm'),
    Input('fragment-token-demo-switch-algorithm', 'checked'),
)

app.clientside_callback(
    '''(token) => {
        let newStyle = `
body {
    background: ${token.colorBgBase} !important;
}`
        console.log(newStyle)
        return newStyle;
    }''',
    Output('fragment-token-demo-dynamic-style', 'rawStyle'),
    Input('fragment-token-demo', 'token'),
)
"""
    }
]
