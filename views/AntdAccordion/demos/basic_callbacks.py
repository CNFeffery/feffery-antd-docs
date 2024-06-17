import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdAccordion(
            id='accordion-demo',
            items=[
                {
                    'title': f'手风琴项示例{i}',
                    'key': i,
                    'children': fac.AntdText(f'手风琴项示例{i}'),
                }
                for i in range(1, 6)
            ],
            defaultActiveKey=['2'],
        ),
        fac.AntdParagraph(id='accordion-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('accordion-demo-output', 'children'),
    Input('accordion-demo', 'activeKey'),
)
def accordion_demo(activeKey):
    return f'activeKey: {activeKey}'


code_string = [
    {
        'code': """
[
    fac.AntdAccordion(
        id='accordion-demo',
        items=[
            {
                'title': f'手风琴项示例{i}',
                'key': i,
                'children': fac.AntdText(f'手风琴项示例{i}'),
            }
            for i in range(1, 6)
        ],
        defaultActiveKey=['2'],
    ),
    fac.AntdParagraph(id='accordion-demo-output'),
]

...

@app.callback(
    Output('accordion-demo-output', 'children'),
    Input('accordion-demo', 'activeKey'),
)
def accordion_demo(activeKey):
    return f'activeKey: {activeKey}'
"""
    }
]
