import feffery_antd_components as fac
from dash.dependencies import Component
from dash import html
from server import app
from dash.dependencies import Input, Output


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdText(id='back-top-demo-text'),
        html.Div(
            [
                fac.AntdBackTop(
                    id='back-top-callback-demo',
                    containerId='back-top-container-callback-demo',
                    duration=1,
                ),
                fac.AntdTitle('向下滚动一段距离并点击BackTop按钮', level=4),
            ]
            + [html.Div([i if i % 2 == 0 else html.Br() for i in range(200)])],
            id='back-top-container-callback-demo',
            style={
                'maxHeight': '500px',
                'overflowY': 'auto',
                'position': 'relative',
                'backgroundColor': 'rgba(240, 240, 240, 0.2)',
                'border': '1px solid #f0f0f0',
                'padding': '20px',
            },
        ),
    ]

    return demo_contents


@app.callback(
    Output('back-top-demo-text', 'children'),
    Input('back-top-callback-demo', 'nClicks'),
)
def back_top_demo_text(nClicks):
    if nClicks is not None:
        return f'nClicks: {nClicks}'


code_string = [
    {
        'code': """
fac.AntdText(id='back-top-demo-text'),
html.Div(
    [
        fac.AntdBackTop(
            id='back-top-callback-demo',
            containerId='back-top-container-callback-demo',
            duration=1,
        ),
        fac.AntdTitle('向下滚动一段距离并点击BackTop按钮', level=4),
    ]
    + [html.Div([i if i % 2 == 0 else html.Br() for i in range(200)])],
    id='back-top-container-callback-demo',
    style={
        'maxHeight': '500px',
        'overflowY': 'auto',
        'position': 'relative',
        'backgroundColor': 'rgba(240, 240, 240, 0.2)',
        'border': '1px solid #f0f0f0',
        'padding': '20px',
    },
)


@app.callback(
    Output('back-top-demo-text', 'children'),
    Input('back-top-callback-demo', 'nClicks'),
)
def back_top_demo_text(nClicks):
    if nClicks is not None:
        return f'nClicks: {nClicks}'
"""
    }
]
