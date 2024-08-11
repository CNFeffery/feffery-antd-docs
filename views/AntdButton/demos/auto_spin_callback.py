import time
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdButton(
        '按钮示例',
        id='button-auto-spin-demo',
        loadingChildren='计算中',
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
    time.sleep(2)

    return False


code_string = [
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
