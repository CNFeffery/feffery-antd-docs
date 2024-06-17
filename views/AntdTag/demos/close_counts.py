import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                '尝试点击标签内的关闭按钮', innerTextOrientation='left'
            ),
            fac.AntdTag(
                content='标签', closeIcon=True, id='tag-close-counts-demo'
            ),
            fac.AntdCard(
                '当前未点击标签关闭按钮',
                id='tag-close-counts-output-demo',
                headStyle={'display': 'none'},
            ),
        ],
        direction='vertical',
        style={
            'width': '100%',
        },
    )

    return demo_contents


@app.callback(
    Output('tag-close-counts-output-demo', 'children'),
    Input('tag-close-counts-demo', 'closeCounts'),
    prevent_initial_call=True,
)
def close_counts_callback(closeCounts):
    return f'当前标签关闭按钮点击次数为：{closeCounts}次'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider(
            '尝试点击标签内的关闭按钮', innerTextOrientation='left'
        ),
        fac.AntdTag(
            content='标签', closeIcon=True, id='tag-close-counts-demo'
        ),
        fac.AntdCard(
            '当前未点击标签关闭按钮',
            id='tag-close-counts-output-demo',
            headStyle={'display': 'none'},
        ),
        
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)


@app.callback(
    Output('tag-close-counts-output-demo', 'children'),
    Input('tag-close-counts-demo', 'closeCounts'),
    prevent_initial_call=True,
)
def close_counts_callback(closeCounts):
    return f'当前标签关闭按钮点击次数为：{closeCounts}次'
"""
    }
]
