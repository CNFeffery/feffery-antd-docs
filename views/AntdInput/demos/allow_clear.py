import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                value='内容',
                placeholder='mode="default"（默认）',
                allowClear=True,
            ),
            fac.AntdInput(
                value='内容',
                placeholder='mode="search"',
                mode='search',
                allowClear=True,
            ),
            fac.AntdInput(
                value='内容',
                placeholder='mode="text-area"',
                mode='text-area',
                allowClear=True,
            ),
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
        fac.AntdInput(
            value='内容',
            placeholder='mode="default"（默认）',
            allowClear=True,
        ),
        fac.AntdInput(
            value='内容',
            placeholder='mode="search"',
            mode='search',
            allowClear=True,
        ),
        fac.AntdInput(
            value='内容',
            placeholder='mode="text-area"',
            mode='text-area',
            allowClear=True,
        ),
    ],
    direction='vertical',
    style={'width': '350px'},
)
"""
    }
]
