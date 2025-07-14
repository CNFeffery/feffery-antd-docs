import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例对话框',
            id='modal-responsive-width-demo-open',
            type='primary',
        ),
        fac.AntdModal(
            '示例内容',
            id='modal-responsive-width-demo',
            title='对话框示例',
            width={
                'xs': '100vw',
                'sm': '100vw',
                'md': '100vw',
                'lg': '60vw',
                'xl': '60vw',
                'xxl': '60vw',
            },
        ),
    ]

    return demo_contents


@app.callback(
    Output('modal-responsive-width-demo', 'visible'),
    Input('modal-responsive-width-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def modal_responsive_width_demo(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例对话框',
        id='modal-responsive-width-demo-open',
        type='primary',
    ),
    fac.AntdModal(
        '示例内容',
        id='modal-responsive-width-demo',
        title='对话框示例',
        width={
            'xs': '100vw',
            'sm': '100vw',
            'md': '100vw',
            'lg': '60vw',
            'xl': '60vw',
            'xxl': '60vw',
        },
    ),
]

...

@app.callback(
    Output('modal-responsive-width-demo', 'visible'),
    Input('modal-responsive-width-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def modal_responsive_width_demo(nClicks):
    return True
"""
    }
]
