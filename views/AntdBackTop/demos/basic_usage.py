import feffery_antd_components as fac
from dash.dependencies import Component
from dash import html


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            fac.AntdBackTop(containerId='back-top-container-demo', duration=1),
            fac.AntdTitle('向下滚动一段距离', level=4),
        ]
        + [html.Div([i if i % 2 == 0 else html.Br() for i in range(200)])],
        id='back-top-container-demo',
        style={
            'maxHeight': '500px',
            'overflowY': 'auto',
            'position': 'relative',
            'backgroundColor': 'rgba(240, 240, 240, 0.2)',
            'border': '1px solid #f0f0f0',
            'padding': '20px',
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
html.Div(
    [
        fac.AntdBackTop(containerId='back-top-container-demo', duration=1),
        fac.AntdTitle('向下滚动一段距离', level=4),
    ]
    + [html.Div([i if i % 2 == 0 else html.Br() for i in range(200)])],
    id='back-top-container-demo',
    style={
        'maxHeight': '500px',
        'overflowY': 'auto',
        'position': 'relative',
        'backgroundColor': 'rgba(240, 240, 240, 0.2)',
        'border': '1px solid #f0f0f0',
        'padding': '20px',
    },
)
"""
    }
]
