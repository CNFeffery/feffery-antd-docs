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
                    "autoClearSearchValue=True", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    placeholder="输入内容以搜索选项",
                    mode="multiple",
                    autoClearSearchValue=True,
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    placeholder="输入内容以搜索选项",
                    mode="tags",
                    autoClearSearchValue=True,
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdDivider(
                    "autoClearSearchValue=False", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    placeholder="输入内容以搜索选项",
                    mode="multiple",
                    autoClearSearchValue=False,
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    placeholder="输入内容以搜索选项",
                    mode="tags",
                    autoClearSearchValue=False,
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
                    "autoClearSearchValue=True", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    placeholder="Type to search options",
                    mode="multiple",
                    autoClearSearchValue=True,
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    placeholder="Type to search options",
                    mode="tags",
                    autoClearSearchValue=True,
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    "autoClearSearchValue=False", innerTextOrientation="left"
                ),
                fac.AntdSelect(
                    placeholder="Type to search options",
                    mode="multiple",
                    autoClearSearchValue=False,
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    placeholder="Type to search options",
                    mode="tags",
                    autoClearSearchValue=False,
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
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDivider('autoClearSearchValue=True', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='输入内容以搜索选项',
            mode='multiple',
            autoClearSearchValue=True,
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='输入内容以搜索选项',
            mode='tags',
            autoClearSearchValue=True,
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdDivider('autoClearSearchValue=False', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='输入内容以搜索选项',
            mode='multiple',
            autoClearSearchValue=False,
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='输入内容以搜索选项',
            mode='tags',
            autoClearSearchValue=False,
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
fac.AntdSpace(
    [
        fac.AntdDivider('autoClearSearchValue=True', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='Type to search options',
            mode='multiple',
            autoClearSearchValue=True,
            options=[f'Option {i}' for i in range(1, 6)],
            style={'width': '100%'},
            locale="en-us",
        ),
        fac.AntdSelect(
            placeholder='Type to search options',
            mode='tags',
            autoClearSearchValue=True,
            options=[f'Option {i}' for i in range(1, 6)],
            style={'width': '100%'},
            locale="en-us",
        ),
        fac.AntdDivider('autoClearSearchValue=False', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='Type to search options',
            mode='multiple',
            autoClearSearchValue=False,
            options=[f'Option {i}' for i in range(1, 6)],
            style={'width': '100%'},
            locale="en-us",
        ),
        fac.AntdSelect(
            placeholder='Type to search options',
            mode='tags',
            autoClearSearchValue=False,
            options=[f'Option {i}' for i in range(1, 6)],
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
