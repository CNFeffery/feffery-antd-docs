from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('accordion-demo-output', 'children'),
    Input('accordion-demo', 'activeKey')
)
def accordion_demo(activeKey):

    return f'activeKey: {activeKey}'
