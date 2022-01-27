from dash.dependencies import Input, Output, State

from server import app

app.clientside_callback(
    """
    function(nClicks, value, selectedOptions) {
    
        if ( !value ) {
            value = ''
        }
        
        if ( !selectedOptions ) {
            selectedOptions = []
        }
    
        return [
            value.toString(),
            selectedOptions.toString()
        ];
    }
    """,
    [Output('mentions-demo-output-value', 'children'),
     Output('mentions-demo-output-selectedOptions', 'children')],
    Input('mentions-submit', 'nClicks'),
    [State('mentions-demo', 'value'),
     State('mentions-demo', 'selectedOptions')],
    prevent_initial_call=True
)
