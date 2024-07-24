import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdAlert(
        message=[
            '君不见黄河之水天上来',
            '奔流到海不复回',
            '君不见高堂明镜悲白发',
            '朝如青丝暮成雪',
            '人生得意须尽欢',
            '莫使金樽空对月',
            '天生我材必有用',
            '千金散尽还复来',
        ],
        description='轮播模式示例',
        showIcon=True,
        messageRenderMode='loop-text',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdAlert(
    message=[
        '君不见黄河之水天上来',
        '奔流到海不复回',
        '君不见高堂明镜悲白发',
        '朝如青丝暮成雪',
        '人生得意须尽欢',
        '莫使金樽空对月',
        '天生我材必有用',
        '千金散尽还复来',
    ],
    description='轮播模式示例',
    showIcon=True,
    messageRenderMode='loop-text',
)
"""
    }
]
