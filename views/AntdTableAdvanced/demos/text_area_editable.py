import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        col_title = "文本域编辑示例"
        data_key = "文本域编辑示例"
        sample_value = "内容示例"
    else:  # en-us fallback
        col_title = "Text Area Edit Example"
        data_key = "Text Area Edit Example"
        sample_value = "Content Example"

    demo_contents = fac.AntdTable(
        columns=[
            {
                "title": col_title,
                "dataIndex": data_key,
                "editable": True,
                "editOptions": {
                    "mode": "text-area",  # text-area edit mode
                    "autoSize": {"minRows": 1, "maxRows": 3},
                },
            }
        ],
        data=[{data_key: sample_value}] * 3,
        bordered=True,
        style={"width": 200},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdTable(
    columns=[
        {
            'title': '文本域编辑示例',
            'dataIndex': '文本域编辑示例',
            'editable': True,
            'editOptions': {
                'mode': 'text-area',  # 开启文本域编辑模式
                'autoSize': {'minRows': 1, 'maxRows': 3},
            },
        }
    ],
    data=[{'文本域编辑示例': '内容示例'}] * 3,
    bordered=True,
    style={'width': 200},
)
"""
            }
        ]
    else:  # en-us
        return [
            {
                "code": """
fac.AntdTable(
    columns=[
        {
            'title': 'Text Area Edit Example',
            'dataIndex': 'Text Area Edit Example',
            'editable': True,
            'editOptions': {
                'mode': 'text-area',  # enable text-area edit mode
                'autoSize': {'minRows': 1, 'maxRows': 3},
            },
        }
    ],
    data=[{'Text Area Edit Example': 'Content Example'}] * 3,
    bordered=True,
    style={'width': 200},
)
"""
            }
        ]
