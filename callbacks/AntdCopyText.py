from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('copy-text-output', 'text'),
    Input('copy-text-input', 'value')
)
def copy_text_callback(value):
    return value or '无内容'
