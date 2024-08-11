import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider(
            '默认hideOnSinglePage=False', innerTextOrientation='left'
        ),
        fac.AntdPagination(total=10, pageSize=20),
        fac.AntdDivider('hideOnSinglePage=True', innerTextOrientation='left'),
        fac.AntdPagination(total=10, pageSize=20, hideOnSinglePage=True),
    ]

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDivider(
    '默认hideOnSinglePage=False',
    innerTextOrientation='left'
),

fac.AntdPagination(
    total=10,
    pageSize=20
),

fac.AntdDivider(
    'hideOnSinglePage=True',
    innerTextOrientation='left'
),

fac.AntdPagination(
    total=10,
    pageSize=20,
    hideOnSinglePage=True
)
"""
    }
]
