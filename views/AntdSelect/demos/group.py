import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSelect(
            options=[
                {
                    "group": "分组1",
                    "options": [
                        {"label": f"选项1-{i}", "value": f"选项1-{i}"}
                        for i in range(1, 4)
                    ],
                },
                {
                    "group": "分组2",
                    "options": [
                        {"label": f"选项2-{i}", "value": f"选项2-{i}"}
                        for i in range(1, 4)
                    ],
                },
            ],
            style={"width": 350},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSelect(
            options=[
                {
                    "group": "Group 1",
                    "options": [
                        {"label": f"Option 1-{i}", "value": f"Option 1-{i}"}
                        for i in range(1, 4)
                    ],
                },
                {
                    "group": "Group 2",
                    "options": [
                        {"label": f"Option 2-{i}", "value": f"Option 2-{i}"}
                        for i in range(1, 4)
                    ],
                },
            ],
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
            options=[
                {
                    "group": "分组1",
                    "options": [
                        {"label": f"选项1-{i}", "value": f"选项1-{i}"}
                        for i in range(1, 4)
                    ],
                },
                {
                    "group": "分组2",
                    "options": [
                        {"label": f"选项2-{i}", "value": f"选项2-{i}"}
                        for i in range(1, 4)
                    ],
                },
            ],
            style={"width": 350},
        )
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSelect(
            options=[
                {
                    "group": "Group 1",
                    "options": [
                        {"label": f"Option 1-{i}", "value": f"Option 1-{i}"}
                        for i in range(1, 4)
                    ],
                },
                {
                    "group": "Group 2",
                    "options": [
                        {"label": f"Option 2-{i}", "value": f"Option 2-{i}"}
                        for i in range(1, 4)
                    ],
                },
            ],
            style={"width": 350},
            locale="en-us",
        )
"""
            }
        ]
