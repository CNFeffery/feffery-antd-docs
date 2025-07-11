import feffery_antd_components as fac
from dash.dependencies import Component
from datetime import datetime, timedelta


def render() -> Component:
    """渲染当前演示用例"""

    start_time = datetime.now() - timedelta(seconds=2 * 24 * 60 * 60 + 30)

    # 构造演示用例相关内容
    demo_contents = fac.AntdCountup(
        title='Countup',
        titleTooltip='这是信息提示示例',
        value=start_time.strftime('%Y-%m-%d %H:%M:%S:%f'),
    )

    return demo_contents


code_string = [
    {
        'code': """
start_time = datetime.now() - timedelta(seconds=2 * 24 * 60 * 60 + 30)

...

fac.AntdCountup(
    title='Countup',
    titleTooltip='这是信息提示示例',
    value=start_time.strftime('%Y-%m-%d %H:%M:%S:%f'),
)
"""
    }
]
