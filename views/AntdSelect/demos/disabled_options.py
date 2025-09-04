import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider("常规用法", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[
                        {
                            "label": f"选项{i}",
                            "value": f"选项{i}",
                            "disabled": True if i == 3 else False,
                        }
                        for i in range(1, 6)
                    ],
                    style={"width": "100%"},
                ),
                fac.AntdDivider("自定义label用法", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[
                        {
                            "label": fac.AntdFlex(
                                [
                                    fac.AntdFlex(
                                        [
                                            fac.AntdAvatar(
                                                text=f"{i}", mode="text", size="small"
                                            ),
                                            fac.AntdTag(
                                                content=f"选项{i}",
                                                color=[
                                                    "blue",
                                                    "green",
                                                    "purple",
                                                    "orange",
                                                    "cyan",
                                                ][i - 1],
                                            ),
                                        ],
                                        justify="flex-start",
                                        align="center",
                                        gap=5,
                                    ),
                                    (
                                        fac.AntdIcon(
                                            icon="antd-stop", style={"color": "gray"}
                                        )
                                        if i == 3
                                        else None
                                    ),
                                ],
                                justify="space-between",
                                align="center",
                                gap=5,
                            ),
                            "value": f"选项{i}",
                            "disabled": True if i == 3 else False,
                        }
                        for i in range(1, 6)
                    ],
                    size="large",
                    style={"width": 350},
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider("Basic usage", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[
                        {
                            "label": f"Option {i}",
                            "value": f"Option {i}",
                            "disabled": True if i == 3 else False,
                        }
                        for i in range(1, 6)
                    ],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider("Custom label usage", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[
                        {
                            "label": fac.AntdFlex(
                                [
                                    fac.AntdFlex(
                                        [
                                            fac.AntdAvatar(
                                                text=f"{i}", mode="text", size="small"
                                            ),
                                            fac.AntdTag(
                                                content=f"Option {i}",
                                                color=[
                                                    "blue",
                                                    "green",
                                                    "purple",
                                                    "orange",
                                                    "cyan",
                                                ][i - 1],
                                            ),
                                        ],
                                        justify="flex-start",
                                        align="center",
                                        gap=5,
                                    ),
                                    (
                                        fac.AntdIcon(
                                            icon="antd-stop", style={"color": "gray"}
                                        )
                                        if i == 3
                                        else None
                                    ),
                                ],
                                justify="space-between",
                                align="center",
                                gap=5,
                            ),
                            "value": f"Option {i}",
                            "disabled": True if i == 3 else False,
                        }
                        for i in range(1, 6)
                    ],
                    size="large",
                    style={"width": 350},
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
        fac.AntdDivider('常规用法', innerTextOrientation='left'),
        fac.AntdSelect(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}',
                    'disabled': True if i == 3 else False,
                }
                for i in range(1, 6)
            ],
            style={'width': '100%'},
        ),
        fac.AntdDivider('自定义label用法', innerTextOrientation='left'),
        fac.AntdSelect(
            options=[
                {
                    'label': fac.AntdFlex(
                        [
                            fac.AntdFlex(
                                [
                                    fac.AntdAvatar(
                                        text=f'{i}',
                                        mode='text',
                                        size='small',
                                    ),
                                    fac.AntdTag(
                                        content=f'选项{i}',
                                        color=[
                                            'blue',
                                            'green',
                                            'purple',
                                            'orange',
                                            'cyan',
                                        ][i - 1],
                                    ),
                                ],
                                justify='flex-start',
                                align='center',
                                gap=5,
                            ),
                            # 可通过额外的元素来展示disabled的视觉效果
                            fac.AntdIcon(
                                icon='antd-stop',
                                style={
                                    'color': 'gray',
                                },
                            )
                            if i == 3
                            else None,
                        ],
                        justify='space-between',
                        align='center',
                        gap=5,
                    ),
                    'value': f'选项{i}',
                    'disabled': True if i == 3 else False,
                }
                for i in range(1, 6)
            ],
            size='large',
            style={'width': 350},
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
                fac.AntdDivider("Basic usage", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[
                        {
                            "label": f"Option {i}",
                            "value": f"Option {i}",
                            "disabled": True if i == 3 else False,
                        }
                        for i in range(1, 6)
                    ],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider("Custom label usage", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[
                        {
                            "label": fac.AntdFlex(
                                [
                                    fac.AntdFlex(
                                        [
                                            fac.AntdAvatar(
                                                text=f"{i}", mode="text", size="small"
                                            ),
                                            fac.AntdTag(
                                                content=f"Option {i}",
                                                color=[
                                                    "blue",
                                                    "green",
                                                    "purple",
                                                    "orange",
                                                    "cyan",
                                                ][i - 1],
                                            ),
                                        ],
                                        justify="flex-start",
                                        align="center",
                                        gap=5,
                                    ),
                                    (
                                        fac.AntdIcon(
                                            icon="antd-stop", style={"color": "gray"}
                                        )
                                        if i == 3
                                        else None
                                    ),
                                ],
                                justify="space-between",
                                align="center",
                                gap=5,
                            ),
                            "value": f"Option {i}",
                            "disabled": True if i == 3 else False,
                        }
                        for i in range(1, 6)
                    ],
                    size="large",
                    style={"width": 350},
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )
"""
            }
        ]
