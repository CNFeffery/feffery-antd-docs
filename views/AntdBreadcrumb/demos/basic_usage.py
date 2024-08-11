import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdBreadcrumb(
        items=[
            {'title': '首页'},
            {'title': '下属页面1'},
            {'title': '下属页面1-1'},
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdBreadcrumb(
    items=[
        {
            'title': '首页'
        },
        {
            'title': '下属页面1'
        },
        {
            'title': '下属页面1-1'
        }
    ]
)
"""
    }
]
