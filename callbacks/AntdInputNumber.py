from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('input-number-demo-output', 'children'),
    Input('input-number-demo', 'value')
)
def input_number_demo(value):

    return f'value: {value}'

@app.callback(
    Output('input-number-debounce-demo-output', 'children'),
    Input('input-number-debounce-demo', 'debounceValue')
)
def input_number_debounce_demo(debounceValue):

    return f'debounceValue: {debounceValue}'