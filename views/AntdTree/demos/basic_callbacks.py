import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTree(
            id='tree-demo',
            treeData=[
                {
                    'title': '四川省',
                    'key': '四川省',
                    'children': [
                        {'title': '成都市', 'key': '成都市'},
                        {'title': '广安市', 'key': '广安市'},
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
                                {'title': '解放碑街道', 'key': '解放碑街道'}
                            ],
                        },
                        {'title': '渝北区', 'key': '渝北区'},
                    ],
                },
            ],
            multiple=True,
            checkable=True,
        ),
        html.Pre(id='tree-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('tree-demo-output', 'children'),
    [
        Input('tree-demo', 'selectedKeys'),
        Input('tree-demo', 'checkedKeys'),
        Input('tree-demo', 'halfCheckedKeys'),
        Input('tree-demo', 'expandedKeys'),
    ],
)
def tree_demo(selectedKeys, checkedKeys, halfCheckedKeys, expandedKeys):
    return json.dumps(
        dict(
            selectedKeys=selectedKeys,
            checkedKeys=checkedKeys,
            halfCheckedKeys=halfCheckedKeys,
            expandedKeys=expandedKeys,
        ),
        indent=4,
        ensure_ascii=False,
    )


code_string = [
    {
        'code': """
[
    fac.AntdTree(
        id='tree-demo',
        treeData=[
            {
                'title': '四川省',
                'key': '四川省',
                'children': [
                    {'title': '成都市', 'key': '成都市'},
                    {'title': '广安市', 'key': '广安市'},
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
                            {'title': '解放碑街道', 'key': '解放碑街道'}
                        ],
                    },
                    {'title': '渝北区', 'key': '渝北区'},
                ],
            },
        ],
        multiple=True,
        checkable=True,
    ),
    html.Pre(id='tree-demo-output'),
]

...

@app.callback(
    Output('tree-demo-output', 'children'),
    [
        Input('tree-demo', 'selectedKeys'),
        Input('tree-demo', 'checkedKeys'),
        Input('tree-demo', 'halfCheckedKeys'),
        Input('tree-demo', 'expandedKeys'),
    ],
)
def tree_demo(selectedKeys, checkedKeys, halfCheckedKeys, expandedKeys):
    return json.dumps(
        dict(
            selectedKeys=selectedKeys,
            checkedKeys=checkedKeys,
            halfCheckedKeys=halfCheckedKeys,
            expandedKeys=expandedKeys,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
    }
]
