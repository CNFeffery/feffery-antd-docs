from dash.dependencies import Input, Output, State

from server import app


app.clientside_callback(
    '''(nClicks, collapsed) => {
        return [!collapsed, collapsed ? 'antd-arrow-left' : 'antd-arrow-right'];
    }''',
    [Output('menu-collapse-sider-custom-demo', 'collapsed'),
     Output('menu-collapse-sider-custom-demo-trigger-icon', 'icon')],
    Input('menu-collapse-sider-custom-demo-trigger', 'nClicks'),
    State('menu-collapse-sider-custom-demo', 'collapsed'),
    prevent_initial_call=True
)

@app.callback(
    Output('menu-demo-output', 'children'),
    Input('menu-demo', 'currentKey')
)
def menu_callback_demo(currentKey):

    return f'currentKey: {currentKey}'