import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSteps(
        steps=[
            {
                'title': 'Login',
                'status': 'finish',
                'icon': fac.AntdIcon(icon='antd-user'),
            },
            {
                'title': 'Verification',
                'status': 'finish',
                'icon': fac.AntdIcon(icon='antd-file-protect'),
            },
            {
                'title': 'Pay',
                'status': 'process',
                'icon': fac.AntdIcon(icon='antd-loading'),
            },
            {
                'title': 'Done',
                'status': 'wait',
                'icon': fac.AntdIcon(icon='antd-smile'),
            },
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSteps(
    steps=[
        {
            'title': 'Login',
            'status': 'finish',
            'icon': fac.AntdIcon(icon='antd-user'),
        },
        {
            'title': 'Verification',
            'status': 'finish',
            'icon': fac.AntdIcon(icon='antd-file-protect'),
        },
        {
            'title': 'Pay',
            'status': 'process',
            'icon': fac.AntdIcon(icon='antd-loading'),
        },
        {
            'title': 'Done',
            'status': 'wait',
            'icon': fac.AntdIcon(icon='antd-smile'),
        },
    ]
)
"""
    }
]
