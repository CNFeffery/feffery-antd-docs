import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
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
        style={
            'width': '100%',
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
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
    style={
        'width': '100%',
    },
)
"""
    }
]
