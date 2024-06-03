import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdMentions(
            id='mentions-demo',
            autoSize={'minRows': 2, 'maxRows': 4},
            options=[
                {'label': f'用户{c}', 'value': f'用户{c}'}
                for c in list('abcdef')
            ],
            style={'width': 300},
        ),
        html.Br(),
        fac.AntdSpace(id='mentions-demo-output', direction='vertical'),
    ]

    return demo_contents


@app.callback(
    Output('mentions-demo-output', 'children'),
    [
        Input('mentions-demo', 'value'),
        Input('mentions-demo', 'selectedOptions'),
    ],
)
def mentions_demo(value, selectedOptions):
    return [
        fac.AntdText(f'value: {value}'),
        fac.AntdText(f'selectedOptions: {selectedOptions}'),
    ]


code_string = [
    {
        'code': """
fac.AntdMentions(
    id='mentions-demo',
    autoSize={
        'minRows': 2,
        'maxRows': 4
    },
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

html.Br(),

fac.AntdSpace(
    id='mentions-demo-output',
    direction='vertical'
)

...

@app.callback(
    Output('mentions-demo-output', 'children'),
    [Input('mentions-demo', 'value'),
     Input('mentions-demo', 'selectedOptions')]
)
def mentions_demo(value, selectedOptions):

    return [
        fac.AntdText(
            f'value: {value}'
        ),
        fac.AntdText(
            f'selectedOptions: {selectedOptions}'
        )
    ]
"""
    }
]
