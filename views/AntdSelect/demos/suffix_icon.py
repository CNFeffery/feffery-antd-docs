import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSelect(
            options=[f"选项{i}" for i in range(1, 6)],
            value="选项1",
            suffixIcon=fac.AntdIcon(icon="antd-user"),
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSelect(
            options=[f"Option {i}" for i in range(1, 6)],
            value="Option 1",
            suffixIcon=fac.AntdIcon(icon="antd-user"),
            locale="en-us",
        )

    return demo_contents


def code_string() -> list:
    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSelect(
    options=[f'选项{i}' for i in range(1, 6)],
    value='选项1',
    suffixIcon=fac.AntdIcon(icon='antd-user'),
)
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSelect(
    options=[f'Option {i}' for i in range(1, 6)],
    value='Option 1',
    suffixIcon=fac.AntdIcon(icon='antd-user'),
    locale="en-us",
)
"""
            }
        ]
