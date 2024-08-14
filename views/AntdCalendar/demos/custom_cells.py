import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

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
        ],
        value='2024-08-12',
    )

    return demo_contents


code_string = [
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
    ],
    value='2024-08-12',
)
"""
    }
]
