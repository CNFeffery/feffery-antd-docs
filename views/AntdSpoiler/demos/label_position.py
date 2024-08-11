import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdFlex(
        [
            fac.AntdSegmented(
                id='spolier-label-position-options',
                options=[
                    {'label': 'left', 'value': 'left'},
                    {'label': 'right', 'value': 'right'},
                ],
                defaultValue='left',
            ),
            fac.AntdSpoiler(
                fac.AntdParagraph('内容示例' * 100),
                id='spolier-label-position-demo',
                maxHeight=70,
            ),
        ],
        gap='small',
        align='flex-start',
        vertical=True,
    )

    return demo_contents


@app.callback(
    Output('spolier-label-position-demo', 'labelPosition'),
    Input('spolier-label-position-options', 'value'),
)
def update_spoiler_label_position(value):
    return value


code_string = [
    {
        'code': """
fac.AntdFlex(
    [
        fac.AntdSegmented(
            id='spolier-label-position-options',
            options=[
                {'label': 'left', 'value': 'left'},
                {'label': 'right', 'value': 'right'},
            ],
            defaultValue='left',
        ),
        fac.AntdSpoiler(
            fac.AntdParagraph('内容示例' * 100),
            id='spolier-label-position-demo',
            maxHeight=70,
        ),
    ],
    gap='small',
    align='flex-start',
    vertical=True,
)

...

@app.callback(
    Output('spolier-label-position-demo', 'labelPosition'),
    Input('spolier-label-position-options', 'value'),
)
def update_spoiler_label_position(value):
    return value
"""
    }
]
