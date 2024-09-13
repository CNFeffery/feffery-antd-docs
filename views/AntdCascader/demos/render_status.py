import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdCascader(
                    placeholder=f'status="{status}"',
                    options=[
                        {
                            'value': 'Node 1',
                            'label': 'Node 1',
                            'children': [
                                {'value': 'Node 1-1', 'label': 'Node 1-1'},
                                {
                                    'value': 'Node 1-2',
                                    'label': 'Node 1-2',
                                    'children': [
                                        {
                                            'value': 'Node 1-2-1',
                                            'label': 'Node 1-2-1',
                                        },
                                        {
                                            'value': 'Node 1-2-2',
                                            'label': 'Node 1-2-2',
                                        },
                                    ],
                                },
                            ],
                        },
                        {
                            'value': 'Node 2',
                            'label': 'Node 2',
                            'children': [
                                {'value': 'Node 2-1', 'label': 'Node 2-1'},
                                {'value': 'Node 2-2', 'label': 'Node 2-2'},
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdCascader(
            placeholder=f'status="{status}"',
            options=[
                {
                    'value': 'Node 1',
                    'label': 'Node 1',
                    'children': [
                        {'value': 'Node 1-1', 'label': 'Node 1-1'},
                        {
                            'value': 'Node 1-2',
                            'label': 'Node 1-2',
                            'children': [
                                {
                                    'value': 'Node 1-2-1',
                                    'label': 'Node 1-2-1',
                                },
                                {
                                    'value': 'Node 1-2-2',
                                    'label': 'Node 1-2-2',
                                },
                            ],
                        },
                    ],
                },
                {
                    'value': 'Node 2',
                    'label': 'Node 2',
                    'children': [
                        {'value': 'Node 2-1', 'label': 'Node 2-1'},
                        {'value': 'Node 2-2', 'label': 'Node 2-2'},
                    ],
                },
            ],
            status=status,
        )
        for status in ['warning', 'error']
    ],
    direction='vertical',
)
"""
            }
        ]
