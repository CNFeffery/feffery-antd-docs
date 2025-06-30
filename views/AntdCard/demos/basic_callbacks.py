import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, ALL
from dash import html
from server import app
import dash


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('卡片点击回调监听', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    fac.AntdCard(
                        f'卡片{i}',
                        id={'type': 'card-click-demo', 'index': i},
                        # 设置鼠标悬浮指针为点击样式
                        style={'cursor': 'pointer'},
                        styles={'header': {'display': 'none'}},
                    )
                    for i in range(1, 4)
                ],
                wrap=True,
            ),
            html.Div('未点击卡片', id='card-click-demo-output'),
            fac.AntdDivider(
                '卡片网格点击回调监听', innerTextOrientation='left'
            ),
            fac.AntdCard(
                [
                    fac.AntdCardGrid(
                        f'卡片网格{i}',
                        id={'type': 'card-grid-click-demo', 'index': i},
                        # 设置鼠标悬浮指针为点击样式
                        style={'cursor': 'pointer'},
                    )
                    for i in range(1, 4)
                ],
                style={'width': 300, 'marginBottom': 10},
                styles={'header': {'display': 'none'}},
            ),
            html.Div('未点击卡片网格', id='card-grid-click-demo-output'),
        ],
        direction='vertical',
    )

    return demo_contents


# 点击卡片回调函数
@app.callback(
    Output('card-click-demo-output', 'children'),
    Input({'type': 'card-click-demo', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True,
)
def card_click_callback(nClicks):
    nClicks = [i for i in nClicks if i is not None]
    num = sum(nClicks)
    current_card = f'卡片{dash.ctx.triggered_id["index"]}'
    return f'卡片已点击{num}次，当前点击的是：{current_card}'


# 点击卡片网格回调函数
@app.callback(
    Output('card-grid-click-demo-output', 'children'),
    Input({'type': 'card-grid-click-demo', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True,
)
def card_grid_click_callback(nClicks):
    nClicks = [i for i in nClicks if i is not None]
    num = sum(nClicks)
    current_card = f'卡片网格{dash.ctx.triggered_id["index"]}'
    return f'卡片网格已点击{num}次，当前点击的是：{current_card}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('卡片点击回调监听', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                fac.AntdCard(
                    f'卡片{i}',
                    id={'type': 'card-click-demo', 'index': i},
                    # 设置鼠标悬浮指针为点击样式
                    style={'cursor': 'pointer'},
                    styles={'header': {'display': 'none'}},
                )
                for i in range(1, 4)
            ],
            wrap=True,
        ),
        html.Div('未点击卡片', id='card-click-demo-output'),
        fac.AntdDivider(
            '卡片网格点击回调监听', innerTextOrientation='left'
        ),
        fac.AntdCard(
            [
                fac.AntdCardGrid(
                    f'卡片网格{i}',
                    id={'type': 'card-grid-click-demo', 'index': i},
                    # 设置鼠标悬浮指针为点击样式
                    style={'cursor': 'pointer'},
                )
                for i in range(1, 4)
            ],
            style={'width': 300, 'marginBottom': 10},
            styles={'header': {'display': 'none'}},
        ),
        html.Div('未点击卡片网格', id='card-grid-click-demo-output'),
    ],
    direction='vertical',
)


# 点击卡片回调函数
@app.callback(
    Output('card-click-demo-output', 'children'),
    Input({'type': 'card-click-demo', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True,
)
def card_click_callback(nClicks):
    nClicks = [i for i in nClicks if i is not None]
    num = sum(nClicks)
    current_card = f"卡片{dash.ctx.triggered_id['index']}"
    return f'卡片已点击{num}次，当前点击的是：{current_card}'


# 点击卡片网格回调函数
@app.callback(
    Output('card-grid-click-demo-output', 'children'),
    Input({'type': 'card-grid-click-demo', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True,
)
def card_grid_click_callback(nClicks):
    nClicks = [i for i in nClicks if i is not None]
    num = sum(nClicks)
    current_card = f"卡片网格{dash.ctx.triggered_id['index']}"
    return f'卡片网格已点击{num}次，当前点击的是：{current_card}'
"""
    }
]
