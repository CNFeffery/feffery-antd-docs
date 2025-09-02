import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDatePicker(extraFooter=fac.AntdText("底部额外内容示例")),
                fac.AntdDatePicker(
                    placeholder="请选择日期时间",
                    showTime=True,
                    extraFooter=fac.AntdText("底部额外内容示例"),
                ),
            ],
            wrap=True,
        )
    else:
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDatePicker(
                    extraFooter=fac.AntdText("Example of extra footer content"),
                    locale="en-us",
                ),
                fac.AntdDatePicker(
                    placeholder="Please select date & time",
                    showTime=True,
                    extraFooter=fac.AntdText("Example of extra footer content"),
                    locale="en-us",
                ),
            ],
            wrap=True,
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDatePicker(extraFooter=fac.AntdText('底部额外内容示例')),
        fac.AntdDatePicker(
            placeholder='请选择日期时间',
            showTime=True,
            extraFooter=fac.AntdText('底部额外内容示例'),
        ),
    ],
    wrap=True,
)
"""
            }
        ]
    else:
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDatePicker(extraFooter=fac.AntdText('Example of extra footer content'), locale="en-us"),
        fac.AntdDatePicker(
            placeholder='Please select date & time',
            showTime=True,
            extraFooter=fac.AntdText('Example of extra footer content'),
            locale="en-us"
        ),
    ],
    wrap=True,
)
"""
            }
        ]
