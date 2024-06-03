import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdText('emptyAsNone:'),
                    fac.AntdSwitch(
                        checked=True,
                        checkedChildren='True',
                        unCheckedChildren='False',
                        id='input-empty-as-none-demo-switch',
                    ),
                ]
            ),
            fac.AntdInput(
                placeholder='尝试输入后清空内容，观察回调输出',
                allowClear=True,
                emptyAsNone=True,
                id='input-empty-as-none-demo',
            ),
            fac.AntdCard(
                id='input-empty-as-none-demo-output',
                headStyle={'display': 'none'},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


# switch切换emptyAsNone状态
@app.callback(
    Output('input-empty-as-none-demo', 'emptyAsNone'),
    Input('input-empty-as-none-demo-switch', 'checked'),
)
def input_empty_as_none_demo_switch(checked):
    return checked


# 回调显示当前输入框内容
@app.callback(
    Output('input-empty-as-none-demo-output', 'children'),
    Input('input-empty-as-none-demo', 'value'),
)
def input_empty_as_none_demo_output(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(
            addonBefore='前缀元素示例',
            addonAfter='后缀元素示例',
        ),
        fac.AntdInput(
            addonBefore=fac.AntdSelect(
                defaultValue='http://',
                options=[
                    {'label': option, 'value': option}
                    for option in ['http://', 'https://']
                ],
                allowClear=False,
            ),
            addonAfter=fac.AntdSelect(
                defaultValue='.com',
                options=[
                    {'label': option, 'value': option}
                    for option in ['.com', '.cn']
                ],
                allowClear=False,
            ),
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
    }
]
