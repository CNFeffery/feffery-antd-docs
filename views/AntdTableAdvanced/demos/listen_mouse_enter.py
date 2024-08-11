from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTable(
            id='table-hover-event-demo',
            columns=[
                {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
                for i in range(1, 6)
            ],
            data=[
                {
                    'key': f'row-{row}',
                    **{f'字段{i}': f'字段{i}第{row}行' for i in range(1, 6)},
                }
                for row in range(1, 6)
            ],
            bordered=True,
            enableHoverListen=True,
        ),
        html.Pre(id='table-hover-event-demo-output'),
    ]

    return demo_contents


app.clientside_callback(
    """( recentlyMouseEnterColumnDataIndex,
         recentlyMouseEnterRowKey,
         recentlyMouseEnterRow ) => {
        return JSON.stringify(
            {
                recentlyMouseEnterColumnDataIndex,
                recentlyMouseEnterRowKey,
                recentlyMouseEnterRow
            },
            null,
            4
        );
    }""",
    Output('table-hover-event-demo-output', 'children'),
    [
        Input('table-hover-event-demo', 'recentlyMouseEnterColumnDataIndex'),
        Input('table-hover-event-demo', 'recentlyMouseEnterRowKey'),
        Input('table-hover-event-demo', 'recentlyMouseEnterRow'),
    ],
    prevent_initial_call=True,
)


code_string = [
    {
        'code': '''
[
    fac.AntdTable(
        id='table-hover-event-demo',
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[
            {
                'key': f'row-{row}',
                **{f'字段{i}': f'字段{i}第{row}行' for i in range(1, 6)},
            }
            for row in range(1, 6)
        ],
        bordered=True,
        enableHoverListen=True,
    ),
    html.Pre(id='table-hover-event-demo-output'),
]

...

app.clientside_callback(
    """( recentlyMouseEnterColumnDataIndex,
         recentlyMouseEnterRowKey,
         recentlyMouseEnterRow ) => {
        return JSON.stringify(
            {
                recentlyMouseEnterColumnDataIndex,
                recentlyMouseEnterRowKey,
                recentlyMouseEnterRow
            },
            null,
            4
        );
    }""",
    Output('table-hover-event-demo-output', 'children'),
    [
        Input('table-hover-event-demo', 'recentlyMouseEnterColumnDataIndex'),
        Input('table-hover-event-demo', 'recentlyMouseEnterRowKey'),
        Input('table-hover-event-demo', 'recentlyMouseEnterRow'),
    ],
    prevent_initial_call=True,
)
'''
    }
]
