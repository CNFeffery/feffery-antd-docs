import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例"""
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider("maxTagCount=5（默认）", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[f"选项{i}" for i in range(1, 26)],
                    mode="multiple",
                    value=[f"选项{i}" for i in range(1, 8)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    options=[f"选项{i}" for i in range(1, 26)],
                    mode="tags",
                    value=[
                        "选项1",
                        "选项2",
                        "选项3",
                        "选项4",
                        "自由设置的较长选项",
                        "选项5",
                        "选项6",
                    ],
                    style={"width": "100%"},
                ),
                fac.AntdDivider("maxTagCount=3", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[f"选项{i}" for i in range(1, 26)],
                    mode="multiple",
                    maxTagCount=3,
                    value=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    options=[f"选项{i}" for i in range(1, 26)],
                    mode="tags",
                    maxTagCount=3,
                    value=["选项1", "选项2", "自由设置的较长选项", "选项5", "选项6"],
                    style={"width": "100%"},
                ),
                fac.AntdDivider(
                    'maxTagCount="responsive"', innerTextOrientation="left"
                ),
                fac.AntdText("选择框宽度："),
                fac.AntdRadioGroup(
                    id="select-width-radio-group-demo",
                    options=[f"{i}00px" for i in range(1, 5)],
                    defaultValue="300px",
                    optionType="button",
                    buttonStyle="solid",
                ),
                fac.AntdSelect(
                    options=[f"{i}" for i in range(1, 26)],
                    id="select-multiple-responsive-demo",
                    mode="multiple",
                    value=[f"{i}" for i in range(1, 11)],
                    maxTagCount="responsive",
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    options=[f"{i}" for i in range(1, 26)],
                    id="select-tags-responsive-demo",
                    mode="tags",
                    value=["自由设置的较长选项"] + [f"{i}" for i in range(1, 11)],
                    maxTagCount="responsive",
                    style={"width": "100%"},
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider("maxTagCount=5 (default)", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[f"Option {i}" for i in range(1, 26)],
                    mode="multiple",
                    value=[f"Option {i}" for i in range(1, 8)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    options=[f"Option {i}" for i in range(1, 26)],
                    mode="tags",
                    value=[
                        "Option 1",
                        "Option 2",
                        "Option 3",
                        "Option 4",
                        "A longer custom option",
                        "Option 5",
                        "Option 6",
                    ],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider("maxTagCount=3", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[f"Option {i}" for i in range(1, 26)],
                    mode="multiple",
                    maxTagCount=3,
                    value=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    options=[f"Option {i}" for i in range(1, 26)],
                    mode="tags",
                    maxTagCount=3,
                    value=[
                        "Option 1",
                        "Option 2",
                        "A longer custom option",
                        "Option 5",
                        "Option 6",
                    ],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    'maxTagCount="responsive"', innerTextOrientation="left"
                ),
                fac.AntdText("Select width:"),
                fac.AntdRadioGroup(
                    id="select-width-radio-group-demo",
                    options=[f"{i}00px" for i in range(1, 5)],
                    defaultValue="300px",
                    optionType="button",
                    buttonStyle="solid",
                ),
                fac.AntdSelect(
                    options=[f"{i}" for i in range(1, 26)],
                    id="select-multiple-responsive-demo",
                    mode="multiple",
                    value=[f"{i}" for i in range(1, 11)],
                    maxTagCount="responsive",
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    options=[f"{i}" for i in range(1, 26)],
                    id="select-tags-responsive-demo",
                    mode="tags",
                    value=["A longer custom option"] + [f"{i}" for i in range(1, 11)],
                    maxTagCount="responsive",
                    style={"width": "100%"},
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    return demo_contents


@app.callback(
    [
        Output("select-multiple-responsive-demo", "style"),
        Output("select-tags-responsive-demo", "style"),
    ],
    Input("select-width-radio-group-demo", "value"),
    prevent_initial_call=True,
)
def select_width_radio_group_callback(value):
    return {"width": value}, {"width": value}


def code_string() -> list:
    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
            [
                fac.AntdDivider("maxTagCount=5（默认）", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[f"选项{i}" for i in range(1, 26)],
                    mode="multiple",
                    value=[f"选项{i}" for i in range(1, 8)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    options=[f"选项{i}" for i in range(1, 26)],
                    mode="tags",
                    value=[
                        "选项1",
                        "选项2",
                        "选项3",
                        "选项4",
                        "自由设置的较长选项",
                        "选项5",
                        "选项6",
                    ],
                    style={"width": "100%"},
                ),
                fac.AntdDivider("maxTagCount=3", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[f"选项{i}" for i in range(1, 26)],
                    mode="multiple",
                    maxTagCount=3,
                    value=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    options=[f"选项{i}" for i in range(1, 26)],
                    mode="tags",
                    maxTagCount=3,
                    value=["选项1", "选项2", "自由设置的较长选项", "选项5", "选项6"],
                    style={"width": "100%"},
                ),
                fac.AntdDivider(
                    'maxTagCount="responsive"', innerTextOrientation="left"
                ),
                fac.AntdText("选择框宽度："),
                fac.AntdRadioGroup(
                    id="select-width-radio-group-demo",
                    options=[f"{i}00px" for i in range(1, 5)],
                    defaultValue="300px",
                    optionType="button",
                    buttonStyle="solid",
                ),
                fac.AntdSelect(
                    options=[f"{i}" for i in range(1, 26)],
                    id="select-multiple-responsive-demo",
                    mode="multiple",
                    value=[f"{i}" for i in range(1, 11)],
                    maxTagCount="responsive",
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    options=[f"{i}" for i in range(1, 26)],
                    id="select-tags-responsive-demo",
                    mode="tags",
                    value=["自由设置的较长选项"] + [f"{i}" for i in range(1, 11)],
                    maxTagCount="responsive",
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
                fac.AntdDivider("maxTagCount=5 (default)", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[f"Option {i}" for i in range(1, 26)],
                    mode="multiple",
                    value=[f"Option {i}" for i in range(1, 8)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    options=[f"Option {i}" for i in range(1, 26)],
                    mode="tags",
                    value=[
                        "Option 1",
                        "Option 2",
                        "Option 3",
                        "Option 4",
                        "A longer custom option",
                        "Option 5",
                        "Option 6",
                    ],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider("maxTagCount=3", innerTextOrientation="left"),
                fac.AntdSelect(
                    options=[f"Option {i}" for i in range(1, 26)],
                    mode="multiple",
                    maxTagCount=3,
                    value=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    options=[f"Option {i}" for i in range(1, 26)],
                    mode="tags",
                    maxTagCount=3,
                    value=[
                        "Option 1",
                        "Option 2",
                        "A longer custom option",
                        "Option 5",
                        "Option 6",
                    ],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider(
                    'maxTagCount="responsive"', innerTextOrientation="left"
                ),
                fac.AntdText("Select width:"),
                fac.AntdRadioGroup(
                    id="select-width-radio-group-demo",
                    options=[f"{i}00px" for i in range(1, 5)],
                    defaultValue="300px",
                    optionType="button",
                    buttonStyle="solid",
                ),
                fac.AntdSelect(
                    options=[f"{i}" for i in range(1, 26)],
                    id="select-multiple-responsive-demo",
                    mode="multiple",
                    value=[f"{i}" for i in range(1, 11)],
                    maxTagCount="responsive",
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    options=[f"{i}" for i in range(1, 26)],
                    id="select-tags-responsive-demo",
                    mode="tags",
                    value=["A longer custom option"] + [f"{i}" for i in range(1, 11)],
                    maxTagCount="responsive",
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
