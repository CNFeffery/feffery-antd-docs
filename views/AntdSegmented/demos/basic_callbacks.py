import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSegmented(
                id='segmented-demo',
                options=[
                    {'label': i, 'value': i}
                    for i in [
                        'Daily',
                        'Weekly',
                        'Monthly',
                        'Quarterly',
                        'Yearly',
                    ]
                ],
                defaultValue='Daily',
            ),
            fac.AntdText(id='segmented-demo-output'),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('segmented-demo-output', 'children'),
    Input('segmented-demo', 'value'),
)
def segmented_demo(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSegmented(
            id='segmented-demo',
            options=[
                {'label': i, 'value': i}
                for i in [
                    'Daily',
                    'Weekly',
                    'Monthly',
                    'Quarterly',
                    'Yearly',
                ]
            ],
            defaultValue='Daily',
        ),
        fac.AntdText(id='segmented-demo-output'),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('segmented-demo-output', 'children'),
    Input('segmented-demo', 'value'),
)
def segmented_demo(value):
    return f'value: {value}
"""
    }
]
