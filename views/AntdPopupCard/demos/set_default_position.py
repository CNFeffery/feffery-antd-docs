import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '点击触发', id='popup-card-custom-position-demo-trigger'
        ),
        fac.AntdPopupCard(
            fac.AntdParagraph('内容示例' * 20),
            id='popup-card-custom-position-demo',
            title='弹出式卡片示例',
            visible=False,
            style={
                'bottom': 25,
                'left': 25,
                'position': 'fixed',
                'top': 'auto',  # 用于覆盖默认的top: 100px设定
            },
        ),
    ]

    return demo_contents


@app.callback(
    Output('popup-card-custom-position-demo', 'visible'),
    Input('popup-card-custom-position-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def popup_card_custom_position_demo(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '点击触发', id='popup-card-custom-position-demo-trigger'
    ),
    fac.AntdPopupCard(
        fac.AntdParagraph('内容示例' * 20),
        id='popup-card-custom-position-demo',
        title='弹出式卡片示例',
        visible=False,
        style={
            'bottom': 25,
            'left': 25,
            'position': 'fixed',
            'top': 'auto',  # 用于覆盖默认的top: 100px设定
        },
    ),
]

...

@app.callback(
    Output('popup-card-custom-position-demo', 'visible'),
    Input('popup-card-custom-position-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def popup_card_custom_position_demo(nClicks):
    return True
"""
    }
]
