import time
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdButton(
            '按钮示例',
            id='button-auto-spin-demo',
            loadingChildren='计算中',
            autoSpin=True,
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdButton(
            'Button',
            id='button-auto-spin-demo',
            loadingChildren='Calculating',
            autoSpin=True,
        )

    return demo_contents


@app.callback(
    Output('button-auto-spin-demo', 'loading'),
    Input('button-auto-spin-demo', 'nClicks'),
    prevent_initial_call=True,
)
def button_auto_spin_demo(nClicks):
    # 模拟计算任务耗时
    # simulate calculation
    time.sleep(2)

    return False


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdButton(
    '按钮示例',
    id='button-auto-spin-demo',
    loadingChildren='计算中',
    autoSpin=True,
)

...

@app.callback(
    Output('button-auto-spin-demo', 'loading'),
    Input('button-auto-spin-demo', 'nClicks'),
    prevent_initial_call=True,
)
def button_auto_spin_demo(nClicks):
    # 模拟计算任务耗时
    time.sleep(2)

    return False
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdButton(
    'Button',
    id='button-auto-spin-demo',
    loadingChildren='Calculating',
    autoSpin=True,
)

...

@app.callback(
    Output('button-auto-spin-demo', 'loading'),
    Input('button-auto-spin-demo', 'nClicks'),
    prevent_initial_call=True,
)
def button_auto_spin_demo(nClicks):
    # simulate calculation
    time.sleep(2)

    return False
"""
            }
        ]
