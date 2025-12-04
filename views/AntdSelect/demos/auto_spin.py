import time

import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider('基础使用', innerTextOrientation='left'),
                fac.AntdSelect(
                    id='select-auto-spin-remote-load-options',
                    placeholder='请输入要搜索的内容',
                    options=[],
                    autoSpin=True,
                    debounceWait=200,
                    style={'width': '100%'},
                ),
                fac.AntdDivider(
                    '自定义loading内容', innerTextOrientation='left'
                ),
                fac.AntdSelect(
                    id='select-auto-spin-remote-load-custom-empty-options',
                    placeholder='请输入要搜索的内容',
                    options=[],
                    autoSpin=True,
                    debounceWait=200,
                    loadingEmptyContent=fac.AntdCenter(
                        fac.AntdIcon(icon='antd-loading')
                    ),
                    style={'width': '100%'},
                ),
            ],
            direction='vertical',
            style={'width': 350},
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider('Basic usage', innerTextOrientation='left'),
                fac.AntdSelect(
                    id='select-auto-spin-remote-load-options',
                    placeholder='Type to search',
                    options=[],
                    autoSpin=True,
                    debounceWait=200,
                    style={'width': '100%'},
                    locale='en-us',
                ),
                fac.AntdDivider(
                    'Custom loading content', innerTextOrientation='left'
                ),
                fac.AntdSelect(
                    id='select-auto-spin-remote-load-custom-empty-options',
                    placeholder='Type to search',
                    options=[],
                    autoSpin=True,
                    debounceWait=200,
                    loadingEmptyContent=fac.AntdCenter(
                        fac.AntdIcon(icon='antd-loading')
                    ),
                    style={'width': '100%'},
                    locale='en-us',
                ),
            ],
            direction='vertical',
            style={'width': 350},
        )

    return demo_contents


@app.callback(
    Output('select-auto-spin-remote-load-custom-empty-options', 'options'),
    Input(
        'select-auto-spin-remote-load-custom-empty-options',
        'debounceSearchValue',
    ),
)
def select_auto_spin_remote_load_options_demo(debounceSearchValue):
    if debounceSearchValue:
        time.sleep(1)
        return [
            {
                'label': f'{debounceSearchValue}模拟选项{i}',
                'value': f'{debounceSearchValue}模拟选项{i}',
            }
            for i in range(1, 6)
        ]
    return []


@app.callback(
    Output('select-auto-spin-remote-load-options', 'options'),
    Input('select-auto-spin-remote-load-options', 'debounceSearchValue'),
)
def select_auto_spin_remote_load_options_custom_content_demo(
    debounceSearchValue,
):
    if debounceSearchValue:
        time.sleep(1)
        return [
            {
                'label': f'{debounceSearchValue}模拟选项{i}',
                'value': f'{debounceSearchValue}模拟选项{i}',
            }
            for i in range(1, 6)
        ]
    return []


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()
    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdDivider("基础使用", innerTextOrientation="left"),
        fac.AntdSelect(
            id="select-auto-spin-remote-load-options",
            placeholder="请输入要搜索的内容",
            options=[],
            autoSpin=True,
            debounceWait=200,
            style={"width": "100%"},
        ),
        fac.AntdDivider("自定义loading内容", innerTextOrientation="left"),
        fac.AntdSelect(
            id="select-auto-spin-remote-load-custom-empty-options",
            placeholder="请输入要搜索的内容",
            options=[],
            autoSpin=True,
            debounceWait=200,
            loadingEmptyContent=fac.AntdCenter(
                fac.AntdIcon(icon="antd-loading")
            ),
            style={"width": "100%"},
        ),
    ],
    direction="vertical",
    style={"width": 350},
)

...

@app.callback(
    Output("select-auto-spin-remote-load-custom-empty-options", "options"),
    Input("select-auto-spin-remote-load-custom-empty-options", "debounceSearchValue"),
)
def select_auto_spin_remote_load_options_demo(debounceSearchValue):
    if debounceSearchValue:
        time.sleep(1)
        return [
            {
                "label": f"{debounceSearchValue}模拟选项{i}",
                "value": f"{debounceSearchValue}模拟选项{i}",
            }
            for i in range(1, 6)
        ]
    return []


@app.callback(
    Output("select-auto-spin-remote-load-options", "options"),
    Input("select-auto-spin-remote-load-options", "debounceSearchValue"),
)
def select_auto_spin_remote_load_options_custom_content_demo(debounceSearchValue):
    if debounceSearchValue:
        time.sleep(1)
        return [
            {
                "label": f"{debounceSearchValue}模拟选项{i}",
                "value": f"{debounceSearchValue}模拟选项{i}",
            }
            for i in range(1, 6)
        ]
    return []
"""
            }
        ]
    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdDivider("Basic usage", innerTextOrientation="left"),
        fac.AntdSelect(
            id="select-auto-spin-remote-load-options",
            placeholder="Type to search",
            options=[],
            autoSpin=True,
            debounceWait=200,
            style={"width": "100%"},
            locale="en-us",
        ),
        fac.AntdDivider("Custom loading content", innerTextOrientation="left"),
        fac.AntdSelect(
            id="select-auto-spin-remote-load-custom-empty-options",
            placeholder="Type to search",
            options=[],
            autoSpin=True,
            debounceWait=200,
            loadingEmptyContent=fac.AntdCenter(
                fac.AntdIcon(icon="antd-loading")
            ),
            style={"width": "100%"},
            locale="en-us",
        ),
    ],
    direction="vertical",
    style={"width": 350},
)

...

@app.callback(
    Output("select-auto-spin-remote-load-custom-empty-options", "options"),
    Input("select-auto-spin-remote-load-custom-empty-options", "debounceSearchValue"),
)
def select_auto_spin_remote_load_options_demo(debounceSearchValue):
    if debounceSearchValue:
        time.sleep(1)
        return [
            {
                "label": f"{debounceSearchValue}模拟选项{i}",
                "value": f"{debounceSearchValue}模拟选项{i}",
            }
            for i in range(1, 6)
        ]
    return []


@app.callback(
    Output("select-auto-spin-remote-load-options", "options"),
    Input("select-auto-spin-remote-load-options", "debounceSearchValue"),
)
def select_auto_spin_remote_load_options_custom_content_demo(debounceSearchValue):
    if debounceSearchValue:
        time.sleep(1)
        return [
            {
                "label": f"{debounceSearchValue}模拟选项{i}",
                "value": f"{debounceSearchValue}模拟选项{i}",
            }
            for i in range(1, 6)
        ]
    return []
"""
            }
        ]
