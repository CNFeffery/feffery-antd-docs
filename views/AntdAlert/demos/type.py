import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdAlert(message=f'{type.capitalize()} Text', type=type)
            for type in ['success', 'info', 'warning', 'error']
        ],
        direction='vertical',
        size='middle',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdAlert(message=f'{type.capitalize()} Text', type=type)
        for type in ['success', 'info', 'warning', 'error']
    ],
    direction='vertical',
    size='middle',
    style={'width': '100%'},
)
"""
    }
]
