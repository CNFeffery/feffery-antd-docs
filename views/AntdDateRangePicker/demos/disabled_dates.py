import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider("mode='eq'", innerTextOrientation='left'),
        fac.AntdDateRangePicker(
            placeholder=['禁用每月6号', ''],
            style={'width': 400},
            disabledDatesStrategy=[{'mode': 'eq', 'target': 'day', 'value': 6}],
        ),
        fac.AntdDivider("mode='ne'", innerTextOrientation='left'),
        fac.AntdDateRangePicker(
            placeholder=['禁用每月非6号', ''],
            style={'width': 400},
            disabledDatesStrategy=[{'mode': 'ne', 'target': 'day', 'value': 6}],
        ),
        fac.AntdDivider("mode='le'", innerTextOrientation='left'),
        fac.AntdDateRangePicker(
            placeholder=['禁用每月小于等于6号', ''],
            style={'width': 400},
            disabledDatesStrategy=[{'mode': 'le', 'target': 'day', 'value': 6}],
        ),
        fac.AntdDivider("mode='lt'", innerTextOrientation='left'),
        fac.AntdDateRangePicker(
            placeholder=['禁用每月小于6号', ''],
            style={'width': 400},
            disabledDatesStrategy=[{'mode': 'lt', 'target': 'day', 'value': 6}],
        ),
        fac.AntdDivider("mode='ge'", innerTextOrientation='left'),
        fac.AntdDateRangePicker(
            placeholder=['禁用每月大于等于6号', ''],
            style={'width': 400},
            disabledDatesStrategy=[{'mode': 'ge', 'target': 'day', 'value': 6}],
        ),
        fac.AntdDivider("mode='gt'", innerTextOrientation='left'),
        fac.AntdDateRangePicker(
            placeholder=['禁用每月大于6号', ''],
            style={'width': 400},
            disabledDatesStrategy=[{'mode': 'gt', 'target': 'day', 'value': 6}],
        ),
        fac.AntdDivider("mode='in'", innerTextOrientation='left'),
        fac.AntdDateRangePicker(
            placeholder=['禁用每月的5号到25号', ''],
            style={'width': 400},
            disabledDatesStrategy=[
                {'mode': 'in', 'target': 'day', 'value': list(range(5, 26))}
            ],
        ),
        fac.AntdDivider("mode='not-in'", innerTextOrientation='left'),
        fac.AntdDateRangePicker(
            placeholder=['禁用非每月的5号到25号', ''],
            style={'width': 400},
            disabledDatesStrategy=[
                {'mode': 'not-in', 'target': 'day', 'value': list(range(5, 26))}
            ],
        ),
        fac.AntdDivider(
            "mode='in-enumerate-dates'", innerTextOrientation='left'
        ),
        fac.AntdDateRangePicker(
            placeholder=['禁用枚举列表中的日期', ''],
            style={'width': 400},
            disabledDatesStrategy=[
                {
                    'mode': 'in-enumerate-dates',
                    'value': [f'2023-01-0{i}' for i in range(1, 10)],
                }
            ],
            defaultPickerValue='2023-01-01',
        ),
        fac.AntdDivider(
            "mode='not-in-enumerate-dates'", innerTextOrientation='left'
        ),
        fac.AntdDateRangePicker(
            placeholder=['禁用非枚举列表中的日期', ''],
            style={'width': 400},
            disabledDatesStrategy=[
                {
                    'mode': 'not-in-enumerate-dates',
                    'value': [f'2023-01-0{i}' for i in range(1, 10)],
                }
            ],
            defaultPickerValue='2023-01-01',
        ),
        fac.AntdDivider("target='specific-date'", innerTextOrientation='left'),
        fac.AntdDateRangePicker(
            placeholder=['禁用指定日期之前的日期', ''],
            style={'width': 400},
            disabledDatesStrategy=[
                {'mode': 'lt', 'target': 'specific-date', 'value': '2023-01-15'}
            ],
            defaultPickerValue='2023-01-01',
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider("mode='eq'", innerTextOrientation='left'),
    fac.AntdDateRangePicker(
        placeholder=['禁用每月6号', ''],
        style={'width': 400},
        disabledDatesStrategy=[{'mode': 'eq', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='ne'", innerTextOrientation='left'),
    fac.AntdDateRangePicker(
        placeholder=['禁用每月非6号', ''],
        style={'width': 400},
        disabledDatesStrategy=[{'mode': 'ne', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='le'", innerTextOrientation='left'),
    fac.AntdDateRangePicker(
        placeholder=['禁用每月小于等于6号', ''],
        style={'width': 400},
        disabledDatesStrategy=[{'mode': 'le', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='lt'", innerTextOrientation='left'),
    fac.AntdDateRangePicker(
        placeholder=['禁用每月小于6号', ''],
        style={'width': 400},
        disabledDatesStrategy=[{'mode': 'lt', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='ge'", innerTextOrientation='left'),
    fac.AntdDateRangePicker(
        placeholder=['禁用每月大于等于6号', ''],
        style={'width': 400},
        disabledDatesStrategy=[{'mode': 'ge', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='gt'", innerTextOrientation='left'),
    fac.AntdDateRangePicker(
        placeholder=['禁用每月大于6号', ''],
        style={'width': 400},
        disabledDatesStrategy=[{'mode': 'gt', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='in'", innerTextOrientation='left'),
    fac.AntdDateRangePicker(
        placeholder=['禁用每月的5号到25号', ''],
        style={'width': 400},
        disabledDatesStrategy=[
            {'mode': 'in', 'target': 'day', 'value': list(range(5, 26))}
        ],
    ),
    fac.AntdDivider("mode='not-in'", innerTextOrientation='left'),
    fac.AntdDateRangePicker(
        placeholder=['禁用非每月的5号到25号', ''],
        style={'width': 400},
        disabledDatesStrategy=[
            {'mode': 'not-in', 'target': 'day', 'value': list(range(5, 26))}
        ],
    ),
    fac.AntdDivider(
        "mode='in-enumerate-dates'", innerTextOrientation='left'
    ),
    fac.AntdDateRangePicker(
        placeholder=['禁用枚举列表中的日期', ''],
        style={'width': 400},
        disabledDatesStrategy=[
            {
                'mode': 'in-enumerate-dates',
                'value': [f'2023-01-0{i}' for i in range(1, 10)],
            }
        ],
        defaultPickerValue='2023-01-01',
    ),
    fac.AntdDivider(
        "mode='not-in-enumerate-dates'", innerTextOrientation='left'
    ),
    fac.AntdDateRangePicker(
        placeholder=['禁用非枚举列表中的日期', ''],
        style={'width': 400},
        disabledDatesStrategy=[
            {
                'mode': 'not-in-enumerate-dates',
                'value': [f'2023-01-0{i}' for i in range(1, 10)],
            }
        ],
        defaultPickerValue='2023-01-01',
    ),
    fac.AntdDivider("target='specific-date'", innerTextOrientation='left'),
    fac.AntdDateRangePicker(
        placeholder=['禁用指定日期之前的日期', ''],
        style={'width': 400},
        disabledDatesStrategy=[
            {'mode': 'lt', 'target': 'specific-date', 'value': '2023-01-15'}
        ],
        defaultPickerValue='2023-01-01',
    ),
]
"""
    }
]
