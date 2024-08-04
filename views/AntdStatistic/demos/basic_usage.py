import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdFlex(
        [
            fac.AntdStatistic(title='数值型统计数值示例', value=1321321.3213),
            fac.AntdStatistic(title='字符型统计数值示例', value='99.65%'),
        ],
        gap='small',
        align='flex-start',
        vertical=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdFlex(
    [
        fac.AntdStatistic(title='数值型统计数值示例', value=1321321.3213),
        fac.AntdStatistic(title='字符型统计数值示例', value='99.65%'),
    ],
    gap='small',
    align='flex-start',
    vertical=True,
)
"""
    }
]
