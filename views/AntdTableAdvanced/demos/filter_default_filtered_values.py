import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        col_title = '基础示例'
        data_key = '基础示例'
    elif current_locale == 'en-us':
        col_title = 'Basic Example'
        data_key = 'Basic Example'
    else:
        col_title = '基础示例'
        data_key = '基础示例'

    demo_contents = fac.AntdTable(
        columns=[{'title': col_title, 'dataIndex': data_key}],
        data=[{data_key: s} for s in list('abced')],
        filterOptions={data_key: {}},
        defaultFilteredValues={data_key: ['a', 'c', 'e']},
        style={'width': 200},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdTable(
    columns=[{'title': '基础示例', 'dataIndex': '基础示例'}],
    data=[{'基础示例': s} for s in list('abced')],
    filterOptions={'基础示例': {}},
    defaultFilteredValues={'基础示例': ['a', 'c', 'e']},
    style={'width': 200},
)
"""
            }
        ]
    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdTable(
    columns=[{'title': 'Basic Example', 'dataIndex': 'Basic Example'}],
    data=[{'Basic Example': s} for s in list('abced')],
    filterOptions={'Basic Example': {}},
    defaultFilteredValues={'Basic Example': ['a', 'c', 'e']},
    style={'width': 200},
)
"""
            }
        ]
