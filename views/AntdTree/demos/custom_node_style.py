import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        # 动态样式
        fuc.FefferyStyle(
            rawStyle="""
.tree-node-style-demo1 {
    color: #2f9e44;
}

.tree-node-style-demo1:hover {
    color: #b2f2bb;
}

.tree-node-style-demo2 {
    color: #fd7e14;
}
"""
        ),
        fac.AntdTree(
            treeData=[
                {
                    'title': '四川省',
                    'key': '四川省',
                    'className': 'tree-node-style-demo1',
                    'children': [
                        {
                            'title': '成都市',
                            'key': '成都市',
                            'className': 'tree-node-style-demo1',
                        },
                        {
                            'title': '广安市',
                            'key': '广安市',
                            'className': 'tree-node-style-demo1',
                        },
                    ],
                },
                {
                    'title': '重庆市',
                    'key': '重庆市',
                    'className': 'tree-node-style-demo2',
                    'children': [
                        {
                            'title': '渝中区',
                            'key': '渝中区',
                            'className': 'tree-node-style-demo2',
                            'children': [
                                {
                                    'title': '解放碑街道',
                                    'key': '解放碑街道',
                                    'className': 'tree-node-style-demo2',
                                }
                            ],
                        },
                        {
                            'title': '渝北区',
                            'key': '渝北区',
                            'className': 'tree-node-style-demo2',
                        },
                    ],
                },
            ],
            defaultExpandAll=True,
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': '''
[
    # 动态样式
    fuc.FefferyStyle(
        rawStyle="""
.tree-node-style-demo1 {
    color: #2f9e44;
}

.tree-node-style-demo1:hover {
    color: #b2f2bb;
}

.tree-node-style-demo2 {
    color: #fd7e14;
}
"""
    ),
    fac.AntdTree(
        treeData=[
            {
                'title': '四川省',
                'key': '四川省',
                'className': 'tree-node-style-demo1',
                'children': [
                    {
                        'title': '成都市',
                        'key': '成都市',
                        'className': 'tree-node-style-demo1',
                    },
                    {
                        'title': '广安市',
                        'key': '广安市',
                        'className': 'tree-node-style-demo1',
                    },
                ],
            },
            {
                'title': '重庆市',
                'key': '重庆市',
                'className': 'tree-node-style-demo2',
                'children': [
                    {
                        'title': '渝中区',
                        'key': '渝中区',
                        'className': 'tree-node-style-demo2',
                        'children': [
                            {
                                'title': '解放碑街道',
                                'key': '解放碑街道',
                                'className': 'tree-node-style-demo2',
                            }
                        ],
                    },
                    {
                        'title': '渝北区',
                        'key': '渝北区',
                        'className': 'tree-node-style-demo2',
                    },
                ],
            },
        ],
        defaultExpandAll=True,
    ),
]
'''
    }
]
