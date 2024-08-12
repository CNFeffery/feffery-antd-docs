from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    primary_color,  # noqa: F401
    disabled,  # noqa: F401
    size,  # noqa: F401
    locale,  # noqa: F401
    algorithm,  # noqa: F401
    waves_disabled,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'primary_color',
        'title': '主题色配置',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('primaryColor', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部元素的主题色进行快捷设置。',
            ]
        ),
    },
    {
        'path': 'disabled',
        'title': '禁用状态配置',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('componentDisabled', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素的禁用状态进行快捷设置。',
            ]
        ),
    },
    {
        'path': 'size',
        'title': '尺寸规格配置',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('componentSize', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素的尺寸规格进行快捷设置。',
            ]
        ),
    },
    {
        'path': 'locale',
        'title': '国际化配置',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('locale', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素的国际化语种进行快捷切换。',
            ]
        ),
    },
    {
        'path': 'algorithm',
        'title': '使用主题样式算法',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('algorithm', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素应用内置的主题样式算法。',
            ]
        ),
    },
    {
        'path': 'waves_disabled',
        'title': '禁用水波纹动效',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('wavesDisabled=True', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素的水波纹交互动效进行禁用，典型如',
                fac.AntdText('AntdButton', strong=True),
                '。',
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
                            views.AntdConfigProvider.demos, item['path']
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
                                views.AntdConfigProvider.demos, item['path']
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
