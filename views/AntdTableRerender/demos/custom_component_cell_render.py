from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
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

    return demo_contents


code_string = [
    {
        'code': '''
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
