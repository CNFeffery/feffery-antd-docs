import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

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
                        fac.AntdText("options_type："),
                        fac.AntdRadioGroup(
                            id="select-short-options-type-demo",
                            options=["list of string", "list of number"],
                            value="list of string",
                            optionType="button",
                            buttonStyle="solid",
                        ),
                    ]
                ),
                fac.AntdSelect(
                    id="select-short-options-demo",
                    options=[i for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdCard(
                    id="select-short-options-output-demo",
                    styles={"header": {"display": "none"}},
                ),
            ],
            direction="vertical",
            style={"width": 350, "gap": 5},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSpace(
                    [
                        fac.AntdText("options_type:"),
                        fac.AntdRadioGroup(
                            id="select-short-options-type-demo",
                            options=["list of string", "list of number"],
                            value="list of string",
                            optionType="button",
                            buttonStyle="solid",
                        ),
                    ]
                ),
                fac.AntdSelect(
                    id="select-short-options-demo",
                    options=[i for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdCard(
                    id="select-short-options-output-demo",
                    styles={"header": {"display": "none"}},
                ),
            ],
            direction="vertical",
            style={"width": 350, "gap": 5},
        )

    return demo_contents


@app.callback(
    [
        Output("select-short-options-demo", "options"),
        Output("select-short-options-demo", "value"),
    ],
    Input("select-short-options-type-demo", "value"),
)
def select_short_options_type_demo_callback(value):
    if value == "list of string":
        return [f"{i}" for i in range(1, 6)], "1"
    elif value == "list of number":
        return [i for i in range(1, 6)], 1


@app.callback(
    Output("select-short-options-output-demo", "children"),
    [
        Input("select-short-options-demo", "value"),
        State("select-short-options-demo", "options"),
    ],
)
def select_short_options_demo_callback(value, options):
    return fac.AntdSpace(
        [
            fac.AntdParagraph(f"options：{options}", style={"margin": 0}),
            fac.AntdParagraph(f"value：{value}", style={"margin": 0}),
            fac.AntdParagraph(f"value_type：{type(value)}", style={"margin": 0}),
        ],
        direction="vertical",
    )


def code_string() -> list:
    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        return [
            {
                "code": """fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdText('options_type：'),
                fac.AntdRadioGroup(
                    id='select-short-options-type-demo',
                    options=[
                        'list of string',
                        'list of number',
                    ],
                    value='list of string',
                    optionType='button',
                    buttonStyle='solid',
                ),
            ]
        ),
        fac.AntdSelect(
            id='select-short-options-demo',
            options=[i for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdCard(
            id='select-short-options-output-demo',
            styles={'header': {'display': 'none'}},
        ),
    ],
    direction='vertical',
    style={'width': 350, 'gap': 5},
)


# radioGroup回调设置select的options
@app.callback(
    [
        Output('select-short-options-demo', 'options'),
        Output('select-short-options-demo', 'value'),
    ],
    Input('select-short-options-type-demo', 'value'),
)
def select_short_options_type_demo_callback(value):
    if value == 'list of string':
        return [f'{i}' for i in range(1, 6)], '1'
    elif value == 'list of number':
        return [i for i in range(1, 6)], 1


# 回调数据展示
@app.callback(
    Output('select-short-options-output-demo', 'children'),
    [
        Input('select-short-options-demo', 'value'),
        State('select-short-options-demo', 'options'),
    ],
)
def select_short_options_demo_callback(value, options):
    return fac.AntdSpace(
        [
            fac.AntdParagraph(f'options：{options}', style={'margin': 0}),
            fac.AntdParagraph(f'value：{value}', style={'margin': 0}),
            fac.AntdParagraph(
                f'value_type：{type(value)}', style={'margin': 0}
            ),
        ],
        direction='vertical',
    )"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """fac.AntdSpace(
                    [
                        fac.AntdText("options_type:"),
                        fac.AntdRadioGroup(
                            id="select-short-options-type-demo",
                            options=["list of string", "list of number"],
                            value="list of string",
                            optionType="button",
                            buttonStyle="solid",
                        ),
                    ]
                ),
                fac.AntdSelect(
                    id="select-short-options-demo",
                    options=[i for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdCard(
                    id="select-short-options-output-demo",
                    styles={"header": {"display": "none"}},
                ),
            ],
            direction="vertical",
            style={"width": 350, "gap": 5},
        )

        # radioGroup回调设置select的options
@app.callback(
    [
        Output('select-short-options-demo', 'options'),
        Output('select-short-options-demo', 'value'),
    ],
    Input('select-short-options-type-demo', 'value'),
)
def select_short_options_type_demo_callback(value):
    if value == 'list of string':
        return [f'{i}' for i in range(1, 6)], '1'
    elif value == 'list of number':
        return [i for i in range(1, 6)], 1


# 回调数据展示
@app.callback(
    Output('select-short-options-output-demo', 'children'),
    [
        Input('select-short-options-demo', 'value'),
        State('select-short-options-demo', 'options'),
    ],
)
def select_short_options_demo_callback(value, options):
    return fac.AntdSpace(
        [
            fac.AntdParagraph(f'options：{options}', style={'margin': 0}),
            fac.AntdParagraph(f'value：{value}', style={'margin': 0}),
            fac.AntdParagraph(
                f'value_type：{type(value)}', style={'margin': 0}
            ),
        ],
        direction='vertical',
    )
        """
            }
        ]
