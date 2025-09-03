import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    demo_contents = fac.AntdSpace(
        [
            fac.AntdDatePicker(
                placement=placement, placeholder=f'placement="{placement}"'
            )
            for placement in [
                "bottomLeft",
                "bottomRight",
                "topLeft",
                "topRight",
            ]
        ],
        direction="vertical",
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    return [
        {
            "code": """
fac.AntdSpace(
    [
        fac.AntdDatePicker(
            placement=placement, placeholder=f'placement="{placement}"'
        )
        for placement in [
            'bottomLeft',
            'bottomRight',
            'topLeft',
            'topRight',
        ]
    ],
    direction='vertical',
)
"""
        }
    ]
