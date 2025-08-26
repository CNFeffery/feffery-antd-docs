import feffery_antd_components as fac
import numpy as np
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdTable(
            columns=[
                {
                    "title": "mini-line示例1",
                    "dataIndex": "mini-line示例1",
                    "renderOptions": {"renderType": "mini-line"},
                },
                {
                    "title": "mini-line示例2",
                    "dataIndex": "mini-line示例2",
                    "renderOptions": {
                        "renderType": "mini-line",
                        "tooltipCustomContent": """(x, data) => `数值：${data[0]?.data?.y.toFixed(3)}`""",
                    },
                },
                {
                    "title": "自定义颜色示例",
                    "dataIndex": "自定义颜色示例",
                    "renderOptions": {
                        "renderType": "mini-line",
                        "miniChartColor": "#ff7875",
                    },
                },
            ],
            data=[
                {
                    "mini-line示例1": [np.random.rand() for i in range(25)],
                    "mini-line示例2": [np.random.rand() for i in range(25)],
                    "自定义颜色示例": [np.random.rand() for i in range(25)],
                }
            ]
            * 3,
            bordered=True,
            tableLayout="fixed",
            style={"width": 400},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdTable(
            locale="en-us",
            columns=[
                {
                    "title": "mini-line Example 1",
                    "dataIndex": "mini-line Example 1",
                    "renderOptions": {"renderType": "mini-line"},
                },
                {
                    "title": "mini-line Example 2",
                    "dataIndex": "mini-line Example 2",
                    "renderOptions": {
                        "renderType": "mini-line",
                        "tooltipCustomContent": """(x, data) => `Value: ${data[0]?.data?.y.toFixed(3)}`""",
                    },
                },
                {
                    "title": "Custom Color Example",
                    "dataIndex": "Custom Color Example",
                    "renderOptions": {
                        "renderType": "mini-line",
                        "miniChartColor": "#ff7875",
                    },
                },
            ],
            data=[
                {
                    "mini-line Example 1": [np.random.rand() for i in range(25)],
                    "mini-line Example 2": [np.random.rand() for i in range(25)],
                    "Custom Color Example": [np.random.rand() for i in range(25)],
                }
            ]
            * 3,
            bordered=True,
            tableLayout="fixed",
            style={"width": 400},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": '''
fac.AntdTable(
    columns=[
        {
            'title': 'mini-line示例1',
            'dataIndex': 'mini-line示例1',
            'renderOptions': {'renderType': 'mini-line'},
        },
        {
            'title': 'mini-line示例2',
            'dataIndex': 'mini-line示例2',
            'renderOptions': {
                'renderType': 'mini-line',
                'tooltipCustomContent': """(x, data) => `数值：${data[0]?.data?.y.toFixed(3)}`""",
            },
        },
        {
            'title': '自定义颜色示例',
            'dataIndex': '自定义颜色示例',
            'renderOptions': {
                'renderType': 'mini-line',
                'miniChartColor': '#ff7875',
            },
        },
    ],
    data=[
        {
            'mini-line示例1': [np.random.rand() for i in range(25)],
            'mini-line示例2': [np.random.rand() for i in range(25)],
            '自定义颜色示例': [np.random.rand() for i in range(25)],
        }
    ]
    * 3,
    bordered=True,
    tableLayout='fixed',
    style={'width': 400},
)
'''
            }
        ]

    elif current_locale == "en-us":
        return [
            {
                "code": '''
fac.AntdTable(
    locale="en-us",
    columns=[
        {
            'title': 'mini-line Example 1',
            'dataIndex': 'mini-line Example 1',
            'renderOptions': {'renderType': 'mini-line'},
        },
        {
            'title': 'mini-line Example 2',
            'dataIndex': 'mini-line Example 2',
            'renderOptions': {
                'renderType': 'mini-line',
                'tooltipCustomContent': """(x, data) => `Value: ${data[0]?.data?.y.toFixed(3)}`""",
            },
        },
        {
            'title': 'Custom Color Example',
            'dataIndex': 'Custom Color Example',
            'renderOptions': {
                'renderType': 'mini-line',
                'miniChartColor': '#ff7875',
            },
        },
    ],
    data=[
        {
            'mini-line Example 1': [np.random.rand() for i in range(25)],
            'mini-line Example 2': [np.random.rand() for i in range(25)],
            'Custom Color Example': [np.random.rand() for i in range(25)],
        }
    ]
    * 3,
    bordered=True,
    tableLayout='fixed',
    style={'width': 400},
)
'''
            }
        ]
