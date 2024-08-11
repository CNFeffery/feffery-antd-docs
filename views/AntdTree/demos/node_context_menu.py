import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTree(
        treeData=[
            {
                'title': '四川省',
                'key': '四川省',
                'children': [
                    {
                        'title': '成都市',
                        'key': '成都市',
                    },
                    {
                        'title': '广安市',
                        'key': '广安市',
                    },
                ],
                'contextMenu': [
                    {'key': f'四川省-操作选项{i}', 'label': f'操作选项{i}'}
                    for i in range(1, 6)
                ],
            },
            {
                'title': '重庆市',
                'key': '重庆市',
                'children': [
                    {
                        'title': '渝中区',
                        'key': '渝中区',
                        'children': [
                            {
                                'title': '解放碑街道',
                                'key': '解放碑街道',
                            }
                        ],
                    },
                    {
                        'title': '渝北区',
                        'key': '渝北区',
                    },
                ],
                'contextMenu': [
                    {
                        'key': f'重庆市-操作选项{i}',
                        'label': f'操作选项{i}',
                        'icon': 'antd-function',
                    }
                    for i in range(1, 6)
                ],
            },
        ],
        defaultExpandAll=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTree(
    treeData=[
        {
            'title': '四川省',
            'key': '四川省',
            'children': [
                {
                    'title': '成都市',
                    'key': '成都市',
                },
                {
                    'title': '广安市',
                    'key': '广安市',
                },
            ],
            'contextMenu': [
                {'key': f'四川省-操作选项{i}', 'label': f'操作选项{i}'}
                for i in range(1, 6)
            ],
        },
        {
            'title': '重庆市',
            'key': '重庆市',
            'children': [
                {
                    'title': '渝中区',
                    'key': '渝中区',
                    'children': [
                        {
                            'title': '解放碑街道',
                            'key': '解放碑街道',
                        }
                    ],
                },
                {
                    'title': '渝北区',
                    'key': '渝北区',
                },
            ],
            'contextMenu': [
                {
                    'key': f'重庆市-操作选项{i}',
                    'label': f'操作选项{i}',
                    'icon': 'antd-function',
                }
                for i in range(1, 6)
            ],
        },
    ],
    defaultExpandAll=True,
)
"""
    }
]
