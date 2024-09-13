import time
import feffery_antd_components as fac
from feffery_dash_utils.tree_utils import TreeManager
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTree(
        id='tree-async-demo',
        treeData=[
            {
                'key': '节点1',
                'title': '节点1',
            },
            {
                'key': '节点2',
                'title': '节点2',
                'children': [
                    {
                        'key': '节点2-1',
                        'title': '节点2-1',
                        'isLeaf': True,
                    },
                ],
            },
            {
                'key': '节点3',
                'title': '节点3',
                'isLeaf': True,
            },
        ],
        enableAsyncLoad=True,
    )

    return demo_contents


@app.callback(
    Output('tree-async-demo', 'treeData'),
    Input('tree-async-demo', 'loadingNode'),
    State('tree-async-demo', 'treeData'),
    prevent_initial_call=True,
)
def tree_demo(loadingNode, treeData):
    time.sleep(0.5)
    return TreeManager.update_tree_node(
        treeData,
        node_key=loadingNode['key'],
        new_node={
            'children': [
                {
                    'key': loadingNode['key'] + '-1',
                    'title': loadingNode['key'] + '-1',
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

fac.AntdTree(
    id='tree-async-demo',
    treeData=[
        {
            'key': '节点1',
            'title': '节点1',
        },
        {
            'key': '节点2',
            'title': '节点2',
            'children': [
                {
                    'key': '节点2-1',
                    'title': '节点2-1',
                    'isLeaf': True,
                },
            ],
        },
        {
            'key': '节点3',
            'title': '节点3',
            'isLeaf': True,
        },
    ],
    enableAsyncLoad=True,
)

...

@app.callback(
    Output('tree-async-demo', 'treeData'),
    Input('tree-async-demo', 'loadingNode'),
    State('tree-async-demo', 'treeData'),
    prevent_initial_call=True,
)
def tree_demo(loadingNode, treeData):
    time.sleep(0.5)
    return TreeManager.update_tree_node(
        treeData,
        node_key=loadingNode['key'],
        new_node={
            'children': [
                {
                    'key': loadingNode['key'] + '-1',
                    'title': loadingNode['key'] + '-1',
                }
            ]
        },
        mode='overlay',
    )
"""
    }
]
