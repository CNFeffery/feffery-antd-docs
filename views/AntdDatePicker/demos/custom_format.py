import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDatePicker(
                    placeholder='picker="date"',
                    format="YYYY年MM月DD日",
                    style={"width": 175},
                ),
                fac.AntdDatePicker(
                    placeholder='picker="week"',
                    picker="week",
                    format="YYYY年第w周",
                    style={"width": 175},
                ),
                fac.AntdDatePicker(
                    placeholder='picker="month"',
                    picker="month",
                    format="YYYY-MM",
                    style={"width": 175},
                ),
                fac.AntdDatePicker(
                    placeholder='picker="year"',
                    picker="year",
                    format="YYYY年",
                    style={"width": 175},
                ),
            ],
            direction="vertical",
        )
    else:
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDatePicker(
                    placeholder='picker="date"',
                    format="YYYY-MM-DD",
                    style={"width": 175},
                    locale="en-us",
                ),
                fac.AntdDatePicker(
                    placeholder='picker="week"',
                    picker="week",
                    format="YYYY [Week] w",
                    style={"width": 175},
                    locale="en-us",
                ),
                fac.AntdDatePicker(
                    placeholder='picker="month"',
                    picker="month",
                    format="YYYY-MM",
                    style={"width": 175},
                    locale="en-us",
                ),
                fac.AntdDatePicker(
                    placeholder='picker="year"',
                    picker="year",
                    format="YYYY",
                    style={"width": 175},
                    locale="en-us",
                ),
            ],
            direction="vertical",
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDatePicker(
            placeholder='picker="date"',
            format='YYYY年MM月DD日',
            style={'width': 175},
        ),
        fac.AntdDatePicker(
            placeholder='picker="week"',
            picker='week',
            format='YYYY年第w周',
            style={'width': 175},
        ),
        fac.AntdDatePicker(
            placeholder='picker="month"',
            picker='month',
            format='YYYY-MM',
            style={'width': 175},
        ),
        fac.AntdDatePicker(
            placeholder='picker="year"',
            picker='year',
            format='YYYY年',
            style={'width': 175},
        ),
    ],
    direction='vertical',
)
"""
            }
        ]
    else:
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDatePicker(
            placeholder='picker="date"',
            format='YYYY-MM-DD',
            style={'width': 175},
            locale="en-us"
        ),
        fac.AntdDatePicker(
            placeholder='picker="week"',
            picker='week',
            format='YYYY [Week] w',
            style={'width': 175},
            locale="en-us"
        ),
        fac.AntdDatePicker(
            placeholder='picker="month"',
            picker='month',
            format='YYYY-MM',
            style={'width': 175},
            locale="en-us"
        ),
        fac.AntdDatePicker(
            placeholder='picker="year"',
            picker='year',
            format='YYYY',
            style={'width': 175},
            locale="en-us"
        ),
    ],
    direction='vertical',
)
"""
            }
        ]
