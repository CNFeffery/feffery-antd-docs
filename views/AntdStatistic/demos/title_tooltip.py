import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdStatistic(
        title='数值统计示例', value=98.67, titleTooltip='这是信息提示示例'
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdStatistic(
    title='数值统计示例', value=98.67, titleTooltip='这是信息提示示例'
)
"""
    }
]
