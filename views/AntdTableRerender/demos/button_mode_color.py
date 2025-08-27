import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdTable(
            columns=[
                {
                    "dataIndex": "variant参数值",
                    "title": "variant参数值",
                },
                {
                    "dataIndex": "渲染效果",
                    "title": "渲染效果",
                    "renderOptions": {"renderType": "button"},
                },
            ],
            data=[
                {
                    "variant参数值": variant,
                    "渲染效果": [
                        {"content": color, "color": color, "variant": variant}
                        for color in [
                            "default",
                            "primary",
                            "danger",
                            "blue",
                            "purple",
                            "cyan",
                            "green",
                            "magenta",
                            "pink",
                            "red",
                            "orange",
                            "yellow",
                            "volcano",
                            "geekblue",
                            "lime",
                            "gold",
                        ]
                    ],
                }
                for variant in [
                    "outlined",
                    "dashed",
                    "solid",
                    "filled",
                    "text",
                    "link",
                ]
            ],
            bordered=True,
            tableLayout="fixed",
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdTable(
            locale="en-us",
            columns=[
                {
                    "dataIndex": "Variant Value",
                    "title": "Variant Value",
                },
                {
                    "dataIndex": "Render Effect",
                    "title": "Render Effect",
                    "renderOptions": {"renderType": "button"},
                },
            ],
            data=[
                {
                    "Variant Value": variant,
                    "Render Effect": [
                        {"content": color, "color": color, "variant": variant}
                        for color in [
                            "default",
                            "primary",
                            "danger",
                            "blue",
                            "purple",
                            "cyan",
                            "green",
                            "magenta",
                            "pink",
                            "red",
                            "orange",
                            "yellow",
                            "volcano",
                            "geekblue",
                            "lime",
                            "gold",
                        ]
                    ],
                }
                for variant in [
                    "outlined",
                    "dashed",
                    "solid",
                    "filled",
                    "text",
                    "link",
                ]
            ],
            bordered=True,
            tableLayout="fixed",
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdTable(
    columns=[
        {
            'dataIndex': 'variant参数值',
            'title': 'variant参数值',
        },
        {
            'dataIndex': '渲染效果',
            'title': '渲染效果',
            'renderOptions': {'renderType': 'button'},
        },
    ],
    data=[
        {
            'variant参数值': variant,
            '渲染效果': [
                {'content': color, 'color': color, 'variant': variant}
                for color in [
                    'default',
                    'primary',
                    'danger',
                    'blue',
                    'purple',
                    'cyan',
                    'green',
                    'magenta',
                    'pink',
                    'red',
                    'orange',
                    'yellow',
                    'volcano',
                    'geekblue',
                    'lime',
                    'gold',
                ]
            ],
        }
        for variant in [
            'outlined',
            'dashed',
            'solid',
            'filled',
            'text',
            'link',
        ]
    ],
    bordered=True,
    tableLayout='fixed',
)
"""
            }
        ]

    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdTable(
    locale='en-us',
    columns=[
        {
            'dataIndex': 'Variant Value',
            'title': 'Variant Value',
        },
        {
            'dataIndex': 'Render Effect',
            'title': 'Render Effect',
            'renderOptions': {'renderType': 'button'},
        },
    ],
    data=[
        {
            'Variant Value': variant,
            'Render Effect': [
                {'content': color, 'color': color, 'variant': variant}
                for color in [
                    'default',
                    'primary',
                    'danger',
                    'blue',
                    'purple',
                    'cyan',
                    'green',
                    'magenta',
                    'pink',
                    'red',
                    'orange',
                    'yellow',
                    'volcano',
                    'geekblue',
                    'lime',
                    'gold',
                ]
            ],
        }
        for variant in [
            'outlined',
            'dashed',
            'solid',
            'filled',
            'text',
            'link',
        ]
    ],
    bordered=True,
    tableLayout='fixed',
)
"""
            }
        ]
