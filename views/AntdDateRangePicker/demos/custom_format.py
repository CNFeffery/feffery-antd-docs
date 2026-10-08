from i18n import get_current_locale
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDateRangePicker(
                placeholder=['picker="date"', ''],
                format=(
                    'YYYY/MM/DD'
                    if get_current_locale() == 'en-us'
                    else 'YYYY年MM月DD日'
                ),
                style={'width': 300},
            ),
            fac.AntdDateRangePicker(
                placeholder=['picker="week"', ''],
                picker='week',
                format=(
                    'YYYY-[week]w'
                    if get_current_locale() == 'en-us'
                    else 'YYYY年第w周'
                ),
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
                format=(
                    'YYYY' if get_current_locale() == 'en-us' else 'YYYY年'
                ),
                style={'width': 300},
            ),
        ],
        direction='vertical',
    )

    return demo_contents


def code_string():
    codes = [
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

    if get_current_locale() == 'en-us':
        for item in codes:
            item['code'] = item['code'].replace('YYYY年MM月DD日', 'YYYY/MM/DD')
            item['code'] = item['code'].replace('YYYY年第w周', 'YYYY-[week]w')
            item['code'] = item['code'].replace('YYYY年', 'YYYY')
    return codes
