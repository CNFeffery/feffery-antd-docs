import feffery_antd_components as fac
from dash.dependencies import Component
from dash import html
from server import app
from dash.dependencies import Input, Output


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            html.Div(
                [
                    fac.AntdBackTop(id='back-top-backtop-demo', duration=1),
                    fac.AntdSwitch(
                        id='back-top-container-switch-demo',
                        checkedChildren='containerId',
                        unCheckedChildren='containerSelector',
                        checked=True,
                    ),
                ],
                style={'marginBottom': '20px'},
            ),
            fac.AntdSpace(
                [
                    html.Div(
                        [fac.AntdTitle('选择方法：containerId', level=4)]
                        + [i if i % 2 == 0 else html.Br() for i in range(200)],
                        id='back-top-container-container-id-demo',
                        style={
                            'maxHeight': '500px',
                            'overflowY': 'auto',
                            'position': 'relative',
                            'backgroundColor': 'rgba(240, 240, 240, 0.2)',
                            'border': '1px solid #f0f0f0',
                            'padding': '20px',
                        },
                    ),
                    html.Div(
                        [fac.AntdTitle('选择方法：containerSelector', level=4)]
                        + [i if i % 2 == 0 else html.Br() for i in range(200)],
                        id='back-top-container-container-selector-demo',
                        style={
                            'maxHeight': '500px',
                            'overflowY': 'auto',
                            'position': 'relative',
                            'backgroundColor': 'rgba(240, 240, 240, 0.2)',
                            'border': '1px solid #f0f0f0',
                            'padding': '20px',
                        },
                    ),
                ],
                style={
                    'justifyContent': 'space-between',
                    'width': '100%',
                },
            ),
        ],
        direction='vertical',
        style={
            'width': '100%',
        },
    )

    return demo_contents


@app.callback(
    [
        Output('back-top-backtop-demo', 'containerId'),
        Output('back-top-backtop-demo', 'containerSelector'),
    ],
    Input('back-top-container-switch-demo', 'checked'),
)
def back_top_container_id_demo(checked):
    if checked:
        return 'back-top-container-container-id-demo', None
    else:
        return (
            None,
            'document.querySelector("#back-top-container-container-selector-demo")',
        )


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        html.Div(
            [
                fac.AntdBackTop(id='back-top-backtop-demo', duration=1),
                fac.AntdSwitch(
                    id='back-top-container-switch-demo',
                    checkedChildren='containerId',
                    unCheckedChildren='containerSelector',
                    checked=True,
                ),
            ],
            style={'marginBottom': '20px'},
        ),
        fac.AntdSpace(
            [
                html.Div(
                    [fac.AntdTitle('选择方法：containerId', level=4)]
                    + [i if i % 2 == 0 else html.Br() for i in range(200)],
                    id='back-top-container-container-id-demo',
                    style={
                        'maxHeight': '500px',
                        'overflowY': 'auto',
                        'position': 'relative',
                        'backgroundColor': 'rgba(240, 240, 240, 0.2)',
                        'border': '1px solid #f0f0f0',
                        'padding': '20px',
                    },
                ),
                html.Div(
                    [fac.AntdTitle('选择方法：containerSelector', level=4)]
                    + [i if i % 2 == 0 else html.Br() for i in range(200)],
                    id='back-top-container-container-selector-demo',
                    style={
                        'maxHeight': '500px',
                        'overflowY': 'auto',
                        'position': 'relative',
                        'backgroundColor': 'rgba(240, 240, 240, 0.2)',
                        'border': '1px solid #f0f0f0',
                        'padding': '20px',
                    },
                ),
            ],
            style={
                'justifyContent': 'space-between',
                'width': '100%',
            },
        ),
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)


@app.callback(
    [
        Output('back-top-backtop-demo', 'containerId'),
        Output('back-top-backtop-demo', 'containerSelector'),
    ],
    Input('back-top-container-switch-demo', 'checked'),
)
def back_top_container_id_demo(checked):
    if checked:
        return 'back-top-container-container-id-demo', None
    else:
        return (
            None,
            'document.querySelector("#back-top-container-container-selector-demo")',
        )
"""
    }
]
