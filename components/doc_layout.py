import uuid
from dash import html, dcc
from typing import Callable, Union
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
from dash.dependencies import Component

import utils
from config import AppConfig, DocsConfig
from components import contributors_avatar
from utils.doc_renderer import MarkdownRenderer

# 国际化
from i18n import translator, get_current_locale

markdown_renderer = MarkdownRenderer()


def render(
    component: Component,
    intro: Component,
    demos: Component,
    catalog: Union[list, Callable] = None,
    section_name: str = None,
) -> Component:
    """渲染组件文档页"""

    # 待国际化翻译文档页提示信息
    i18n_modal = None

    # 处理函数型catalog
    if not isinstance(catalog, list) and catalog:
        catalog = catalog()
    elif catalog and get_current_locale() == 'en-us':
        # 若当前文档页尚未翻译完成，则更新相应的参与翻译贡献提示信息
        i18n_modal = fac.AntdModal(
            markdown_renderer.render(
                'The **English** version of the current component documentation page has not been completed yet. If you are interested in participating in the **English translation** of this document, please read the [Contribution Guide](%s).'
                % AppConfig.i18n_guide_link
            ),
            title='Notice',
            transitionType='fade',
            visible=True,
            width=600,
        )

    return fac.AntdRow(
        [
            # 文档页面响应式监听
            fuc.FefferyResponsive(id='doc-layout-responsive'),
            # 按键esc点击监听
            fuc.FefferyKeyPress(id='doc-layout-listen-esc-press', keys='esc'),
            # 文档初始化锚点滚动
            fuc.FefferyExecuteJs(
                jsString="""
setTimeout(() => {
    if ( window.location.hash ) {
        let hashTarget = window.location.hash.substring(1)
        let scrollTarget = document.getElementById(hashTarget)
        if ( scrollTarget ) {
            window.location.hash = '';
            window.location.hash = '#' + hashTarget;
            window.scrollBy(0, -80);
        }
    }
}, 500)
"""
            ),
            fac.AntdCol(
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            [
                                # 组件介绍
                                fac.Fragment(intro),
                                # 文档贡献者
                                contributors_avatar.render(
                                    component=component,
                                    section_name=section_name,
                                ),
                                # 组件使用示例
                                fac.Fragment(demos),
                                # 通用页尾信息
                                fac.AntdSpace(
                                    [
                                        fac.AntdTitle(
                                            translator.t('更多组件库'),
                                            level=4,
                                            style={
                                                'color': '#1d1e1e',
                                                'fontWeight': 'normal',
                                            },
                                        ),
                                        fac.AntdSpace(
                                            [
                                                html.A(
                                                    translator.t(
                                                        'fact: 数据可视化组件库'
                                                    ),
                                                    href='https://fact.feffery.tech/',
                                                    target='_blank',
                                                    className='more-components-link',
                                                ),
                                                html.A(
                                                    translator.t(
                                                        'fuc: 实用工具组件库'
                                                    ),
                                                    href='https://fuc.feffery.tech/',
                                                    target='_blank',
                                                    className='more-components-link',
                                                ),
                                                html.A(
                                                    translator.t(
                                                        'fmc: markdown渲染组件库'
                                                    ),
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
                        # 组件文档页侧边示例目录
                        (
                            fac.AntdCol(
                                fac.AntdAnchor(
                                    linkDict=utils.get_doc_anchor_link_dict(
                                        catalog
                                    ),
                                    id='doc-anchor',
                                    className='light-scroll-bar',
                                    offsetTop=70,
                                    style={
                                        'width': 150,
                                        'height': 'calc(100vh - 64px)',
                                        'overflowY': 'auto',
                                    },
                                ),
                                id='doc-anchor-col',
                                flex='none',
                            )
                            if catalog
                            else None
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
                                            f'{component.__name__} '
                                            + translator.t('API参数说明'),
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
                                                placeholder=translator.t(
                                                    '请输入搜索关键词'
                                                ),
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
                                    'right': 6,
                                    'background': 'white',
                                    'boxShadow': '0 4px 10px 0 rgba(0, 0, 0, .1)',
                                },
                            ),
                            fuc.FefferyDiv(
                                [
                                    # 关键词搜索状态存储
                                    dcc.Store(
                                        id='side-props-markdown-search-status'
                                    ),
                                    # 针对部分特殊组件渲染额外API说明文档
                                    *(
                                        fac.AntdCollapse(
                                            fmc.FefferyMarkdown(
                                                id='side-props-extra-markdown',
                                                markdownStr=utils.get_extra_api_descriptions(
                                                    component
                                                ),
                                                style={
                                                    'paddingLeft': 12,
                                                    'paddingRight': 12,
                                                },
                                            ),
                                            title=translator.t('特殊参数说明'),
                                            ghost=True,
                                            isOpen=False,
                                            className='tip-collapse',
                                        )
                                        # 若当前组件具有额外API说明文档
                                        if (
                                            component.__name__
                                            in DocsConfig.components_with_extra_params
                                        )
                                        else None,
                                    ),
                                    fmc.FefferyMarkdown(
                                        id='side-props-markdown',
                                        markdownStr=utils.parse_component_props(
                                            component=component
                                        ),
                                        highlightClassName='side-props-keyword-highlight',
                                        style={'paddingBottom': 56},
                                    ),
                                ],
                                id='side-props-markdown-container',
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
                            (
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
                                )
                                if catalog
                                else None
                            ),
                        ],
                        style={
                            'padding': '0px 0px 0px 20px',
                            'position': 'relative',
                            'background': 'white',
                            'borderLeft': '1px solid #e9ecef',
                        },
                    ),
                    id='side-props',
                    offsetTop=64.1,
                    style={'width': 500},
                ),
                flex='none',
            ),
            fac.AntdBackTop(id='doc-layout-back-top', duration=0.5),
            i18n_modal,
        ],
        key=str(uuid.uuid4()),  # 强制刷新
        wrap=False,
    )
