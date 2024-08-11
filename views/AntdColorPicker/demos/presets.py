import feffery_antd_components as fac
from dash.dependencies import Component
from palettable.colorbrewer.sequential import Blues_9, Greens_9, Reds_9


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdColorPicker(
        presets=[
            {'colors': c.hex_colors, 'label': c.name, 'defaultOpen': i == 0}
            for i, c in enumerate([Blues_9, Greens_9, Reds_9])
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdColorPicker(
    presets=[
        {'colors': c.hex_colors, 'label': c.name, 'defaultOpen': i == 0}
        for i, c in enumerate([Blues_9, Greens_9, Reds_9])
    ]
)
"""
    }
]
