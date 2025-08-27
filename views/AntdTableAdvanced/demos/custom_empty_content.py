import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        title = lambda i: f"字段{i}"
        data_key = lambda i: f"字段{i}"
        empty_desc = fac.AntdText("没有数据哦~", type="secondary")
    elif current_locale == "en-us":
        title = lambda i: f"Field {i}"
        data_key = lambda i: f"Field {i}"
        empty_desc = fac.AntdText("No data ~", type="secondary")
    else:
        title = lambda i: f"字段{i}"
        data_key = lambda i: f"字段{i}"
        empty_desc = fac.AntdText("没有数据哦~", type="secondary")

    demo_contents = fac.AntdTable(
        columns=[
            {"title": title(i), "dataIndex": data_key(i), "width": "20%"}
            for i in range(1, 6)
        ],
        emptyContent=fac.AntdEmpty(
            image="/assets/imgs/components/AntdEmpty/自定义占位图.png",
            description=empty_desc,
            styles={"image": {"height": 150}},
        ),
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdTable(
    columns=[
        {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
        for i in range(1, 6)
    ],
    emptyContent=fac.AntdEmpty(
        image='/assets/imgs/components/AntdEmpty/自定义占位图.png',
        description=fac.AntdText('没有数据哦~', type='secondary'),
        styles={'image': {'height': 150}},
    ),
)
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdTable(
    columns=[
        {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': '20%'}
        for i in range(1, 6)
    ],
    emptyContent=fac.AntdEmpty(
        image='/assets/imgs/components/AntdEmpty/自定义占位图.png',
        description=fac.AntdText('No data ~', type='secondary'),
        styles={'image': {'height': 150}},
    ),
)
"""
            }
        ]
