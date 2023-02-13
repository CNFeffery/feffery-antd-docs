from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('checkbox-demo-output', 'children'),
    Input('checkbox-demo', 'checked')
)
def checkbox_demo(checked):

    return f'checked: {checked}'
