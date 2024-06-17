import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, ALL
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('单标签回调', innerTextOrientation='left'),
            fac.AntdCheckableTag(
                content='单标签', id='checkable-tag-single-demo'
            ),
            fac.AntdCard(
                id='checkable-tag-single-demo-output',
                headStyle={'display': 'none'},
            ),
            fac.AntdDivider('多标签回调', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    fac.AntdCheckableTag(
                        id={'type': 'checkable-tag-demo', 'index': i},
                        content=f'标签{i}',
                    )
                    for i in range(1, 6)
                ]
            ),
            fac.AntdCard(
                id='checkable-tag-output-demo', headStyle={'display': 'none'}
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


# 单标签回调
@app.callback(
    Output('checkable-tag-single-demo-output', 'children'),
    Input('checkable-tag-single-demo', 'checked'),
)
def checkable_tag_single_demo(checked):
    return f'checked: {checked}'


# 多标签回调
@app.callback(
    Output('checkable-tag-output-demo', 'children'),
    Input({'type': 'checkable-tag-demo', 'index': ALL}, 'checked'),
)
def checkable_tag_demo(checked_list):
    return f'checked_list: {checked_list}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('单标签回调', innerTextOrientation='left'),
        fac.AntdCheckableTag(
            content='单标签', id='checkable-tag-single-demo'
        ),
        fac.AntdCard(
            id='checkable-tag-single-demo-output',
            headStyle={'display': 'none'},
        ),
        fac.AntdDivider('多标签回调', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                fac.AntdCheckableTag(
                    id={'type': 'checkable-tag-demo', 'index': i},
                    content=f'标签{i}',
                )
                for i in range(1, 6)
            ]
        ),
        fac.AntdCard(
            id='checkable-tag-output-demo', headStyle={'display': 'none'}
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)


# 单标签回调
@app.callback(
    Output('checkable-tag-single-demo-output', 'children'),
    Input('checkable-tag-single-demo', 'checked'),
)
def checkable_tag_single_demo(checked):
    return f'checked: {checked}'


# 多标签回调
@app.callback(
    Output('checkable-tag-output-demo', 'children'),
    Input({'type': 'checkable-tag-demo', 'index': ALL}, 'checked'),
)
def checkable_tag_demo(checked_list):
    return f'checked_list: {checked_list}'
"""
    }
]
