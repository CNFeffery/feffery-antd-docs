import dash
from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc

from config import AppConfig

# 国际化
from i18n import translator


def render(locale: str = 'zh-cn'):
    """渲染页首"""

    return fac.AntdRow(
        [
            # 文档页面响应式监听
            fuc.FefferyResponsive(id='page-header-responsive'),
            fac.AntdCol(
                fac.AntdSpace(
                    [
                        dcc.Link(
                            html.Img(
                                src=dash.get_asset_url(AppConfig.logo_path),
                                height=48,
                            ),
                            href='/',
                        ),
                        html.Div(
                            style={
                                'width': 1,
                                'height': 24,
                                'backgroundColor': '#ccc',
                                'margin': '0 12px',
                            }
                        ),
                        fac.AntdSpace(
                            [
                                fac.AntdText(
                                    AppConfig.page_header_title,
                                    style={
                                        'color': '#000000d9',
                                        'fontWeight': 500,
                                        'fontSize': 28,
                                    },
                                ),
                                fac.AntdText(
                                    'v' + AppConfig.library_version,
                                    style={'fontSize': 12},
                                ),
                            ],
                            size=4,
                            align='end',
                        ),
                        html.Div(
                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        'Ctrl',
                                        keyboard=True,
                                        style={'color': '#8c8c8c'},
                                    ),
                                    fac.AntdText(
                                        'K',
                                        keyboard=True,
                                        style={'color': '#8c8c8c'},
                                    ),
                                    fac.AntdText(
                                        translator.t('唤出搜索面板'),
                                        style={'color': '#8c8c8c'},
                                    ),
                                ],
                                style={'margin': '0 0 0 16px'},
                            ),
                            id='open-global-search-panel',
                            style={'cursor': 'pointer'},
                        ),
                    ],
                    style={'height': '100%'},
                ),
                id='doc-layout-header-standard-col1',
                style={'display': 'none'},
            ),
            fac.AntdCol(
                fac.AntdSpace(
                    [
                        fac.AntdTooltip(
                            fac.AntdButton(
                                id='global-locale-switch',
                                icon=fac.AntdIcon(
                                    icon='md-translate',
                                    style={
                                        'fontSize': 18,
                                        'verticalAlign': '-0.4em',
                                    },
                                ),
                                type='text',
                                clickExecuteJsString=(
                                    """
window.dash_clientside.set_props('global-locale', { value: '%s' })
window.dash_clientside.set_props('global-reload', { reload: true })
"""
                                    % (
                                        'zh-cn'
                                        if locale == 'en-us'
                                        else 'en-us'
                                    )
                                ),
                            ),
                            placement='bottom',
                            title=translator.t('English / 中文'),
                        ),
                        html.Div(
                            style={
                                'width': 1,
                                'height': 10,
                                'backgroundColor': '#ccc',
                                'marginRight': 22,
                            }
                        ),
                        html.A(
                            fac.AntdImage(
                                src='https://img.shields.io/github/stars/{}/{}?style=social'.format(
                                    *AppConfig.library_repo.split('/')[-2:]
                                ),
                                preview=False,
                                fallback='/assets/imgs/fac-github.svg',
                                style={
                                    'transform': 'translateY(-2px) scale(1.25)'
                                },
                            ),
                            href=AppConfig.library_repo,
                            target='_blank',
                            style={'cursor': 'pointer'},
                        ),
                        html.A(
                            '皖ICP备2021012734号-1',
                            id='icp-info',
                            href='https://beian.miit.gov.cn/',
                            target='_blank',
                            style={
                                'fontSize': '10px',
                                'marginLeft': '42px',
                                'color': '#494f54',
                                'display': (
                                    'block' if locale == 'zh-cn' else 'none'
                                ),
                            },
                        ),
                    ],
                    align='center',
                    style={'height': '100%'},
                ),
                id='doc-layout-header-standard-col2',
                style={'display': 'none'},
            ),
            fac.AntdCol(
                fac.AntdCenter(
                    fac.AntdText(
                        AppConfig.page_header_title,
                        style={
                            'color': '#000000d9',
                            'fontWeight': 500,
                            'fontSize': 'calc(min(4vw, 32px))',
                        },
                    ),
                    style={'height': '100%'},
                ),
                id='doc-layout-header-standard-col3',
                span=24,
                style={'display': 'none'},
            ),
        ],
        justify='space-between',
        wrap=False,
        style={
            'height': 64,
            'boxShadow': '0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
            'paddingLeft': 32,
            'paddingRight': 32,
            'position': 'sticky',
            'top': 0,
            'zIndex': 1000,
            'background': '#fff',
        },
    )
