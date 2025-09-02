import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        demo_contents = [
            fac.AntdDivider("mode='eq'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="禁用每月6号",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "eq", "target": "day", "value": 6}],
            ),
            fac.AntdDivider("mode='ne'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="禁用每月非6号",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "ne", "target": "day", "value": 6}],
            ),
            fac.AntdDivider("mode='le'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="禁用每月小于等于6号",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "le", "target": "day", "value": 6}],
            ),
            fac.AntdDivider("mode='lt'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="禁用每月小于6号",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "lt", "target": "day", "value": 6}],
            ),
            fac.AntdDivider("mode='ge'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="禁用每月大于等于6号",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "ge", "target": "day", "value": 6}],
            ),
            fac.AntdDivider("mode='gt'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="禁用每月大于6号",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "gt", "target": "day", "value": 6}],
            ),
            fac.AntdDivider("mode='in'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="禁用每月的5号到25号",
                style={"width": 200},
                disabledDatesStrategy=[
                    {"mode": "in", "target": "day", "value": list(range(5, 26))}
                ],
            ),
            fac.AntdDivider("mode='not-in'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="禁用非每月的5号到25号",
                style={"width": 200},
                disabledDatesStrategy=[
                    {"mode": "not-in", "target": "day", "value": list(range(5, 26))}
                ],
            ),
            fac.AntdDivider("mode='in-enumerate-dates'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="禁用枚举列表中的日期",
                style={"width": 200},
                disabledDatesStrategy=[
                    {
                        "mode": "in-enumerate-dates",
                        "value": [f"2023-01-0{i}" for i in range(1, 10)],
                    }
                ],
                pickerValue="2023-01-01",
            ),
            fac.AntdDivider(
                "mode='not-in-enumerate-dates'", innerTextOrientation="left"
            ),
            fac.AntdDatePicker(
                placeholder="禁用非枚举列表中的日期",
                style={"width": 200},
                disabledDatesStrategy=[
                    {
                        "mode": "not-in-enumerate-dates",
                        "value": [f"2023-01-0{i}" for i in range(1, 10)],
                    }
                ],
                pickerValue="2023-01-01",
            ),
            fac.AntdDivider("target='specific-date'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="禁用指定日期之前的日期",
                style={"width": 200},
                disabledDatesStrategy=[
                    {"mode": "lt", "target": "specific-date", "value": "2023-01-15"}
                ],
                pickerValue="2023-01-01",
            ),
        ]
    else:  # en-us
        demo_contents = [
            fac.AntdDivider("mode='eq'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="Disable the 6th of each month",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "eq", "target": "day", "value": 6}],
                locale="en-us",
            ),
            fac.AntdDivider("mode='ne'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="Disable all days except the 6th",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "ne", "target": "day", "value": 6}],
                locale="en-us",
            ),
            fac.AntdDivider("mode='le'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="Disable days ≤ 6th each month",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "le", "target": "day", "value": 6}],
                locale="en-us",
            ),
            fac.AntdDivider("mode='lt'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="Disable days < 6th each month",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "lt", "target": "day", "value": 6}],
                locale="en-us",
            ),
            fac.AntdDivider("mode='ge'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="Disable days ≥ 6th each month",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "ge", "target": "day", "value": 6}],
                locale="en-us",
            ),
            fac.AntdDivider("mode='gt'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="Disable days > 6th each month",
                style={"width": 200},
                disabledDatesStrategy=[{"mode": "gt", "target": "day", "value": 6}],
                locale="en-us",
            ),
            fac.AntdDivider("mode='in'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="Disable the 5th–25th each month",
                style={"width": 200},
                disabledDatesStrategy=[
                    {"mode": "in", "target": "day", "value": list(range(5, 26))}
                ],
                locale="en-us",
            ),
            fac.AntdDivider("mode='not-in'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="Disable dates not between the 5th and 25th",
                style={"width": 200},
                disabledDatesStrategy=[
                    {"mode": "not-in", "target": "day", "value": list(range(5, 26))}
                ],
                locale="en-us",
            ),
            fac.AntdDivider("mode='in-enumerate-dates'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="Disable dates in the enumeration list",
                style={"width": 200},
                disabledDatesStrategy=[
                    {
                        "mode": "in-enumerate-dates",
                        "value": [f"2023-01-0{i}" for i in range(1, 10)],
                    }
                ],
                pickerValue="2023-01-01",
                locale="en-us",
            ),
            fac.AntdDivider(
                "mode='not-in-enumerate-dates'", innerTextOrientation="left"
            ),
            fac.AntdDatePicker(
                placeholder="Disable dates not in the enumeration list",
                style={"width": 200},
                disabledDatesStrategy=[
                    {
                        "mode": "not-in-enumerate-dates",
                        "value": [f"2023-01-0{i}" for i in range(1, 10)],
                    }
                ],
                pickerValue="2023-01-01",
                locale="en-us",
            ),
            fac.AntdDivider("target='specific-date'", innerTextOrientation="left"),
            fac.AntdDatePicker(
                placeholder="Disable dates before the specified date",
                style={"width": 200},
                disabledDatesStrategy=[
                    {"mode": "lt", "target": "specific-date", "value": "2023-01-15"}
                ],
                pickerValue="2023-01-01",
                locale="en-us",
            ),
        ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
[
    fac.AntdDivider("mode='eq'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用每月6号',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'eq', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='ne'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用每月非6号',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'ne', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='le'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用每月小于等于6号',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'le', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='lt'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用每月小于6号',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'lt', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='ge'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用每月大于等于6号',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'ge', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='gt'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用每月大于6号',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'gt', 'target': 'day', 'value': 6}],
    ),
    fac.AntdDivider("mode='in'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用每月的5号到25号',
        style={'width': 200},
        disabledDatesStrategy=[
            {'mode': 'in', 'target': 'day', 'value': list(range(5, 26))}
        ],
    ),
    fac.AntdDivider("mode='not-in'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用非每月的5号到25号',
        style={'width': 200},
        disabledDatesStrategy=[
            {'mode': 'not-in', 'target': 'day', 'value': list(range(5, 26))}
        ],
    ),
    fac.AntdDivider("mode='in-enumerate-dates'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用枚举列表中的日期',
        style={'width': 200},
        disabledDatesStrategy=[
            {
                'mode': 'in-enumerate-dates',
                'value': [f'2023-01-0{i}' for i in range(1, 10)],
            }
        ],
        pickerValue='2023-01-01',
    ),
    fac.AntdDivider("mode='not-in-enumerate-dates'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用非枚举列表中的日期',
        style={'width': 200},
        disabledDatesStrategy=[
            {
                'mode': 'not-in-enumerate-dates',
                'value': [f'2023-01-0{i}' for i in range(1, 10)],
            }
        ],
        pickerValue='2023-01-01',
    ),
    fac.AntdDivider("target='specific-date'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='禁用指定日期之前的日期',
        style={'width': 200},
        disabledDatesStrategy=[
            {'mode': 'lt', 'target': 'specific-date', 'value': '2023-01-15'}
        ],
        pickerValue='2023-01-01',
    ),
]
"""
            }
        ]
    else:
        return [
            {
                "code": """
[
    fac.AntdDivider("mode='eq'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable the 6th of each month',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'eq', 'target': 'day', 'value': 6}],
        locale="en-us"
    ),
    fac.AntdDivider("mode='ne'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable all days except the 6th',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'ne', 'target': 'day', 'value': 6}],
        locale="en-us"
    ),
    fac.AntdDivider("mode='le'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable days ≤ 6th each month',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'le', 'target': 'day', 'value': 6}],
        locale="en-us"
    ),
    fac.AntdDivider("mode='lt'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable days < 6th each month',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'lt', 'target': 'day', 'value': 6}],
        locale="en-us"
    ),
    fac.AntdDivider("mode='ge'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable days ≥ 6th each month',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'ge', 'target': 'day', 'value': 6}],
        locale="en-us"
    ),
    fac.AntdDivider("mode='gt'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable days > 6th each month',
        style={'width': 200},
        disabledDatesStrategy=[{'mode': 'gt', 'target': 'day', 'value': 6}],
        locale="en-us"
    ),
    fac.AntdDivider("mode='in'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable the 5th-25th each month',
        style={'width': 200},
        disabledDatesStrategy=[
            {'mode': 'in', 'target': 'day', 'value': list(range(5, 26))}
        ],
        locale="en-us"
    ),
    fac.AntdDivider("mode='not-in'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable dates not between the 5th and 25th',
        style={'width': 200},
        disabledDatesStrategy=[
            {'mode': 'not-in', 'target': 'day', 'value': list(range(5, 26))}
        ],
        locale="en-us"
    ),
    fac.AntdDivider("mode='in-enumerate-dates'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable dates in the enumeration list',
        style={'width': 200},
        disabledDatesStrategy=[
            {
                'mode': 'in-enumerate-dates',
                'value': [f'2023-01-0{i}' for i in range(1, 10)],
            }
        ],
        pickerValue='2023-01-01',
        locale="en-us"
    ),
    fac.AntdDivider("mode='not-in-enumerate-dates'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable dates not in the enumeration list',
        style={'width': 200},
        disabledDatesStrategy=[
            {
                'mode': 'not-in-enumerate-dates',
                'value': [f'2023-01-0{i}' for i in range(1, 10)],
            }
        ],
        pickerValue='2023-01-01',
        locale="en-us"
    ),
    fac.AntdDivider("target='specific-date'", innerTextOrientation='left'),
    fac.AntdDatePicker(
        placeholder='Disable dates before the specified date',
        style={'width': 200},
        disabledDatesStrategy=[
            {'mode': 'lt', 'target': 'specific-date', 'value': '2023-01-15'}
        ],
        pickerValue='2023-01-01',
        locale="en-us"
    ),
]
"""
            }
        ]
