import feffery_antd_components as fac
import numpy as np
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = fac.AntdTable(
            columns=[
                {
                    'title': '数值测试1',
                    'dataIndex': '数值测试1',
                    'width': '50%',
                    'renderOptions': {'renderType': 'custom-format'},
                },
                {
                    'title': '数值测试2',
                    'dataIndex': '数值测试2',
                    'width': '50%',
                    'renderOptions': {'renderType': 'custom-format'},
                },
            ],
            data=[
                {'数值测试1': np.random.rand(), '数值测试2': np.random.rand()}
                for i in range(10)
            ],
            sortOptions={'sortDataIndexes': ['数值测试1', '数值测试2']},
            bordered=True,
            customFormatFuncs={
                '数值测试1': '(x) => `${(x*100).toFixed(2)}%`',
                '数值测试2': '(x) => x <= 0.5 ? `低水平：${x.toFixed(2)}` : `高水平：${x.toFixed(2)}`',
            },
            style={'width': '500px'},
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdTable(
            locale='en-us',
            columns=[
                {
                    'title': 'Numeric Test 1',
                    'dataIndex': 'Numeric Test 1',
                    'width': '50%',
                    'renderOptions': {'renderType': 'custom-format'},
                },
                {
                    'title': 'Numeric Test 2',
                    'dataIndex': 'Numeric Test 2',
                    'width': '50%',
                    'renderOptions': {'renderType': 'custom-format'},
                },
            ],
            data=[
                {
                    'Numeric Test 1': np.random.rand(),
                    'Numeric Test 2': np.random.rand(),
                }
                for i in range(10)
            ],
            sortOptions={
                'sortDataIndexes': ['Numeric Test 1', 'Numeric Test 2']
            },
            bordered=True,
            customFormatFuncs={
                'Numeric Test 1': '(x) => `${(x*100).toFixed(2)}%`',
                'Numeric Test 2': '(x) => x <= 0.5 ? `Low Level: ${x.toFixed(2)}` : `High Level: ${x.toFixed(2)}`',
            },
            style={'width': '500px'},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdTable(
    columns=[
        {
            'title': '数值测试1',
            'dataIndex': '数值测试1',
            'width': '50%',
            'renderOptions': {'renderType': 'custom-format'},
        },
        {
            'title': '数值测试2',
            'dataIndex': '数值测试2',
            'width': '50%',
            'renderOptions': {'renderType': 'custom-format'},
        },
    ],
    data=[
        {'数值测试1': np.random.rand(), '数值测试2': np.random.rand()}
        for i in range(10)
    ],
    sortOptions={'sortDataIndexes': ['数值测试1', '数值测试2']},
    bordered=True,
    customFormatFuncs={
        '数值测试1': '(x) => `${(x*100).toFixed(2)}%`',
        '数值测试2': '(x) => x <= 0.5 ? `低水平：${x.toFixed(2)}` : `高水平：${x.toFixed(2)}`',
    },
    style={'width': '500px'},
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdTable(
    locale='en-us',
    columns=[
        {
            'title': 'Numeric Test 1',
            'dataIndex': 'Numeric Test 1',
            'width': '50%',
            'renderOptions': {'renderType': 'custom-format'},
        },
        {
            'title': 'Numeric Test 2',
            'dataIndex': 'Numeric Test 2',
            'width': '50%',
            'renderOptions': {'renderType': 'custom-format'},
        },
    ],
    data=[
        {'Numeric Test 1': np.random.rand(), 'Numeric Test 2': np.random.rand()}
        for i in range(10)
    ],
    sortOptions={'sortDataIndexes': ['Numeric Test 1', 'Numeric Test 2']},
    bordered=True,
    customFormatFuncs={
        'Numeric Test 1': '(x) => `${(x*100).toFixed(2)}%`',
        'Numeric Test 2': '(x) => x <= 0.5 ? `Low Level: ${x.toFixed(2)}` : `High Level: ${x.toFixed(2)}`',
    },
    style={'width': '500px'},
)
"""
            }
        ]
