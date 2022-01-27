import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('input-value-demo-output', 'children'),
    Input('input-value-demo', 'value'),
    prevent_initial_call=True
)
def input_value_callback_demo(value):

    return fac.AntdText(f'value: {value}', italic=True)


@app.callback(
    Output('input-nSubmit-demo-output', 'children'),
    Input('input-nSubmit-demo', 'nSubmit'),
    State('input-nSubmit-demo', 'value'),
    prevent_initial_call=True
)
def input_nSubmit_callback_demo(nSubmit, value):

    if nSubmit and value:
        return fac.AntdText(f'nSubmit: {nSubmit}   value: {value}', italic=True)


@app.callback(
    Output('input-nClicksSearch-demo-output', 'children'),
    Input('input-nClicksSearch-demo', 'nClicksSearch'),
    State('input-nClicksSearch-demo', 'value'),
    prevent_initial_call=True
)
def input_nClicksSearch_callback_demo(nClicksSearch, value):

    if nClicksSearch and value:
        return fac.AntdText(f'nClicksSearch: {nClicksSearch}   value: {value}', italic=True)
