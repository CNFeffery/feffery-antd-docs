import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTimeRangePicker(
        defaultValue=['11:00:00', '12:00:00'],
        suffixIcon=fac.AntdIcon(icon='antd-user'),
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTimeRangePicker(
    defaultValue=['11:00:00', '12:00:00'],
    suffixIcon=fac.AntdIcon(icon='antd-user'),
)
"""
    }
]
