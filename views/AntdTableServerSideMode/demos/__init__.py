from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    pandas_pagination,  # noqa: F401
    pandas_pagination_single_sort,  # noqa: F401
    pandas_pagination_multiple_sort,  # noqa: F401
    pandas_pagination_filter,  # noqa: F401
    database_pagination,  # noqa: F401
    database_pagination_single_sort,  # noqa: F401
    database_pagination_multiple_sort,  # noqa: F401
    database_pagination_filter,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'pandas_pagination',
        'title': '翻页驱动（pandas示例）',
        'description': fac.AntdParagraph(
            [
                '此例展示了在服务端数据加载模式下，针对',
                fac.AntdText('pandas', strong=True),
                '数据框，联动表格翻页相关事件实现远程数据加载。',
            ]
        ),
    },
    {
        'path': 'pandas_pagination_single_sort',
        'title': '翻页+单字段排序驱动（pandas示例）',
        'description': fac.AntdParagraph(
            [
                '此例展示了在服务端数据加载模式下，针对',
                fac.AntdText('pandas', strong=True),
                '数据框，联动表格翻页+单字段排序相关事件实现远程数据加载。',
            ]
        ),
    },
    {
        'path': 'pandas_pagination_multiple_sort',
        'title': '翻页+组合排序驱动（pandas示例）',
        'description': fac.AntdParagraph(
            [
                '此例展示了在服务端数据加载模式下，针对',
                fac.AntdText('pandas', strong=True),
                '数据框，联动表格翻页+多字段组合排序相关事件实现远程数据加载。',
            ]
        ),
    },
    {
        'path': 'pandas_pagination_filter',
        'title': '翻页+筛选驱动（pandas示例）',
        'description': fac.AntdParagraph(
            [
                '此例展示了在服务端数据加载模式下，针对',
                fac.AntdText('pandas', strong=True),
                '数据框，联动表格翻页+字段筛选相关事件实现远程数据加载。',
            ]
        ),
    },
    {
        'path': 'database_pagination',
        'title': '翻页驱动（数据库示例）',
        'description': fac.AntdParagraph(
            '此例展示了在服务端数据加载模式下，针对数据库表格，联动表格翻页相关事件实现远程数据加载。'
        ),
    },
    {
        'path': 'database_pagination_single_sort',
        'title': '翻页+单字段排序驱动（数据库示例）',
        'description': fac.AntdParagraph(
            [
                '此例展示了在服务端数据加载模式下，针对数据库表格，联动表格翻页+单字段排序相关事件实现远程数据加载。',
            ]
        ),
    },
    {
        'path': 'database_pagination_multiple_sort',
        'title': '翻页+组合排序驱动（数据库示例）',
        'description': fac.AntdParagraph(
            [
                '此例展示了在服务端数据加载模式下，针对数据库表格，联动表格翻页+多字段组合排序相关事件实现远程数据加载。',
            ]
        ),
    },
    {
        'path': 'database_pagination_filter',
        'title': '翻页+筛选驱动（数据库示例）',
        'description': fac.AntdParagraph(
            [
                '此例展示了在服务端数据加载模式下，针对数据库表格，联动表格翻页+字段筛选相关事件实现远程数据加载。',
            ]
        ),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return fac.AntdSpace(
        [
            html.Div(
                [
                    html.Div(
                        getattr(
                            views.AntdTableServerSideMode.demos, item['path']
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
                                                section_name
                                                or component.__name__,
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
                                            section_name or component.__name__,
                                            item['path'],
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
                                views.AntdTableServerSideMode.demos,
                                item['path'],
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
