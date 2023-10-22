import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('table-editable-demo-output', 'children'),
    [Input('table-editable-demo', 'recentlyChangedRow'),
    Input('table-editable-demo', 'recentlyChangedColumn')],
    prevent_initial_call=True
)
def table_editable_demo(recentlyChangedRow, recentlyChangedColumn):

    return json.dumps(
        dict(
            recentlyChangedRow=recentlyChangedRow,
            recentlyChangedColumn=recentlyChangedColumn
        ),
        indent=4,
        ensure_ascii=False
    )
