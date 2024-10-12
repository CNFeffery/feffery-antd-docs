import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdButton(variant, color=color, variant=variant)
                    for variant in [
                        'outlined',
                        'dashed',
                        'solid',
                        'filled',
                        'text',
                        'link',
                    ]
                ],
                wrap=True,
            )
            for color in ['default', 'primary', 'danger']
        ],
        direction='vertical',
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdButton('按钮示例')
"""
        },
    ]
