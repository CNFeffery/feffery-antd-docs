import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[{'title': '基础示例', 'dataIndex': '基础示例'}],
        data=[{'基础示例': s} for s in list('abced')],
        filterOptions={'基础示例': {}},
        defaultFilteredValues={'基础示例': ['a', 'c', 'e']},
        style={'width': 200},
    )

    return demo_contents


code_string = [
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
