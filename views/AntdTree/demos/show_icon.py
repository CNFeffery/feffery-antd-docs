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
                'icon': 'antd-cloud',
                'children': [
                    {
                        'title': '成都市',
                        'key': '成都市',
                        'icon': 'antd-cloud-server',
                    },
                    {
                        'title': '广安市',
                        'key': '广安市',
                        'icon': 'antd-cloud-server',
                    },
                ],
            },
            {
                'title': '重庆市',
                'key': '重庆市',
                'icon': 'antd-cloud',
                'children': [
                    {
                        'title': '渝中区',
                        'key': '渝中区',
                        'icon': 'antd-cloud-server',
                        'children': [
                            {
                                'title': '解放碑街道',
                                'key': '解放碑街道',
                                'icon': 'antd-cloud-server',
                            }
                        ],
                    },
                    {
                        'title': '渝北区',
                        'key': '渝北区',
                        'icon': 'antd-cloud-server',
                    },
                ],
            },
        ],
        showIcon=True,
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
            'icon': 'antd-cloud',
            'children': [
                {
                    'title': '成都市',
                    'key': '成都市',
                    'icon': 'antd-cloud-server',
                },
                {
                    'title': '广安市',
                    'key': '广安市',
                    'icon': 'antd-cloud-server',
                },
            ],
        },
        {
            'title': '重庆市',
            'key': '重庆市',
            'icon': 'antd-cloud',
            'children': [
                {
                    'title': '渝中区',
                    'key': '渝中区',
                    'icon': 'antd-cloud-server',
                    'children': [
                        {
                            'title': '解放碑街道',
                            'key': '解放碑街道',
                            'icon': 'antd-cloud-server',
                        }
                    ],
                },
                {
                    'title': '渝北区',
                    'key': '渝北区',
                    'icon': 'antd-cloud-server',
                },
            ],
        },
    ],
    showIcon=True,
    defaultExpandAll=True,
)
"""
    }
]
