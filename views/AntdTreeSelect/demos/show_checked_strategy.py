import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider(
            'showCheckedStrategy="show-all"（默认）',
            innerTextOrientation='left',
        ),
        fac.AntdTreeSelect(
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
        fac.AntdDivider(
            'showCheckedStrategy="show-parent"', innerTextOrientation='left'
        ),
        fac.AntdTreeSelect(
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
            showCheckedStrategy='show-parent',
            style={'width': 256},
        ),
        fac.AntdDivider(
            'showCheckedStrategy="show-child"', innerTextOrientation='left'
        ),
        fac.AntdTreeSelect(
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
            showCheckedStrategy='show-child',
            style={'width': 256},
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider(
        'showCheckedStrategy="show-all"（默认）',
        innerTextOrientation='left',
    ),
    fac.AntdTreeSelect(
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
    fac.AntdDivider(
        'showCheckedStrategy="show-parent"', innerTextOrientation='left'
    ),
    fac.AntdTreeSelect(
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
        showCheckedStrategy='show-parent',
        style={'width': 256},
    ),
    fac.AntdDivider(
        'showCheckedStrategy="show-child"', innerTextOrientation='left'
    ),
    fac.AntdTreeSelect(
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
        showCheckedStrategy='show-child',
        style={'width': 256},
    ),
]
"""
    }
]
