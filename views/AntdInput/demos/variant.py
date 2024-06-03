import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                variant='outlined', placeholder='variant="outlined"（默认）'
            ),
            fac.AntdInput(variant='filled', placeholder='variant="filled"'),
            fac.AntdInput(
                variant='borderless', placeholder='variant="borderless"'
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
            placeholder='mode="default"（默认）'
        ),

        fac.AntdInput(
            placeholder='mode="search"',
            mode='search'
        ),

        fac.AntdInput(
            placeholder='mode="text-area"',
            mode='text-area'
        ),

        fac.AntdInput(
            placeholder='mode="password"',
            mode='password'
        )
    ],
    direction='vertical',
    style={
        'width': '350px'
    }
)
"""
    }
]
