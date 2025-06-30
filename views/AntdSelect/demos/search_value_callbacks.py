import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSelect(
                id='select-search-value-demo',
                placeholder='basic search',
                options=[f'选项{i}' for i in range(1, 6)],
                placement='topLeft',
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                id='select-search-value-multiple-demo',
                placeholder='multiple mode search',
                mode='multiple',
                options=[f'选项{i}' for i in range(1, 6)],
                placement='topLeft',
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                id='select-search-value-auto-clear-false-demo',
                placeholder='autoClearSearchValue=False',
                mode='multiple',
                autoClearSearchValue=False,
                options=[f'选项{i}' for i in range(1, 6)],
                placement='topLeft',
                style={'width': '100%'},
            ),
            fac.AntdCard(
                id='select-search-value-demo-output',
                styles={'header': {'display': 'none'}},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


@app.callback(
    Output('select-search-value-demo-output', 'children'),
    [
        Input('select-search-value-demo', 'searchValue'),
        Input('select-search-value-multiple-demo', 'searchValue'),
        Input('select-search-value-auto-clear-false-demo', 'searchValue'),
    ],
)
def select_search_value_demo(searchValue1, searchValue2, searchValue3):
    return fac.AntdSpace(
        [
            fac.AntdParagraph(
                f'searchValue：{searchValue1}', style={'margin': 0}
            ),
            fac.AntdParagraph(
                f'multiple searchValue：{searchValue2}', style={'margin': 0}
            ),
            fac.AntdParagraph(
                f'autoClearSearchValue=False：{searchValue3}',
                style={'margin': 0},
            ),
        ],
        direction='vertical',
        size=5,
    )


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSelect(
            id='select-search-value-demo',
            placeholder='basic search',
            options=[f'选项{i}' for i in range(1, 6)],
            placement='topLeft',
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            id='select-search-value-multiple-demo',
            placeholder='multiple mode search',
            mode='multiple',
            options=[f'选项{i}' for i in range(1, 6)],
            placement='topLeft',
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            id='select-search-value-auto-clear-false-demo',
            placeholder='autoClearSearchValue=False',
            mode='multiple',
            autoClearSearchValue=False,
            options=[f'选项{i}' for i in range(1, 6)],
            placement='topLeft',
            style={'width': '100%'},
        ),
        fac.AntdCard(
            id='select-search-value-demo-output',
            styles={'header': {'display': 'none'}},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)


@app.callback(
    Output('select-search-value-demo-output', 'children'),
    [
        Input('select-search-value-demo', 'searchValue'),
        Input('select-search-value-multiple-demo', 'searchValue'),
        Input('select-search-value-auto-clear-false-demo', 'searchValue'),
    ],
)
def select_search_value_demo(searchValue1, searchValue2, searchValue3):
    return fac.AntdSpace(
        [
            fac.AntdParagraph(
                f'searchValue：{searchValue1}', style={'margin': 0}
            ),
            fac.AntdParagraph(
                f'multiple searchValue：{searchValue2}', style={'margin': 0}
            ),
            fac.AntdParagraph(
                f'autoClearSearchValue=False：{searchValue3}',
                style={'margin': 0},
            ),
        ],
        direction='vertical',
        size=5,
    )
"""
    }
]
