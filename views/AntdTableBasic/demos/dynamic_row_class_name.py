from datetime import datetime
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyStyle(
            rawStyle="""
.odd-row-class-name-demo {
    color: #f5222d;
}

.even-row-class-name-demo {
    color: #52c41a;
}
"""
        ),
        fac.AntdTable(
            columns=[
                {'title': 'int型示例', 'dataIndex': 'int型示例'},
                {'title': 'float型示例', 'dataIndex': 'float型示例'},
                {'title': 'str型示例', 'dataIndex': 'str型示例'},
                {'title': '日期时间示例', 'dataIndex': '日期时间示例'},
            ],
            data=[
                {
                    'int型示例': 123,
                    'float型示例': 1.23,
                    'str型示例': '示例字符',
                    '日期时间示例': datetime.now(),
                }
            ]
            * 4,
            rowClassName={
                'func': "(record, index) => index % 2 === 1 ? 'odd-row-class-name-demo' : 'even-row-class-name-demo'"
            },
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': '''
[
    fuc.FefferyStyle(
        rawStyle="""
.odd-row-class-name-demo {
    color: #f5222d;
}

.even-row-class-name-demo {
    color: #52c41a;
}
"""
    ),
    fac.AntdTable(
        columns=[
            {'title': 'int型示例', 'dataIndex': 'int型示例'},
            {'title': 'float型示例', 'dataIndex': 'float型示例'},
            {'title': 'str型示例', 'dataIndex': 'str型示例'},
            {'title': '日期时间示例', 'dataIndex': '日期时间示例'},
        ],
        data=[
            {
                'int型示例': 123,
                'float型示例': 1.23,
                'str型示例': '示例字符',
                '日期时间示例': datetime.now(),
            }
        ]
        * 4,
        rowClassName={
            'func': "(record, index) => index % 2 === 1 ? 'odd-row-class-name-demo' : 'even-row-class-name-demo'"
        },
    ),
]
'''
    }
]
