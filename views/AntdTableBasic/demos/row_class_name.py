from datetime import datetime

import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = [
            fuc.FefferyStyle(
                rawStyle="""
.table-row-class-name-demo {
    color: #1890ff;
    font-weight: bold;
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
                * 3,
                rowClassName='table-row-class-name-demo',
            ),
        ]

    elif current_locale == 'en-us':
        demo_contents = [
            fuc.FefferyStyle(
                rawStyle="""
.table-row-class-name-demo {
    color: #1890ff;
    font-weight: bold;
}
"""
            ),
            fac.AntdTable(
                columns=[
                    {'title': 'int Example', 'dataIndex': 'int Example'},
                    {'title': 'float Example', 'dataIndex': 'float Example'},
                    {'title': 'str Example', 'dataIndex': 'str Example'},
                    {
                        'title': 'Datetime Example',
                        'dataIndex': 'Datetime Example',
                    },
                ],
                data=[
                    {
                        'int Example': 123,
                        'float Example': 1.23,
                        'str Example': 'Example string',
                        'Datetime Example': datetime.now(),
                    }
                ]
                * 3,
                rowClassName='table-row-class-name-demo',
                locale='en-us',
            ),
        ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': '''
[
    fuc.FefferyStyle(
        rawStyle="""
.table-row-class-name-demo {
    color: #1890ff;
    font-weight: bold;
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
        * 3,
        rowClassName='table-row-class-name-demo',
    ),
]
'''
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': '''
[
    fuc.FefferyStyle(
        rawStyle="""
.table-row-class-name-demo {
    color: #1890ff;
    font-weight: bold;
}
"""
    ),
    fac.AntdTable(
        columns=[
            {'title': 'int Example', 'dataIndex': 'int Example'},
            {'title': 'float Example', 'dataIndex': 'float Example'},
            {'title': 'str Example', 'dataIndex': 'str Example'},
            {'title': 'Datetime Example', 'dataIndex': 'Datetime Example'},
        ],
        data=[
            {
                'int Example': 123,
                'float Example': 1.23,
                'str Example': 'Example string',
                'Datetime Example': datetime.now(),
            }
        ]
        * 3,
        rowClassName='table-row-class-name-demo',
    ),
]
'''
            }
        ]
