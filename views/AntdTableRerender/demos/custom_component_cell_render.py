import feffery_antd_components as fac
import feffery_markdown_components as fmc
import feffery_utils_components as fuc
from dash import html
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        # 中文演示
        demo_contents = fac.AntdTable(
            columns=[{"title": "自定义元素示例", "dataIndex": "自定义元素示例"}],
            data=[
                {
                    "自定义元素示例": html.Div(
                        fac.AntdText("示例内容" * 100, style={"textIndent": "2rem"}),
                        style={
                            "maxHeight": 50,
                            "overflowY": "auto",
                            "textAlign": "left",
                        },
                    )
                },
                {
                    "自定义元素示例": fmc.FefferyMarkdown(
                        markdownStr="""
```python
import numpy as np
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
```
"""
                    )
                },
                {"自定义元素示例": fuc.FefferyQRCode(value="FefferyQRCode示例")},
            ],
            bordered=True,
            style={"width": "100%"},
        )

    elif current_locale == "en-us":
        # English demo
        demo_contents = fac.AntdTable(
            locale="en-us",
            columns=[
                {
                    "title": "Custom Component Example",
                    "dataIndex": "Custom Component Example",
                }
            ],
            data=[
                {
                    "Custom Component Example": html.Div(
                        fac.AntdText(
                            "Example content" * 100, style={"textIndent": "2rem"}
                        ),
                        style={
                            "maxHeight": 50,
                            "overflowY": "auto",
                            "textAlign": "left",
                        },
                    )
                },
                {
                    "Custom Component Example": fmc.FefferyMarkdown(
                        markdownStr="""
```python
import numpy as np
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
```
"""
                    )
                },
                {
                    "Custom Component Example": fuc.FefferyQRCode(
                        value="FefferyQRCode example"
                    )
                },
            ],
            bordered=True,
            style={"width": "100%"},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": '''
fac.AntdTable(
    columns=[{'title': '自定义元素示例', 'dataIndex': '自定义元素示例'}],
    data=[
        {
            '自定义元素示例': html.Div(
                fac.AntdText(
                    '示例内容' * 100, style={'textIndent': '2rem'}
                ),
                style={
                    'maxHeight': 50,
                    'overflowY': 'auto',
                    'textAlign': 'left',
                },
            )
        },
        {
            '自定义元素示例': fmc.FefferyMarkdown(
                markdownStr="""
```python
import numpy as np
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
```
"""
            )
        },
        {'自定义元素示例': fuc.FefferyQRCode(value='FefferyQRCode示例')},
    ],
    bordered=True,
    style={'width': '100%'},
)
'''
            }
        ]

    elif current_locale == "en-us":
        return [
            {
                "code": '''
fac.AntdTable(
    locale='en-us',
    columns=[{'title': 'Custom Component Example', 'dataIndex': 'Custom Component Example'}],
    data=[
        {
            'Custom Component Example': html.Div(
                fac.AntdText(
                    'Example content' * 100, style={'textIndent': '2rem'}
                ),
                style={
                    'maxHeight': 50,
                    'overflowY': 'auto',
                    'textAlign': 'left',
                },
            )
        },
        {
            'Custom Component Example': fmc.FefferyMarkdown(
                markdownStr="""
```python
import numpy as np
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
```
"""
            )
        },
        {'Custom Component Example': fuc.FefferyQRCode(value='FefferyQRCode example')},
    ],
    bordered=True,
    style={'width': '100%'},
)
'''
            }
        ]
