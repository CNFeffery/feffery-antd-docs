import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider("align='start'"),
        fac.AntdPagination(defaultPageSize=10, total=100, align='start'),
        fac.AntdDivider("align='center'"),
        fac.AntdPagination(defaultPageSize=10, total=100, align='center'),
        fac.AntdDivider("align='end'"),
        fac.AntdPagination(defaultPageSize=10, total=100, align='end'),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider("align='start'"),
    fac.AntdPagination(defaultPageSize=10, total=100, align='start'),
    fac.AntdDivider("align='center'"),
    fac.AntdPagination(defaultPageSize=10, total=100, align='center'),
    fac.AntdDivider("align='end'"),
    fac.AntdPagination(defaultPageSize=10, total=100, align='end'),
]
"""
    }
]
