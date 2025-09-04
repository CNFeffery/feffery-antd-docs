import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider("默认模式不同尺寸示例", innerTextOrientation="left"),
                fac.AntdSelect(
                    size="small",
                    placeholder='size="small"',
                    options=[f"选项{i}" for i in range(1, 6)],
                    value="选项1",
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    size="middle",
                    placeholder='size="middle"（默认）',
                    options=[f"选项{i}" for i in range(1, 6)],
                    value="选项1",
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    size="large",
                    placeholder='size="large"',
                    options=[f"选项{i}" for i in range(1, 6)],
                    value="选项1",
                    style={"width": "100%"},
                ),
                fac.AntdDivider("多选模式不同尺寸示例", innerTextOrientation="left"),
                fac.AntdSelect(
                    size="small",
                    mode="multiple",
                    placeholder='size="small"',
                    options=[f"选项{i}" for i in range(1, 6)],
                    value=[f"选项{i}" for i in range(1, 3)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    size="middle",
                    mode="multiple",
                    placeholder='size="middle"（默认）',
                    options=[f"选项{i}" for i in range(1, 6)],
                    value=[f"选项{i}" for i in range(1, 3)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    size="large",
                    mode="multiple",
                    placeholder='size="large"',
                    options=[f"选项{i}" for i in range(1, 6)],
                    value=[f"选项{i}" for i in range(1, 3)],
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
                    "Size examples (single select)", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    size="small",
                    placeholder='size="small"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value="Option 1",
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    size="middle",
                    placeholder='size="middle" (default)',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value="Option 1",
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    size="large",
                    placeholder='size="large"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value="Option 1",
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    "Size examples (multiple select)", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    size="small",
                    mode="multiple",
                    placeholder='size="small"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value=[f"Option {i}" for i in range(1, 3)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    size="middle",
                    mode="multiple",
                    placeholder='size="middle" (default)',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value=[f"Option {i}" for i in range(1, 3)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    size="large",
                    mode="multiple",
                    placeholder='size="large"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value=[f"Option {i}" for i in range(1, 3)],
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
                "code": """"fac.AntdSpace(
    [
        fac.AntdDivider(
            '默认模式不同尺寸示例', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            size='small',
            placeholder='size="small"',
            options=[f'选项{i}' for i in range(1, 6)],
            value='选项1',
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            size='middle',
            placeholder='size="middle"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            value='选项1',
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            size='large',
            placeholder='size="large"',
            options=[f'选项{i}' for i in range(1, 6)],
            value='选项1',
            style={'width': '100%'},
        ),
        fac.AntdDivider(
            '多选模式不同尺寸示例', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            size='small',
            mode='multiple',
            placeholder='size="small"',
            options=[f'选项{i}' for i in range(1, 6)],
            value=[f'选项{i}' for i in range(1, 3)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            size='middle',
            mode='multiple',
            placeholder='size="middle"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            value=[f'选项{i}' for i in range(1, 3)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            size='large',
            mode='multiple',
            placeholder='size="large"',
            options=[f'选项{i}' for i in range(1, 6)],
            value=[f'选项{i}' for i in range(1, 3)],
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """fac.AntdSpace(
            [
                fac.AntdDivider(
                    "Size examples (single select)", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    size="small",
                    placeholder='size="small"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value="Option 1",
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    size="middle",
                    placeholder='size="middle" (default)',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value="Option 1",
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    size="large",
                    placeholder='size="large"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value="Option 1",
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    "Size examples (multiple select)", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    size="small",
                    mode="multiple",
                    placeholder='size="small"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value=[f"Option {i}" for i in range(1, 3)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    size="middle",
                    mode="multiple",
                    placeholder='size="middle" (default)',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value=[f"Option {i}" for i in range(1, 3)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    size="large",
                    mode="multiple",
                    placeholder='size="large"',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value=[f"Option {i}" for i in range(1, 3)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )"""
            }
        ]
