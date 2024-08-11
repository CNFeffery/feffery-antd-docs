import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('单选示例', innerTextOrientation='left'),
        fac.AntdTreeSelect(
            id='tree-select-demo',
            treeData=[
                {
                    'key': '节点1',
                    'value': '1',
                    'title': '节点1',
                    'children': [
                        {
                            'key': f'节点1-{i}',
                            'value': f'1-{i}',
                            'title': f'节点1-{i}',
                        }
                        for i in range(1, 5)
                    ],
                },
                {'key': '节点2', 'value': '2', 'title': '节点2'},
            ],
            placeholder='请选择',
            style={'width': 256},
        ),
        fac.AntdSpace(
            id='tree-select-demo-output',
            direction='vertical',
            style={'width': '100%'},
        ),
        fac.AntdDivider('多选示例', innerTextOrientation='left'),
        fac.AntdTreeSelect(
            id='tree-select-multiple-demo',
            treeData=[
                {
                    'key': '节点1',
                    'value': '1',
                    'title': '节点1',
                    'children': [
                        {
                            'key': f'节点1-{i}',
                            'value': f'1-{i}',
                            'title': f'节点1-{i}',
                        }
                        for i in range(1, 5)
                    ],
                },
                {'key': '节点2', 'value': '2', 'title': '节点2'},
            ],
            placeholder='请选择',
            multiple=True,
            treeCheckable=True,
            style={'width': 256},
        ),
        fac.AntdSpace(
            id='tree-select-multiple-demo-output',
            direction='vertical',
            style={'width': '100%'},
        ),
    ]

    return demo_contents


@app.callback(
    Output('tree-select-demo-output', 'children'),
    [
        Input('tree-select-demo', 'value'),
        Input('tree-select-demo', 'treeExpandedKeys'),
    ],
)
def tree_select_demo(value, treeExpandedKeys):
    return [
        fac.AntdText(f'value: {value}'),
        fac.AntdText(f'treeExpandedKeys: {treeExpandedKeys}'),
    ]


@app.callback(
    Output('tree-select-multiple-demo-output', 'children'),
    [
        Input('tree-select-multiple-demo', 'value'),
        Input('tree-select-multiple-demo', 'treeExpandedKeys'),
    ],
)
def tree_select_multiple_demo(value, treeExpandedKeys):
    return [
        fac.AntdText(f'value: {value}'),
        fac.AntdText(f'treeExpandedKeys: {treeExpandedKeys}'),
    ]


code_string = [
    {
        'code': """
[
    fac.AntdDivider('单选示例', innerTextOrientation='left'),
    fac.AntdTreeSelect(
        id='tree-select-demo',
        treeData=[
            {
                'key': '节点1',
                'value': '1',
                'title': '节点1',
                'children': [
                    {
                        'key': f'节点1-{i}',
                        'value': f'1-{i}',
                        'title': f'节点1-{i}',
                    }
                    for i in range(1, 5)
                ],
            },
            {'key': '节点2', 'value': '2', 'title': '节点2'},
        ],
        placeholder='请选择',
        style={'width': 256},
    ),
    fac.AntdSpace(
        id='tree-select-demo-output',
        direction='vertical',
        style={'width': '100%'},
    ),
    fac.AntdDivider('多选示例', innerTextOrientation='left'),
    fac.AntdTreeSelect(
        id='tree-select-multiple-demo',
        treeData=[
            {
                'key': '节点1',
                'value': '1',
                'title': '节点1',
                'children': [
                    {
                        'key': f'节点1-{i}',
                        'value': f'1-{i}',
                        'title': f'节点1-{i}',
                    }
                    for i in range(1, 5)
                ],
            },
            {'key': '节点2', 'value': '2', 'title': '节点2'},
        ],
        placeholder='请选择',
        multiple=True,
        treeCheckable=True,
        style={'width': 256},
    ),
    fac.AntdSpace(
        id='tree-select-multiple-demo-output',
        direction='vertical',
        style={'width': '100%'},
    ),
]

...

@app.callback(
    Output('tree-select-multiple-demo-output', 'children'),
    [
        Input('tree-select-multiple-demo', 'value'),
        Input('tree-select-multiple-demo', 'treeExpandedKeys'),
    ],
)
def tree_select_multiple_demo(value, treeExpandedKeys):
    return [
        fac.AntdText(f'value: {value}'),
        fac.AntdText(f'treeExpandedKeys: {treeExpandedKeys}'),
    ]
"""
    }
]
