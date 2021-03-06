from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('tree-demo-output', 'children'),
    [Input('tree-demo', 'selectedKeys'),
     Input('tree-demo', 'checkedKeys'),
     Input('tree-demo', 'halfCheckedKeys')],
    prevent_initial_call=True
)
def tree_callback_demo(selectedKeys, checkedKeys, halfCheckedKeys):
    return [
        fac.AntdTitle('selectedKeys：', level=5),
        html.Pre(str(selectedKeys)),

        fac.AntdTitle('checkedKeys：', level=5),
        html.Pre(str(checkedKeys)),

        fac.AntdTitle('halfCheckedKeys：', level=5),
        html.Pre(str(halfCheckedKeys))
    ]
