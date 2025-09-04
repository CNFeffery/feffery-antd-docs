import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        fruits = [
            {"label": "香蕉", "value": "banana"},
            {"label": "苹果", "value": "apple"},
            {"label": "西瓜", "value": "watermelon"},
            {"label": "草莓", "value": "strawberry"},
            {"label": "葡萄", "value": "grape"},
        ]
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider('尝试搜索"香蕉"', innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="search label",
                    optionFilterProp="label",
                    options=fruits,
                    style={"width": "100%"},
                ),
                fac.AntdDivider('尝试搜索"banana"', innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="search value",
                    optionFilterProp="value",
                    options=fruits,
                    style={"width": "100%"},
                ),
                fac.AntdDivider(
                    '针对组件型label，只可搜索"value"', innerTextOrientation="left"
                ),
                fac.AntdText("针对组件型label，只可搜索value"),
                fac.AntdSelect(
                    placeholder="search value in component label options",
                    optionFilterProp="value",
                    options=[
                        {"label": fac.AntdText("香蕉", strong=True), "value": "banana"},
                        {"label": fac.AntdText("苹果", strong=True), "value": "apple"},
                        {
                            "label": fac.AntdText("西瓜", strong=True),
                            "value": "watermelon",
                        },
                        {
                            "label": fac.AntdText("草莓", strong=True),
                            "value": "strawberry",
                        },
                        {"label": fac.AntdText("葡萄", strong=True), "value": "grape"},
                    ],
                    style={"width": "100%"},
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    elif current_locale == "en-us":
        fruits_en = [
            {"label": "Banana", "value": "banana"},
            {"label": "Apple", "value": "apple"},
            {"label": "Watermelon", "value": "watermelon"},
            {"label": "Strawberry", "value": "strawberry"},
            {"label": "Grape", "value": "grape"},
        ]
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider('Try searching "banana"', innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="Search label",
                    optionFilterProp="label",
                    options=fruits_en,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider('Try searching "banana"', innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="Search value",
                    optionFilterProp="value",
                    options=fruits_en,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    'For component labels, only "value" is searchable',
                    innerTextOrientation="left",
                ),
                fac.AntdText("For component labels, only value is searchable"),
                fac.AntdSelect(
                    placeholder="Search value in component label options",
                    optionFilterProp="value",
                    options=[
                        {
                            "label": fac.AntdText("Banana", strong=True),
                            "value": "banana",
                        },
                        {"label": fac.AntdText("Apple", strong=True), "value": "apple"},
                        {
                            "label": fac.AntdText("Watermelon", strong=True),
                            "value": "watermelon",
                        },
                        {
                            "label": fac.AntdText("Strawberry", strong=True),
                            "value": "strawberry",
                        },
                        {"label": fac.AntdText("Grape", strong=True), "value": "grape"},
                    ],
                    style={"width": "100%"},
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    return demo_contents


def code_string() -> list:
    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
            [
                fac.AntdDivider('尝试搜索"香蕉"', innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="search label",
                    optionFilterProp="label",
                    options=fruits,
                    style={"width": "100%"},
                ),
                fac.AntdDivider('尝试搜索"banana"', innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="search value",
                    optionFilterProp="value",
                    options=fruits,
                    style={"width": "100%"},
                ),
                fac.AntdDivider(
                    '针对组件型label，只可搜索"value"', innerTextOrientation="left"
                ),
                fac.AntdText("针对组件型label，只可搜索value"),
                fac.AntdSelect(
                    placeholder="search value in component label options",
                    optionFilterProp="value",
                    options=[
                        {"label": fac.AntdText("香蕉", strong=True), "value": "banana"},
                        {"label": fac.AntdText("苹果", strong=True), "value": "apple"},
                        {
                            "label": fac.AntdText("西瓜", strong=True),
                            "value": "watermelon",
                        },
                        {
                            "label": fac.AntdText("草莓", strong=True),
                            "value": "strawberry",
                        },
                        {"label": fac.AntdText("葡萄", strong=True), "value": "grape"},
                    ],
                    style={"width": "100%"},
                ),
            ],
            direction="vertical",
            style={"width": 350},
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
                fac.AntdDivider('Try searching "banana"', innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="Search label",
                    optionFilterProp="label",
                    options=fruits_en,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider('Try searching "banana"', innerTextOrientation="left"),
                fac.AntdSelect(
                    placeholder="Search value",
                    optionFilterProp="value",
                    options=fruits_en,
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    'For component labels, only "value" is searchable',
                    innerTextOrientation="left",
                ),
                fac.AntdText("For component labels, only value is searchable"),
                fac.AntdSelect(
                    placeholder="Search value in component label options",
                    optionFilterProp="value",
                    options=[
                        {
                            "label": fac.AntdText("Banana", strong=True),
                            "value": "banana",
                        },
                        {"label": fac.AntdText("Apple", strong=True), "value": "apple"},
                        {
                            "label": fac.AntdText("Watermelon", strong=True),
                            "value": "watermelon",
                        },
                        {
                            "label": fac.AntdText("Strawberry", strong=True),
                            "value": "strawberry",
                        },
                        {"label": fac.AntdText("Grape", strong=True), "value": "grape"},
                    ],
                    style={"width": "100%"},
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )
"""
            }
        ]
