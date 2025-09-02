import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        col_title = '搜索型筛选'
        data_key = '搜索型筛选'
    elif current_locale == 'en-us':
        col_title = 'Search Filter'
        data_key = 'Search Filter'
    else:
        col_title = '搜索型筛选'
        data_key = '搜索型筛选'

    demo_contents = fac.AntdTable(
        columns=[{'title': col_title, 'dataIndex': data_key}],
        data=[{data_key: s} for s in list('abced')],
        filterOptions={data_key: {'filterMode': 'keyword'}},
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
    columns=[{'title': '搜索型筛选', 'dataIndex': '搜索型筛选'}],
    data=[{'搜索型筛选': s} for s in list('abced')],
    filterOptions={'搜索型筛选': {'filterMode': 'keyword'}},
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
    columns=[{'title': 'Search Filter', 'dataIndex': 'Search Filter'}],
    data=[{'Search Filter': s} for s in list('abced')],
    filterOptions={'Search Filter': {'filterMode': 'keyword'}},
    style={'width': 200},
)
"""
            }
        ]
