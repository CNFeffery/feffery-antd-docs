import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDatePicker(
        placeholder='请选择日期时间', showTime={'defaultValue': '18:33:33'}
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDatePicker(
    placeholder='请选择日期时间', showTime={'defaultValue': '18:33:33'}
)
"""
    }
]
