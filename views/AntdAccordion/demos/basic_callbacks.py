import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = [
            fac.AntdAccordion(
                id="accordion-demo",
                items=[
                    {
                        "title": f"手风琴项示例{i}",
                        "key": i,
                        "children": fac.AntdText(f"手风琴项示例{i}"),
                    }
                    for i in range(1, 6)
                ],
                defaultActiveKey=["2"],
            ),
            fac.AntdParagraph(id="accordion-demo-output"),
        ]

    elif current_locale == "en-us":
        demo_contents = [
            fac.AntdAccordion(
                id="accordion-demo",
                items=[
                    {
                        "title": f"Accordion item example {i}",
                        "key": i,
                        "children": fac.AntdText(f"Accordion item example {i}"),
                    }
                    for i in range(1, 6)
                ],
                defaultActiveKey=["2"],
            ),
            fac.AntdParagraph(id="accordion-demo-output"),
        ]

    return demo_contents


@app.callback(
    Output("accordion-demo-output", "children"),
    Input("accordion-demo", "activeKey"),
)
def accordion_demo(activeKey):
    # localize output prefix if desired (kept consistent with original)
    prefix = "activeKey"
    return f"{prefix}: {activeKey}"


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
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
    elif current_locale == "en-us":
        return [
            {
                "code": """
[
    fac.AntdAccordion(
        id='accordion-demo',
        items=[
            {
                'title': f'Accordion item example {i}',
                'key': i,
                'children': fac.AntdText(f'Accordion item example {i}'),
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
