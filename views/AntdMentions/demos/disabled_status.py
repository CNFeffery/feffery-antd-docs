import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdMentions(
        options=[
            {'label': f'用户{c}', 'value': f'用户{c}'} for c in list('abcdef')
        ],
        disabled=True,
        style={'width': 200},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdMentions(
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    disabled=True,
    style={
        'width': 200
    }
)
"""
    }
]
