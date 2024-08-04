import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdPageHeader(
        id='page-header-demo',
        title='页头标题示例',
        subTitle='页头副标题示例',
        historyBackDisabled=True,
    )

    return demo_contents


@app.callback(
    Output('page-header-demo', 'children'),
    Input('page-header-demo', 'backClicks'),
)
def page_header_demo_callback(backClicks):
    return [fac.AntdText('backClicks: ', strong=True), fac.AntdText(backClicks)]


code_string = [
    {
        'code': """
fac.AntdPageHeader(
    id='page-header-demo',
    title='页头标题示例',
    subTitle='页头副标题示例',
    historyBackDisabled=True
)

...

@app.callback(
    Output('page-header-demo', 'children'),
    Input('page-header-demo', 'backClicks')
)
def page_header_demo_callback(backClicks):
    return [
        fac.AntdText('backClicks: ', strong=True),
        fac.AntdText(backClicks)
    ]
"""
    }
]
