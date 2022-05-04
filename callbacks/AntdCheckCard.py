from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('check-card-demo-output', 'children'),
    Input('check-card-demo', 'checked')
)
def check_card_demo_callback(checked):

    return str(checked)