import time
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('checkbox-group-demo-output', 'children'),
    Input('checkbox-group-demo', 'value')
)
def checkbox_group_demo_callback(value):
    time.sleep(0.5)
    return str(value)


app.clientside_callback(
    """
    function(checked, value, options) {

        const ctx = dash_clientside.callback_context;

        if ( ctx?.triggered[0].prop_id === 'checkbox-group-demo-client-side.value' ) {
            return [
                value.length === options.length ? true : false,
                value
            ]
        } else if ( ctx?.triggered[0].prop_id === 'checkbox-demo-client-side.checked' ) {
            return [
                checked,
                checked ? options.map(item => item.value) : []
            ]
        }
        return dash_clientside.no_update;
    }
    """,
    [Output('checkbox-demo-client-side', 'checked'),
     Output('checkbox-group-demo-client-side', 'value')],
    [Input('checkbox-demo-client-side', 'checked'),
     Input('checkbox-group-demo-client-side', 'value')],
    State('checkbox-group-demo-client-side', 'options'),
    prevent_initial_call=True
)
