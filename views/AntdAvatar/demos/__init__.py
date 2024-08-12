from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    background,  # noqa: F401
    use_with_AntdIcon,  # noqa: F401
    use_with_AntdBadge,  # noqa: F401
    sizes,  # noqa: F401
    responsive_sizes,  # noqa: F401
    square_shape,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('基础的图标、文字及图片类型头像。'),
    },
    {
        'path': 'background',
        'title': '背景色',
        'description': fac.AntdParagraph(
            [
                '通过设置参数',
                fac.AntdText('style', code=True),
                '控制头像的背景色。',
            ]
        ),
    },
    {
        'path': 'use_with_AntdIcon',
        'title': '配合AntdIcon',
        'description': fac.AntdParagraph(
            [
                '图标型头像直接使用',
                fac.AntdText('AntdIcon', strong=True),
                '中内置的大量图标。',
            ]
        ),
    },
    {
        'path': 'use_with_AntdBadge',
        'title': '添加额外徽标',
        'description': fac.AntdParagraph(
            [
                '配合',
                fac.AntdText('AntdBadge', strong=True),
                '为头像添加额外徽标。',
            ]
        ),
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': fac.AntdParagraph('头像可灵活地设置尺寸规格。'),
    },
    {
        'path': 'responsive_sizes',
        'title': '响应式尺寸规格',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('size', code=True),
                '可控制头像在不同屏幕宽度断点下的尺寸规格。',
            ]
        ),
    },
    {
        'path': 'square_shape',
        'title': '方形头像',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('shape="square"', code=True),
                '渲染方形头像。',
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
                        getattr(views.AntdAvatar.demos, item['path']).render(),
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
                                        fac.AntdIcon(
                                            icon='si-gitee',
                                            style={'verticalAlign': '-0.3em'},
                                        ),
                                        href='{}/blob/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_gitee_library_repo,
                                            AppConfig.doc_library_branch,
                                            component.__name__,
                                            item['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
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
                                views.AntdAvatar.demos, item['path']
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
