import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdRadioGroup(
            id='radio-group-demo',
            options=[{'label': f'选项{c}', 'value': c} for c in list('abcdef')],
            defaultValue='a',
        ),
        fac.AntdParagraph(id='radio-group-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('radio-group-demo-output', 'children'),
    Input('radio-group-demo', 'value'),
)
def radio_group_demo(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdRadioGroup(
    id='radio-group-demo',
    options=[
        {
            'label': f'选项{c}',
            'value': c
        }
        for c in list('abcdef')
    ],
    defaultValue='a'
),

fac.AntdParagraph(
    id='radio-group-demo-output'
)

...

@app.callback(
    Output('radio-group-demo-output', 'children'),
    Input('radio-group-demo', 'value')
)
def radio_group_demo(value):

    return f'value: {value}'
"""
    }
]
