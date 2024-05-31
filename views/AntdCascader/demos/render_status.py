import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCascader(
                placeholder=f'status="{status}"',
                options=[
                    {
                        'value': '节点1',
                        'label': '节点1',
                        'children': [
                            {'value': '节点1-1', 'label': '节点1-1'},
                            {
                                'value': '节点1-2',
                                'label': '节点1-2',
                                'children': [
                                    {
                                        'value': '节点1-2-1',
                                        'label': '节点1-2-1',
                                    },
                                    {
                                        'value': '节点1-2-2',
                                        'label': '节点1-2-2',
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        'value': '节点2',
                        'label': '节点2',
                        'children': [
                            {'value': '节点2-1', 'label': '节点2-1'},
                            {'value': '节点2-2', 'label': '节点2-2'},
                        ],
                    },
                ],
                status=status,
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
        fac.AntdCascader(
            placeholder=f'status="{status}"',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                },
                {
                    'value': '节点2',
                    'label': '节点2',
                    'children': [
                        {
                            'value': '节点2-1',
                            'label': '节点2-1'
                        },
                        {
                            'value': '节点2-2',
                            'label': '节点2-2'
                        }
                    ]
                }
            ],
            status=status
        )
        for status in ['warning', 'error']
    ],
    direction='vertical'
)
"""
    }
]
