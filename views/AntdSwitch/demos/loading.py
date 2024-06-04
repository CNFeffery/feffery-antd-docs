import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app
import time
from dash import html


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
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

    return demo_contents


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


code_string = [
    {
        'code': """
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
