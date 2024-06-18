import dash
import uuid
from datetime import datetime
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State, ALL

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdComment(
            id='comment-demo',
            authorName='费弗里',
            authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
            publishTime={
                'value': '2024-01-01 19:29:01',
                'format': 'YYYY-MM-DD hh:mm:ss',
            },
            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
            defaultAction='liked',
            likesCount=1,
        ),
        fac.AntdSpace(
            [
                fac.AntdInput(
                    id='comment-demo-input',
                    placeholder='发表你的感想...',
                    mode='text-area',
                    maxLength=140,
                    allowClear=True,
                    showCount=True,
                    style={'width': '100%'},
                ),
                fac.AntdButton(
                    '提交评论',
                    id='comment-demo-submit',
                    type='primary',
                    style={'float': 'right'},
                ),
            ],
            size='large',
            direction='vertical',
            style={'width': '100%'},
        ),
    ]

    return demo_contents


@app.callback(
    [Output('comment-demo', 'children'), Output('comment-demo-input', 'value')],
    [
        Input('comment-demo-submit', 'nClicks'),
        Input({'type': 'comment-demo-children', 'index': ALL}, 'deleteClicks'),
    ],
    [State('comment-demo-input', 'value'), State('comment-demo', 'children')],
    prevent_initial_call=True,
)
def comment_demo_add_children_callback(nClicks, deleteClicks, value, children):
    # 本次回调由子回复删除功能触发
    if 'deleteClicks' in dash.callback_context.triggered[0]['prop_id']:
        triggerIndex = eval(
            dash.callback_context.triggered[0]['prop_id'].replace(
                '.deleteClicks', ''
            )
        )['index']

        return [
            child
            for child in children
            if child['props']['id']['index'] != triggerIndex
        ], dash.no_update

    if value:
        return children + [
            fac.AntdComment(
                id={
                    'type': 'comment-demo-children',
                    'index': str(uuid.uuid4()),
                },
                authorName='dash学习者',
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss',
                },
                commentContent=value,
                showReply=False,
                showDelete=True,
            )
        ] if children else [
            fac.AntdComment(
                id={
                    'type': 'comment-demo-children',
                    'index': str(uuid.uuid4()),
                },
                authorName='dash学习者',
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss',
                },
                commentContent=value,
                showReply=False,
                showDelete=True,
            )
        ], None

    else:
        return children, None


code_string = [
    {
        'code': """
[
    fac.AntdComment(
        id='comment-demo',
        authorName='费弗里',
        authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
        publishTime={
            'value': '2024-01-01 19:29:01',
            'format': 'YYYY-MM-DD hh:mm:ss',
        },
        commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
        defaultAction='liked',
        likesCount=1,
    ),
    fac.AntdSpace(
        [
            fac.AntdInput(
                id='comment-demo-input',
                placeholder='发表你的感想...',
                mode='text-area',
                maxLength=140,
                allowClear=True,
                showCount=True,
                style={'width': '100%'},
            ),
            fac.AntdButton(
                '提交评论',
                id='comment-demo-submit',
                type='primary',
                style={'float': 'right'},
            ),
        ],
        size='large',
        direction='vertical',
        style={'width': '100%'},
    ),
]

...

@app.callback(
    [Output('comment-demo', 'children'), Output('comment-demo-input', 'value')],
    [
        Input('comment-demo-submit', 'nClicks'),
        Input({'type': 'comment-demo-children', 'index': ALL}, 'deleteClicks'),
    ],
    [State('comment-demo-input', 'value'), State('comment-demo', 'children')],
    prevent_initial_call=True,
)
def comment_demo_add_children_callback(nClicks, deleteClicks, value, children):
    # 本次回调由子回复删除功能触发
    if 'deleteClicks' in dash.callback_context.triggered[0]['prop_id']:
        triggerIndex = eval(
            dash.callback_context.triggered[0]['prop_id'].replace(
                '.deleteClicks', ''
            )
        )['index']

        return [
            child
            for child in children
            if child['props']['id']['index'] != triggerIndex
        ], dash.no_update

    if value:
        return children + [
            fac.AntdComment(
                id={
                    'type': 'comment-demo-children',
                    'index': str(uuid.uuid4()),
                },
                authorName='dash学习者',
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss',
                },
                commentContent=value,
                showReply=False,
                showDelete=True,
            )
        ] if children else [
            fac.AntdComment(
                id={
                    'type': 'comment-demo-children',
                    'index': str(uuid.uuid4()),
                },
                authorName='dash学习者',
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss',
                },
                commentContent=value,
                showReply=False,
                showDelete=True,
            )
        ], None

    else:
        return children, None
"""
    }
]
