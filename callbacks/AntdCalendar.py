from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('calendar-demo-output', 'children'),
    Input('calendar-demo', 'value')
)
def calendar_demo(value):

    return f'value: {value}'


@app.callback(
    Output('calendar-format-demo-output', 'children'),
    Input('calendar-format-demo', 'value')
)
def calendar_format_demo(value):

    return f'value: {value}'
