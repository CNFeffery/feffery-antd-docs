import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    current_locale = get_current_locale()

    letters = ["A", "a", "B", "b", "c", "D", "e"]

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider("尝试搜索大小写字母", innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="case-insensitive",
                    optionFilterMode="case-insensitive",
                    options=[f"选项{i}-{index}" for index, i in enumerate(letters)],
                    style={"width": "100%"},
                ),
                fac.AntdDivider("尝试搜索大小写字母", innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="case-sensitive",
                    optionFilterMode="case-sensitive",
                    options=[f"选项{i}-{index}" for index, i in enumerate(letters)],
                    style={"width": "100%"},
                ),
                fac.AntdDivider(
                    "尝试搜索[a-z]、[a-z]|[A-Z]、[0-9]等", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    placeholder="regex",
                    optionFilterMode="regex",
                    options=[f"选项{i}-{index}" for index, i in enumerate(letters)],
                    style={"width": "100%"},
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider(
                    "Try searching uppercase/lowercase letters",
                    innerTextOrientation="left",
                ),
                fac.AntdSelect(
                    placeholder="case-insensitive",
                    optionFilterMode="case-insensitive",
                    options=[f"Option {i}-{index}" for index, i in enumerate(letters)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    "Try searching uppercase/lowercase letters",
                    innerTextOrientation="left",
                ),
                fac.AntdSelect(
                    placeholder="case-sensitive",
                    optionFilterMode="case-sensitive",
                    options=[f"Option {i}-{index}" for index, i in enumerate(letters)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    "Try searching [a-z], [a-z]|[A-Z], [0-9], etc.",
                    innerTextOrientation="left",
                ),
                fac.AntdSelect(
                    placeholder="regex",
                    optionFilterMode="regex",
                    options=[f"Option {i}-{index}" for index, i in enumerate(letters)],
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
                fac.AntdDivider("尝试搜索大小写字母", innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="case-insensitive",
                    optionFilterMode="case-insensitive",
                    options=[f"选项{i}-{index}" for index, i in enumerate(letters)],
                    style={"width": "100%"},
                ),
                fac.AntdDivider("尝试搜索大小写字母", innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="case-sensitive",
                    optionFilterMode="case-sensitive",
                    options=[f"选项{i}-{index}" for index, i in enumerate(letters)],
                    style={"width": "100%"},
                ),
                fac.AntdDivider(
                    "尝试搜索[a-z]、[a-z]|[A-Z]、[0-9]等", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    placeholder="regex",
                    optionFilterMode="regex",
                    options=[f"选项{i}-{index}" for index, i in enumerate(letters)],
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
                fac.AntdDivider(
                    "Try searching uppercase/lowercase letters",
                    innerTextOrientation="left",
                ),
                fac.AntdSelect(
                    placeholder="case-insensitive",
                    optionFilterMode="case-insensitive",
                    options=[f"Option {i}-{index}" for index, i in enumerate(letters)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    "Try searching uppercase/lowercase letters",
                    innerTextOrientation="left",
                ),
                fac.AntdSelect(
                    placeholder="case-sensitive",
                    optionFilterMode="case-sensitive",
                    options=[f"Option {i}-{index}" for index, i in enumerate(letters)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    "Try searching [a-z], [a-z]|[A-Z], [0-9], etc.",
                    innerTextOrientation="left",
                ),
                fac.AntdSelect(
                    placeholder="regex",
                    optionFilterMode="regex",
                    options=[f"Option {i}-{index}" for index, i in enumerate(letters)],
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
