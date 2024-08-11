import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton('点击触发', id='popup-card-basic-demo-trigger'),
        fac.AntdPopupCard(
            fac.AntdParagraph('内容示例' * 20),
            id='popup-card-basic-demo',
            title='弹出式卡片示例',
            visible=False,
        ),
    ]

    return demo_contents


@app.callback(
    Output('popup-card-basic-demo', 'visible'),
    Input('popup-card-basic-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def popup_card_basic_demo(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdButton('点击触发', id='popup-card-basic-demo-trigger'),
    fac.AntdPopupCard(
        fac.AntdParagraph('内容示例' * 20),
        id='popup-card-basic-demo',
        title='弹出式卡片示例',
        visible=False,
    ),
]

...

@app.callback(
    Output('popup-card-basic-demo', 'visible'),
    Input('popup-card-basic-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def popup_card_basic_demo(nClicks):
    return True
"""
    }
]
