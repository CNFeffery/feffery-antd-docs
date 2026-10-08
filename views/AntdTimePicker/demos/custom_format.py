from i18n import get_current_locale
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTimePicker(
        format=(
            'HH[h]mm[m]ss[s]'
            if get_current_locale() == 'en-us'
            else 'HH点mm分ss秒'
        ),
        defaultValue=(
            '12h18m17s' if get_current_locale() == 'en-us' else '12点18分17秒'
        ),
    )

    return demo_contents


def code_string():
    codes = [
        {
            'code': """
fac.AntdTimePicker(
    format='HH点mm分ss秒', defaultValue='12点18分17秒'
)
    """
        }
    ]

    if get_current_locale() == 'en-us':
        for item in codes:
            item['code'] = item['code'].replace(
                'HH点mm分ss秒', 'HH[h]mm[m]ss[s]'
            )
            item['code'] = item['code'].replace('12点18分17秒', '12h18m17s')
    return codes
