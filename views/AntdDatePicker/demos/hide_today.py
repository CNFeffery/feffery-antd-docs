import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        demo_contents = fac.AntdDatePicker(showToday=False)
    else:
        demo_contents = fac.AntdDatePicker(showToday=False, locale="en-us")

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdDatePicker(showToday=False)
"""
            }
        ]
    else:
        return [
            {
                "code": """
fac.AntdDatePicker(showToday=False, locale='en-us')
"""
            }
        ]
