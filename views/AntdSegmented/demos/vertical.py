import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSegmented(
        options=[
            {'label': i, 'value': i}
            for i in ['Daily', 'Weekly', 'Monthly', 'Quarterly', 'Yearly']
        ],
        defaultValue='Daily',
        vertical=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSegmented(
    options=[
        {'label': i, 'value': i}
        for i in ['Daily', 'Weekly', 'Monthly', 'Quarterly', 'Yearly']
    ],
    defaultValue='Daily',
    vertical=True,
)
"""
    }
]
