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
                    id='popup-card-close-icon-type-demo-select',
                    defaultValue='default',
                    allowClear=False,
                    options=[
                        {'label': closeIconType, 'value': closeIconType}
                        for closeIconType in ['default', 'outlined', 'two-tone']
                    ],
                    style={'width': 200},
                ),
                fac.AntdButton(
                    '点击触发', id='popup-card-close-icon-type-demo-trigger'
                ),
            ]
        ),
        fac.AntdPopupCard(
            fac.AntdParagraph('内容示例' * 20),
            id='popup-card-close-icon-type-demo',
            title='弹出式卡片示例',
            visible=False,
        ),
    ]

    return demo_contents


@app.callback(
    Output('popup-card-close-icon-type-demo', 'closeIconType'),
    Input('popup-card-close-icon-type-demo-select', 'value'),
)
def popup_card_close_icon_type_demo(value):
    return value


@app.callback(
    Output('popup-card-close-icon-type-demo', 'visible'),
    Input('popup-card-close-icon-type-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def popup_card_close_icon_type_demo_visible(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdSpace(
        [
            fac.AntdSelect(
                id='popup-card-close-icon-type-demo-select',
                defaultValue='default',
                allowClear=False,
                options=[
                    {'label': closeIconType, 'value': closeIconType}
                    for closeIconType in ['default', 'outlined', 'two-tone']
                ],
                style={'width': 200},
            ),
            fac.AntdButton(
                '点击触发', id='popup-card-close-icon-type-demo-trigger'
            ),
        ]
    ),
    fac.AntdPopupCard(
        fac.AntdParagraph('内容示例' * 20),
        id='popup-card-close-icon-type-demo',
        title='弹出式卡片示例',
        visible=False,
    ),
]

...

@app.callback(
    Output('popup-card-close-icon-type-demo', 'closeIconType'),
    Input('popup-card-close-icon-type-demo-select', 'value'),
)
def popup_card_close_icon_type_demo(value):
    return value


@app.callback(
    Output('popup-card-close-icon-type-demo', 'visible'),
    Input('popup-card-close-icon-type-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def popup_card_close_icon_type_demo_visible(nClicks):
    return True
"""
    }
]
