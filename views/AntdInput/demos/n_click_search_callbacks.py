import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                id='input-search-demo',
                placeholder='按下搜索按钮',
                mode='search',
            ),
            fac.AntdCard(
                id='input-search-demo-output', headStyle={'display': 'none'}
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


@app.callback(
    Output('input-search-demo-output', 'children'),
    Input('input-search-demo', 'nClicksSearch'),
)
def input_search_dmeo(nClicksSearch):
    return f'nClicksSearch: {nClicksSearch}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(
            id='input-search-demo',
            placeholder='按下搜索按钮',
            mode='search',
        ),
        fac.AntdCard(
            id='input-search-demo-output', headStyle={'display': 'none'}
        ),
    ],
    direction='vertical',
    style={'width': 350},
)


@app.callback(
    Output('input-search-demo-output', 'children'),
    Input('input-search-demo', 'nClicksSearch'),
)
def input_search_dmeo(nClicksSearch):
    return f'nClicksSearch: {nClicksSearch}'
"""
    }
]
