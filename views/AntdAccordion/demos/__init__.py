from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    accordion_off,  # noqa: F401
    default_active_key,  # noqa: F401
    expand_icon_right,  # noqa: F401
    extra,  # noqa: F401
    ghost,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '默认的手风琴模式下，最多只能展开一个面板。'
        ),
    },
    {
        'path': 'accordion_off',
        'title': '关闭手风琴模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('accordion=False', code=True),
                '关闭手风琴模式。',
            ]
        ),
    },
    {
        'path': 'default_active_key',
        'title': '设置默认展开项',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('defaultActiveKey', code=True),
                '控制默认展开项。',
            ]
        ),
    },
    {
        'path': 'expand_icon_right',
        'title': '展开图标靠右',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('expandIconPosition="right"', code=True),
                '控制展开图标靠右。',
            ]
        ),
    },
    {
        'path': 'extra',
        'title': '子项额外内容',
        'description': fac.AntdParagraph(
            [
                '为子项设置参数',
                fac.AntdText('extra', code=True),
                '添加额外内容。',
            ]
        ),
    },
    {
        'path': 'ghost',
        'title': '透明面板模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('ghost=True', code=True),
                '开启透明面板格式。',
            ]
        ),
    },
    {'path': 'basic_callbacks', 'title': '回调监听', 'description': None},
]


def render(component: Component) -> Component:
    """渲染当前组件演示用例"""

    return fac.AntdSpace(
        [
            html.Div(
                [
                    html.Div(
                        getattr(
                            views.AntdAccordion.demos, item['path']
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
                                views.AntdAccordion.demos, item['path']
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
