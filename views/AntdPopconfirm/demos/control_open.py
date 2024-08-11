import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSwitch(id='popconfirm-open-switch', checked=False),
            fac.AntdPopconfirm(
                fac.AntdButton('触发'),
                id='popconfirm-open-demo',
                title='确认继续',
            ),
        ]
    )

    return demo_contents


@app.callback(
    Output('popconfirm-open-demo', 'open'),
    Input('popconfirm-open-switch', 'checked'),
    prevent_initial_call=True,
)
def control_popconfirm_open(checked):
    return checked


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSwitch(id='popconfirm-open-switch', checked=False),
        fac.AntdPopconfirm(
            fac.AntdButton('触发'),
            id='popconfirm-open-demo',
            title='确认继续',
        ),
    ]
)

...

@app.callback(
    Output('popconfirm-open-demo', 'open'),
    Input('popconfirm-open-switch', 'checked'),
    prevent_initial_call=True,
)
def control_popconfirm_open(checked):
    return checked
"""
    }
]
