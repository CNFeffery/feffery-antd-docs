from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    color,  # noqa: F401
    custom_preset_color,  # noqa: F401
    border,  # noqa: F401
    icon,  # noqa: F401
    close_icon,  # noqa: F401
    close_counts,  # noqa: F401
    add_delete_tag,  # noqa: F401
    draggable_tag,  # noqa: F401
    as_link,  # noqa: F401
)

from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                '基本的标签用法，向标签的',
                fac.AntdText('content', strong=True),
                '属性传入标签内容。',
            ]
        ),
    },
    {
        'path': 'border',
        'title': '无边框标签',
        'description': fac.AntdParagraph('可设置是否渲染边框。'),
    },
    {
        'path': 'color',
        'title': '标签颜色',
        'description': fac.AntdParagraph(
            [
                '可以自定义标签颜色，可使用内置的11种色彩主题，色彩主题会配置好',
                fac.AntdText('color', code=True),
                '、',
                fac.AntdText('background-color', code=True),
                '、',
                fac.AntdText('border-color', code=True),
                '三种CSS属性。而直接传入CSS颜色值则会令文字颜色为白色，背景颜色为传入的CSS颜色。',
            ]
        ),
    },
    {
        'path': 'custom_preset_color',
        'title': '扩展预设颜色',
        'description': fac.AntdParagraph(
            '可以自行设计算法，实现近似内置色彩主题的效果。'
        ),
    },
    {
        'path': 'icon',
        'title': '标签内前缀图标',
        'description': fac.AntdParagraph(
            [
                '可设置标签内的前置图标，如需将图标设置在其他位置，仍需以组件形式传入',
                fac.AntdText('content', strong=True),
                '属性。',
            ]
        ),
    },
    {
        'path': 'close_icon',
        'title': '关闭标签按钮',
        'description': fac.AntdParagraph(
            [
                '可设置是否渲染标签内部右侧的关闭按钮。',
            ]
        ),
    },
    {
        'path': 'close_counts',
        'title': '关闭标签按钮监听回调',
        'description': fac.AntdParagraph(
            [
                '通过监听关闭标签按钮的点击数量来触发回调。',
            ]
        ),
    },
    {
        'path': 'as_link',
        'title': '充当链接使用',
        'description': fac.AntdParagraph(
            [
                '可设置',
                fac.AntdText('href', strong=True),
                '和',
                fac.AntdText('target', strong=True),
                '属性，将标签作为链接使用。',
            ]
        ),
    },
    {
        'path': 'add_delete_tag',
        'title': '动态增删标签示例',
        'description': fac.AntdParagraph(
            [
                '通过设置新增按钮和监听',
                fac.AntdText('closeCounts', strong=True),
                '回调，实现动态增删标签。配合',
                dcc.Link(
                    'fuc.FefferyAutoAnimate',
                    href='https://fuc.feffery.tech/FefferyAutoAnimate',
                    target='_blank',
                ),
                '可实现增删动画效果。',
            ]
        ),
    },
    {
        'path': 'draggable_tag',
        'title': '可拖拽标签组示例',
        'description': fac.AntdParagraph(
            [
                '配合',
                fac.AntdText('fuc.FefferySortable', strong=True),
                '组件，实现可拖拽的标签组效果。',
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
                        getattr(views.AntdTag.demos, item['path']).render(),
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
                                views.AntdTag.demos, item['path']
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
