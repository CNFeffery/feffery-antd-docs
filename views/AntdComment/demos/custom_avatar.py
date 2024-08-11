import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdComment(
        authorName='费弗里',
        authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
        publishTime={
            'value': '2024-01-01 19:29:01',
            'format': 'YYYY-MM-DD hh:mm:ss',
        },
        commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
        avatarProps={
            'mode': 'image',
            'src': '/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdComment(
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2024-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss',
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
    avatarProps={
        'mode': 'image',
        'src': '/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
    },
)
"""
    }
]
