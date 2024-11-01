import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdIcon(
                        icon=icon,
                        mode='iconfont',
                        scriptUrl='//at.alicdn.com/t/font_8d5l8fzk5b87iudi.js',
                    )
                    for icon in ['icon-tuichu', 'icon-facebook', 'icon-twitter']
                ]
            ),
            fac.AntdSpace(
                [
                    fac.AntdIcon(
                        icon=icon,
                        mode='iconfont',
                        scriptUrl=[
                            '//at.alicdn.com/t/font_1788044_0dwu4guekcwr.js',
                            '//at.alicdn.com/t/font_1788592_a5xf2bdic3u.js',
                        ],
                    )
                    for icon in [
                        'icon-javascript',
                        'icon-java',
                        'icon-shoppingcart',
                        'icon-python',
                    ]
                ]
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdIcon(
                    icon=icon,
                    mode='iconfont',
                    scriptUrl='//at.alicdn.com/t/font_8d5l8fzk5b87iudi.js',
                )
                for icon in ['icon-tuichu', 'icon-facebook', 'icon-twitter']
            ]
        ),
        fac.AntdSpace(
            [
                fac.AntdIcon(
                    icon=icon,
                    mode='iconfont',
                    scriptUrl=[
                        '//at.alicdn.com/t/font_1788044_0dwu4guekcwr.js',
                        '//at.alicdn.com/t/font_1788592_a5xf2bdic3u.js',
                    ],
                )
                for icon in [
                    'icon-javascript',
                    'icon-java',
                    'icon-shoppingcart',
                    'icon-python',
                ]
            ]
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
        }
    ]
