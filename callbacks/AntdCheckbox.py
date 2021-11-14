import time
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('checkbox-demo-output', 'children'),
    Input('checkbox-demo', 'checked')
)
def checkbox_demo_callback(checked):
    time.sleep(0.5)

    return str(checked)