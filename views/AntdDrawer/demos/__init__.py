from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    placement,  # noqa: F401
    footer,  # noqa: F401
    extra,  # noqa: F401
    local_container,  # noqa: F401
    local_container_selector,  # noqa: F401
    loading,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('通过对应的回调触发抽屉的弹出显示。'),
    },
    {
        'path': 'placement',
        'title': '抽屉弹出方位',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('placement', code=True),
                '控制抽屉的弹出方位。',
            ]
        ),
    },
    {
        'path': 'footer',
        'title': '设置底部内容',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('footer', code=True),
                '为抽屉设置固定的底部内容。',
            ]
        ),
    },
    {
        'path': 'extra',
        'title': '设置额外区内容',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('extra', code=True),
                '为抽屉设置额外区内容。',
            ]
        ),
    },
    {
        'path': 'local_container',
        'title': '局部容器中展示抽屉',
        'description': fac.AntdParagraph(
            [
                '配合',
                fac.AntdText('相对-绝对', strong=True),
                '定位，在局部容器中展示抽屉。',
            ]
        ),
    },
    {
        'path': 'local_container',
        'title': '局部容器中展示抽屉',
        'description': fac.AntdParagraph(
            [
                '配合',
                fac.AntdText('相对-绝对', strong=True),
                '定位，在局部容器中展示抽屉。',
            ]
        ),
    },
    {
        'path': 'local_container_selector',
        'title': '更自由地指定局部容器',
        'description': fac.AntdParagraph(
            [
                '基于参数',
                fac.AntdText('containerSelector', code=True),
                '更自由地指定抽屉渲染的目标局部容器。',
            ]
        ),
    },
    {
        'path': 'loading',
        'title': '加载中状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('loading=True', code=True),
                '为抽屉内容区开启加载中状态。',
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
                        getattr(views.AntdDrawer.demos, item['path']).render(),
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
                                views.AntdDrawer.demos, item['path']
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
