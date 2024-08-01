from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    actions,  # noqa: F401
    basic_callbacks,  # noqa: F401
    size,  # noqa: F401
    extra_link,  # noqa: F401
    head_style,  # noqa: F401
    body_style,  # noqa: F401
    card_meta,  # noqa: F401
    card_grid,  # noqa: F401
    basic_usage,  # noqa: F401
    extra,  # noqa: F401
    hoverable,  # noqa: F401
    cover,  # noqa: F401,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('基本的使用示例。'),
    },
    {
        'path': 'size',
        'title': '尺寸规格',
        'description': fac.AntdParagraph(
            [
                '可设置两种不同大小：',
                fac.AntdText("'default'", code=True),
                '、',
                fac.AntdText("'small'", code=True),
                '，默认值：',
                fac.AntdText("'default'", code=True),
                '。',
            ]
        ),
    },
    {
        'path': 'extra_link',
        'title': '添加右上角链接',
        'description': fac.AntdParagraph('可在卡片右上角添加自定义链接。'),
    },
    {
        'path': 'extra',
        'title': '添加右上角额外内容',
        'description': fac.AntdParagraph(
            [
                '可在卡片右上角添加自定义组件，优先级比',
                fac.AntdText('extraLink', strong=True),
                '更高，所以设置的',
                fac.AntdText('extraLink', strong=True),
                '将不会生效。',
            ],
        ),
    },
    {
        'path': 'hoverable',
        'title': '悬停效果',
        'description': fac.AntdParagraph(
            '可设置是否在鼠标悬停时显示特殊样式。'
        ),
    },
    {
        'path': 'head_style',
        'title': '标题栏CSS样式',
        'description': fac.AntdParagraph('可设置标题栏的CSS样式。'),
    },
    {
        'path': 'body_style',
        'title': '内容区CSS样式',
        'description': fac.AntdParagraph('可设置内容区的CSS样式。'),
    },
    {
        'path': 'cover',
        'title': '添加封面图片',
        'description': fac.AntdParagraph(
            '可在卡片的标题栏与内容区之间插入封面图片。'
        ),
    },
    {
        'path': 'card_grid',
        'title': '卡片网格',
        'description': fac.AntdParagraph('使用内嵌网格模式来分隔卡片内容。'),
    },
    {
        'path': 'card_meta',
        'title': '结构化卡片',
        'description': fac.AntdParagraph(
            '用于为卡片添加结构化信息，如头像、标题、描述等，更灵活地展示卡片内容。'
        ),
    },
    {
        'path': 'actions',
        'title': '添加底部操作栏',
        'description': fac.AntdParagraph(
            '可添加底部操作栏，实现更复杂的功能。'
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '卡片点击回调监听',
        'description': fac.AntdParagraph('可监听卡片点击事件触发回调。'),
    },
]


def render(component: Component) -> Component:
    """渲染当前组件演示用例"""

    return fac.AntdSpace(
        [
            html.Div(
                [
                    html.Div(
                        getattr(views.AntdCard.demos, item['path']).render(),
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
                                views.AntdCard.demos, item['path']
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
