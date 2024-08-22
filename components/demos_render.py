from dash import html, dcc
from typing import Callable, Union
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from config import AppConfig
from components import mock_browser
from utils.doc_renderer import MarkdownRenderer

# 国际化
from i18n import translator

description_renderer = MarkdownRenderer()


def render(
    component: Component,
    demos_config: Union[list, Callable],
    section_name: str = None,
) -> Component:
    """渲染组件文档页示例内容"""

    # 处理函数型demos_config
    if not isinstance(demos_config, list):
        demos_config = demos_config()

    return fac.AntdSpace(
        [
            html.Div(
                [
                    html.Div(
                        (
                            fac.AntdSpace(
                                [
                                    mock_browser.render(),
                                    # 懒加载优化
                                    fuc.FefferyLazyLoad(
                                        html.Iframe(
                                            src='/~demo/{}/{}{}'.format(
                                                component.__name__,
                                                demo['path'],
                                                '?'
                                                + '&'.join(
                                                    [
                                                        '{}={}'.format(k, v)
                                                        for k, v in demo.get(
                                                            'query'
                                                        ).items()
                                                    ]
                                                )
                                                if demo.get('query')
                                                and isinstance(
                                                    demo.get('query'), dict
                                                )
                                                else '',
                                            ),
                                            style={
                                                'border': '1px solid #f0f0f0',
                                                'boxSizing': 'border-box',
                                                'width': '100%',
                                                'height': 350,
                                            },
                                        ),
                                        height=350,
                                        throttle=500,
                                    ),
                                ],
                                direction='vertical',
                                size=0,
                                style={'width': '100%'},
                            )
                            if demo.get('iframe')
                            else getattr(
                                getattr(
                                    views, section_name or component.__name__
                                ).demos,
                                demo['path'],
                            ).render()
                        ),
                        className='demo-box',
                    ),
                    html.Div(
                        [
                            fac.AntdText(
                                [
                                    demo['title'],
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
                                                demo['path'],
                                            ),
                                            target='_blank',
                                        ),
                                        title=translator.t(
                                            '在Github上编辑此示例'
                                        ),
                                    ),
                                ],
                                className='demo-title',
                            ),
                            html.Div(
                                (
                                    demo['description']
                                    if isinstance(
                                        demo['description'], Component
                                    )
                                    else description_renderer.render(
                                        demo['description']
                                    )
                                    if isinstance(demo['description'], str)
                                    else None
                                ),
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
                                        href='/~demo/{}/{}{}'.format(
                                            section_name or component.__name__,
                                            demo['path'],
                                            '?'
                                            + '&'.join(
                                                [
                                                    '{}={}'.format(k, v)
                                                    for k, v in demo.get(
                                                        'query'
                                                    ).items()
                                                ]
                                            )
                                            if demo.get('query')
                                            and isinstance(
                                                demo.get('query'), dict
                                            )
                                            else '',
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title=translator.t('在新窗口打开'),
                                ),
                                fac.AntdTooltip(
                                    fac.AntdIcon(
                                        id={
                                            'type': 'demo-code-toggle',
                                            'index': '{}/{}'.format(
                                                component.__name__,
                                                demo['path'],
                                            ),
                                        },
                                        icon='antd-code',
                                        className='demo-operations-icon',
                                    ),
                                    title=translator.t('展开/收起代码'),
                                ),
                                fac.AntdTooltip(
                                    dcc.Link(
                                        fac.AntdIcon(icon='antd-github'),
                                        href='{}/tree/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_library_repo,
                                            AppConfig.doc_library_branch,
                                            section_name or component.__name__,
                                            demo['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title=translator.t(
                                        '在Github中查看完整代码'
                                    ),
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
                                            section_name or component.__name__,
                                            demo['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title=translator.t('在Gitee中查看完整代码'),
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
                            # 兼容处理不同类型的code_string
                            for item in (
                                lambda code_string: code_string
                                if isinstance(code_string, list)
                                else code_string()
                            )(
                                (
                                    getattr(
                                        getattr(
                                            views,
                                            section_name or component.__name__,
                                        ).demos,
                                        demo['path'],
                                    ).code_string
                                )
                            )
                        ],
                        centered=True,
                        className='demo-code-tabs',
                        id={
                            'type': 'demo-code',
                            'index': '{}/{}'.format(
                                component.__name__, demo['path']
                            ),
                        },
                        style={'display': 'none'},
                    ),
                ],
                className='demo-container',
                id='demo-container-' + demo['path'],
            )
            for demo in demos_config
        ],
        direction='vertical',
        size='large',
        style={'width': '100%'},
    )
