import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('tree-demo-output', 'children'),
    [Input('tree-demo', 'selectedKeys'),
     Input('tree-demo', 'checkedKeys'),
     Input('tree-demo', 'halfCheckedKeys'),
     Input('tree-demo', 'expandedKeys')]
)
def tree_demo(selectedKeys, checkedKeys, halfCheckedKeys, expandedKeys):

    return json.dumps(
        dict(
            selectedKeys=selectedKeys,
            checkedKeys=checkedKeys,
            halfCheckedKeys=halfCheckedKeys,
            expandedKeys=expandedKeys
        ),
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    Output('tree-drag-demo-output', 'children'),
    [Input('tree-drag-demo', 'treeData'),
     Input('tree-drag-demo', 'draggedNodeKey')]
)
def tree_drag_demo(treeData, draggedNodeKey):

    return json.dumps(
        dict(
            treeData=treeData,
            draggedNodeKey=draggedNodeKey
        ),
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    Output('tree-context-menu-demo-output', 'children'),
    Input('tree-context-menu-demo', 'clickedContextMenu')
)
def tree_context_menu_demo(clickedContextMenu):

    return json.dumps(
        dict(
            clickedContextMenu=clickedContextMenu
        ),
        indent=4,
        ensure_ascii=False
    )
