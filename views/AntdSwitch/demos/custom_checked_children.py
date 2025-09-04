import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render this demo case"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                # 直接传入字符串
                fac.AntdSwitch(checkedChildren="开", unCheckedChildren="关"),
                # 传入AntdIcon组件
                fac.AntdSwitch(
                    checkedChildren=fac.AntdIcon(icon="antd-check"),
                    unCheckedChildren=fac.AntdIcon(icon="antd-close"),
                    checked=True,
                ),
                # 传入任意适宜静态展示的组件并配合style属性自定义样式，以AntdText为例
                fac.AntdSwitch(
                    checkedChildren=fac.AntdText(
                        "checked", strong=True, style={"color": "yellow"}
                    ),
                    unCheckedChildren=fac.AntdText(
                        "unChecked", strong=True, style={"color": "black"}
                    ),
                ),
            ],
            direction="vertical",
            style={"width": "100%"},
        )
    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                # Pass plain strings directly
                fac.AntdSwitch(checkedChildren="On", unCheckedChildren="Off"),
                # Pass an AntdIcon component
                fac.AntdSwitch(
                    checkedChildren=fac.AntdIcon(icon="antd-check"),
                    unCheckedChildren=fac.AntdIcon(icon="antd-close"),
                    checked=True,
                ),
                # Pass any component suitable for static display and customize styles via style prop; AntdText as an example
                fac.AntdSwitch(
                    checkedChildren=fac.AntdText(
                        "checked", strong=True, style={"color": "yellow"}
                    ),
                    unCheckedChildren=fac.AntdText(
                        "unChecked", strong=True, style={"color": "black"}
                    ),
                ),
            ],
            direction="vertical",
            style={"width": "100%"},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        # 直接传入字符串
        fac.AntdSwitch(
            checkedChildren='开',
            unCheckedChildren='关',
        ),
        # 传入AntdIcon组件
        fac.AntdSwitch(
            checkedChildren=fac.AntdIcon(icon='antd-check'),
            unCheckedChildren=fac.AntdIcon(icon='antd-close'),
            checked=True,
        ),
        # 传入任意适宜静态展示的组件并配合style属性自定义样式，以AntdText为例
        fac.AntdSwitch(
            checkedChildren=fac.AntdText(
                'checked', strong=True, style={'color': 'yellow'}
            ),
            unCheckedChildren=fac.AntdText(
                'unChecked', strong=True, style={'color': 'black'}
            ),
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        # Pass plain strings directly
        fac.AntdSwitch(
            checkedChildren='On',
            unCheckedChildren='Off',
        ),
        # Pass an AntdIcon component
        fac.AntdSwitch(
            checkedChildren=fac.AntdIcon(icon='antd-check'),
            unCheckedChildren=fac.AntdIcon(icon='antd-close'),
            checked=True,
        ),
        # Pass any component suitable for static display and customize styles via style prop; AntdText as an example
        fac.AntdSwitch(
            checkedChildren=fac.AntdText(
                'checked', strong=True, style={'color': 'yellow'}
            ),
            unCheckedChildren=fac.AntdText(
                'unChecked', strong=True, style={'color': 'black'}
            ),
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
