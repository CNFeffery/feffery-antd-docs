import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTimePicker(placeholder='请选择时间')

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTimePicker(placeholder='请选择时间')
"""
    }
]
