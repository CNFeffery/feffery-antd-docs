import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('autoSize=False（默认）', innerTextOrientation='left'),
        fac.AntdMentions(
            defaultValue='示例内容' * 20,
            options=[
                {'label': f'用户{c}', 'value': f'用户{c}'}
                for c in list('abcdef')
            ],
            style={'width': 300},
        ),
        fac.AntdDivider('autoSize=True', innerTextOrientation='left'),
        fac.AntdMentions(
            defaultValue='示例内容' * 20,
            options=[
                {'label': f'用户{c}', 'value': f'用户{c}'}
                for c in list('abcdef')
            ],
            autoSize=True,
            style={'width': 300},
        ),
        fac.AntdDivider(
            '配置minRows、maxRows参数', innerTextOrientation='left'
        ),
        fac.AntdMentions(
            defaultValue='示例内容' * 20,
            options=[
                {'label': f'用户{c}', 'value': f'用户{c}'}
                for c in list('abcdef')
            ],
            autoSize={'minRows': 2, 'maxRows': 6},
            style={'width': 300},
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDivider(
    'autoSize=False（默认）',
    innerTextOrientation='left'
),
fac.AntdMentions(
    defaultValue='示例内容'*20,
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    style={
        'width': 300
    }
),

fac.AntdDivider(
    'autoSize=True',
    innerTextOrientation='left'
),
fac.AntdMentions(
    defaultValue='示例内容'*20,
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    autoSize=True,
    style={
        'width': 300
    }
),

fac.AntdDivider(
    '配置minRows、maxRows参数',
    innerTextOrientation='left'
),
fac.AntdMentions(
    defaultValue='示例内容'*20,
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    autoSize={
        'minRows': 2,
        'maxRows': 6
    },
    style={
        'width': 300
    }
)
"""
    }
]
