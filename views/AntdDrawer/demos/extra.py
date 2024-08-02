import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '打开示例抽屉', id='drawer-extra-demo-open', type='primary'
        ),
        fac.AntdDrawer(
            '示例内容',
            id='drawer-extra-demo',
            title='抽屉示例',
            width='50vw',
            extra=fac.AntdSpace(
                [
                    fac.AntdButton('操作1', type='primary'),
                    fac.AntdButton('操作2', type='primary', danger=True),
                ],
                size='small',
            ),
        ),
    ]

    return demo_contents


@app.callback(
    Output('drawer-extra-demo', 'visible'),
    Input('drawer-extra-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def drawer_extra_demo(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '打开示例抽屉', id='drawer-extra-demo-open', type='primary'
    ),
    fac.AntdDrawer(
        '示例内容',
        id='drawer-extra-demo',
        title='抽屉示例',
        width='50vw',
        extra=fac.AntdSpace(
            [
                fac.AntdButton('操作1', type='primary'),
                fac.AntdButton('操作2', type='primary', danger=True),
            ],
            size='small',
        ),
    ),
]

...

@app.callback(
    Output('drawer-extra-demo', 'visible'),
    Input('drawer-extra-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def drawer_extra_demo(nClicks):
    return True
"""
    }
]
