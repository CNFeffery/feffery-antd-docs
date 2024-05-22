import uuid
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
from dash.dependencies import Component

import utils


def render(
    component: Component, intro: Component, demos: Component, catalog: list
) -> Component:
    """渲染组件文档页"""

    return fac.AntdRow(
        [
            fac.AntdCol(
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            [
                                # 组件介绍
                                fac.Fragment(intro),
                                # 组件使用示例
                                fac.Fragment(demos),
                                # 通用页尾信息
                                fac.AntdSpace(
                                    [
                                        fac.AntdTitle(
                                            '更多组件库',
                                            level=4,
                                            style={
                                                'color': '#1d1e1e',
                                                'fontWeight': 'normal',
                                            },
                                        ),
                                        fac.AntdSpace(
                                            [
                                                html.A(
                                                    'fuc: 实用工具组件库',
                                                    href='https://fuc.feffery.tech/',
                                                    target='_blank',
                                                    className='more-components-link',
                                                ),
                                                html.A(
                                                    'fmc: markdown渲染组件库',
                                                    href='https://fmc.feffery.tech/',
                                                    target='_blank',
                                                    className='more-components-link',
                                                ),
                                            ],
                                            direction='vertical',
                                            style={'marginBottom': '75px'},
                                        ),
                                        'Made with ❤ by CNFeffery',
                                    ],
                                    direction='vertical',
                                    style={
                                        'display': 'block',
                                        'background': '#f2f3f5',
                                        'padding': '50px 75px',
                                        'color': '#868e96',
                                        'boxShadow': 'inset 0 106px 36px -116px rgb(0 0 0 / 14%)',
                                        'marginTop': 32,
                                    },
                                ),
                            ],
                            flex='auto',
                        ),
                        fac.AntdCol(
                            fac.AntdAnchor(
                                linkDict=[
                                    {
                                        'title': item['title'],
                                        'href': '#'
                                        + 'demo-container-'
                                        + item['path'],
                                    }
                                    for item in catalog
                                ],
                                id='doc-anchor',
                                offsetTop=64.1,
                                style={'width': 150},
                            ),
                            flex='none',
                        ),
                    ],
                    wrap=False,
                    gutter=8,
                ),
                flex='auto',
                style={'padding': '30px 30px 0 0', 'minWidth': 0},
            ),
            fac.AntdCol(
                fac.AntdAffix(
                    fuc.FefferyDiv(
                        [
                            fac.AntdRow(
                                [
                                    fac.AntdCol(
                                        fac.AntdText(
                                            f'{component.__name__} API参数说明',
                                            style={
                                                'color': 'white',
                                                'background': '#1890ff',
                                                'fontSize': 18,
                                                'padding': '5px 8px 5px 15px',
                                            },
                                        )
                                    ),
                                    fac.AntdCol(
                                        fac.AntdSpace(
                                            [
                                                fac.AntdIcon(
                                                    id='side-props-search-bar-toggle',
                                                    icon='antd-search',
                                                    style={
                                                        'cursor': 'pointer',
                                                        'color': '#777777',
                                                        'fontSize': 16,
                                                    },
                                                )
                                            ],
                                            style={'paddingRight': 8},
                                        )
                                    ),
                                    fac.AntdCol(
                                        fac.AntdConfigProvider(
                                            fac.AntdInput(
                                                id='side-props-search-bar-keyword',
                                                placeholder='请输入搜索关键词',
                                                variant='filled',
                                                debounceWait=200,
                                                allowClear=True,
                                                autoComplete='off',
                                                style={'width': '100%'},
                                            ),
                                            token={'borderRadius': 0},
                                        ),
                                        id='side-props-search-bar',
                                        span=24,
                                        style={
                                            'paddingTop': 3,
                                            'display': 'none',
                                        },
                                    ),
                                ],
                                justify='space-between',
                                align='middle',
                                style={
                                    'position': 'absolute',
                                    'zIndex': 999,
                                    'top': 0,
                                    'left': 20,
                                    'right': 20,
                                    'background': 'white',
                                    'boxShadow': '0 4px 10px 0 rgba(0, 0, 0, .1)',
                                },
                            ),
                            fuc.FefferyDiv(
                                [
                                    fmc.FefferyMarkdown(
                                        id='side-props-markdown',
                                        markdownStr=utils.parse_component_props(
                                            component=component
                                        ),
                                        style={'paddingBottom': 56},
                                    ),
                                ],
                                scrollbar='simple',
                                style={
                                    'height': 'calc(100vh - 64px)',
                                    'overflowY': 'auto',
                                    'background': 'white',
                                    'paddingTop': 56,
                                },
                            ),
                            fac.AntdButton(
                                fac.AntdIcon(
                                    id='toggle-side-props-visible-icon',
                                    icon='antd-arrow-right',
                                ),
                                id='toggle-side-props-visible',
                                type='text',
                                shape='circle',
                                style={
                                    'position': 'absolute',
                                    'zIndex': 999,
                                    'top': '10px',
                                    'left': '-15px',
                                    'boxShadow': '0 4px 10px 0 rgba(0, 0, 0, .1)',
                                    'background': 'white',
                                },
                            ),
                            fac.AntdButton(
                                fac.AntdIcon(
                                    id='toggle-doc-anchor-visible-icon',
                                    icon='antd-menu-unfold',
                                ),
                                id='toggle-doc-anchor-visible',
                                type='text',
                                shape='circle',
                                style={
                                    'position': 'absolute',
                                    'zIndex': 999,
                                    'top': '55px',
                                    'left': '-15px',
                                    'boxShadow': '0 4px 10px 0 rgba(0, 0, 0, .1)',
                                    'background': 'white',
                                },
                            ),
                        ],
                        style={
                            'padding': '0px 20px',
                            'position': 'relative',
                            'background': '#f2f3f5',
                        },
                    ),
                    id='side-props',
                    offsetTop=64.1,
                    style={'width': 500},
                ),
                flex='none',
            ),
            fac.AntdBackTop(duration=0.5),
        ],
        key=str(uuid.uuid4()),  # 强制刷新
        wrap=False,
    )