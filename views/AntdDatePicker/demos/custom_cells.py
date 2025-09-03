from datetime import datetime, timedelta

import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                "精确日期匹配：明天",
                fac.AntdDatePicker(
                    customCells=[
                        {
                            "year": datetime.now().year,
                            "month": datetime.now().month,
                            "date": (datetime.now() + timedelta(days=1)).day,
                            "style": {"border": "1px dashed #595959"},
                        }
                    ]
                ),
                "年份通配：每年的本月第10天",
                fac.AntdDatePicker(
                    customCells=[
                        {
                            "month": datetime.now().month,
                            "date": 10,
                            "style": {"border": "1px dashed #595959"},
                        }
                    ]
                ),
                "年份+月份通配：每月的第10天",
                fac.AntdDatePicker(
                    customCells=[
                        {
                            "date": 10,
                            "style": {"border": "1px dashed #595959"},
                        }
                    ]
                ),
            ],
            direction="vertical",
            style={"width": "100%"},
        )
    else:
        demo_contents = fac.AntdSpace(
            [
                "Exact date match: tomorrow",
                fac.AntdDatePicker(
                    customCells=[
                        {
                            "year": datetime.now().year,
                            "month": datetime.now().month,
                            "date": (datetime.now() + timedelta(days=1)).day,
                            "style": {"border": "1px dashed #595959"},
                        }
                    ],
                    locale="en-us",
                ),
                "Year wildcard: the 10th day of this month each year",
                fac.AntdDatePicker(
                    customCells=[
                        {
                            "month": datetime.now().month,
                            "date": 10,
                            "style": {"border": "1px dashed #595959"},
                        }
                    ],
                    locale="en-us",
                ),
                "Year+month wildcard: the 10th day of each month",
                fac.AntdDatePicker(
                    customCells=[
                        {
                            "date": 10,
                            "style": {"border": "1px dashed #595959"},
                        }
                    ],
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": "100%"},
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
        '精确日期匹配：明天',
        fac.AntdDatePicker(
            customCells=[
                {
                    'year': datetime.now().year,
                    'month': datetime.now().month,
                    'date': (datetime.now() + timedelta(days=1)).day,
                    'style': {
                        'border': '1px dashed #595959',
                    },
                }
            ]
        ),
        '年份通配：每年的本月第10天',
        fac.AntdDatePicker(
            customCells=[
                {
                    'month': datetime.now().month,
                    'date': 10,
                    'style': {
                        'border': '1px dashed #595959',
                    },
                }
            ]
        ),
        '年份+月份通配：每月的第10天',
        fac.AntdDatePicker(
            customCells=[
                {
                    'date': 10,
                    'style': {
                        'border': '1px dashed #595959',
                    },
                }
            ]
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
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
        'Exact date match: tomorrow',
        fac.AntdDatePicker(
            customCells=[
                {
                    'year': datetime.now().year,
                    'month': datetime.now().month,
                    'date': (datetime.now() + timedelta(days=1)).day,
                    'style': {
                        'border': '1px dashed #595959',
                    },
                }
            ],
            locale="en-us"
        ),
        'Year wildcard: the 10th day of this month each year',
        fac.AntdDatePicker(
            customCells=[
                {
                    'month': datetime.now().month,
                    'date': 10,
                    'style': {
                        'border': '1px dashed #595959',
                    },
                }
            ],
            locale="en-us"
        ),
        'Year+month wildcard: the 10th day of each month',
        fac.AntdDatePicker(
            customCells=[
                {
                    'date': 10,
                    'style': {
                        'border': '1px dashed #595959',
                    },
                }
            ],
            locale="en-us"
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
