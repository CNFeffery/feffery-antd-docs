from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('menu-demo-output', 'children'),
    [Input('menu-demo', 'currentKey'),
     Input('menu-demo', 'openKeys')]
)
def menu_callback_demo(currentKey, openKeys):
     

    return f"已选中菜单项：{currentKey}  已展开菜单项：{openKeys}"
