import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdCheckCardGroup(
            [fac.AntdCheckCard(f'选项{i}', value=i) for i in range(1, 6)],
            id='check-card-group-demo',
            size='small',
            multiple=True,
            defaultValue=[1, 2],
        ),
        fac.AntdParagraph(id='check-card-group-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('check-card-group-demo-output', 'children'),
    Input('check-card-group-demo', 'value'),
)
def check_card_group_demo(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
[
    fac.AntdCheckCardGroup(
        [fac.AntdCheckCard(f'选项{i}', value=i) for i in range(1, 6)],
        id='check-card-group-demo',
        size='small',
        multiple=True,
        defaultValue=[1, 2],
    ),
    fac.AntdParagraph(id='check-card-group-demo-output'),
]

...

@app.callback(
    Output('check-card-group-demo-output', 'children'),
    Input('check-card-group-demo', 'value'),
)
def check_card_group_demo(value):
    return f'value: {value}'
"""
    }
]
