import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('cascader-demo1-output', 'children'),
    Input('cascader-demo1', 'value'),
    prevent_initial_call=True
)
def cascader_demo1(value):

    return str(value)


@app.callback(
    Output('cascader-demo2-output', 'children'),
    Input('cascader-demo2', 'value'),
    prevent_initial_call=True
)
def cascader_demo2(value):

    return str(value)


@app.callback(
    Output('cascader-demo3-output', 'children'),
    Input('cascader-demo3', 'value'),
    prevent_initial_call=True
)
def cascader_demo3(value):

    return json.dumps(
        value,
        indent=4,
        ensure_ascii=False
    )
