import random
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdButton(
                '随机滚动', id='tree-scroll-demo-trigger', type='primary'
            ),
            fac.AntdTree(
                id='tree-scroll-demo',
                treeData=[
                    {
                        'title': '全部节点',
                        'key': '全部节点',
                        'children': [
                            {'title': f'节点{i}', 'key': f'节点{i}'}
                            for i in range(1, 51)
                        ],
                    }
                ],
                defaultExpandAll=True,
                height=200,
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('tree-scroll-demo', 'scrollTarget'),
    Input('tree-scroll-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def tree_scroll_demo(nClicks):
    return {'key': f'节点{random.randint(1, 51)}'}


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdButton(
            '随机滚动', id='tree-scroll-demo-trigger', type='primary'
        ),
        fac.AntdTree(
            id='tree-scroll-demo',
            treeData=[
                {
                    'title': '全部节点',
                    'key': '全部节点',
                    'children': [
                        {'title': f'节点{i}', 'key': f'节点{i}'}
                        for i in range(1, 51)
                    ],
                }
            ],
            defaultExpandAll=True,
            height=200,
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('tree-scroll-demo', 'scrollTarget'),
    Input('tree-scroll-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def tree_scroll_demo(nClicks):
    return {'key': f'节点{random.randint(1, 51)}'}
"""
    }
]
