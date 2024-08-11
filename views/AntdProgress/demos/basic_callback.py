import feffery_antd_components as fac
from dash.dependencies import Component
from dash.dependencies import Input, Output
from dash import DiskcacheManager
from server import app
import time
import diskcache


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdProgress(id='progress-demo-line', style={'width': 200}),
            fac.AntdProgress(id='progress-demo-dashboard', type='dashboard'),
            fac.AntdProgress(id='progress-demo-circle', type='dashboard'),
            fac.AntdButton(
                '执行任务',
                type='primary',
                loadingChildren='执行中',
                id='progress-demo-start-button',
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


# 定义background回调所需的后端缓存管理器
cache = diskcache.Cache('./cache')
background_callback_manager = DiskcacheManager(cache)


@app.callback(
    Input('progress-demo-start-button', 'nClicks'),
    # 配合running参数，使button在任务执行时显示loading状态，任务结束后恢复初始状态
    running=[Output('progress-demo-start-button', 'loading'), True, False],
    # 配合progress参数，使进度条实时更新
    progress=[
        Output('progress-demo-dashboard', 'percent'),
        Output('progress-demo-line', 'percent'),
        Output('progress-demo-circle', 'percent'),
    ],
    # 设置background回调模式
    background=True,
    interval=500,
    # 设置background回调的后端缓存管理器
    manager=background_callback_manager,
)
def execute_task(set_progress, nClicks):
    for i in range(1, 7):
        time.sleep(0.5)
        # 使用set_progress，在循环中同时更新多个进度条
        # set_progress仅接受一个参数
        set_progress((i * 20, i * 20, i * 20))


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdProgress(id='progress-demo-line', style={'width': 200}),
        fac.AntdProgress(id='progress-demo-dashboard', type='dashboard'),
        fac.AntdProgress(id='progress-demo-circle', type='dashboard'),
        fac.AntdButton(
            '执行任务',
            type='primary',
            loadingChildren='执行中',
            id='progress-demo-start-button',
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)


# 定义background回调所需的后端缓存管理器
cache = diskcache.Cache('./cache')
background_callback_manager = DiskcacheManager(cache)


@app.callback(
    Input('progress-demo-start-button', 'nClicks'),
    # 配合running参数，使button在任务执行时显示loading状态，任务结束后恢复初始状态
    running=[Output('progress-demo-start-button', 'loading'), True, False],
    # 配合progress参数，使进度条实时更新
    progress=[
        Output('progress-demo-dashboard', 'percent'),
        Output('progress-demo-line', 'percent'),
        Output('progress-demo-circle', 'percent'),
    ],
    # 设置background回调模式
    background=True,
    interval=500,
    # 设置background回调的后端缓存管理器
    manager=background_callback_manager,
)
def execute_task(set_progress, nClicks):
    for i in range(1, 7):
        time.sleep(0.5)
        # 使用set_progress，在循环中同时更新多个进度条
        # set_progress仅接受一个参数
        set_progress((i * 20, i * 20, i * 20))
"""
    }
]
