import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSelect(
            options=[f"选项{i}" for i in range(1, 6)],
            mode="multiple",
            style={"width": 350},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSelect(
            options=[f"Option {i}" for i in range(1, 6)],
            mode="multiple",
            style={"width": 350},
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
    mode='multiple',
    style={'width': 350},
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
    mode='multiple',
    style={'width': 350},
    locale="en-us",
)
"""
            }
        ]
