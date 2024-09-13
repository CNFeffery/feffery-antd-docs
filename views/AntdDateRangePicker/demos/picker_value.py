import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDateRangePicker(
                pickerValue='1999-12-31', style={'width': 300}
            ),
            fac.AntdDateRangePicker(
                placeholder=['配合自定义format', ''],
                pickerValue='1999年12月31日',
                format='YYYY年MM月DD日',
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
            pickerValue='1999-12-31', style={'width': 300}
        ),
        fac.AntdDateRangePicker(
            placeholder=['配合自定义format', ''],
            pickerValue='1999年12月31日',
            format='YYYY年MM月DD日',
            style={'width': 300},
        ),
    ],
    direction='vertical',
)
"""
    }
]
