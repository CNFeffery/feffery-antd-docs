import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State
from server import app
import dash


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('基础示例', innerTextOrientation='left'),
            fac.AntdSelect(
                options=[f'选项{i}' for i in range(1, 6)],
                dropdownBefore=fac.AntdInput(placeholder='输入关键字搜索'),
                dropdownAfter=fac.AntdButton(
                    type='primary', children='新增选项'
                ),
                style={'width': '100%'},
            ),
            fac.AntdDivider('添加选项示例', innerTextOrientation='left'),
            fac.AntdSelect(
                id='select-add-option-demo',
                options=[f'选项{i}' for i in range(1, 6)],
                dropdownAfter=fac.AntdInput(
                    id='select-add-option-input-demo',
                    placeholder='输入新增选项',
                    suffix=fac.AntdButton(
                        id='select-add-option-button-demo',
                        icon=fac.AntdIcon(icon='antd-plus'),
                        type='primary',
                    ),
                ),
                style={'width': '100%'},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


# 新增选项回调
@app.callback(
    [
        Output('select-add-option-demo', 'options'),
        Output('select-add-option-input-demo', 'value'),
    ],
    Input('select-add-option-button-demo', 'nClicks'),
    [
        State('select-add-option-input-demo', 'value'),
        State('select-add-option-demo', 'options'),
    ],
    prevent_initial_call=True,
)
def add_option(nClicks, value, options):
    if nClicks and value:
        # 需注意，options写法如果是简写，应向列表追加 string|number 类型，非简写则应按options格式追加dict
        options.append(value)
        return options, None
    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('基础示例', innerTextOrientation='left'),
        fac.AntdSelect(
            options=[f'选项{i}' for i in range(1, 6)],
            dropdownBefore=fac.AntdInput(placeholder='输入关键字搜索'),
            dropdownAfter=fac.AntdButton(
                type='primary', children='新增选项'
            ),
            style={'width': '100%'},
        ),
        fac.AntdDivider('添加选项示例', innerTextOrientation='left'),
        fac.AntdSelect(
            id='select-add-option-demo',
            options=[f'选项{i}' for i in range(1, 6)],
            dropdownAfter=fac.AntdInput(
                id='select-add-option-input-demo',
                placeholder='输入新增选项',
                suffix=fac.AntdButton(
                    id='select-add-option-button-demo',
                    icon=fac.AntdIcon(icon='antd-plus'),
                    type='primary',
                ),
            ),
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)


# 新增选项回调
@app.callback(
    [
        Output('select-add-option-demo', 'options'),
        Output('select-add-option-input-demo', 'value'),
    ],
    Input('select-add-option-button-demo', 'nClicks'),
    [
        State('select-add-option-input-demo', 'value'),
        State('select-add-option-demo', 'options'),
    ],
    prevent_initial_call=True,
)
def add_option(nClicks, value, options):
    if nClicks and value:
        # 需注意，options写法如果是简写，应向列表追加 string|number 类型，非简写则应按options格式追加dict
        options.append(value)
        return options, None
    return dash.no_update
"""
    }
]
