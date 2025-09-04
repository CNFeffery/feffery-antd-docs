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
                            options=[f"选项{i}" for i in range(1, 6)],
                            placeholder=f'placement="{placement}"',
                            placement=placement,
                            popupMatchSelectWidth=False,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                        )
                        for placement in [
                            "bottomLeft",
                            "bottomRight",
                            "topLeft",
                            "topRight",
                        ]
                    ],
                    direction="vertical",
                    style={"width": 350},
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
                            options=[f"Option {i}" for i in range(1, 6)],
                            placeholder=f'placement="{placement}"',
                            placement=placement,
                            popupMatchSelectWidth=False,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                            locale="en-us",
                        )
                        for placement in [
                            "bottomLeft",
                            "bottomRight",
                            "topLeft",
                            "topRight",
                        ]
                    ],
                    direction="vertical",
                    style={"width": 350},
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
                            options=[f"选项{i}" for i in range(1, 6)],
                            placeholder=f'placement="{placement}"',
                            placement=placement,
                            popupMatchSelectWidth=False,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                        )
                        for placement in [
                            "bottomLeft",
                            "bottomRight",
                            "topLeft",
                            "topRight",
                        ]
                    ],
                    direction="vertical",
                    style={"width": 350},
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
                            options=[f"Option {i}" for i in range(1, 6)],
                            placeholder=f'placement="{placement}"',
                            placement=placement,
                            popupMatchSelectWidth=False,
                            popupClassName="popup-custom-style",
                            style={"width": "100%"},
                            locale="en-us",
                        )
                        for placement in [
                            "bottomLeft",
                            "bottomRight",
                            "topLeft",
                            "topRight",
                        ]
                    ],
                    direction="vertical",
                    style={"width": 350},
                ),
            ]
        )"""
            }
        ]
