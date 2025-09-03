import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    demo_contents = fac.AntdSpace(
        [
            fac.AntdDatePicker(picker=picker, placeholder=f'picker="{picker}"')
            for picker in ["date", "week", "month", "quarter", "year"]
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
        fac.AntdDatePicker(picker=picker, placeholder=f'picker="{picker}"')
        for picker in ['date', 'week', 'month', 'quarter', 'year']
    ],
    direction='vertical',
)
"""
        }
    ]
