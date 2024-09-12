import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdCalendar(
            size='large',
            customCells=[
                {
                    'type': 'date',
                    'month': 8,
                    'date': 1,
                    'content': fac.AntdTag(content='建军节', color='red'),
                },
                {
                    'type': 'date',
                    'month': 8,
                    'date': 7,
                    'content': fac.AntdTag(content='立秋', color='gold'),
                },
                {
                    'type': 'date',
                    'month': 8,
                    'date': 12,
                    'content': fac.AntdSpace(
                        ['0.3.0发布', '🎉🎉🎉'],
                        direction='vertical',
                        align='center',
                        size=0,
                        style={'width': '100%', 'fontSize': 16},
                    ),
                },
                {
                    'type': 'date',
                    'month': 8,
                    'date': 22,
                    'content': fac.AntdTag(content='处暑', color='volcano'),
                },
                {
                    'type': 'month',
                    'month': 7,
                    'content': fac.AntdTag(content='暑假', color='volcano'),
                },
                {
                    'type': 'month',
                    'month': 8,
                    'content': fac.AntdTag(content='暑假', color='volcano'),
                },
                {
                    'type': 'date',
                    'date': 6,
                    'content': fac.AntdTag(content='每月6号', color='red'),
                },
            ],
            value='2024-08-12',
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdCalendar(
            size='large',
            customCells=[
                {
                    'type': 'date',
                    'month': 8,
                    'date': 1,
                    'content': fac.AntdTag(content='建军节', color='red'),
                },
                {
                    'type': 'date',
                    'month': 8,
                    'date': 7,
                    'content': fac.AntdTag(content='立秋', color='gold'),
                },
                {
                    'type': 'date',
                    'month': 8,
                    'date': 12,
                    'content': fac.AntdSpace(
                        ['0.3.0 Release', '🎉🎉🎉'],
                        direction='vertical',
                        align='center',
                        size=0,
                        style={'width': '100%', 'fontSize': 16},
                    ),
                },
                {
                    'type': 'date',
                    'month': 8,
                    'date': 22,
                    'content': fac.AntdTag(content='处暑', color='volcano'),
                },
                {
                    'type': 'month',
                    'month': 7,
                    'content': fac.AntdTag(content='Summer', color='volcano'),
                },
                {
                    'type': 'month',
                    'month': 8,
                    'content': fac.AntdTag(content='Summer', color='volcano'),
                },
                {
                    'type': 'date',
                    'date': 6,
                    'content': fac.AntdTag(content='Every 6th', color='red'),
                },
            ],
            value='2024-08-12',
            locale='en-us',
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdCalendar(
    size='large',
    customCells=[
        {
            'type': 'date',
            'month': 8,
            'date': 1,
            'content': fac.AntdTag(content='建军节', color='red'),
        },
        {
            'type': 'date',
            'month': 8,
            'date': 7,
            'content': fac.AntdTag(content='立秋', color='gold'),
        },
        {
            'type': 'date',
            'month': 8,
            'date': 12,
            'content': fac.AntdSpace(
                ['0.3.0发布', '🎉🎉🎉'],
                direction='vertical',
                align='center',
                size=0,
                style={'width': '100%', 'fontSize': 16},
            ),
        },
        {
            'type': 'date',
            'month': 8,
            'date': 22,
            'content': fac.AntdTag(content='处暑', color='volcano'),
        },
        {
            'type': 'month',
            'month': 7,
            'content': fac.AntdTag(content='暑假', color='volcano'),
        },
        {
            'type': 'month',
            'month': 8,
            'content': fac.AntdTag(content='暑假', color='volcano'),
        },
        {
            'type': 'date',
            'date': 6,
            'content': fac.AntdTag(content='每月6号', color='red'),
        },
    ],
    value='2024-08-12',
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdCalendar(
    size='large',
    customCells=[
        {
            'type': 'date',
            'month': 8,
            'date': 1,
            'content': fac.AntdTag(content='建军节', color='red'),
        },
        {
            'type': 'date',
            'month': 8,
            'date': 7,
            'content': fac.AntdTag(content='立秋', color='gold'),
        },
        {
            'type': 'date',
            'month': 8,
            'date': 12,
            'content': fac.AntdSpace(
                ['0.3.0 Release', '🎉🎉🎉'],
                direction='vertical',
                align='center',
                size=0,
                style={'width': '100%', 'fontSize': 16},
            ),
        },
        {
            'type': 'date',
            'month': 8,
            'date': 22,
            'content': fac.AntdTag(content='处暑', color='volcano'),
        },
        {
            'type': 'month',
            'month': 7,
            'content': fac.AntdTag(content='Summer', color='volcano'),
        },
        {
            'type': 'month',
            'month': 8,
            'content': fac.AntdTag(content='Summer', color='volcano'),
        },
        {
            'type': 'date',
            'date': 6,
            'content': fac.AntdTag(content='Every 6th', color='red'),
        },
    ],
    value='2024-08-12',
    locale='en-us',
)
"""
            }
        ]
