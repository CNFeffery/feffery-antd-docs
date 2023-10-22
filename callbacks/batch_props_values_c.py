import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('batch-props-values-demo-output', 'children'),
    Input('batch-props-values-demo', 'batchPropsValues')
)
def batch_props_values_demo(batchPropsValues):

    return json.dumps(
        dict(
            batchPropsValues=batchPropsValues
        ),
        indent=4,
        ensure_ascii=False
    )
