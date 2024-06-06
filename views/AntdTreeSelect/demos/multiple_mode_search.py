import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdRadioGroup(
                id='tree-select-multiple-mode-search-demo-switch-mode',
                options=[
                    {'label': mode, 'value': mode}
                    for mode in ['case-insensitive', 'case-sensitive', 'regex']
                ],
                defaultValue='case-insensitive',
                optionType='button',
            ),
            fac.AntdTreeSelect(
                id='tree-select-multiple-mode-search-demo',
                treeData=[
                    {
                        'key': f'节点{i}',
                        'title': f'节点{i}',
                        'value': f'节点{i}',
                        'children': [
                            {
                                'key': f'节点{i}-{j}',
                                'title': f'节点{i}-{j}',
                                'value': f'节点{i}-{j}',
                            }
                            for j in range(1, 4)
                        ],
                    }
                    for i in list('AbCdEf')
                ],
                style={'width': 300},
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('tree-select-multiple-mode-search-demo', 'treeNodeFilterMode'),
    Input('tree-select-multiple-mode-search-demo-switch-mode', 'value'),
)
def tree_select_multiple_mode_search_demo(value):
    return value


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdRadioGroup(
            id='tree-select-multiple-mode-search-demo-switch-mode',
            options=[
                {'label': mode, 'value': mode}
                for mode in ['case-insensitive', 'case-sensitive', 'regex']
            ],
            defaultValue='case-insensitive',
            optionType='button',
        ),
        fac.AntdTreeSelect(
            id='tree-select-multiple-mode-search-demo',
            treeData=[
                {
                    'key': f'节点{i}',
                    'title': f'节点{i}',
                    'value': f'节点{i}',
                    'children': [
                        {
                            'key': f'节点{i}-{j}',
                            'title': f'节点{i}-{j}',
                            'value': f'节点{i}-{j}',
                        }
                        for j in range(1, 4)
                    ],
                }
                for i in list('AbCdEf')
            ],
            style={'width': 300},
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('tree-select-multiple-mode-search-demo', 'treeNodeFilterMode'),
    Input('tree-select-multiple-mode-search-demo-switch-mode', 'value'),
)
def tree_select_multiple_mode_search_demo(value):
    return value
"""
    }
]
