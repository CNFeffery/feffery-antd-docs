import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTreeSelect(
        id='test-max-count-demo',
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
                    for i in range(1, 11)
                ],
            }
        ],
        placeholder='请选择',
        multiple=True,
        treeCheckable=True,
        showCheckedStrategy='show-child',
        maxCount=3,
        style={'width': 256},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTreeSelect(
    id='test-max-count-demo',
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
                for i in range(1, 11)
            ],
        }
    ],
    placeholder='请选择',
    multiple=True,
    treeCheckable=True,
    showCheckedStrategy='show-child',
    maxCount=3,
    style={'width': 256},
)
"""
    }
]
