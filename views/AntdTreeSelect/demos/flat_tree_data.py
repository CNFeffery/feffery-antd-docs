import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTreeSelect(
        treeDataMode='flat',
        treeData=[
            {'key': '节点1', 'value': '1', 'title': '节点1'},
            *[
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}',
                    'parent': '节点1',
                }
                for i in range(1, 6)
            ],
        ],
        placeholder='请选择',
        style={'width': 256},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTreeSelect(
    treeDataMode='flat',
    treeData=[
        {'key': '节点1', 'value': '1', 'title': '节点1'},
        *[
            {
                'key': f'节点1-{i}',
                'value': f'1-{i}',
                'title': f'节点1-{i}',
                'parent': '节点1',
            }
            for i in range(1, 6)
        ],
    ],
    placeholder='请选择',
    style={'width': 256},
)
"""
    }
]
