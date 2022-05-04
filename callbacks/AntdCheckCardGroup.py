from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('check-card-group-demo1-output', 'children'),
    Input('check-card-group-demo1', 'value')
)
def check_card_group_demo1_callback(value):
    return str(value)


@app.callback(
    Output('check-card-group-demo2-output', 'children'),
    Input('check-card-group-demo2', 'value')
)
def check_card_group_demo2_callback(value):
    return str(value)
