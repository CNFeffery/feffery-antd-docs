import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider(
                    "allowClear=True（默认值）", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    placeholder='mode="default"（默认）',
                    options=[f"选项{i}" for i in range(1, 6)],
                    value="选项1",
                    allowClear=True,
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    placeholder='mode="multiple"',
                    mode="multiple",
                    options=[f"选项{i}" for i in range(1, 6)],
                    value=[f"选项{i}" for i in range(1, 3)],
                    allowClear=True,
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    placeholder='mode="tags"',
                    mode="tags",
                    options=[f"选项{i}" for i in range(1, 6)],
                    value=["选项1", "自由新增选项"],
                    allowClear=True,
                    style={"width": "100%"},
                ),
                fac.AntdDivider("allowClear=False", innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder='mode="default"（默认）',
                    options=[f"选项{i}" for i in range(1, 6)],
                    value="选项1",
                    allowClear=False,
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    placeholder='mode="multiple"',
                    mode="multiple",
                    options=[f"选项{i}" for i in range(1, 6)],
                    value=[f"选项{i}" for i in range(1, 3)],
                    allowClear=False,
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    placeholder='mode="tags"',
                    mode="tags",
                    options=[f"选项{i}" for i in range(1, 6)],
                    value=["选项1", "自由新增选项"],
                    allowClear=False,
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
                    "allowClear=True (default)", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    placeholder='mode="default" (default)',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value="Option 1",
                    allowClear=True,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    placeholder='mode="multiple"',
                    mode="multiple",
                    options=[f"Option {i}" for i in range(1, 6)],
                    value=[f"Option {i}" for i in range(1, 3)],
                    allowClear=True,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    placeholder='mode="tags"',
                    mode="tags",
                    options=[f"Option {i}" for i in range(1, 6)],
                    value=["Option 1", "Newly added option"],
                    allowClear=True,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider("allowClear=False", innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder='mode="default" (default)',
                    options=[f"Option {i}" for i in range(1, 6)],
                    value="Option 1",
                    allowClear=False,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    placeholder='mode="multiple"',
                    mode="multiple",
                    options=[f"Option {i}" for i in range(1, 6)],
                    value=[f"Option {i}" for i in range(1, 3)],
                    allowClear=False,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    placeholder='mode="tags"',
                    mode="tags",
                    options=[f"Option {i}" for i in range(1, 6)],
                    value=["Option 1", "Newly added option"],
                    allowClear=False,
                    style={"width": "100%"},
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDivider('allowClear=True（默认值）', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='mode="default"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            value='选项1',
            allowClear=True,
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='mode="multiple"',
            mode='multiple',
            options=[f'选项{i}' for i in range(1, 6)],
            value=[f'选项{i}' for i in range(1, 3)],
            allowClear=True,
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='mode="tags"',
            mode='tags',
            options=[f'选项{i}' for i in range(1, 6)],
            value=['选项1', '自由新增选项'],
            allowClear=True,
            style={'width': '100%'},
        ),
        fac.AntdDivider('allowClear=False', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='mode="default"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            value='选项1',
            allowClear=False,
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='mode="multiple"',
            mode='multiple',
            options=[f'选项{i}' for i in range(1, 6)],
            value=[f'选项{i}' for i in range(1, 3)],
            allowClear=False,
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='mode="tags"',
            mode='tags',
            options=[f'选项{i}' for i in range(1, 6)],
            value=['选项1', '自由新增选项'],
            allowClear=False,
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
fac.AntdSpace(
    [
        fac.AntdDivider('allowClear=True (default)', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='mode="default" (default)',
            options=[f'Option {i}' for i in range(1, 6)],
            value='Option 1',
            allowClear=True,
            style={'width': '100%'},
            locale="en-us",
        ),
        fac.AntdSelect(
            placeholder='mode="multiple"',
            mode='multiple',
            options=[f'Option {i}' for i in range(1, 6)],
            value=[f'Option {i}' for i in range(1, 3)],
            allowClear=True,
            style={'width': '100%'},
            locale="en-us",
        ),
        fac.AntdSelect(
            placeholder='mode="tags"',
            mode='tags',
            options=[f'Option {i}' for i in range(1, 6)],
            value=['Option 1', 'Newly added option'],
            allowClear=True,
            style={'width': '100%'},
            locale="en-us",
        ),
        fac.AntdDivider('allowClear=False', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='mode="default" (default)',
            options=[f'Option {i}' for i in range(1, 6)],
            value='Option 1',
            allowClear=False,
            style={'width': '100%'},
            locale="en-us",
        ),
        fac.AntdSelect(
            placeholder='mode="multiple"',
            mode='multiple',
            options=[f'Option {i}' for i in range(1, 6)],
            value=[f'Option {i}' for i in range(1, 3)],
            allowClear=False,
            style={'width': '100%'},
            locale="en-us",
        ),
        fac.AntdSelect(
            placeholder='mode="tags"',
            mode='tags',
            options=[f'Option {i}' for i in range(1, 6)],
            value=['Option 1', 'Newly added option'],
            allowClear=False,
            style={'width': '100%'},
            locale="en-us",
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
            }
        ]
