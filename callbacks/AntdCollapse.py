from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('collapse-child-demo1-output', 'children'),
    Input('collapse-child-demo1', 'value')
)
def collapse_child_demo1(value):

    return value


@app.callback(
    Output('collapse-child-demo2-output', 'children'),
    Input('collapse-child-demo2', 'value')
)
def collapse_child_demo2(value):

    return value


@app.callback(
    Output('collapse-demo-output', 'children'),
    Input('collapse-demo', 'isOpen')
)
def collapse_demo(isOpen):

    return f'isOpen={isOpen}'
