from dash.dependencies import Input, Output

from server import app


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
