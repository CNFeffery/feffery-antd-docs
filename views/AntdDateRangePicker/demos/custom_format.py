import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDateRangePicker(
                placeholder=['picker="date"', ''],
                format='YYYY年MM月DD日',
                style={'width': 300},
            ),
            fac.AntdDateRangePicker(
                placeholder=['picker="week"', ''],
                picker='week',
                format='YYYY年第w周',
                style={'width': 300},
            ),
            fac.AntdDateRangePicker(
                placeholder=['picker="month"', ''],
                picker='month',
                format='YYYY-MM',
                style={'width': 300},
            ),
            fac.AntdDateRangePicker(
                placeholder=['picker="year"', ''],
                picker='year',
                format='YYYY年',
                style={'width': 300},
            ),
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDateRangePicker(
            placeholder=['picker="date"', ''],
            format='YYYY年MM月DD日',
            style={'width': 300},
        ),
        fac.AntdDateRangePicker(
            placeholder=['picker="week"', ''],
            picker='week',
            format='YYYY年第w周',
            style={'width': 300},
        ),
        fac.AntdDateRangePicker(
            placeholder=['picker="month"', ''],
            picker='month',
            format='YYYY-MM',
            style={'width': 300},
        ),
        fac.AntdDateRangePicker(
            placeholder=['picker="year"', ''],
            picker='year',
            format='YYYY年',
            style={'width': 300},
        ),
    ],
    direction='vertical',
)
"""
    }
]
