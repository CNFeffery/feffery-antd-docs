import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': '搜索型筛选',
                'dataIndex': '搜索型筛选',
            }
        ],
        data=[{'搜索型筛选': s} for s in list('abced')],
        filterOptions={'搜索型筛选': {'filterMode': 'keyword'}},
        style={'width': 200},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': '搜索型筛选',
            'dataIndex': '搜索型筛选',
        }
    ],
    data=[{'搜索型筛选': s} for s in list('abced')],
    filterOptions={'搜索型筛选': {'filterMode': 'keyword'}},
    style={'width': 200},
)
"""
    }
]
