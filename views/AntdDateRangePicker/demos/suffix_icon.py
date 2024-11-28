import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDateRangePicker(
        value=['2023-01-01', '2023-01-20'],
        suffixIcon=fac.AntdIcon(icon='antd-user'),
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDateRangePicker(
    value=['2023-01-01', '2023-01-20'],
    suffixIcon=fac.AntdIcon(icon='antd-user'),
)
"""
    }
]
