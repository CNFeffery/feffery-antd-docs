import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdSpace(id='pagination-demo-output', direction='vertical'),
            fac.AntdPagination(
                id='pagination-demo',
                defaultPageSize=10,
                total=100,
                pageSizeOptions=[5, 10, 20],
                showSizeChanger=True,
            ),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdSpace(id='pagination-demo-output', direction='vertical'),
            fac.AntdPagination(
                id='pagination-demo',
                defaultPageSize=10,
                total=100,
                pageSizeOptions=[5, 10, 20],
                showSizeChanger=True,
                locale='en-us',
            ),
        ]

    return demo_contents


@app.callback(
    Output('pagination-demo-output', 'children'),
    [Input('pagination-demo', 'current'), Input('pagination-demo', 'pageSize')],
)
def pagination_callback_demo(current, pageSize):
    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            fac.AntdText(f'内容项{i}')
            for i in range((current - 1) * pageSize, current * pageSize)
        ]

    elif current_locale == 'en-us':
        return [
            fac.AntdText(f'Item {i}')
            for i in range((current - 1) * pageSize, current * pageSize)
        ]


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdSpace(id='pagination-demo-output', direction='vertical'),
    fac.AntdPagination(
        id='pagination-demo',
        defaultPageSize=10,
        total=100,
        pageSizeOptions=[5, 10, 20],
        showSizeChanger=True,
    ),
]

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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdSpace(id='pagination-demo-output', direction='vertical'),
    fac.AntdPagination(
        id='pagination-demo',
        defaultPageSize=10,
        total=100,
        pageSizeOptions=[5, 10, 20],
        showSizeChanger=True,
        locale='en-us',
    ),
]

...

@app.callback(
    Output('pagination-demo-output', 'children'),
    [Input('pagination-demo', 'current'),
     Input('pagination-demo', 'pageSize')]
)
def pagination_callback_demo(current, pageSize):

    return [
        fac.AntdText(f'Item {i}')
        for i in range((current - 1) * pageSize, current * pageSize)
    ]
"""
            }
        ]
