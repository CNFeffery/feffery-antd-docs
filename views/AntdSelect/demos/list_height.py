import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSelect(
                    placeholder="listHeight=400",
                    options=[f"选项{i}" for i in range(1, 26)],
                    listHeight=400,
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    placeholder="listHeight=100",
                    options=[f"选项{i}" for i in range(1, 26)],
                    listHeight=100,
                    style={"width": "100%"},
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSelect(
                    placeholder="listHeight=400",
                    options=[f"Option {i}" for i in range(1, 26)],
                    listHeight=400,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    placeholder="listHeight=100",
                    options=[f"Option {i}" for i in range(1, 26)],
                    listHeight=100,
                    style={"width": "100%"},
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    return demo_contents


def code_string() -> list:
    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
            [
                fac.AntdSelect(
                    placeholder="listHeight=400",
                    options=[f"选项{i}" for i in range(1, 26)],
                    listHeight=400,
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    placeholder="listHeight=100",
                    options=[f"选项{i}" for i in range(1, 26)],
                    listHeight=100,
                    style={"width": "100%"},
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSpace(
            [
                fac.AntdSelect(
                    placeholder="listHeight=400",
                    options=[f"Option {i}" for i in range(1, 26)],
                    listHeight=400,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    placeholder="listHeight=100",
                    options=[f"Option {i}" for i in range(1, 26)],
                    listHeight=100,
                    style={"width": "100%"},
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )
"""
            }
        ]
