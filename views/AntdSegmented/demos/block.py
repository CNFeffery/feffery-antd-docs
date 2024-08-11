import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSegmented(
        options=[
            {'label': f'{i}', 'value': i}
            for i in [123, 456, 'longtext-longtext-longtext-longtext']
        ],
        defaultValue=123,
        block=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSegmented(
    options=[
        {'label': f'{i}', 'value': i}
        for i in [123, 456, 'longtext-longtext-longtext-longtext']
    ],
    defaultValue=123,
    block=True,
)
"""
    }
]
