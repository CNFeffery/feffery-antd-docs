from dash.dependencies import Input, Output

from server import app


@app.callback(
    [Output('segmented-coloring-demo1', 'bordered'),
     Output('segmented-coloring-demo1', 'controls'),
     Output('segmented-coloring-demo1', 'disabled'),
     Output('segmented-coloring-demo1', 'readOnly'),
     Output('segmented-coloring-demo1', 'colorBlockPosition')],
    [Input('segmented-coloring-demo1-bordered', 'checked'),
     Input('segmented-coloring-demo1-controls', 'checked'),
     Input('segmented-coloring-demo1-disabled', 'checked'),
     Input('segmented-coloring-demo1-readOnly', 'checked'),
     Input('segmented-coloring-demo1-colorBlockPosition', 'checked')]
)
def segmented_coloring_demo1_callback(*checked_list):
    return [
        *checked_list[:4],
        'right' if checked_list[4] else 'left'
    ]


@app.callback(
    Output('segmented-coloring-demo2-output', 'children'),
    Input('segmented-coloring-demo2', 'breakpoints')
)
def segmented_coloring_demo2_callback(breakpoints):
    return str(breakpoints)
