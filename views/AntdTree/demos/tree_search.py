import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                id='tree-search-demo-keyword',
                placeholder='请输入搜索关键词',
                value='省',
                style={'width': '100%'},
            ),
            fac.AntdTree(
                id='tree-search-demo',
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
                defaultExpandAll=True,
                highlightStyle={'background': '#ffffb8', 'padding': 0},
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


app.clientside_callback(
    """(value) => value""",
    Output('tree-search-demo', 'searchKeyword'),
    Input('tree-search-demo-keyword', 'value'),
)


code_string = [
    {
        'code': '''
fac.AntdSpace(
    [
        fac.AntdInput(
            id='tree-search-demo-keyword',
            placeholder='请输入搜索关键词',
            value='省',
            style={'width': '100%'},
        ),
        fac.AntdTree(
            id='tree-search-demo',
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
            defaultExpandAll=True,
            highlightStyle={'background': '#ffffb8', 'padding': 0},
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

app.clientside_callback(
    """(value) => value""",
    Output('tree-search-demo', 'searchKeyword'),
    Input('tree-search-demo-keyword', 'value'),
)
'''
    }
]
