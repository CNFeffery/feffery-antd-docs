import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdAvatar(
        mode='image',
        src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
        size={'xs': 24, 'sm': 28, 'md': 32, 'lg': 36, 'xl': 40, 'xxl': 45},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdAvatar(
    mode='image',
    src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
    size={'xs': 24, 'sm': 28, 'md': 32, 'lg': 36, 'xl': 40, 'xxl': 45},
)
"""
    }
]
