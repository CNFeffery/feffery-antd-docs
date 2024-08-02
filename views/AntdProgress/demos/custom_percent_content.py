import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdProgress(
                percent=80, format={'prefix': '进度'}, style={'width': 200}
            ),
            fac.AntdProgress(
                percent=80, format={'suffix': '分'}, type='circle'
            ),
            fac.AntdProgress(
                percent=80, format={'content': '🚀🚀🚀'}, type='dashboard'
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdProgress(
            percent=80, format={'prefix': '进度'}, style={'width': 200}
        ),
        fac.AntdProgress(
            percent=80, format={'suffix': '分'}, type='circle'
        ),
        fac.AntdProgress(
            percent=80, format={'content': '🚀🚀🚀'}, type='dashboard'
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
