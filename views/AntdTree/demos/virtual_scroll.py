import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTree(
        treeData=[
            {
                'title': f'节点{i}',
                'key': f'节点{i}',
                'children': [
                    {
                        'title': f'节点{i}-{j}',
                        'key': f'节点{i}-{j}',
                    }
                    for j in range(1, 10)
                ],
            }
            for i in range(1, 101)
        ],
        height=200,
        style={'border': '1px dashed #ced4da'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTree(
    treeData=[
        {
            'title': f'节点{i}',
            'key': f'节点{i}',
            'children': [
                {
                    'title': f'节点{i}-{j}',
                    'key': f'节点{i}-{j}',
                }
                for j in range(1, 10)
            ],
        }
        for i in range(1, 101)
    ],
    height=200,
    style={'border': '1px dashed #ced4da'},
)
"""
    }
]
