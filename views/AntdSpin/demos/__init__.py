from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    exclude_mode,  # noqa: F401
    include_mode,  # noqa: F401
    custom_indicator,  # noqa: F401
    percent,  # noqa: F401
    fullscreen,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '默认情况下，加载动画会监听其内部的各个组件是否处于回调函数运算输出中状态，从而自动控制加载状态的切换。'
        ),
    },
    {
        'path': 'exclude_mode',
        'title': '排除监听模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('listenPropsMode="exclude"', code=True),
                '开启排除监听模式，该模式下加载动画将忽略监听参数',
                fac.AntdText('excludeProps', code=True),
                '所定义的组件属性更新过程。',
            ]
        ),
    },
    {
        'path': 'include_mode',
        'title': '包含监听模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('listenPropsMode="include"', code=True),
                '开启包含监听模式，该模式下加载动画将只监听参数',
                fac.AntdText('includeProps', code=True),
                '所定义的组件属性更新过程。',
            ]
        ),
    },
    {
        'path': 'custom_indicator',
        'title': '自定义加载动画',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('indicator', code=True),
                '自定义充当加载动画的元素。',
            ]
        ),
    },
    {
        'path': 'percent',
        'title': '环状进度动画',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('percent', code=True),
                '控制加载动画以环状进度图形式呈现。',
            ]
        ),
    },
    {
        'path': 'fullscreen',
        'title': '全屏加载动画',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('fullscreen=True', code=True),
                '启用全屏遮罩形式的加载动画。',
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
                        getattr(views.AntdSpin.demos, item['path']).render(),
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
                                views.AntdSpin.demos, item['path']
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
