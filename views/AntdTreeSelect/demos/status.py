import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
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
                placeholder=f'status="{status}"',
                status=status,
                style={'width': 256},
            )
            for status in ['warning', 'error']
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
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
            placeholder=f'status="{status}"',
            status=status,
            style={'width': 256},
        )
        for status in ['warning', 'error']
    ],
    direction='vertical',
)
"""
    }
]
