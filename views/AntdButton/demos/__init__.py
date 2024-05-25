from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    button_types,  # noqa: F401
    sizes,  # noqa: F401
    disabled_status,  # noqa: F401
    danger_status,  # noqa: F401
    ghost_background,  # noqa: F401
    button_shape,  # noqa: F401
    block_button,  # noqa: F401
    as_link,  # noqa: F401
    button_icon,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最基础的按钮。'),
    },
    {
        'path': 'button_types',
        'title': '按钮类型',
        'description': fac.AntdParagraph('不同类型的按钮。'),
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': fac.AntdParagraph('不同尺寸的按钮。'),
    },
    {
        'path': 'disabled_status',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('disabled=True', code=True),
                '开启禁用状态。',
            ]
        ),
    },
    {
        'path': 'danger_status',
        'title': '危险状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('danger=True', code=True),
                '开启危险状态。',
            ]
        ),
    },
    {
        'path': 'ghost_background',
        'title': '透明背景',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('ghost=True', code=True),
                '开启透明背景。',
            ]
        ),
    },
    {
        'path': 'button_shape',
        'title': '按钮形状',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('shape', code=True),
                '控制按钮形状。',
            ]
        ),
    },
    {
        'path': 'block_button',
        'title': '撑满父元素',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('block=True', code=True),
                '撑满父元素。',
            ]
        ),
    },
    {
        'path': 'as_link',
        'title': '链接跳转功能',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('href', code=True),
                '添加链接跳转功能。',
            ]
        ),
    },
    {
        'path': 'button_icon',
        'title': '额外图标',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('icon', code=True),
                '添加自定义图标元素。',
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
                        getattr(views.AntdButton.demos, item['path']).render(),
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
                                views.AntdButton.demos, item['path']
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
