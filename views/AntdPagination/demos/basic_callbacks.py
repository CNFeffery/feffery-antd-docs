import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(id='pagination-demo-output', direction='vertical'),
        fac.AntdPagination(
            id='pagination-demo',
            defaultPageSize=10,
            total=100,
            pageSizeOptions=[5, 10, 20],
            showSizeChanger=True
        ),
    ]

    return demo_contents


@app.callback(
    Output('pagination-demo-output', 'children'),
    [Input('pagination-demo', 'current'), Input('pagination-demo', 'pageSize')],
)
def pagination_callback_demo(current, pageSize):
    return [
        fac.AntdText(f'内容项{i}')
        for i in range((current - 1) * pageSize, current * pageSize)
    ]


code_string = [
    {
        'code': """
fac.AntdSpace(
    id='pagination-demo-output',
    direction='vertical'
),

fac.AntdPagination(
    id='pagination-demo',
    defaultPageSize=10,
    total=100,
    pageSizeOptions=[5, 10, 20],
    showSizeChanger=True
)

...

@app.callback(
    Output('pagination-demo-output', 'children'),
    [Input('pagination-demo', 'current'),
     Input('pagination-demo', 'pageSize')]
)
def pagination_callback_demo(current, pageSize):

    return [
        fac.AntdText(f'内容项{i}')
        for i in range((current - 1) * pageSize, current * pageSize)
    ]
"""
    }
]
