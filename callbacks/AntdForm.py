from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    [Output('form-demo-1', 'validateStatus'),
     Output('form-demo-1', 'help')],
    Input('form-demo-1-status', 'value')
)
def form_demo_1_callback(value):
    if not value or value == 'None':
        return None, None

    return value, f'validateStatus="{value}"'


@app.callback(
    [Output('form-item-validate-demo-username', 'validateStatus'),
     Output('form-item-validate-demo-password', 'validateStatus'),
     Output('form-item-validate-demo-username', 'help'),
     Output('form-item-validate-demo-password', 'help')],
    Input('form-validate-demo-submit', 'nClicks'),
    [State('form-validate-demo-username', 'value'),
     State('form-validate-demo-password', 'value')],
    prevent_initial_call=True
)
def form_demo_2_callback(nClicks, username, password):

    if username and password:
        return [
            None if username == 'fac' else 'error',
            ('success' if password == '123456' else 'error')
            if username == 'fac' else None,
            None if username == 'fac' else '用户不存在！',
            ('密码正确！' if password == '123456' else '密码错误！')
            if username == 'fac' else None
        ]

    return [
        None if username else 'error',
        None if password else 'error',
        None if username else '用户名不能为空！',
        None if password else '密码不能为空！'
    ]
