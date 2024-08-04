import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('基于AntdSpace', innerTextOrientation='left'),
        fac.AntdSpace(
            [fac.AntdButton(f'按钮{i}') for i in range(1, 6)], size=0
        ),
        fac.AntdDivider('基于AntdCompact', innerTextOrientation='left'),
        fac.AntdCompact([fac.AntdButton(f'按钮{i}') for i in range(1, 6)]),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider('基于AntdSpace', innerTextOrientation='left'),
    fac.AntdSpace(
        [fac.AntdButton(f'按钮{i}') for i in range(1, 6)], size=0
    ),
    fac.AntdDivider('基于AntdCompact', innerTextOrientation='left'),
    fac.AntdCompact([fac.AntdButton(f'按钮{i}') for i in range(1, 6)]),
]
"""
    }
]
