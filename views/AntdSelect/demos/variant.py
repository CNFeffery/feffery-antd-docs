import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider("默认模式不同变体示例", innerTextOrientation="left"),
                fac.AntdSelect(
                    variant="outlined",
                    placeholder='variant="outlined"（默认）',
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    variant="filled",
                    placeholder='variant="filled"',
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    variant="underlined",
                    placeholder='variant="underlined"',
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    variant="borderless",
                    placeholder='variant="borderless"',
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdDivider("多选模式不同变体示例", innerTextOrientation="left"),
                fac.AntdSelect(
                    variant="outlined",
                    mode="multiple",
                    placeholder='variant="outlined"（默认）',
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    variant="filled",
                    mode="multiple",
                    placeholder='variant="filled"',
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    variant="borderless",
                    mode="multiple",
                    placeholder='variant="borderless"',
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    variant="underlined",
                    mode="multiple",
                    placeholder='variant="underlined"',
                    options=[f"选项{i}" for i in range(1, 6)],
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
                    "Variant examples (single select)", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    variant="outlined",
                    placeholder='variant="outlined" (default)',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="filled",
                    placeholder='variant="filled"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="underlined",
                    placeholder='variant="underlined"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="borderless",
                    placeholder='variant="borderless"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    "Variant examples (multiple select)", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    variant="outlined",
                    mode="multiple",
                    placeholder='variant="outlined" (default)',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="filled",
                    mode="multiple",
                    placeholder='variant="filled"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="borderless",
                    mode="multiple",
                    placeholder='variant="borderless"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="underlined",
                    mode="multiple",
                    placeholder='variant="underlined"',
                    options=[f"Option {i}" for i in range(1, 6)],
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
        fac.AntdDivider(
            '默认模式不同变体示例', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            variant='outlined',
            placeholder='variant="outlined"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            variant='filled',
            placeholder='variant="filled"',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            variant='underlined',
            placeholder='variant="underlined"',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            variant='borderless',
            placeholder='variant="borderless"',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdDivider(
            '多选模式不同变体示例', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            variant='outlined',
            mode='multiple',
            placeholder='variant="outlined"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            variant='filled',
            mode='multiple',
            placeholder='variant="filled"',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            variant='borderless',
            mode='multiple',
            placeholder='variant="borderless"',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            variant='underlined',
            mode='multiple',
            placeholder='variant="underlined"',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdDivider(
                    "Variant examples (single select)", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    variant="outlined",
                    placeholder='variant="outlined" (default)',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="filled",
                    placeholder='variant="filled"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="underlined",
                    placeholder='variant="underlined"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="borderless",
                    placeholder='variant="borderless"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    "Variant examples (multiple select)", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    variant="outlined",
                    mode="multiple",
                    placeholder='variant="outlined" (default)',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="filled",
                    mode="multiple",
                    placeholder='variant="filled"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="borderless",
                    mode="multiple",
                    placeholder='variant="borderless"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    variant="underlined",
                    mode="multiple",
                    placeholder='variant="underlined"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
)
"""
            }
        ]
