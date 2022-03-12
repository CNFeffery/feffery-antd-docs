import dash
from datetime import datetime
from dash.dependencies import Input, Output

from server import app


@app.callback(
    [Output('collapse-demo', 'children'),
     Output('collapse-demo', 'is_open')],
    Input('collapse-switch-demo', 'checked')
)
def collapse_demo_callback(checked):
    if checked:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S'), checked

    return dash.no_update, checked
