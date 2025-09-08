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
                fac.AntdSelect(
                    id="select-options-share-1-demo",
                    placeholder="选择选项后查看其他下拉选择框的options",
                    options=[{"label": f"选项{i}", "value": i} for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    id="select-options-share-2-demo",
                    placeholder="选择选项后查看其他下拉选择框的options",
                    options=[{"label": f"选项{i}", "value": i} for i in range(1, 6)],
                    style={"width": "100%"},
                ),
                fac.AntdSelect(
                    id="select-options-share-3-demo",
                    placeholder="选择选项后查看其他下拉选择框的options",
                    options=[{"label": f"选项{i}", "value": i} for i in range(1, 6)],
                    mode="multiple",
                    style={"width": "100%"},
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSelect(
                    id="select-options-share-1-demo",
                    placeholder="After selecting, check options of the other selects",
                    options=[{"label": f"Option {i}", "value": i} for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    id="select-options-share-2-demo",
                    placeholder="After selecting, check options of the other selects",
                    options=[{"label": f"Option {i}", "value": i} for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    id="select-options-share-3-demo",
                    placeholder="After selecting, check options of the other selects",
                    options=[{"label": f"Option {i}", "value": i} for i in range(1, 6)],
                    mode="multiple",
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
        Output("select-options-share-1-demo", "options"),
        Output("select-options-share-2-demo", "options"),
        Output("select-options-share-3-demo", "options"),
    ],
    [
        Input("select-options-share-1-demo", "value"),
        Input("select-options-share-2-demo", "value"),
        Input("select-options-share-3-demo", "value"),
    ],
)
def share_options(value1, value2, value3):
    if not value3:
        value3 = []
    options_1 = [
        {
            "label": f"选项{i}",
            "value": i,
            "disabled": True if i in [value2] + value3 else False,
        }
        for i in range(1, 6)
    ]
    options_2 = [
        {
            "label": f"选项{i}",
            "value": i,
            "disabled": True if i in [value1] + value3 else False,
        }
        for i in range(1, 6)
    ]
    options_3 = [
        {
            "label": f"选项{i}",
            "value": i,
            "disabled": True if i in [value2, value1] else False,
        }
        for i in range(1, 6)
    ]
    return options_1, options_2, options_3


def code_string() -> list:
    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        return [
            {
                "code": """fac.AntdSpace(
    [
        fac.AntdSelect(
            id='select-options-share-1-demo',
            placeholder='选择选项后查看其他下拉选择框的options',
            options=[
                {'label': f'选项{i}', 'value': i} for i in range(1, 6)
            ],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            id='select-options-share-2-demo',
            placeholder='选择选项后查看其他下拉选择框的options',
            options=[
                {'label': f'选项{i}', 'value': i} for i in range(1, 6)
            ],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            id='select-options-share-3-demo',
            placeholder='选择选项后查看其他下拉选择框的options',
            options=[
                {'label': f'选项{i}', 'value': i} for i in range(1, 6)
            ],
            mode='multiple',
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)

    
@app.callback(
    [
        Output('select-options-share-1-demo', 'options'),
        Output('select-options-share-2-demo', 'options'),
        Output('select-options-share-3-demo', 'options'),
    ],
    [
        Input('select-options-share-1-demo', 'value'),
        Input('select-options-share-2-demo', 'value'),
        Input('select-options-share-3-demo', 'value'),
    ],
)
def share_options(value1, value2, value3):
    # 避免value3 is None的情况
    if not value3:
        value3 = []
    options_1 = [
        {
            'label': f'选项{i}',
            'value': i,
            'disabled': True if i in [value2] + value3 else False,
        }
        for i in range(1, 6)
    ]
    options_2 = [
        {
            'label': f'选项{i}',
            'value': i,
            'disabled': True if i in [value1] + value3 else False,
        }
        for i in range(1, 6)
    ]
    options_3 = [
        {
            'label': f'选项{i}',
            'value': i,
            'disabled': True if i in [value2, value1] else False,
        }
        for i in range(1, 6)
    ]
    return options_1, options_2, options_3"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """fac.AntdSpace(
            [
                fac.AntdSelect(
                    id="select-options-share-1-demo",
                    placeholder="After selecting, check options of the other selects",
                    options=[{"label": f"Option {i}", "value": i} for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    id="select-options-share-2-demo",
                    placeholder="After selecting, check options of the other selects",
                    options=[{"label": f"Option {i}", "value": i} for i in range(1, 6)],
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdSelect(
                    id="select-options-share-3-demo",
                    placeholder="After selecting, check options of the other selects",
                    options=[{"label": f"Option {i}", "value": i} for i in range(1, 6)],
                    mode="multiple",
                    style={"width": "100%"},
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )
        
        @app.callback(
    [
        Output("select-options-share-1-demo", "options"),
        Output("select-options-share-2-demo", "options"),
        Output("select-options-share-3-demo", "options"),
    ],
    [
        Input("select-options-share-1-demo", "value"),
        Input("select-options-share-2-demo", "value"),
        Input("select-options-share-3-demo", "value"),
    ],
)
def share_options(value1, value2, value3):
    if not value3:
        value3 = []
    options_1 = [
        {
            "label": f"选项{i}",
            "value": i,
            "disabled": True if i in [value2] + value3 else False,
        }
        for i in range(1, 6)
    ]
    options_2 = [
        {
            "label": f"选项{i}",
            "value": i,
            "disabled": True if i in [value1] + value3 else False,
        }
        for i in range(1, 6)
    ]
    options_3 = [
        {
            "label": f"选项{i}",
            "value": i,
            "disabled": True if i in [value2, value1] else False,
        }
        for i in range(1, 6)
    ]
    return options_1, options_2, options_3"""
            }
        ]
