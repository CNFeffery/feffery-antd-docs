from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('alert-description-output', 'children'),
    Input('alert-message-button-input', 'nClicks'),
    prevent_initial_call=True
)
def alert_message_description_callback_demo(nClicks):

    return f'这是组件型description参数示例，上面的按钮被点了{nClicks}次'
