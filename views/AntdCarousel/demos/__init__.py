from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    auto_play,  # noqa: F401
    auto_play_speed,  # noqa: F401
    dot_position,  # noqa: F401
    fade_effect,  # noqa: F401
    transition_speed,  # noqa: F401
    show_arrows,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('对一组平级的元素进行轮播切换。'),
    },
    {
        'path': 'auto_play',
        'title': '自动轮播',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('autoplay=True', code=True),
                '开启自动轮播。',
            ]
        ),
    },
    {
        'path': 'auto_play_speed',
        'title': '自动轮播速度',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('autoplaySpeed', code=True),
                '控制自动轮播间隔时长。',
            ]
        ),
    },
    {
        'path': 'dot_position',
        'title': '指示器位置',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('dotPosition', code=True),
                '控制走马灯指示器位置。',
            ]
        ),
    },
    {
        'path': 'fade_effect',
        'title': '渐显切换效果',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('effect="fade"', code=True),
                '启用渐显切换效果。',
            ]
        ),
    },
    {
        'path': 'transition_speed',
        'title': '动画过渡时长',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('speed', code=True),
                '控制切换动画过程毫秒耗时。',
            ]
        ),
    },
    {
        'path': 'show_arrows',
        'title': '显示切换箭头',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('arrows=True', code=True),
                '开启额外的切换用箭头。',
            ]
        ),
    },
]


def render(component: Component) -> Component:
    """渲染当前组件演示用例"""

    return fac.AntdSpace(
        [
            html.Div(
                [
                    html.Div(
                        getattr(
                            views.AntdCarousel.demos, item['path']
                        ).render(),
                        className='demo-box',
                    ),
                    html.Div(
                        [
                            fac.AntdText(
                                [
                                    item['title'],
                                    fac.AntdTooltip(
                                        html.A(
                                            fac.AntdIcon(
                                                icon='antd-edit',
                                                className='demo-github-link',
                                            ),
                                            href='{}/edit/{}/views/{}/demos/{}.py'.format(
                                                AppConfig.doc_library_repo,
                                                AppConfig.doc_library_branch,
                                                component.__name__,
                                                item['path'],
                                            ),
                                            target='_blank',
                                        ),
                                        title='在Github上编辑此示例',
                                    ),
                                ],
                                className='demo-title',
                            ),
                            html.Div(
                                item['description'],
                                style={'padding': '18px 24px 12px 28px'},
                            ),
                        ],
                        style={'position': 'relative'},
                    ),
                    fac.AntdCenter(
                        fac.AntdSpace(
                            [
                                fac.AntdTooltip(
                                    dcc.Link(
                                        fac.AntdIcon(icon='antd-export'),
                                        href='/~demo/{}/{}'.format(
                                            component.__name__, item['path']
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title='在新窗口打开',
                                ),
                                fac.AntdTooltip(
                                    fac.AntdIcon(
                                        id={
                                            'type': 'demo-code-toggle',
                                            'index': '{}/{}'.format(
                                                component.__name__, item['path']
                                            ),
                                        },
                                        icon='antd-code',
                                        className='demo-operations-icon',
                                    ),
                                    title='展开/收起代码',
                                ),
                                fac.AntdTooltip(
                                    dcc.Link(
                                        fac.AntdIcon(icon='antd-github'),
                                        href='{}/tree/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_library_repo,
                                            AppConfig.doc_library_branch,
                                            component.__name__,
                                            item['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title='在Github中查看完整代码',
                                ),
                                fac.AntdTooltip(
                                    dcc.Link(
                                        html.Img(
                                            src='/assets/imgs/gitee-logo.svg',
                                            width=18,
                                            height=18,
                                            style={
                                                'display': 'block',
                                                'transform': 'translate(-0.05em, 0.05em)',
                                            },
                                        ),
                                        href='{}/blob/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_gitee_library_repo,
                                            AppConfig.doc_library_branch,
                                            component.__name__,
                                            item['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-img',
                                    ),
                                    title='在Gitee中查看完整代码',
                                ),
                            ],
                            size=12,
                        ),
                        className='demo-operations',
                    ),
                    fac.AntdTabs(
                        items=[
                            {
                                'label': item.get('language') or 'Python',
                                'key': item.get('language') or 'Python',
                                'children': fmc.FefferySyntaxHighlighter(
                                    codeString=item['code'],
                                    language=(
                                        item.get('language') or 'Python'
                                    ).lower(),
                                    codeTheme='coy-without-shadows',
                                    codeBlockStyle={'overflowX': 'auto'},
                                ),
                            }
                            for item in getattr(
                                views.AntdCarousel.demos, item['path']
                            ).code_string
                        ],
                        centered=True,
                        className='demo-code-tabs',
                        id={
                            'type': 'demo-code',
                            'index': '{}/{}'.format(
                                component.__name__, item['path']
                            ),
                        },
                        style={'display': 'none'},
                    ),
                ],
                className='demo-container',
                id='demo-container-' + item['path'],
            )
            for item in demos_config
        ],
        direction='vertical',
        size='large',
        style={'width': '100%'},
    )
