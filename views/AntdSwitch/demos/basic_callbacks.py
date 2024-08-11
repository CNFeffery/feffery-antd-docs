import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('基础回调', innerTextOrientation='left'),
            fac.AntdSwitch(id='switch-callback-demo'),
            fac.AntdCard(
                id='switch-callback-output-demo',
                headStyle={'display': 'none'},
            ),
            fac.AntdDivider('简单用例', innerTextOrientation='left'),
            fac.AntdFlex(
                [
                    fac.AntdInput(
                        placeholder='切换右侧开关状态以激活/禁用输入框',
                        id='input-switch-simple-demo',
                        disabled=True,
                    ),
                    fac.AntdSwitch(
                        id='switch-input-simple-demo',
                        checked=False,
                    ),
                ],
                align='center',
                gap=5,
            ),
        ],
        direction='vertical',
        style={
            'width': '100%',
        },
    )

    return demo_contents


# 基础回调展示
@app.callback(
    Output('switch-callback-output-demo', 'children'),
    Input('switch-callback-demo', 'checked'),
    prevent_initial_call=True,
)
def switch_callback_demo(checked):
    return f'checked: {checked}'


# 简单用例展示
@app.callback(
    Output('input-switch-simple-demo', 'disabled'),
    Input('switch-input-simple-demo', 'checked'),
    prevent_initial_call=True,
)
def switch_input_callback_demo(checked):
    return not checked


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('基础回调', innerTextOrientation='left'),
        fac.AntdSwitch(id='switch-callback-demo'),
        fac.AntdCard(
            id='switch-callback-output-demo',
            headStyle={'display': 'none'},
        ),
        fac.AntdDivider('简单用例', innerTextOrientation='left'),
        fac.AntdFlex(
            [
                fac.AntdInput(
                    placeholder='切换右侧开关状态以激活/禁用输入框',
                    id='input-switch-simple-demo',
                    disabled=True,
                ),
                fac.AntdSwitch(
                    id='switch-input-simple-demo',
                    checked=False,
                ),
            ],
            align='center',
            gap=5,
        ),
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)


# 基础回调展示
@app.callback(
    Output('switch-callback-output-demo', 'children'),
    Input('switch-callback-demo', 'checked'),
    prevent_initial_call=True,
)
def switch_callback_demo(checked):
    return f'checked: {checked}'


# 简单用例展示
@app.callback(
    Output('input-switch-simple-demo', 'disabled'),
    Input('switch-input-simple-demo', 'checked'),
    prevent_initial_call=True,
)
def switch_input_callback_demo(checked):
    return not checked
"""
    }
]
