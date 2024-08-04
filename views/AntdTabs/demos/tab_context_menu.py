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
            fac.AntdTabs(
                id='tabs-context-menu-demo',
                items=[
                    {
                        'label': f'标签页{i}',
                        'key': f'标签页{i}',
                        'contextMenu': [
                            {'key': f'菜单项{j}', 'label': f'菜单项{j}'}
                            for j in range(1, 6)
                        ],
                    }
                    for i in range(1, 6)
                ],
                size='large',
            ),
            html.Pre(id='tabs-context-menu-demo-output'),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('tabs-context-menu-demo-output', 'children'),
    Input('tabs-context-menu-demo', 'clickedContextMenu'),
)
def tabs_context_menu_demo(clickedContextMenu):
    return json.dumps(
        dict(clickedContextMenu=clickedContextMenu),
        indent=4,
        ensure_ascii=False,
    )


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdTabs(
            id='tabs-context-menu-demo',
            items=[
                {
                    'label': f'标签页{i}',
                    'key': f'标签页{i}',
                    'contextMenu': [
                        {'key': f'菜单项{j}', 'label': f'菜单项{j}'}
                        for j in range(1, 6)
                    ],
                }
                for i in range(1, 6)
            ],
            size='large',
        ),
        html.Pre(id='tabs-context-menu-demo-output'),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('tabs-context-menu-demo-output', 'children'),
    Input('tabs-context-menu-demo', 'clickedContextMenu'),
)
def tabs_context_menu_demo(clickedContextMenu):
    return json.dumps(
        dict(clickedContextMenu=clickedContextMenu),
        indent=4,
        ensure_ascii=False,
    )
"""
    }
]
