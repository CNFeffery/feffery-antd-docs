from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    type,  # noqa: F401
    duration,  # noqa: F401
    top,  # noqa: F401
    max_count,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '全局提示的常规使用方式是通过回调向某个容器输出，每一次输出都会触发一条新的全局提示的新增。'
        ),
    },
    {
        'path': 'type',
        'title': '提示类型',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('共有五种类型'),
                fac.AntdText('default', code=True),
                fac.AntdText('、'),
                fac.AntdText('info', code=True),
                fac.AntdText('、'),
                fac.AntdText('success', code=True),
                fac.AntdText('、'),
                fac.AntdText('warning', code=True),
                fac.AntdText('、'),
                fac.AntdText('error', code=True),
                fac.AntdText('。'),
            ]
        ),
    },
    {
        'path': 'duration',
        'title': '修改延时',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置参数'),
                fac.AntdText('duration', code=True),
                fac.AntdText('控制全局提示的显示时间，默认为'),
                fac.AntdText('3', code=True),
                fac.AntdText('秒。'),
            ]
        ),
    },
    {
        'path': 'top',
        'title': '顶端最小距离',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置参数'),
                fac.AntdText('top', code=True),
                fac.AntdText('控制全局提示的顶端最小距离。'),
            ]
        ),
    },
    {
        'path': 'max_count',
        'title': '提示消息数量',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置参数'),
                fac.AntdText('maxCount', code=True),
                fac.AntdText('控制同屏最大消息数。'),
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
                        getattr(views.AntdMessage.demos, item['path']).render(),
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
                                        href='/~demo/{}/{}?padding=no'.format(
                                            component.__name__, item['path']
                                        )
                                        if item['path'] == 'top_notice'
                                        else '/~demo/{}/{}'.format(
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
                                views.AntdMessage.demos, item['path']
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
