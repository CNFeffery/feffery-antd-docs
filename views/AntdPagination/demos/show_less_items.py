import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider(
            'showLessItems=False（默认）', innerTextOrientation='left'
        ),
        fac.AntdPagination(defaultPageSize=10, total=100, current=5),
        fac.AntdDivider('showLessItems=True', innerTextOrientation='left'),
        fac.AntdPagination(
            defaultPageSize=10, total=100, showLessItems=True, current=5
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDivider(
    'showLessItems=False（默认）',
    innerTextOrientation='left'
),
fac.AntdPagination(
    defaultPageSize=10,
    total=100,
    current=5
),

fac.AntdDivider(
    'showLessItems=True',
    innerTextOrientation='left'
),
fac.AntdPagination(
    defaultPageSize=10,
    total=100,
    showLessItems=True,
    current=5
)
"""
    }
]
