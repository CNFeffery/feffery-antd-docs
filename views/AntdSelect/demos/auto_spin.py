import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app
import time


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
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
            fac.AntdDivider('自定义loading内容', innerTextOrientation='left'),
            fac.AntdSelect(
                id='select-auto-spin-remote-load-custom-empty-options',
                placeholder='请输入要搜索的内容',
                options=[],
                autoSpin=True,
                debounceWait=200,
                # 使用loadingEmptyContent自定义loading内容
                loadingEmptyContent=fac.AntdCenter(
                    fac.AntdIcon(icon='antd-loading')
                ),
                style={'width': '100%'},
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


code_string = [
    {
        'code': """
fac.AntdSpace(
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
        fac.AntdDivider('自定义loading内容', innerTextOrientation='left'),
        fac.AntdSelect(
            id='select-auto-spin-remote-load-custom-empty-options',
            placeholder='请输入要搜索的内容',
            options=[],
            autoSpin=True,
            debounceWait=200,
            # 使用loadingEmptyContent自定义loading内容
            loadingEmptyContent=fac.AntdCenter(
                fac.AntdIcon(icon='antd-loading')
            ),
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)


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
"""
    }
]
