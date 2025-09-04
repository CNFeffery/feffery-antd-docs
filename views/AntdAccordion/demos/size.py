import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdAccordion(
                    items=[
                        {
                            "title": f"{size}手风琴项示例{i}",
                            "key": i,
                            "children": fac.AntdText(f"{size}手风琴项示例{i}"),
                        }
                        for i in range(1, 3)
                    ],
                    size=size,
                )
                for size in ["small", "middle", "large"]
            ],
            direction="vertical",
            style={"width": "100%"},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdAccordion(
                    items=[
                        {
                            "title": f"{size} accordion item example {i}",
                            "key": i,
                            "children": fac.AntdText(
                                f"{size} accordion item example {i}"
                            ),
                        }
                        for i in range(1, 3)
                    ],
                    size=size,
                )
                for size in ["small", "middle", "large"]
            ],
            direction="vertical",
            style={"width": "100%"},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdAccordion(
            items=[
                {
                    'title': f'{size}手风琴项示例{i}',
                    'key': i,
                    'children': fac.AntdText(f'{size}手风琴项示例{i}'),
                }
                for i in range(1, 3)
            ],
            size=size,
        )
        for size in ['small', 'middle', 'large']
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdAccordion(
            items=[
                {
                    'title': f'{size} accordion item example {i}',
                    'key': i,
                    'children': fac.AntdText(f'{size} accordion item example {i}'),
                }
                for i in range(1, 3)
            ],
            size=size,
        )
        for size in ['small', 'middle', 'large']
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
