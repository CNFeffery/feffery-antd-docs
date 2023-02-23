from dash.dependencies import Input, Output

from server import app


@app.callback(
    [Output('avatar-bg-color-icon-demo', 'style'),
     Output('avatar-bg-color-text-demo', 'style')],
    Input('avatar-bg-color-input', 'color')
)
def avatar_bg_color_demo(color):

    return [
        {
            'background': color
        }
    ] * 2
