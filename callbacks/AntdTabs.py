import json
import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app


app.clientside_callback(
    '''(value) => value''',
    Output('tabs-gutter-demo', 'tabBarGutter'),
    Input('tabs-gutter-demo-slider', 'value')
)

app.clientside_callback(
    '''(inkBarAnimated, tabPaneAnimated) => [inkBarAnimated, tabPaneAnimated]''',
    [Output('tabs-animation-demo', 'inkBarAnimated'),
     Output('tabs-animation-demo', 'tabPaneAnimated')],
    [Input('tabs-animation-demo-inkBarAnimated', 'checked'),
     Input('tabs-animation-demo-tabPaneAnimated', 'checked')]
)


@app.callback(
    Output('tabs-demo-output', 'children'),
    Input('tabs-demo', 'activeKey')
)
def tabs_demo(activeKey):

    return f'activeKey: {activeKey}'


@app.callback(
    [Output('tabs-add-delete-demo', 'items'),
     Output('tabs-add-delete-demo', 'activeKey')],
    [Input('tabs-add-delete-demo-add', 'nClicks'),
     Input('tabs-add-delete-demo', 'latestDeletePane')],
    [State('tabs-add-delete-demo', 'items'),
     State('tabs-add-delete-demo', 'activeKey')]
)
def tabs_add_delete_demo(nClicks,
                         latestDeletePane,
                         origin_items,
                         activeKey):

    if dash.ctx.triggered_id == 'tabs-add-delete-demo-add':

        # 提取已有items中的最大key值
        origin_max_key = max([int(item['key']) for item in origin_items])

        return [
            [
                *origin_items,
                {
                    'label': f'标签页{origin_max_key+1}',
                    'key': str(origin_max_key+1),
                    'children': html.Div(
                        f'标签页{origin_max_key+1}',
                        style={
                            'height': 200,
                            'fontSize': 28,
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    )
                }
            ],
            str(origin_max_key+1)
        ]

    elif dash.ctx.triggered_id == 'tabs-add-delete-demo':

        return [
            [
                item
                for item in origin_items
                if item['key'] != latestDeletePane
            ],
            '1' if latestDeletePane == activeKey else dash.no_update
        ]

    return dash.no_update


@app.callback(
    Output('tabs-add-delete-demo-tab-count', 'children'),
    Input('tabs-add-delete-demo', 'tabCount'),
    State('tabs-add-delete-demo', 'tabCloseCounts'),
    prevent_initial_call=True
)
def tabs_add_delete_demo_tab_count(tabCount, tabCloseCounts):

    return fac.AntdMessage(
        content=f'标签页自由增删示例 tabCount: {tabCount}，标签页关闭次数：{tabCloseCounts}',
        type='info'
    )


@app.callback(
    Output('tabs-context-menu-demo-output', 'children'),
    Input('tabs-context-menu-demo', 'clickedContextMenu')
)
def tabs_context_menu_demo(clickedContextMenu):

    return json.dumps(
        dict(
            clickedContextMenu=clickedContextMenu
        ),
        indent=4,
        ensure_ascii=False
    )
