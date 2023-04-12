import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('table-editable-demo-output', 'children'),
    Input('table-editable-demo', 'recentlyChangedRow'),
    prevent_initial_call=True
)
def table_editable_demo(recentlyChangedRow):

    return json.dumps(
        recentlyChangedRow,
        indent=4,
        ensure_ascii=False
    )
