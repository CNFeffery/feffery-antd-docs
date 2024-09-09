import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdPageHeader(
            id='page-header-demo',
            title='页头标题示例',
            subTitle='页头副标题示例',
            historyBackDisabled=True,
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdPageHeader(
            id='page-header-demo',
            title='Page Header',
            subTitle='Page Header Subtitle',
            historyBackDisabled=True,
        )

    return demo_contents


@app.callback(
    Output('page-header-demo', 'children'),
    Input('page-header-demo', 'backClicks'),
)
def page_header_demo_callback(backClicks):
    return [fac.AntdText('backClicks: ', strong=True), fac.AntdText(backClicks)]


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdPageHeader(
    id='page-header-demo',
    title='Page Header',
    subTitle='Page Header Subtitle',
    historyBackDisabled=True,
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
