import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdComment(
        [
            fac.AntdComment(
                authorName='dash爱好者',
                publishTime={
                    'value': '2024-01-01 19:34:19',
                    'format': 'YYYY-MM-DD hh:mm:ss',
                },
                commentContent='资瓷一个！😊',
            ),
            fac.AntdComment(
                authorName='dash-player',
                publishTime={
                    'value': '2024-01-01 19:40:29',
                    'format': 'YYYY-MM-DD hh:mm:ss',
                },
                commentContent='我要好好学习dash和fac，争取早日开发出自己的个人博客网站！',
            ),
        ],
        authorName='费弗里',
        authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
        publishTime={
            'value': '2024-01-01 19:29:01',
            'format': 'YYYY-MM-DD hh:mm:ss',
        },
        commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
        avatarProps={'mode': 'image', 'src': '/assets/imgs/avatar-demo.jpg'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdComment(
    [
        fac.AntdComment(
            authorName='dash爱好者',
            publishTime={
                'value': '2024-01-01 19:34:19',
                'format': 'YYYY-MM-DD hh:mm:ss',
            },
            commentContent='资瓷一个！😊',
        ),
        fac.AntdComment(
            authorName='dash-player',
            publishTime={
                'value': '2024-01-01 19:40:29',
                'format': 'YYYY-MM-DD hh:mm:ss',
            },
            commentContent='我要好好学习dash和fac，争取早日开发出自己的个人博客网站！',
        ),
    ],
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2024-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss',
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
    avatarProps={'mode': 'image', 'src': '/assets/imgs/avatar-demo.jpg'},
)
"""
    }
]
