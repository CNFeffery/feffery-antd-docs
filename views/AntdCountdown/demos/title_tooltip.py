import feffery_antd_components as fac
from dash.dependencies import Component
from datetime import datetime, timedelta


def render() -> Component:
    """渲染当前演示用例"""

    deadline = datetime.now() + timedelta(seconds=2 * 24 * 60 * 60 + 30)

    # 构造演示用例相关内容
    demo_contents = fac.AntdCountdown(
        title='Countdown',
        titleTooltip='这是信息提示示例',
        value=deadline.strftime('%Y-%m-%d %H:%M:%S:%f'),
    )

    return demo_contents


code_string = [
    {
        'code': """
deadline = datetime.now() + timedelta(seconds=2 * 24 * 60 * 60 + 30)

fac.AntdCountdown(
    title='Countdown',
    value=deadline.strftime('%Y-%m-%d %H:%M:%S:%f'),
    titleTooltip='这是信息提示示例',
)
"""
    }
]
