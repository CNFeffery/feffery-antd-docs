import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('tree-select-demo-output', 'children'),
    [Input('tree-select-demo', 'value'),
     Input('tree-select-demo', 'treeExpandedKeys')]
)
def tree_select_demo(value, treeExpandedKeys):

    return [
        fac.AntdText(f'value: {value}'),
        fac.AntdText(f'treeExpandedKeys: {treeExpandedKeys}')
    ]


@app.callback(
    Output('tree-select-multiple-demo-output', 'children'),
    [Input('tree-select-multiple-demo', 'value'),
     Input('tree-select-multiple-demo', 'treeExpandedKeys')]
)
def tree_select_multiple_demo(value, treeExpandedKeys):

    return [
        fac.AntdText(f'value: {value}'),
        fac.AntdText(f'treeExpandedKeys: {treeExpandedKeys}')
    ]
