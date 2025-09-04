import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash import html
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = html.Div(
            [
                fuc.FefferyStyle(
                    rawStyle=".popup-custom-style {min-width: 100px!important;}"
                ),
                fac.AntdSpace(
                    [
                        fac.AntdSelect(
                            options=[f"选项{i}" for i in range(1, 26)],
                            placeholder="popupMatchSelectWidth=True",
                            popupMatchSelectWidth=True,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                        ),
                        fac.AntdSelect(
                            options=[f"选项{i}" for i in range(1, 26)],
                            placeholder="popupMatchSelectWidth=False",
                            popupMatchSelectWidth=False,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                        ),
                    ],
                    direction="vertical",
                    style={"width": 350, "marginBottom": 5},
                ),
                fac.AntdParagraph(
                    [
                        "可以看到，即使设置了自定义的下拉选择菜单宽度，在",
                        fac.AntdText("popupMatchSelectWidth=True", code=True),
                        "时，弹出框的宽度仍与选择框的宽度一致，只有在",
                        fac.AntdText("popupMatchSelectWidth=False", code=True),
                        "时，下拉选择菜单的自定义宽度才能生效。同时不再使用虚拟滚动。",
                    ]
                ),
            ]
        )

    elif current_locale == "en-us":
        demo_contents = html.Div(
            [
                fuc.FefferyStyle(
                    rawStyle=".popup-custom-style {min-width: 100px!important;}"
                ),
                fac.AntdSpace(
                    [
                        fac.AntdSelect(
                            options=[f"Option {i}" for i in range(1, 26)],
                            placeholder="popupMatchSelectWidth=True",
                            popupMatchSelectWidth=True,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                            locale="en-us",
                        ),
                        fac.AntdSelect(
                            options=[f"Option {i}" for i in range(1, 26)],
                            placeholder="popupMatchSelectWidth=False",
                            popupMatchSelectWidth=False,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                            locale="en-us",
                        ),
                    ],
                    direction="vertical",
                    style={"width": 350, "marginBottom": 5},
                ),
                fac.AntdParagraph(
                    [
                        "As you can see, even with a custom dropdown width, when ",
                        fac.AntdText("popupMatchSelectWidth=True", code=True),
                        " the popup matches the select width. Only when ",
                        fac.AntdText("popupMatchSelectWidth=False", code=True),
                        " does the custom width take effect, and virtual scrolling is disabled.",
                    ]
                ),
            ]
        )

    return demo_contents


def code_string() -> list:
    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        return [
            {
                "code": """html.Div(
            [
                fuc.FefferyStyle(
                    rawStyle=".popup-custom-style {min-width: 100px!important;}"
                ),
                fac.AntdSpace(
                    [
                        fac.AntdSelect(
                            options=[f"选项{i}" for i in range(1, 26)],
                            placeholder="popupMatchSelectWidth=True",
                            popupMatchSelectWidth=True,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                        ),
                        fac.AntdSelect(
                            options=[f"选项{i}" for i in range(1, 26)],
                            placeholder="popupMatchSelectWidth=False",
                            popupMatchSelectWidth=False,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                        ),
                    ],
                    direction="vertical",
                    style={"width": 350, "marginBottom": 5},
                ),
                fac.AntdParagraph(
                    [
                        "可以看到，即使设置了自定义的下拉选择菜单宽度，在",
                        fac.AntdText("popupMatchSelectWidth=True", code=True),
                        "时，弹出框的宽度仍与选择框的宽度一致，只有在",
                        fac.AntdText("popupMatchSelectWidth=False", code=True),
                        "时，下拉选择菜单的自定义宽度才能生效。同时不再使用虚拟滚动。",
                    ]
                ),
            ]
        )"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """html.Div(
            [
                fuc.FefferyStyle(
                    rawStyle=".popup-custom-style {min-width: 100px!important;}"
                ),
                fac.AntdSpace(
                    [
                        fac.AntdSelect(
                            options=[f"Option {i}" for i in range(1, 26)],
                            placeholder="popupMatchSelectWidth=True",
                            popupMatchSelectWidth=True,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                            locale="en-us",
                        ),
                        fac.AntdSelect(
                            options=[f"Option {i}" for i in range(1, 26)],
                            placeholder="popupMatchSelectWidth=False",
                            popupMatchSelectWidth=False,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                            locale="en-us",
                        ),
                    ],
                    direction="vertical",
                    style={"width": 350, "marginBottom": 5},
                ),
                fac.AntdParagraph(
                    [
                        "As you can see, even with a custom dropdown width, when ",
                        fac.AntdText("popupMatchSelectWidth=True", code=True),
                        " the popup matches the select width. Only when ",
                        fac.AntdText("popupMatchSelectWidth=False", code=True),
                        " does the custom width take effect, and virtual scrolling is disabled.",
                    ]
                ),
            ]
        )"""
            }
        ]
