import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render this demo case"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        title_basic = "基础回调"
        title_simple = "简单用例"
        placeholder = "切换右侧开关状态以激活/禁用输入框"
    elif current_locale == "en-us":
        title_basic = "Basic callbacks"
        title_simple = "Simple example"
        placeholder = "Toggle the switch on the right to enable/disable the input"

    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(title_basic, innerTextOrientation="left"),
            fac.AntdSwitch(id="switch-callback-demo"),
            fac.AntdCard(
                id="switch-callback-output-demo",
                styles={"header": {"display": "none"}},
            ),
            fac.AntdDivider(title_simple, innerTextOrientation="left"),
            fac.AntdFlex(
                [
                    fac.AntdInput(
                        placeholder=placeholder,
                        id="input-switch-simple-demo",
                        disabled=True,
                    ),
                    fac.AntdSwitch(
                        id="switch-input-simple-demo",
                        checked=False,
                    ),
                ],
                align="center",
                gap=5,
            ),
        ],
        direction="vertical",
        style={"width": "100%"},
    )

    return demo_contents


# 基础回调展示 / Basic callback
@app.callback(
    Output("switch-callback-output-demo", "children"),
    Input("switch-callback-demo", "checked"),
    prevent_initial_call=True,
)
def switch_callback_demo(checked):
    # keeping label 'checked' consistent with source demo
    return f"checked: {checked}"


# 简单用例展示 / Simple example
@app.callback(
    Output("input-switch-simple-demo", "disabled"),
    Input("switch-input-simple-demo", "checked"),
    prevent_initial_call=True,
)
def switch_input_callback_demo(checked):
    return not checked


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDivider('基础回调', innerTextOrientation='left'),
        fac.AntdSwitch(id='switch-callback-demo'),
        fac.AntdCard(
            id='switch-callback-output-demo',
            styles={'header': {'display': 'none'}},
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
    style={'width': '100%'},
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
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDivider('Basic callbacks', innerTextOrientation='left'),
        fac.AntdSwitch(id='switch-callback-demo'),
        fac.AntdCard(
            id='switch-callback-output-demo',
            styles={'header': {'display': 'none'}},
        ),
        fac.AntdDivider('Simple example', innerTextOrientation='left'),
        fac.AntdFlex(
            [
                fac.AntdInput(
                    placeholder='Toggle the switch on the right to enable/disable the input',
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
    style={'width': '100%'},
)


@app.callback(
    Output('switch-callback-output-demo', 'children'),
    Input('switch-callback-demo', 'checked'),
    prevent_initial_call=True,
)
def switch_callback_demo(checked):
    return f'checked: {checked}'


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
