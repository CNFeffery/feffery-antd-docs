from i18n import get_current_locale
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTimeRangePicker(
        format=(
            'HH[h]mm[m]ss[s]'
            if get_current_locale() == 'en-us'
            else 'HH时mm分ss秒'
        )
    )

    return demo_contents


def code_string():
    codes = [
        {
            'code': """
fac.AntdTimeRangePicker(format='HH时mm分ss秒')
    """
        }
    ]

    if get_current_locale() == 'en-us':
        for item in codes:
            item['code'] = item['code'].replace(
                'HH时mm分ss秒', 'HH[h]mm[m]ss[s]'
            )
    return codes
