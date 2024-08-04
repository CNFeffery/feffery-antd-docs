import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSlider(
            id='slider-demo',
            min=0,
            max=100,
            defaultValue=33,
            style={'width': 300},
        ),
        fac.AntdText(id='slider-demo-output'),
        fac.AntdSlider(
            id='slider-range-demo',
            range=True,
            min=0,
            max=100,
            defaultValue=[10, 90],
            style={'width': 300},
        ),
        fac.AntdText(id='slider-range-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('slider-demo-output', 'children'), 
    Input('slider-demo', 'value')
)
def slider_demo(value):
    return f'value: {value}'


@app.callback(
    Output('slider-range-demo-output', 'children'),
    Input('slider-range-demo', 'value'),
)
def slider_range_demo(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdSlider(
    id='slider-demo',
    min=0,
    max=100,
    defaultValue=33,
    style={
        'width': 300
    }
),
fac.AntdText(
    id='slider-demo-output'
),

fac.AntdSlider(
    id='slider-range-demo',
    range=True,
    min=0,
    max=100,
    defaultValue=[10, 90],
    style={
        'width': 300
    }
),
fac.AntdText(
    id='slider-range-demo-output'
)

...

@app.callback(
    Output('slider-demo-output', 'children'),
    Input('slider-demo', 'value')
)
def slider_demo(value):

    return f'value: {value}'


@app.callback(
    Output('slider-range-demo-output', 'children'),
    Input('slider-range-demo', 'value')
)
def slider_range_demo(value):

    return f'value: {value}'
"""
    }
]
