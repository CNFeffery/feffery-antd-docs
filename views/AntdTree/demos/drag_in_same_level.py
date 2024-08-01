import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTree(
        treeData=[
            {
                'title': '根节点',
                'key': '根节点',
                'children': [
                    {
                        'title': f'节点{i}',
                        'key': f'节点{i}',
                    }
                    for i in range(1, 6)
                ],
            }
        ],
        draggable=True,
        dragInSameLevel=True,
        defaultExpandAll=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTree(
    treeData=[
        {
            'title': '根节点',
            'key': '根节点',
            'children': [
                {
                    'title': f'节点{i}',
                    'key': f'节点{i}',
                }
                for i in range(1, 6)
            ],
        }
    ],
    draggable=True,
    dragInSameLevel=True,
    defaultExpandAll=True,
)
"""
    }
]
