import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        '项目1',
        fac.AntdDivider(direction='vertical'),
        '项目2',
        fac.AntdDivider(direction='vertical', lineColor='black'),
        '项目3',
        fac.AntdDivider(direction='vertical', lineColor='red'),
        '项目4',
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    '项目1',
    fac.AntdDivider(direction='vertical'),
    '项目2',
    fac.AntdDivider(direction='vertical', lineColor='black'),
    '项目3',
    fac.AntdDivider(direction='vertical', lineColor='red'),
    '项目4',
]
"""
    }
]
