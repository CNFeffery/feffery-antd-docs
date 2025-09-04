import time

import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render this demo case"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        tip_text = "点击切换后loading 3秒："
    elif current_locale == "en-us":
        tip_text = "After toggling, loading for 3 seconds:"

    demo_contents = fac.AntdSpace(
        [
            fac.AntdSwitch(loading=True),
            fac.AntdSwitch(loading=True, checked=True),
            fac.AntdText(tip_text),
            fac.AntdSwitch(
                # 需要设置好checked参数，否则会无法避免初次加载
                checked=False,
                id="switch-loading-demo",
            ),
            html.Div(id="switch-output-demo"),
        ],
        direction="vertical",
        style={"width": "100%"},
    )

    return demo_contents


@app.callback(
    Output("switch-output-demo", "children"),
    Input("switch-loading-demo", "checked"),
    # 配合running参数，实现回调运行中和运行结束后设置loading状态的效果
    running=[[Output("switch-loading-demo", "loading"), True, False]],
    prevent_initial_call=True,
)
def callback_func(checked):
    # 模拟进行一些耗时的回调内操作
    time.sleep(3)

    locale = get_current_locale()
    if locale == "zh-cn":
        content = "已开启" if checked else "已关闭"
    else:
        content = "Turned on" if checked else "Turned off"

    return fac.AntdMessage(
        content=content,
        type="success" if checked else "warning",
    )


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for current locale"""

    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdSwitch(loading=True),
        fac.AntdSwitch(loading=True, checked=True),
        fac.AntdText('点击切换后loading 3秒：'),
        fac.AntdSwitch(
            # 需要设置好checked参数，否则会无法避免初次加载
            checked=False,
            id='switch-loading-demo',
        ),
        html.Div(id='switch-output-demo'),
    ],
    direction='vertical',
    style={'width': '100%'},
)


@app.callback(
    Output('switch-output-demo', 'children'),
    Input('switch-loading-demo', 'checked'),
    # 配合running参数，实现回调运行中和运行结束后设置loading状态的效果
    running=[[Output('switch-loading-demo', 'loading'), True, False]],
    prevent_initial_call=True,
)
def callback_func(checked):
    # 模拟进行一些耗时的回调内操作
    time.sleep(3)

    return fac.AntdMessage(
        content='已开启' if checked else '已关闭',
        type='success' if checked else 'warning',
    )
"""
            }
        ]
    elif locale == "en-us":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdSwitch(loading=True),
        fac.AntdSwitch(loading=True, checked=True),
        fac.AntdText('After toggling, loading for 3 seconds:'),
        fac.AntdSwitch(
            checked=False,
            id='switch-loading-demo',
        ),
        html.Div(id='switch-output-demo'),
    ],
    direction='vertical',
    style={'width': '100%'},
)


@app.callback(
    Output('switch-output-demo', 'children'),
    Input('switch-loading-demo', 'checked'),
    running=[[Output('switch-loading-demo', 'loading'), True, False]],
    prevent_initial_call=True,
)
def callback_func(checked):
    time.sleep(3)

    return fac.AntdMessage(
        content='Turned on' if checked else 'Turned off',
        type='success' if checked else 'warning',
    )
"""
            }
        ]
