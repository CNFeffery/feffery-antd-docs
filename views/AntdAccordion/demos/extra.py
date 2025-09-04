import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        # 构造演示用例相关内容
        demo_contents = fac.AntdAccordion(
            items=[
                {
                    "title": f"手风琴项示例{i}",
                    "key": i,
                    "children": fac.AntdText(f"手风琴项示例{i}"),
                    "extra": fac.AntdButton("额外内容", type="link", size="small"),
                }
                for i in range(1, 6)
            ],
            collapsible="header",
        )

    elif current_locale == "en-us":
        # construct demo contents
        demo_contents = fac.AntdAccordion(
            items=[
                {
                    "title": f"Accordion item example {i}",
                    "key": i,
                    "children": fac.AntdText(f"Accordion item example {i}"),
                    "extra": fac.AntdButton("Extra content", type="link", size="small"),
                }
                for i in range(1, 6)
            ],
            collapsible="header",
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdAccordion(
    items=[
        {
            'title': f'手风琴项示例{i}',
            'key': i,
            'children': fac.AntdText(f'手风琴项示例{i}'),
            'extra': fac.AntdButton('额外内容', type='link', size='small'),
        }
        for i in range(1, 6)
    ],
    collapsible='header',
)
"""
            }
        ]

    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdAccordion(
    items=[
        {
            'title': f'Accordion item example {i}',
            'key': i,
            'children': fac.AntdText(f'Accordion item example {i}'),
            'extra': fac.AntdButton('Extra content', type='link', size='small'),
        }
        for i in range(1, 6)
    ],
    collapsible='header',
)
"""
            }
        ]
