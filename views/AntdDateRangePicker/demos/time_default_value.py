import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDateRangePicker(
        placeholder=['开始日期时间', '结束日期时间'],
        showTime={'defaultValue': ['08:30:00', '17:30:00']},
        needConfirm=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDateRangePicker(
    placeholder=['开始日期时间', '结束日期时间'],
    showTime={'defaultValue': ['08:30:00', '17:30:00']},
    needConfirm=True,
)
"""
    }
]
