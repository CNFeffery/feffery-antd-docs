import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSpace(
                    [
                        fac.AntdText("当前debounceWait(单位：ms)："),
                        fac.AntdInputNumber(
                            id="select-debounce-wait-demo",
                            value=500,
                            min=0,
                            precision=0,
                        ),
                    ],
                    style={"justify-content": "space-between", "width": "100%"},
                ),
                fac.AntdSelect(
                    id="select-debounce-demo",
                    placeholder="请搜索内容",
                    placement="topLeft",
                    options=[f"选项{i}" for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdCard(
                    [
                        html.Div(id="select-not-debounce-demo-output"),
                        html.Div(id="select-debounce-demo-output"),
                    ],
                    styles={
                        "header": {"display": "none"},
                        "body": {"flexDirection": "column"},
                    },
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSpace(
                    [
                        fac.AntdText("Current debounceWait (ms):"),
                        fac.AntdInputNumber(
                            id="select-debounce-wait-demo",
                            value=500,
                            min=0,
                            precision=0,
                        ),
                    ],
                    style={"justify-content": "space-between", "width": "100%"},
                ),
                fac.AntdSelect(
                    id="select-debounce-demo",
                    placeholder="Please search",
                    placement="topLeft",
                    options=[f"Option {i}" for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdCard(
                    [
                        html.Div(id="select-not-debounce-demo-output"),
                        html.Div(id="select-debounce-demo-output"),
                    ],
                    styles={
                        "header": {"display": "none"},
                        "body": {"flexDirection": "column"},
                    },
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    return demo_contents


# 通过AntdInputNumber回调设定select的debounceWait数值
@app.callback(
    Output("select-debounce-demo", "debounceWait"),
    Input("select-debounce-wait-demo", "value"),
)
def set_debounce_wait(value):
    return value


@app.callback(
    Output("select-not-debounce-demo-output", "children"),
    Input("select-debounce-demo", "searchValue"),
)
def select_demo(searchValue):
    return f"searchValue: {searchValue}"


@app.callback(
    Output("select-debounce-demo-output", "children"),
    Input("select-debounce-demo", "debounceSearchValue"),
)
def select_debounce_demo(debounceSearchValue):
    return f"debounceSearchValue: {debounceSearchValue}"


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdText('当前debounceWait(单位：ms)：'),
                fac.AntdInputNumber(
                    id='select-debounce-wait-demo',
                    value=500,
                    min=0,
                    precision=0,
                ),
            ],
            style={
                'justify-content': 'space-between',
                'width': '100%',
            },
        ),
        fac.AntdSelect(
            id='select-debounce-demo',
            placeholder='请搜索内容',
            placement='topLeft',
            options=[f'选项{i}' for i in range(1, 6)],
            style={
                'width': '100%',
            },
        ),
        fac.AntdCard(
            [
                html.Div(id='select-not-debounce-demo-output'),
                html.Div(id='select-debounce-demo-output'),
            ],
            styles={
                'header': {'display': 'none'},
                'body': {'flexDirection': 'column'},
            },
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
...
@app.callback(
    Output('select-debounce-demo', 'debounceWait'),
    Input('select-debounce-wait-demo', 'value'),
)
def set_debounce_wait(value):
    return value
...
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdText('Current debounceWait (ms):'),
                fac.AntdInputNumber(
                    id='select-debounce-wait-demo',
                    value=500,
                    min=0,
                    precision=0,
                ),
            ],
            style={
                'justify-content': 'space-between',
                'width': '100%',
            },
        ),
        fac.AntdSelect(
            id='select-debounce-demo',
            placeholder='Please search',
            placement='topLeft',
            options=[f'Option {i}' for i in range(1, 6)],
            style={
                'width': '100%',
            },
            locale="en-us",
        ),
        fac.AntdCard(
            [
                html.Div(id='select-not-debounce-demo-output'),
                html.Div(id='select-debounce-demo-output'),
            ],
            styles={
                'header': {'display': 'none'},
                'body': {'flexDirection': 'column'},
            },
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
...
@app.callback(
    Output('select-debounce-demo', 'debounceWait'),
    Input('select-debounce-wait-demo', 'value'),
)
def set_debounce_wait(value):
    return value
...
"""
            }
        ]
