import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdFormItem(
            fac.AntdRadioGroup(
                id='config-provider-component-size',
                options=[
                    {'label': size, 'value': size}
                    for size in ['small', 'middle', 'large']
                ],
                optionType='button',
                defaultValue='small',
            ),
            label='componentSize',
        ),
        fac.AntdDivider(isDashed=True),
        fac.AntdConfigProvider(
            fac.AntdSpace(
                [
                    fac.AntdButton('按钮测试'),
                    fac.AntdCascader(options=[], placeholder='级联选择测试'),
                    fac.AntdDatePicker(),
                    fac.AntdDateRangePicker(),
                    fac.AntdInput(
                        placeholder='输入框测试', style={'width': 256}
                    ),
                    fac.AntdInputNumber(
                        placeholder='数字输入框测试', style={'width': 256}
                    ),
                    fac.AntdRadioGroup(
                        options=[
                            {'label': f'选项{i}', 'value': f'选项{i}'}
                            for i in range(5)
                        ],
                        defaultValue='选项1',
                        optionType='button',
                    ),
                    fac.AntdSegmented(
                        options=[
                            {'label': f'选项{i}', 'value': f'选项{i}'}
                            for i in range(5)
                        ],
                        defaultValue='选项1',
                    ),
                    fac.AntdSegmentedColoring(
                        size='small',
                        min=-10,
                        max=10,
                        breakpoints=[0, 1, 2, 3, 4, 5],
                        colors=[
                            '#deecf9',
                            '#71afe5',
                            '#2b88d8',
                            '#0078d4',
                            '#106ebe',
                        ],
                    ),
                    fac.AntdSelect(
                        placeholder='请选择国家：',
                        options=[
                            {'label': '中国', 'value': '中国'},
                            {'label': '美国', 'value': '美国'},
                            {'label': '俄罗斯', 'value': '俄罗斯'},
                            {
                                'label': '德国',
                                'value': '德国',
                                'disabled': True,
                            },
                            {'label': '加拿大', 'value': '加拿大'},
                        ],
                        style={
                            # 使用css样式固定宽度
                            'width': '200px'
                        },
                    ),
                    fac.AntdTimePicker(),
                    fac.AntdTimeRangePicker(),
                    fac.AntdTreeSelect(
                        treeData=[
                            {
                                'key': '节点1',
                                'value': '1',
                                'title': '节点1',
                                'children': [
                                    {
                                        'key': f'节点1-{i}',
                                        'value': f'1-{i}',
                                        'title': f'节点1-{i}',
                                    }
                                    for i in range(1, 5)
                                ],
                            },
                            {'key': '节点2', 'value': '2', 'title': '节点2'},
                        ],
                        placeholder='请选择',
                        style={'width': 256},
                    ),
                ],
                direction='vertical',
                style={'width': '100%'},
            ),
            id='config-provider-component-size-demo',
            componentSize='small',
        ),
    ]

    return demo_contents


app.clientside_callback(
    '(value) => value',
    Output('config-provider-component-size-demo', 'componentSize'),
    Input('config-provider-component-size', 'value'),
)

code_string = [
    {
        'code': """
[
    fac.AntdFormItem(
        fac.AntdRadioGroup(
            id='config-provider-component-size',
            options=[
                {'label': size, 'value': size}
                for size in ['small', 'middle', 'large']
            ],
            optionType='button',
            defaultValue='small',
        ),
        label='componentSize',
    ),
    fac.AntdDivider(isDashed=True),
    fac.AntdConfigProvider(
        fac.AntdSpace(
            [
                fac.AntdButton('按钮测试'),
                fac.AntdCascader(options=[], placeholder='级联选择测试'),
                fac.AntdDatePicker(),
                fac.AntdDateRangePicker(),
                fac.AntdInput(
                    placeholder='输入框测试', style={'width': 256}
                ),
                fac.AntdInputNumber(
                    placeholder='数字输入框测试', style={'width': 256}
                ),
                fac.AntdRadioGroup(
                    options=[
                        {'label': f'选项{i}', 'value': f'选项{i}'}
                        for i in range(5)
                    ],
                    defaultValue='选项1',
                    optionType='button',
                ),
                fac.AntdSegmented(
                    options=[
                        {'label': f'选项{i}', 'value': f'选项{i}'}
                        for i in range(5)
                    ],
                    defaultValue='选项1',
                ),
                fac.AntdSegmentedColoring(
                    size='small',
                    min=-10,
                    max=10,
                    breakpoints=[0, 1, 2, 3, 4, 5],
                    colors=[
                        '#deecf9',
                        '#71afe5',
                        '#2b88d8',
                        '#0078d4',
                        '#106ebe',
                    ],
                ),
                fac.AntdSelect(
                    placeholder='请选择国家：',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {
                            'label': '德国',
                            'value': '德国',
                            'disabled': True,
                        },
                        {'label': '加拿大', 'value': '加拿大'},
                    ],
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    },
                ),
                fac.AntdTimePicker(),
                fac.AntdTimeRangePicker(),
                fac.AntdTreeSelect(
                    treeData=[
                        {
                            'key': '节点1',
                            'value': '1',
                            'title': '节点1',
                            'children': [
                                {
                                    'key': f'节点1-{i}',
                                    'value': f'1-{i}',
                                    'title': f'节点1-{i}',
                                }
                                for i in range(1, 5)
                            ],
                        },
                        {'key': '节点2', 'value': '2', 'title': '节点2'},
                    ],
                    placeholder='请选择',
                    style={'width': 256},
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        ),
        id='config-provider-component-size-demo',
        componentSize='small',
    ),
]

...

app.clientside_callback(
    '(value) => value',
    Output('config-provider-component-size-demo', 'componentSize'),
    Input('config-provider-component-size', 'value'),
)
"""
    }
]
