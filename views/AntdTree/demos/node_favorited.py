import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTree(
                id='tree-favorites-demo',
                treeData=[
                    {
                        'title': '四川省',
                        'key': '四川省',
                        'enableFavorites': False,
                        'children': [
                            {'title': '成都市', 'key': '成都市'},
                            {'title': '广安市', 'key': '广安市'},
                        ],
                    },
                    {
                        'title': '重庆市',
                        'key': '重庆市',
                        'enableFavorites': False,
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
                enableNodeFavorites=True,
            ),
            html.Pre(id='tree-favorites-demo-output'),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('tree-favorites-demo-output', 'children'),
    Input('tree-favorites-demo', 'favoritedKeys'),
)
def tree_favorites_demo(favoritedKeys):
    return json.dumps(
        dict(favoritedKeys=favoritedKeys), indent=4, ensure_ascii=False
    )


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdTree(
            id='tree-favorites-demo',
            treeData=[
                {
                    'title': '四川省',
                    'key': '四川省',
                    'enableFavorites': False,
                    'children': [
                        {'title': '成都市', 'key': '成都市'},
                        {'title': '广安市', 'key': '广安市'},
                    ],
                },
                {
                    'title': '重庆市',
                    'key': '重庆市',
                    'enableFavorites': False,
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
            enableNodeFavorites=True,
        ),
        html.Pre(id='tree-favorites-demo-output'),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('tree-favorites-demo-output', 'children'),
    Input('tree-favorites-demo', 'favoritedKeys'),
)
def tree_favorites_demo(favoritedKeys):
    return json.dumps(
        dict(favoritedKeys=favoritedKeys), indent=4, ensure_ascii=False
    )
"""
    }
]
