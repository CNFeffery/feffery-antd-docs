import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdParagraph(
            [
                fac.AntdText('code示例', code=True),
                fac.AntdText('copyable示例', copyable=True),
                fac.AntdText('strikethrough示例', strikethrough=True),
                fac.AntdText('disabled示例', disabled=True),
                fac.AntdText('mark示例', mark=True),
                fac.AntdText('strong示例', strong=True),
                fac.AntdText('underline示例', underline=True),
                fac.AntdText('keyboard示例', keyboard=True),
                fac.AntdText('secondary示例', type='secondary'),
                fac.AntdText('success示例', type='success'),
                fac.AntdText('warning示例', type='warning'),
                fac.AntdText('danger示例', type='danger'),
            ]
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdParagraph(
            [
                fac.AntdText('code', code=True),
                fac.AntdText('copyable', copyable=True),
                fac.AntdText('strikethrough', strikethrough=True),
                fac.AntdText('disabled', disabled=True),
                fac.AntdText('mark', mark=True),
                fac.AntdText('strong', strong=True),
                fac.AntdText('underline', underline=True),
                fac.AntdText('keyboard', keyboard=True),
                fac.AntdText('secondary', type='secondary'),
                fac.AntdText('success', type='success'),
                fac.AntdText('warning', type='warning'),
                fac.AntdText('danger', type='danger'),
            ]
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdParagraph(
    [
        fac.AntdText('code示例', code=True),
        fac.AntdText('copyable示例', copyable=True),
        fac.AntdText('strikethrough示例', strikethrough=True),
        fac.AntdText('disabled示例', disabled=True),
        fac.AntdText('mark示例', mark=True),
        fac.AntdText('strong示例', strong=True),
        fac.AntdText('underline示例', underline=True),
        fac.AntdText('keyboard示例', keyboard=True),
        fac.AntdText('secondary示例', type='secondary'),
        fac.AntdText('success示例', type='success'),
        fac.AntdText('warning示例', type='warning'),
        fac.AntdText('danger示例', type='danger'),
    ]
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdParagraph(
    [
        fac.AntdText('code', code=True),
        fac.AntdText('copyable', copyable=True),
        fac.AntdText('strikethrough', strikethrough=True),
        fac.AntdText('disabled', disabled=True),
        fac.AntdText('mark', mark=True),
        fac.AntdText('strong', strong=True),
        fac.AntdText('underline', underline=True),
        fac.AntdText('keyboard', keyboard=True),
        fac.AntdText('secondary', type='secondary'),
        fac.AntdText('success', type='success'),
        fac.AntdText('warning', type='warning'),
        fac.AntdText('danger', type='danger'),
    ]
)
"""
            }
        ]
