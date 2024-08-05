import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdInput(
                    id='copy-text-input', maxLength=20, style={'width': '150px'}
                ),
                fac.AntdCopyText(id='copy-text-output', text='无内容'),
            ]
        )
    ]

    return demo_contents


@app.callback(
    Output('copy-text-output', 'text'), Input('copy-text-input', 'value')
)
def copy_text_callback(value):
    return value or '无内容'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(
            id='copy-text-input',
            maxLength=20,
            style={
                'width': '150px'
            }
        ),
        fac.AntdCopyText(
            id='copy-text-output',
            text='无内容'
        )
    ]
)

...

@app.callback(
    Output('copy-text-output', 'text'),
    Input('copy-text-input', 'value')
)
def copy_text_callback(value):
    return value or '无内容'
"""
    }
]
