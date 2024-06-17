import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output, State, ALL
from server import app
from dash import html
import dash


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            # 使用FefferyAutoAnimate代替html.Div，为其子元素自动添加增删动画
            fuc.FefferyAutoAnimate(
                [
                    fac.AntdTag(
                        content='不可关闭标签',
                        # 调整样式使得内部的关闭按钮居中，字体大小与其他组件统一
                        style={
                            'font-size': 14,
                            'display': 'flex',
                            'align-items': 'center',
                        },
                    ),
                    fac.AntdTag(
                        content='可关闭标签1',
                        closeIcon=True,
                        id={
                            'type': 'tag-close-counts-closeable-demo',
                            'index': 1,
                        },
                        style={
                            'font-size': 14,
                            'display': 'flex',
                            'align-items': 'center',
                        },
                    ),
                    fac.AntdTag(
                        content='可关闭标签2',
                        closeIcon=True,
                        id={
                            'type': 'tag-close-counts-closeable-demo',
                            'index': 2,
                        },
                        style={
                            'font-size': 14,
                            'display': 'flex',
                            'align-items': 'center',
                        },
                    ),
                    html.Div(
                        [
                            # 设置尺寸使得AntdButton的样式大小接近AntdTag
                            fac.AntdButton(
                                '新增标签',
                                icon=fac.AntdIcon(icon='antd-plus'),
                                type='dashed',
                                size='small',
                                id='tag-close-counts-add-btn-demo',
                            ),
                            html.Div(
                                id='tag-close-counts-input-container-demo'
                            ),
                        ]
                    ),
                ],
                id='tag-close-counts-closeable-demo-container',
                style={
                    'display': 'flex',
                    'flex-wrap': 'wrap',
                    'gap': 5,
                },
            ),
        ],
        direction='vertical',
        style={
            'width': '100%',
        },
    )

    return demo_contents


# 添加标签按钮点击后，渲染输入框，并隐藏新增按钮
@app.callback(
    [
        Output('tag-close-counts-input-container-demo', 'children'),
        Output('tag-close-counts-add-btn-demo', 'style'),
    ],
    Input('tag-close-counts-add-btn-demo', 'nClicks'),
    prevent_initial_call=True,
)
def add_tag_callback(nClicks):
    return fac.AntdInput(
        id='tag-close-counts-input-demo',
        autoFocus=True,
        size='small',
        style={'width': 94},
    ), {'display': 'none'}


# 输入框失焦或submit后，删除输入框，并显示新增按钮
@app.callback(
    [
        Output(
            'tag-close-counts-input-container-demo',
            'children',
            allow_duplicate=True,
        ),
        Output('tag-close-counts-add-btn-demo', 'style', allow_duplicate=True),
    ],
    [
        Input('tag-close-counts-input-demo', 'focusing'),
        Input('tag-close-counts-input-demo', 'nSubmit'),
    ],
    prevent_initial_call=True,
)
def switch_show_add_btn_callback(focusing, nSubmit):
    if not focusing or nSubmit:
        return [], {}
    return dash.no_update


# 输入框失焦后或submit后，新增标签
@app.callback(
    Output('tag-close-counts-closeable-demo-container', 'children'),
    [
        Input('tag-close-counts-input-demo', 'focusing'),
        Input('tag-close-counts-input-demo', 'nSubmit'),
    ],
    [
        State('tag-close-counts-input-demo', 'value'),
        State('tag-close-counts-closeable-demo-container', 'children'),
    ],
    prevent_initial_call=True,
)
def add_tag_add_btn_callback(focusing, nSubmit, value, children):
    if not value:
        return dash.no_update
    if not focusing or nSubmit:
        # 替换children末位元素，从AntdButton、AntdInput的容器替换为新增的标签
        children[-1] = fac.AntdTag(
            content=value,
            closeIcon=True,
            id={
                'type': 'tag-close-counts-closeable-demo',
                'index': max(
                    [
                        i['props']['id']['index']
                        for i in children
                        if 'id' in i['props']
                    ]  # 不能使用len，删除前置后新增容易重复导致无法删除
                )
                + 1,
            },
            style={
                'font-size': 14,
                'display': 'flex',
                'align-items': 'center',
            },
        )
        # 将被替换的AntdButton、AntdInput的容器重新添加到末位，实现增删改才会触发的动画效果，同时避免一些显示bug
        children.append(
            html.Div(
                [
                    fac.AntdButton(
                        '新增标签',
                        icon=fac.AntdIcon(icon='antd-plus'),
                        type='dashed',
                        size='small',
                        id='tag-close-counts-add-btn-demo',
                        style={},
                    ),
                    html.Div(id='tag-close-counts-input-container-demo'),
                ]
            )
        )
        return children

    return dash.no_update


# 标签关闭按钮点击事件
@app.callback(
    Output(
        'tag-close-counts-closeable-demo-container',
        'children',
        allow_duplicate=True,
    ),
    Input(
        {
            'type': 'tag-close-counts-closeable-demo',
            'index': ALL,
        },
        'closeCounts',
    ),
    State('tag-close-counts-closeable-demo-container', 'children'),
    prevent_initial_call=True,
)
def close_counts_closeable_callback(closeCounts, children):
    for i in closeCounts:
        if i is not None:
            trigger_id = dash.ctx.triggered_id
            for i, child in enumerate(children.copy()):
                if (
                    'id' in child['props']
                    and trigger_id == child['props']['id']
                ):
                    children.pop(i)

    return children


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        # 使用FefferyAutoAnimate代替html.Div，为其子元素自动添加增删动画
        fuc.FefferyAutoAnimate(
            [
                fac.AntdTag(
                    content='不可关闭标签',
                    # 调整样式使得内部的关闭按钮居中，字体大小与其他组件统一
                    style={
                        'font-size': 14,
                        'display': 'flex',
                        'align-items': 'center',
                    },
                ),
                fac.AntdTag(
                    content='可关闭标签1',
                    closeIcon=True,
                    id={
                        'type': 'tag-close-counts-closeable-demo',
                        'index': 1,
                    },
                    style={
                        'font-size': 14,
                        'display': 'flex',
                        'align-items': 'center',
                    },
                ),
                fac.AntdTag(
                    content='可关闭标签2',
                    closeIcon=True,
                    id={
                        'type': 'tag-close-counts-closeable-demo',
                        'index': 2,
                    },
                    style={
                        'font-size': 14,
                        'display': 'flex',
                        'align-items': 'center',
                    },
                ),
                html.Div(
                    [
                        # 设置尺寸使得AntdButton的样式大小接近AntdTag
                        fac.AntdButton(
                            '新增标签',
                            icon=fac.AntdIcon(icon='antd-plus'),
                            type='dashed',
                            size='small',
                            id='tag-close-counts-add-btn-demo',
                        ),
                        html.Div(
                            id='tag-close-counts-input-container-demo'
                        ),
                    ]
                ),
            ],
            id='tag-close-counts-closeable-demo-container',
            style={
                'display': 'flex',
                'flex-wrap': 'wrap',
                'gap': 5,
            },
        ),
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)


# 添加标签按钮点击后，渲染输入框，并隐藏新增按钮
@app.callback(
    [
        Output('tag-close-counts-input-container-demo', 'children'),
        Output('tag-close-counts-add-btn-demo', 'style'),
    ],
    Input('tag-close-counts-add-btn-demo', 'nClicks'),
    prevent_initial_call=True,
)
def add_tag_callback(nClicks):
    return fac.AntdInput(
        id='tag-close-counts-input-demo',
        autoFocus=True,
        size='small',
        style={'width': 94},
    ), {'display': 'none'}


# 输入框失焦或submit后，删除输入框，并显示新增按钮
@app.callback(
    [
        Output(
            'tag-close-counts-input-container-demo',
            'children',
            allow_duplicate=True,
        ),
        Output('tag-close-counts-add-btn-demo', 'style', allow_duplicate=True),
    ],
    [
        Input('tag-close-counts-input-demo', 'focusing'),
        Input('tag-close-counts-input-demo', 'nSubmit'),
    ],
    prevent_initial_call=True,
)
def switch_show_add_btn_callback(focusing, nSubmit):
    if not focusing or nSubmit:
        return [], {}
    return dash.no_update


# 输入框失焦后或submit后，新增标签
@app.callback(
    Output('tag-close-counts-closeable-demo-container', 'children'),
    [
        Input('tag-close-counts-input-demo', 'focusing'),
        Input('tag-close-counts-input-demo', 'nSubmit'),
    ],
    [
        State('tag-close-counts-input-demo', 'value'),
        State('tag-close-counts-closeable-demo-container', 'children'),
    ],
    prevent_initial_call=True,
)
def add_tag_add_btn_callback(focusing, nSubmit, value, children):
    if not value:
        return dash.no_update
    if not focusing or nSubmit:
        # 替换children末位元素，从AntdButton、AntdInput的容器替换为新增的标签
        children[-1] = fac.AntdTag(
            content=value,
            closeIcon=True,
            id={
                'type': 'tag-close-counts-closeable-demo',
                'index': max(
                    [
                        i['props']['id']['index']
                        for i in children
                        if 'id' in i['props']
                    ]  # 不能使用len，删除前置后新增容易重复导致无法删除
                )
                + 1,
            },
            style={
                'font-size': 14,
                'display': 'flex',
                'align-items': 'center',
            },
        )
        # 将被替换的AntdButton、AntdInput的容器重新添加到末位，实现增删改才会触发的动画效果，同时避免一些显示bug
        children.append(
            html.Div(
                [
                    fac.AntdButton(
                        '新增标签',
                        icon=fac.AntdIcon(icon='antd-plus'),
                        type='dashed',
                        size='small',
                        id='tag-close-counts-add-btn-demo',
                        style={},
                    ),
                    html.Div(id='tag-close-counts-input-container-demo'),
                ]
            )
        )
        return children

    return dash.no_update


# 标签关闭按钮点击事件
@app.callback(
    Output(
        'tag-close-counts-closeable-demo-container',
        'children',
        allow_duplicate=True,
    ),
    Input(
        {
            'type': 'tag-close-counts-closeable-demo',
            'index': ALL,
        },
        'closeCounts',
    ),
    State('tag-close-counts-closeable-demo-container', 'children'),
    prevent_initial_call=True,
)
def close_counts_closeable_callback(closeCounts, children):
    for i in closeCounts:
        if i is not None:
            trigger_id = dash.ctx.triggered_id
            for i, child in enumerate(children.copy()):
                if (
                    'id' in child['props']
                    and trigger_id == child['props']['id']
                ):
                    children.pop(i)
"""
    }
]
