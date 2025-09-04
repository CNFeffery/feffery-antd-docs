import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        demo_contents = [
            fac.AntdSelect(
                id="select-basic-callbacks-demo",
                options=[f"选项{i}" for i in range(1, 6)],
                style={"width": 350},
            ),
            fac.AntdParagraph(id="select-basic-callbacks-output"),
        ]
    elif current_locale == "en-us":
        demo_contents = [
            fac.AntdSelect(
                id="select-basic-callbacks-demo",
                options=[f"Option {i}" for i in range(1, 6)],
                style={"width": 350},
                locale="en-us",
            ),
            fac.AntdParagraph(id="select-basic-callbacks-output"),
        ]
    return demo_contents


@app.callback(
    Output("select-basic-callbacks-output", "children"),
    Input("select-basic-callbacks-demo", "value"),
)
def _show_value(value):
    return f"value: {value}"


def code_string() -> list:
    """返回当前语种对应的演示代码"""
    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        return [
            {
                "code": """
[
    fac.AntdSelect(
        id='select-basic-callbacks-demo',
        options=[f'选项{i}' for i in range(1, 6)],
        style={'width': 350},
    ),
    fac.AntdParagraph(id='select-basic-callbacks-output'),
]
...
@app.callback(
    Output('select-basic-callbacks-output', 'children'),
    Input('select-basic-callbacks-demo', 'value'),
)
def _show_value(value):
    return f'value: {value}'
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
[
    fac.AntdSelect(
        id='select-basic-callbacks-demo',
        options=[f'Option {i}' for i in range(1, 6)],
        style={'width': 350},
        locale="en-us",
    ),
    fac.AntdParagraph(id='select-basic-callbacks-output'),
]
...
@app.callback(
    Output('select-basic-callbacks-output', 'children'),
    Input('select-basic-callbacks-demo', 'value'),
)
def _show_value(value):
    return f'value: {value}'
"""
            }
        ]
