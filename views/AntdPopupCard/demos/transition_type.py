import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdSelect(
                    id='popup-card-transition-type-demo-select',
                    defaultValue='fade',
                    allowClear=False,
                    options=[
                        {'label': transitionType, 'value': transitionType}
                        for transitionType in [
                            'none',
                            'fade',
                            'zoom',
                            'zoom-big',
                            'zoom-big-fast',
                            'slide-up',
                            'slide-down',
                            'slide-left',
                            'slide-right',
                            'move-up',
                            'move-down',
                            'move-left',
                            'move-right',
                        ]
                    ],
                    style={'width': 200},
                ),
                fac.AntdButton(
                    '点击触发', id='popup-card-transition-type-demo-trigger'
                ),
            ]
        ),
        fac.AntdPopupCard(
            fac.AntdParagraph('内容示例' * 20),
            id='popup-card-transition-type-demo',
            title='弹出式卡片示例',
            visible=False,
        ),
    ]

    return demo_contents


@app.callback(
    Output('popup-card-transition-type-demo', 'transitionType'),
    Input('popup-card-transition-type-demo-select', 'value'),
)
def popup_card_transition_type_demo(value):
    return value


@app.callback(
    Output('popup-card-transition-type-demo', 'visible'),
    Input('popup-card-transition-type-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def popup_card_transition_type_demo_visible(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdSpace(
        [
            fac.AntdSelect(
                id='popup-card-transition-type-demo-select',
                defaultValue='fade',
                allowClear=False,
                options=[
                    {'label': transitionType, 'value': transitionType}
                    for transitionType in [
                        'none',
                        'fade',
                        'zoom',
                        'zoom-big',
                        'zoom-big-fast',
                        'slide-up',
                        'slide-down',
                        'slide-left',
                        'slide-right',
                        'move-up',
                        'move-down',
                        'move-left',
                        'move-right',
                    ]
                ],
                style={'width': 200},
            ),
            fac.AntdButton(
                '点击触发', id='popup-card-transition-type-demo-trigger'
            ),
        ]
    ),
    fac.AntdPopupCard(
        fac.AntdParagraph('内容示例' * 20),
        id='popup-card-transition-type-demo',
        title='弹出式卡片示例',
        visible=False,
    ),
]

...

@app.callback(
    Output('popup-card-transition-type-demo', 'transitionType'),
    Input('popup-card-transition-type-demo-select', 'value'),
)
def popup_card_transition_type_demo(value):
    return value


@app.callback(
    Output('popup-card-transition-type-demo', 'visible'),
    Input('popup-card-transition-type-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def popup_card_transition_type_demo_visible(nClicks):
    return True
"""
    }
]
