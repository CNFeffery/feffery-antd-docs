import feffery_antd_components as fac
from dash.dependencies import Component
from dash.dependencies import Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdFormItem(
                fac.AntdSwitch(
                    id='control-table-scroll-to-first-row-on-change-demo',
                    checked=True,
                ),
                label='scrollToFirstRowOnChange',
            ),
            fac.AntdTable(
                id='table-scroll-to-first-row-on-change-demo',
                columns=[
                    {'title': f'字段{i}', 'dataIndex': f'字段{i}'}
                    for i in range(1, 6)
                ],
                data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 50,
                maxHeight=150,
                scrollToFirstRowOnChange=False,
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output(
        'table-scroll-to-first-row-on-change-demo', 'scrollToFirstRowOnChange'
    ),
    Input('control-table-scroll-to-first-row-on-change-demo', 'checked'),
)
def control_table_scroll_to_first_row_on_change(checked):
    return checked


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='control-table-scroll-to-first-row-on-change-demo',
                checked=True,
            ),
            label='scrollToFirstRowOnChange',
        ),
        fac.AntdTable(
            id='table-scroll-to-first-row-on-change-demo',
            columns=[
                {'title': f'字段{i}', 'dataIndex': f'字段{i}'}
                for i in range(1, 6)
            ],
            data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 50,
            maxHeight=150,
            scrollToFirstRowOnChange=False,
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output(
        'table-scroll-to-first-row-on-change-demo', 'scrollToFirstRowOnChange'
    ),
    Input('control-table-scroll-to-first-row-on-change-demo', 'checked'),
)
def control_table_scroll_to_first_row_on_change(checked):
    return checked
"""
    }
]
