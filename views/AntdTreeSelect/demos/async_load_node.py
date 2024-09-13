import time
import feffery_antd_components as fac
from feffery_dash_utils.tree_utils import TreeManager
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTreeSelect(
        id='tree-select-async-demo',
        treeData=[
            {
                'key': '节点1',
                'title': '节点1',
                'value': '节点1',
            },
            {
                'key': '节点2',
                'title': '节点2',
                'value': '节点2',
            },
            {
                'key': '节点3',
                'title': '节点3',
                'value': '节点3',
                'isLeaf': True,
            },
        ],
        enableAsyncLoad=True,
        style={'width': 300},
    )

    return demo_contents


@app.callback(
    Output('tree-select-async-demo', 'treeData'),
    Input('tree-select-async-demo', 'loadingNode'),
    State('tree-select-async-demo', 'treeData'),
    prevent_initial_call=True,
)
def tree_select_async_demo(loadingNode, treeData):
    time.sleep(0.5)
    return TreeManager.update_tree_node(
        treeData,
        node_key=loadingNode['key'],
        new_node={
            'children': [
                {
                    'key': loadingNode['key'] + '-1',
                    'title': loadingNode['key'] + '-1',
                    'value': loadingNode['key'] + '-1',
                }
            ]
        },
        mode='overlay',
    )


code_string = [
    {
        'code': """
from feffery_dash_utils.tree_utils import TreeManager

...

fac.AntdTreeSelect(
    id='tree-select-async-demo',
    treeData=[
        {
            'key': '节点1',
            'title': '节点1',
            'value': '节点1',
        },
        {
            'key': '节点2',
            'title': '节点2',
            'value': '节点2',
        },
        {
            'key': '节点3',
            'title': '节点3',
            'value': '节点3',
            'isLeaf': True,
        },
    ],
    enableAsyncLoad=True,
    style={'width': 300},
)

...

@app.callback(
    Output('tree-select-async-demo', 'treeData'),
    Input('tree-select-async-demo', 'loadingNode'),
    State('tree-select-async-demo', 'treeData'),
    prevent_initial_call=True,
)
def tree_select_async_demo(loadingNode, treeData):
    time.sleep(0.5)
    return TreeManager.update_tree_node(
        treeData,
        node_key=loadingNode['key'],
        new_node={
            'children': [
                {
                    'key': loadingNode['key'] + '-1',
                    'title': loadingNode['key'] + '-1',
                    'value': loadingNode['key'] + '-1',
                }
            ]
        },
        mode='overlay',
    )
"""
    }
]
