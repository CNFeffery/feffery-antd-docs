from i18n import get_current_locale
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
                pickerValue=(
                    '1999/12/31'
                    if get_current_locale() == 'en-us'
                    else '1999年12月31日'
                ),
                format=(
                    'YYYY/MM/DD'
                    if get_current_locale() == 'en-us'
                    else 'YYYY年MM月DD日'
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

    if get_current_locale() == 'en-us':
        for item in codes:
            item['code'] = item['code'].replace('YYYY年MM月DD日', 'YYYY/MM/DD')
            item['code'] = item['code'].replace('YYYY年', 'YYYY')
            item['code'] = item['code'].replace('1999年12月31日', '1999/12/31')
    return codes
