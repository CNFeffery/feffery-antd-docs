import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State, MATCH
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                '社交软件常见交互演示', innerTextOrientation='left'
            ),
            fac.AntdCard(
                fac.AntdCardMeta(
                    avatar=fac.AntdAvatar(
                        mode='image',
                        src='https://images.pexels.com/users/avatars/426868/mantas-sinkevicius-653.jpeg?auto=compress&fit=crop&h=130&w=130&dpr=1',
                    ),
                    description='https://www.pexels.com/@mantasink/',
                    title='Mantas Sinkevičius',
                ),
                coverImg={
                    'alt': 'demo pictrue',
                    'src': 'https://images.pexels.com/photos/18664364/pexels-photo-18664364/free-photo-of-rock-formation-on-sea-shore-in-greece.jpeg',
                },
                actions=[
                    fac.AntdIcon(
                        id={
                            'type': 'card-meta-actions-icon-demo',
                            'index': 'like',
                        },
                        icon='md-favorite-border',
                        style={'fontSize': 20},
                    ),
                    fac.AntdIcon(
                        id={
                            'type': 'card-meta-actions-icon-demo',
                            'index': 'fav',
                        },
                        icon='md-star-border',
                        style={'fontSize': 20},
                    ),
                    fac.AntdPopover(
                        fac.AntdIcon(
                            icon='md-forward',
                            style={'fontSize': 20},
                        ),
                        content=fac.AntdSpace(
                            [
                                '分享到：',
                                fac.AntdSpace(
                                    [
                                        fac.AntdIcon(icon='antd-weibo'),
                                        fac.AntdIcon(icon='antd-alipay-circle'),
                                        fac.AntdIcon(icon='antd-github'),
                                        fac.AntdIcon(icon='antd-link'),
                                    ],
                                    style={'fontSize': 20},
                                ),
                            ],
                            direction='vertical',
                            style={'color': 'rgba(0,0,0,0.65)'},
                        ),
                        trigger=['hover', 'click'],
                    ),
                ],
                hoverable=True,
                styles={'header': {'display': 'none'}},
            ),
        ],
        direction='vertical',
    )

    return demo_contents


# 点击like/favourite icon时切换icon样式
@app.callback(
    Output({'type': 'card-meta-actions-icon-demo', 'index': MATCH}, 'icon'),
    Input({'type': 'card-meta-actions-icon-demo', 'index': MATCH}, 'nClicks'),
    State({'type': 'card-meta-actions-icon-demo', 'index': MATCH}, 'icon'),
    prevent_initial_call=True,
)
def change_icon_style(nClicks, icon):
    if '-border' in icon:
        return icon.replace('-border', '')
    return icon + '-border'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider(
            '社交软件常见交互演示', innerTextOrientation='left'
        ),
        fac.AntdCard(
            fac.AntdCardMeta(
                avatar=fac.AntdAvatar(
                    mode='image',
                    src='https://images.pexels.com/users/avatars/426868/mantas-sinkevicius-653.jpeg?auto=compress&fit=crop&h=130&w=130&dpr=1',
                ),
                description='https://www.pexels.com/@mantasink/',
                title='Mantas Sinkevičius',
            ),
            coverImg={
                'alt': 'demo pictrue',
                'src': 'https://images.pexels.com/photos/18664364/pexels-photo-18664364/free-photo-of-rock-formation-on-sea-shore-in-greece.jpeg',
            },
            actions=[
                fac.AntdIcon(
                    id={
                        'type': 'card-meta-actions-icon-demo',
                        'index': 'like',
                    },
                    icon='md-favorite-border',
                    style={'fontSize': 20},
                ),
                fac.AntdIcon(
                    id={
                        'type': 'card-meta-actions-icon-demo',
                        'index': 'fav',
                    },
                    icon='md-star-border',
                    style={'fontSize': 20},
                ),
                fac.AntdPopover(
                    fac.AntdIcon(
                        icon='md-forward',
                        style={'fontSize': 20},
                    ),
                    content=fac.AntdSpace(
                        [
                            '分享到：',
                            fac.AntdSpace(
                                [
                                    fac.AntdIcon(icon='antd-weibo'),
                                    fac.AntdIcon(icon='antd-alipay-circle'),
                                    fac.AntdIcon(icon='antd-github'),
                                    fac.AntdIcon(icon='antd-link'),
                                ],
                                style={'fontSize': 20},
                            ),
                        ],
                        direction='vertical',
                        style={'color': 'rgba(0,0,0,0.65)'},
                    ),
                    trigger=['hover', 'click'],
                ),
            ],
            hoverable=True,
            styles={'header': {'display': 'none'}},
        ),
    ],
    direction='vertical',
)


# 点击like/favourite icon时切换icon样式
@app.callback(
    Output({'type': 'card-meta-actions-icon-demo', 'index': MATCH}, 'icon'),
    Input({'type': 'card-meta-actions-icon-demo', 'index': MATCH}, 'nClicks'),
    State({'type': 'card-meta-actions-icon-demo', 'index': MATCH}, 'icon'),
    prevent_initial_call=True,
)
def change_icon_style(nClicks, icon):
    if '-border' in icon:
        return icon.replace('-border', '')
    return icon + '-border'

"""
    }
]
