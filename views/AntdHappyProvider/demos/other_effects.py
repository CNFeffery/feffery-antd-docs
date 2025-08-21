import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdHappyProvider(
        fac.AntdSpace(
            [
                fac.AntdSwitch(),
                fac.AntdCheckbox(),
                fac.AntdRadioGroup(
                    options=[f'option{i}' for i in range(1, 4)], value='option1'
                ),
            ]
        )
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdHappyProvider(
    fac.AntdSpace(
        [
            fac.AntdSwitch(),
            fac.AntdCheckbox(),
            fac.AntdRadioGroup(
                options=[f'option{i}' for i in range(1, 4)], value='option1'
            ),
        ]
    )
)
"""
        }
    ]
