import uuid
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('key-demo1-output', 'children'),
    Input('key-demo1-type', 'value')
)
def key_demo1(value):

    return value * 100


@app.callback(
    [Output('key-demo2-output', 'children'),
     Output('key-demo2-output', 'key')],
    Input('key-demo2-type', 'value')
)
def key_demo2(value):

    return [value * 100, str(uuid.uuid4())]
