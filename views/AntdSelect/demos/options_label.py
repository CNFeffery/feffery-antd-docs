import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSelect(
            options=[
                {
                    "label": fac.AntdFlex(
                        [
                            fac.AntdAvatar(text=f"{i}", mode="text", size="small"),
                            fac.AntdTag(
                                content=f"选项{i}",
                                color=["blue", "green", "purple", "orange", "cyan"][
                                    i - 1
                                ],
                            ),
                        ],
                        justify="flex-start",
                        align="center",
                        gap=5,
                    ),
                    "value": f"选项{i}",
                }
                for i in range(1, 6)
            ],
            size="large",
            style={"width": 350},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSelect(
            options=[
                {
                    "label": fac.AntdFlex(
                        [
                            fac.AntdAvatar(text=f"{i}", mode="text", size="small"),
                            fac.AntdTag(
                                content=f"Option {i}",
                                color=["blue", "green", "purple", "orange", "cyan"][
                                    i - 1
                                ],
                            ),
                        ],
                        justify="flex-start",
                        align="center",
                        gap=5,
                    ),
                    "value": f"Option {i}",
                }
                for i in range(1, 6)
            ],
            size="large",
            style={"width": 350},
            locale="en-us",
        )

    return demo_contents


def code_string() -> list:
    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        return [
            {
                "code": """fac.AntdSelect(
            options=[
                {
                    "label": fac.AntdFlex(
                        [
                            fac.AntdAvatar(text=f"{i}", mode="text", size="small"),
                            fac.AntdTag(
                                content=f"选项{i}",
                                color=["blue", "green", "purple", "orange", "cyan"][
                                    i - 1
                                ],
                            ),
                        ],
                        justify="flex-start",
                        align="center",
                        gap=5,
                    ),
                    "value": f"选项{i}",
                }
                for i in range(1, 6)
            ],
            size="large",
            style={"width": 350},
        )"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """fac.AntdSelect(
            options=[
                {
                    "label": fac.AntdFlex(
                        [
                            fac.AntdAvatar(text=f"{i}", mode="text", size="small"),
                            fac.AntdTag(
                                content=f"Option {i}",
                                color=["blue", "green", "purple", "orange", "cyan"][
                                    i - 1
                                ],
                            ),
                        ],
                        justify="flex-start",
                        align="center",
                        gap=5,
                    ),
                    "value": f"Option {i}",
                }
                for i in range(1, 6)
            ],
            size="large",
            style={"width": 350},
            locale="en-us",
        )"""
            }
        ]
