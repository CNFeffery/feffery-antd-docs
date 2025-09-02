import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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

    elif current_locale == 'en-us':
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
                        {'title': f'Field {i}', 'dataIndex': f'Field {i}'}
                        for i in range(1, 6)
                    ],
                    data=[
                        {f'Field {i}': 'Example Content' for i in range(1, 6)}
                    ]
                    * 50,
                    maxHeight=150,
                    scrollToFirstRowOnChange=False,
                    locale='en-us',
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


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
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
                {'title': f'Field {i}', 'dataIndex': f'Field {i}'}
                for i in range(1, 6)
            ],
            data=[{f'Field {i}': 'Example Content' for i in range(1, 6)}] * 50,
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
