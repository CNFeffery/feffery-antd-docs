import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(disabled=True),
            fac.AntdInput(disabled=True, mode='search'),
            fac.AntdInput(disabled=True, mode='text-area'),
            fac.AntdInput(disabled=True, mode='password'),
        ],
        direction='vertical',
        style={'width': '350px'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(disabled=True),
        fac.AntdInput(disabled=True, mode='search'),
        fac.AntdInput(disabled=True, mode='text-area'),
        fac.AntdInput(disabled=True, mode='password'),
    ],
    direction='vertical',
    style={'width': '350px'},
)
"""
    }
]
