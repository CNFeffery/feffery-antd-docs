import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('status="warning"', innerTextOrientation='left'),
        fac.AntdMentions(
            options=[
                {'label': f'用户{c}', 'value': f'用户{c}'}
                for c in list('abcdef')
            ],
            status='warning',
            style={'width': 200},
        ),
        fac.AntdDivider('status="error"', innerTextOrientation='left'),
        fac.AntdMentions(
            options=[
                {'label': f'用户{c}', 'value': f'用户{c}'}
                for c in list('abcdef')
            ],
            status='error',
            style={'width': 200},
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDivider(
    'status="warning"',
    innerTextOrientation='left'
),
fac.AntdMentions(
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    status='warning',
    style={
        'width': 200
    }
),

fac.AntdDivider(
    'status="error"',
    innerTextOrientation='left'
),
fac.AntdMentions(
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    status='error',
    style={
        'width': 200
    }
)
"""
    }
]
