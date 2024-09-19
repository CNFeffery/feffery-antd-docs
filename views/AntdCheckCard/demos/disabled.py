import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdCheckCard(
            fac.AntdText('选择卡片示例' * 10), disabled=True, checked=True
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdCheckCard(
            fac.AntdText('Demo' * 20), disabled=True, checked=True
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdCheckCard(
    fac.AntdText('选择卡片示例' * 10), disabled=True, checked=True
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdCheckCard(
    fac.AntdText('Demo' * 20), disabled=True, checked=True
)
"""
            }
        ]
