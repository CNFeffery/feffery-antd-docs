import feffery_antd_components as fac
import feffery_utils_components as fuc

from dash.dependencies import Component, Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferySortable(
                id='tag-draggable-sortable-demo',
                items=[
                    {
                        'key': f'标签{i}',
                        'content': fac.AntdTag(
                            content=f'标签{i}',
                            href='anywhere',
                            style={'marginInlineEnd': 0},
                        ),
                        'style': {
                            'position': 'relative',
                            'display': 'inline-flex',
                            'borderRadius': 8,
                            'marginRight': 8,
                        },
                        'draggingStyle': {
                            'boxShadow': '0px 0px 12px rgba(0, 0, 0, 0.12)',
                        },
                    }
                    for i in range(1, 6)
                ],
                direction='horizontal',
                itemDraggingScale=1.025,
                # 注：当前示例的实现方式，实际上是将FefferySortable的拖拽handle设为透明并扩大大小覆盖整个AntdTag
                # 因此，如果AntdTag的content中存在任何可交互组件，交互将会失效
                handleStyle={'color': 'transparent'},
                handleClassName={
                    'position': 'absolute',
                    'width': 'calc(100% - 8px)',
                    'height': 'calc(100% - 8px)',
                    'padding': '4px',
                    'borderRadius': '8px',
                },
            ),
            fac.AntdCard(
                id='tag-draggable-output-demo', headStyle={'display': 'none'}
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


# 展示当前排序的回调
@app.callback(
    Output('tag-draggable-output-demo', 'children'),
    Input('tag-draggable-sortable-demo', 'currentOrder'),
)
def sortable_list_demo(currentOrder):
    return str(currentOrder)


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fuc.FefferySortable(
            id='tag-draggable-sortable-demo',
            items=[
                {
                    'key': f'标签{i}',
                    'content': fac.AntdTag(
                        content=f'标签{i}',
                        href='anywhere',
                        style={'marginInlineEnd': 0},
                    ),
                    'style': {
                        'position': 'relative',
                        'display': 'inline-flex',
                        'borderRadius': 8,
                        'marginRight': 8,
                    },
                    'draggingStyle': {
                        'boxShadow': '0px 0px 12px rgba(0, 0, 0, 0.12)',
                    },
                }
                for i in range(1, 6)
            ],
            direction='horizontal',
            itemDraggingScale=1.025,
            # 注：当前示例的实现方式，实际上是将FefferySortable的拖拽handle设为透明并扩大大小覆盖整个AntdTag
            # 因此，如果AntdTag的content中存在任何可交互组件，交互将会失效
            handleStyle={'color': 'transparent'},
            handleClassName={
                'position': 'absolute',
                'width': 'calc(100% - 8px)',
                'height': 'calc(100% - 8px)',
                'padding': '4px',
                'borderRadius': '8px',
            },
        ),
        fac.AntdCard(
            id='tag-draggable-output-demo', headStyle={'display': 'none'}
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)


# 展示当前排序的回调
@app.callback(
    Output('tag-draggable-output-demo', 'children'),
    Input('tag-draggable-sortable-demo', 'currentOrder'),
)
def sortable_list_demo(currentOrder):
    return str(currentOrder)
"""
    }
]
