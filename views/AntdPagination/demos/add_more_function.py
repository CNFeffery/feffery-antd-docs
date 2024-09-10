import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdPagination(
            defaultPageSize=10,
            total=100,
            showQuickJumper=True,
            showSizeChanger=False,
            showTotalPrefix='总记录数：',
            showTotalSuffix='条！🧐',
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdPagination(
            defaultPageSize=10,
            total=100,
            showQuickJumper=True,
            showSizeChanger=False,
            showTotalPrefix='Total records: ',
            showTotalSuffix=' items!🧐',
            locale='en-us',
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdPagination(
    defaultPageSize=10,
    total=100,
    showQuickJumper=True,
    showSizeChanger=False,
    showTotalPrefix='总记录数：',
    showTotalSuffix='条！🧐'
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdPagination(
    defaultPageSize=10,
    total=100,
    showQuickJumper=True,
    showSizeChanger=False,
    showTotalPrefix='Total records: ',
    showTotalSuffix=' items!🧐',
    locale='en-us',
)
"""
            }
        ]
