from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('checkbox-group-demo1-output', 'children'),
    Input('checkbox-group-demo1', 'value')
)
def checkbox_group_demo1(value):

    return f'value: {value}'


app.clientside_callback(
    '''(checked, value, options) => {
        let ctx = dash_clientside.callback_context;
        value = value || []
        if ( ctx?.triggered[0].prop_id === 'checkbox-group-demo-client-side.value' ) {
            return [
                value.length === options.length ? true : false,
                value,
                value.length > 0 && value.length < options.length ? true : false
            ]
        } else if ( ctx?.triggered[0].prop_id === 'checkbox-demo-client-side.checked' ) {
            return [
                checked,
                checked ? options.map(item => item.value) : [],
                !checked && value.length > 0 && value.length < options.length ? true : false
            ]
        }
        return dash_clientside.no_update;
    }''',
    [Output('checkbox-demo-client-side', 'checked'),
     Output('checkbox-group-demo-client-side', 'value'),
     Output('checkbox-demo-client-side', 'indeterminate')],
    [Input('checkbox-demo-client-side', 'checked'),
     Input('checkbox-group-demo-client-side', 'value')],
    State('checkbox-group-demo-client-side', 'options'),
    prevent_initial_call=True
)
