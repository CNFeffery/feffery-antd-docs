import dash
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTabs(
            id='tabs-add-delete-demo',
            type='editable-card',
            items=[
                {
                    'label': f'标签页{i}',
                    'key': str(i),
                    'children': fac.AntdCenter(
                        f'标签页{i}',
                        style={
                            'height': 200,
                            'fontSize': 28,
                        },
                    ),
                    'closable': not (i == 1),
                }
                for i in range(1, 6)
            ],
            tabBarRightExtraContent=fac.AntdIcon(
                id='tabs-add-delete-demo-add',
                icon='antd-plus-circle-two-tone',
                style={'fontSize': 20, 'cursor': 'pointer'},
            ),
        ),
        fac.Fragment(id='tabs-add-delete-demo-tab-count'),
    ]

    return demo_contents


@app.callback(
    [
        Output('tabs-add-delete-demo', 'items'),
        Output('tabs-add-delete-demo', 'activeKey'),
    ],
    [
        Input('tabs-add-delete-demo-add', 'nClicks'),
        Input('tabs-add-delete-demo', 'latestDeletePane'),
    ],
    [
        State('tabs-add-delete-demo', 'items'),
        State('tabs-add-delete-demo', 'activeKey'),
    ],
)
def tabs_add_delete_demo(nClicks, latestDeletePane, origin_items, activeKey):
    if dash.ctx.triggered_id == 'tabs-add-delete-demo-add':
        # 提取已有items中的最大key值
        origin_max_key = max([int(item['key']) for item in origin_items])

        return [
            [
                *origin_items,
                {
                    'label': f'标签页{origin_max_key+1}',
                    'key': str(origin_max_key + 1),
                    'children': fac.AntdCenter(
                        f'标签页{origin_max_key+1}',
                        style={
                            'height': 200,
                            'fontSize': 28,
                        },
                    ),
                },
            ],
            str(origin_max_key + 1),
        ]

    elif dash.ctx.triggered_id == 'tabs-add-delete-demo':
        return [
            [item for item in origin_items if item['key'] != latestDeletePane],
            '1' if latestDeletePane == activeKey else dash.no_update,
        ]

    return dash.no_update


@app.callback(
    Output('tabs-add-delete-demo-tab-count', 'children'),
    Input('tabs-add-delete-demo', 'tabCount'),
    State('tabs-add-delete-demo', 'tabCloseCounts'),
    prevent_initial_call=True,
)
def tabs_add_delete_demo_tab_count(tabCount, tabCloseCounts):
    return fac.AntdMessage(
        content=f'标签页自由增删示例 tabCount: {tabCount}，标签页关闭次数：{tabCloseCounts}',
        type='info',
    )


code_string = [
    {
        'code': """
[
    fac.AntdTabs(
        id='tabs-add-delete-demo',
        type='editable-card',
        items=[
            {
                'label': f'标签页{i}',
                'key': str(i),
                'children': fac.AntdCenter(
                    f'标签页{i}',
                    style={
                        'height': 200,
                        'fontSize': 28,
                    },
                ),
                'closable': not (i == 1),
            }
            for i in range(1, 6)
        ],
        tabBarRightExtraContent=fac.AntdIcon(
            id='tabs-add-delete-demo-add',
            icon='antd-plus-circle-two-tone',
            style={'fontSize': 20, 'cursor': 'pointer'},
        ),
    ),
    fac.Fragment(id='tabs-add-delete-demo-tab-count'),
]

...

@app.callback(
    [
        Output('tabs-add-delete-demo', 'items'),
        Output('tabs-add-delete-demo', 'activeKey'),
    ],
    [
        Input('tabs-add-delete-demo-add', 'nClicks'),
        Input('tabs-add-delete-demo', 'latestDeletePane'),
    ],
    [
        State('tabs-add-delete-demo', 'items'),
        State('tabs-add-delete-demo', 'activeKey'),
    ],
)
def tabs_add_delete_demo(nClicks, latestDeletePane, origin_items, activeKey):
    if dash.ctx.triggered_id == 'tabs-add-delete-demo-add':
        # 提取已有items中的最大key值
        origin_max_key = max([int(item['key']) for item in origin_items])

        return [
            [
                *origin_items,
                {
                    'label': f'标签页{origin_max_key+1}',
                    'key': str(origin_max_key + 1),
                    'children': fac.AntdCenter(
                        f'标签页{origin_max_key+1}',
                        style={
                            'height': 200,
                            'fontSize': 28,
                        },
                    ),
                },
            ],
            str(origin_max_key + 1),
        ]

    elif dash.ctx.triggered_id == 'tabs-add-delete-demo':
        return [
            [item for item in origin_items if item['key'] != latestDeletePane],
            '1' if latestDeletePane == activeKey else dash.no_update,
        ]

    return dash.no_update


@app.callback(
    Output('tabs-add-delete-demo-tab-count', 'children'),
    Input('tabs-add-delete-demo', 'tabCount'),
    State('tabs-add-delete-demo', 'tabCloseCounts'),
    prevent_initial_call=True,
)
def tabs_add_delete_demo_tab_count(tabCount, tabCloseCounts):
    return fac.AntdMessage(
        content=f'标签页自由增删示例 tabCount: {tabCount}，标签页关闭次数：{tabCloseCounts}',
        type='info',
    )
"""
    }
]
