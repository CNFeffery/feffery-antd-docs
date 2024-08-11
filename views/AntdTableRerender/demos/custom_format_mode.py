import numpy as np
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
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

    return demo_contents


code_string = [
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
