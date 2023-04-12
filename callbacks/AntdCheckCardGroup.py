from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('check-card-group-demo-output', 'children'),
    Input('check-card-group-demo', 'value')
)
def check_card_group_demo(value):

    return f'value: {value}'
