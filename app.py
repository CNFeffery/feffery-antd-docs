import re
import os
import uuid
import time
import dash
from dash import dcc, html
from urllib.parse import unquote
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State, ClientsideFunction

import views
from views import (
    table_basic,
    table_advanced,
    table_server_side_mode,
    table_rerender
)
from config import Config
from utils import generate_shortcut_panel_data
from server import app, server

# 侧边菜单自动滚动动作基础参数
router_menu_scroll_params = dict(
    scrollMode='target',
    executeScroll=True,
    offset=-200,
    containerId='router-menu'
)

app.layout = fuc.FefferyTopProgress(
    html.Div(
        [
            # 注入url监听
            dcc.Location(id='url'),

            # 注入侧边菜单栏自动滚动至选中项动作挂载点
            html.Div(id='side-menu-scroll-to-current-key'),

            # 注入基于url中hash信息的页面锚点滚动效果
            html.Div(id='page-anchor-scroll-to-while-page-initial'),

            # 注入侧边参数说明栏展开像素宽度记忆
            dcc.Store(
                id='side-props-width',
                storage_type='local'
            ),

            # 注入快捷搜索面板
            fuc.FefferyShortcutPanel(
                placeholder='输入你想要搜索的组件...',
                data=generate_shortcut_panel_data(
                    Config.menuItems
                ),
                panelStyles={
                    'accentColor': '#1890ff',
                    'zIndex': 99999
                }
            ),

            # 注入快捷添加好友悬浮卡片
            html.Div(
                [
                    fac.AntdSpace(
                        [
                            fac.AntdTooltip(
                                fac.AntdButton(
                                    fac.AntdIcon(icon='antd-bug'),
                                    shape='circle',
                                    href='https://github.com/CNFeffery/feffery-antd-components/issues',
                                    target='_blank',
                                    style={
                                        'zoom': '1.25',
                                        'boxShadow': '0 3px 6px -4px #0000001f, 0 6px 16px #00000014, 0 9px 28px 8px #0000000d'
                                    }
                                ),
                                placement='left',
                                title='问题反馈'
                            ),

                            fac.AntdPopover(
                                fac.AntdButton(
                                    fac.AntdIcon(icon='antd-bulb'),
                                    shape='circle',
                                    style={
                                        'zoom': '1.25',
                                        'boxShadow': '0 3px 6px -4px #0000001f, 0 6px 16px #00000014, 0 9px 28px 8px #0000000d'
                                    }
                                ),
                                placement='left',
                                content=[
                                    fac.AntdText(
                                        '微信扫码加我好友，备注【dash学习】加入学习交流群，更多灵感更快进步',
                                        strong=True
                                    ),
                                    fac.AntdImage(
                                        src=app.get_asset_url(
                                            'imgs/feffery-添加好友二维码.jpg'),
                                        width=250,
                                        preview=False
                                    )
                                ],
                                overlayStyle={
                                    'width': '300px',
                                    'height': '408px'
                                }
                            )
                        ],
                        direction='vertical'
                    )
                ],
                style={
                    'position': 'fixed',
                    'right': '100px',
                    'bottom': '200px',
                    'zIndex': 999
                }
            ),

            # 注入内容区刷新辅助动画锚点
            fac.AntdSpin(
                html.Div(
                    id='docs-content-spin-center',
                    style={
                        'position': 'fixed'  # 强制脱离文档流
                    }
                ),
                indicator=fuc.FefferyExtraSpinner(
                    type='guard',
                    color='#1890ff',
                    style={
                        'position': 'fixed',
                        'top': '50%',
                        'left': '50%',
                        'width': 100,
                        'height': 100,
                        'transform': 'translate(-50%, -50%)',
                        'zIndex': 999
                    }
                )
            ),

            # 页面结构
            fac.AntdRow(
                [
                    fac.AntdCol(
                        fuc.FefferyMotion(
                            html.Img(
                                src=app.get_asset_url(
                                    'imgs/fac-logo.svg'
                                ),
                                style={
                                    'height': '50px',
                                    'padding': '0 10px',
                                    'marginTop': '7px',
                                    'cursor': 'pointer'
                                }
                            ),
                            whileTap={
                                'scale': 1.2
                            },
                            transition={
                                'duration': 0.5,
                                'type': 'spring'
                            }
                        ),
                    ),
                    fac.AntdCol(
                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    'feffery-antd-components',
                                    strong=True,
                                    style={
                                        'fontSize': '35px'
                                    }
                                ),
                                fac.AntdText(
                                    f'v{fac.__version__}',
                                    style={
                                        'fontSize': '10px',
                                        'paddingLeft': '2px'
                                    }
                                )
                            ]
                        )
                    ),
                    fac.AntdCol(
                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    'Ctrl',
                                    keyboard=True,
                                    style={
                                        'color': '#8c8c8c'
                                    }
                                ),
                                fac.AntdText(
                                    'K',
                                    keyboard=True,
                                    style={
                                        'color': '#8c8c8c'
                                    }
                                ),
                                fac.AntdText(
                                    '唤出搜索面板',
                                    style={
                                        'color': '#8c8c8c'
                                    }
                                )
                            ],
                            style={
                                'marginLeft': '50px',
                                'marginTop': '21px'
                            }
                        ),
                        flex='auto'
                    ),
                    fac.AntdCol(
                        html.Div(
                            [
                                html.A(
                                    fac.AntdImage(
                                        id='github-entry',
                                        alt='fac源码仓库，欢迎star',
                                        src='https://img.shields.io/github/stars/CNFeffery/feffery-antd-components?style=social',
                                        preview=False,
                                        fallback=None,
                                        style={
                                            'transform': 'translateY(0px) scale(1.25)'
                                        }
                                    ),
                                    href='https://github.com/CNFeffery/feffery-antd-components',
                                    target='_blank',
                                    style={
                                        'cursor': 'pointer'
                                    }
                                ),

                                html.A(
                                    '皖ICP备2021012734号-1',
                                    href='https://beian.miit.gov.cn/',
                                    target='_blank',
                                    style={
                                        'fontSize': '10px',
                                        'marginLeft': '50px',
                                        'color': '#494f54'
                                    }
                                )
                            ],
                            style={
                                'float': 'right',
                                'paddingRight': '20px',
                                'marginTop': '20.5px'
                            }
                        ),
                        flex='auto'
                    )
                ],
                align="middle",
                style={
                    'height': '64px',
                    'boxShadow': 'rgb(240 241 242) 0px 2px 14px',
                    'background': 'white',
                    'marginBottom': '5px'
                }
            ),

            fac.AntdRow(
                [
                    fac.AntdCol(
                        fac.AntdAffix(
                            html.Div(
                                [
                                    fac.AntdMenu(
                                        id='router-menu',
                                        menuItems=Config.menuItems,
                                        mode='inline',
                                        defaultOpenKeys=Config.side_menu_open_keys,
                                        style={
                                            'height': '100%',
                                            'paddingBottom': '50px'
                                        }
                                    ),

                                    fac.AntdButton(
                                        fac.AntdIcon(
                                            id='fold-side-menu-icon',
                                            icon='antd-arrow-left'
                                        ),
                                        id='fold-side-menu',
                                        type='text',
                                        shape='circle',
                                        style={
                                            'position': 'absolute',
                                            'zIndex': 999,
                                            'top': '10px',
                                            'right': '-15px',
                                            'boxShadow': '0 4px 10px 0 rgba(0,0,0,.1)',
                                            'background': 'white'
                                        }
                                    )
                                ],
                                id='side-menu',
                                style={
                                    'width': '325px',
                                    'height': '100vh',
                                    'transition': 'width 0.2s',
                                    'borderRight': '1px solid rgb(240, 240, 240)',
                                    'paddingRight': 20
                                }
                            ),
                            offsetTop=0
                        ),
                        flex='none'
                    ),

                    fac.AntdCol(
                        [
                            fuc.FefferyDiv(
                                html.Div(
                                    style={
                                        'minHeight': '100vh'
                                    }
                                ),
                                id='docs-content',
                                style={
                                    'backgroundColor': 'rgb(255, 255, 255)'
                                }
                            ),

                            # 页尾信息
                            fac.AntdSpace(
                                [
                                    fac.AntdTitle(
                                        '更多组件库',
                                        level=4,
                                        style={
                                            'color': '#1d1e1e',
                                            'fontWeight': 'normal'
                                        }
                                    ),
                                    fac.AntdSpace(
                                        [
                                            html.A(
                                                'fuc: 实用工具组件库',
                                                href='https://fuc.feffery.tech/',
                                                target='_blank',
                                                className='more-components-link'
                                            ),
                                            html.A(
                                                'fmc: markdown渲染组件库',
                                                href='https://fmc.feffery.tech/',
                                                target='_blank',
                                                className='more-components-link'
                                            ),
                                            # html.A(
                                            #     'fact: 图表可视化组件库',
                                            #     href='https://fact.feffery.tech/',
                                            #     target='_blank',
                                            #     className='more-components-link'
                                            # ),
                                            # html.A(
                                            #     'flc: 交互式地图组件库',
                                            #     href='https://flc.feffery.tech/',
                                            #     target='_blank',
                                            #     className='more-components-link'
                                            # ),
                                        ],
                                        direction='vertical',
                                        style={
                                            'marginBottom': '75px'
                                        }
                                    ),
                                    'Made with ❤ by CNFeffery'
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%',
                                    'background': '#f2f3f5',
                                    'padding': '50px 75px',
                                    'color': '#868e96',
                                    'boxShadow': 'inset 0 106px 36px -116px rgb(0 0 0 / 14%)'
                                }
                            )
                        ],
                        flex='auto'
                    ),

                    fac.AntdBackTop(
                        duration=0.5
                    )
                ],
                wrap=False
            )
        ]
    ),
    listenPropsMode='include',
    includeProps=Config.include_props,
    minimum=0.33,
    speed=800,
    debug=True
)


@app.callback(
    [Output('docs-content', 'children'),
     Output('docs-content-spin-center', 'key')],
    Input('url', 'pathname')
)
def render_docs_content(pathname):
    '''
    路由回调
    '''

    if pathname == '/what-is-fac' or pathname == '/':
        return [
            views.what_is_fac.docs_content,
            str(uuid.uuid4())
        ]

    elif pathname == '/getting-started':
        return [
            views.getting_started.docs_content,
            str(uuid.uuid4())
        ]

    elif pathname == '/advanced-classname':
        return [
            views.advanced_classname.docs_content,
            str(uuid.uuid4())
        ]

    elif pathname == '/popup-container':
        return [
            views.popup_container.docs_content,
            str(uuid.uuid4())
        ]

    elif pathname == '/internationalization':
        return [
            views.internationalization.docs_content,
            str(uuid.uuid4())
        ]

    elif pathname == '/prop-persistence':
        return [
            views.prop_persistence.docs_content,
            str(uuid.uuid4())
        ]

    elif pathname == '/use-key-to-refresh':
        return [
            views.use_key_to_refresh.docs_content,
            str(uuid.uuid4())
        ]

    # 若访问更新日志相关页面
    elif (
        re.fullmatch('/change-log-v\d+\.\d+\.\d+', pathname) and
        pathname[1:]+'.md' in os.listdir('./change_logs')
    ):
        return [
            views.generate_change_logs.genarate_layout(
                pathname
            ),
            str(uuid.uuid4())
        ]

    # 检查当前pathname是否在预设字典中
    elif pathname in Config.key2open_keys.keys():

        # 复杂内容渲染效果优化
        time.sleep(0.5)

        # 检查当前目标pathname中是否包含AntdTable
        if 'AntdTable' in pathname:

            if pathname == '/AntdTable-basic':

                return [
                    table_basic.docs_content,
                    str(uuid.uuid4())
                ]

            elif pathname == '/AntdTable-advanced':

                return [
                    table_advanced.docs_content,
                    str(uuid.uuid4())
                ]

            elif pathname == '/AntdTable-server-side-mode':

                return [
                    table_server_side_mode.docs_content,
                    str(uuid.uuid4())
                ]

            elif pathname == '/AntdTable-rerender':

                return [
                    table_rerender.docs_content,
                    str(uuid.uuid4())
                ]

        try:

            return [
                getattr(views, pathname[1:]).docs_content,
                str(uuid.uuid4())
            ]

        except Exception as e:

            pass

    return [
        fac.AntdResult(
            status='404',
            title='您访问的页面不存在或还在建设中',
            style={
                'height': 'calc(100vh - 65px)'
            }
        ),
        str(uuid.uuid4())
    ]


@app.callback(
    [Output('router-menu', 'currentKey'),
     Output('router-menu', 'openKeys'),
     Output('side-menu-scroll-to-current-key', 'children')],
    Input('url', 'pathname')
)
def handle_other_router_interaction(pathname):
    '''
    路由相关的交互效果优化
    '''

    if pathname == '/what-is-fac' or pathname == '/':
        return [
            '/what-is-fac',
            dash.no_update,
            None
        ]

    elif pathname == '/getting-started':
        return [
            '/getting-started',
            dash.no_update,
            None
        ]

    elif (
        pathname in [
            '/advanced-classname',
            '/popup-container',
            '/internationalization',
            '/prop-persistence',
            '/use-key-to-refresh'
        ]
    ):
        return [
            pathname,
            dash.no_update,
            fuc.FefferyScroll(
                scrollTargetId=pathname,
                **router_menu_scroll_params
            )
        ]

    elif (
        re.fullmatch('/change-log-v\d+\.\d+\.\d+', pathname) and
        pathname[1:]+'.md' in os.listdir('./change_logs')
    ):
        return [
            pathname,
            [re.findall('(v\d+\.\d+\.)', pathname)[0]+'x'],
            fuc.FefferyScroll(
                scrollTargetId=pathname,
                **router_menu_scroll_params
            )
        ]

    # 检查当前pathname是否在预设字典中
    elif pathname in Config.key2open_keys.keys():

        return [
            pathname,
            Config.key2open_keys[pathname],
            fuc.FefferyScroll(
                scrollTargetId=pathname,
                **router_menu_scroll_params
            )
        ]

    return [
        pathname,
        dash.no_update,
        None
    ]


@app.callback(
    Output('page-anchor-scroll-to-while-page-initial', 'children'),
    Input('docs-content-spin-center', 'key'),
    State('url', 'hash')
)
def page_anchor_scroll_to_while_page_initial(_, hash_):

    if _ and hash_:

        return fuc.FefferyScroll(
            scrollTargetId=unquote(hash_)[1:],
            scrollMode='target',
            executeScroll=True,
            offset=0
        )


app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='handleSideMenuCollapse'
    ),
    [Output('side-menu', 'style'),
     Output('fold-side-menu-icon', 'icon')],
    Input('fold-side-menu', 'nClicks'),
    State('side-menu', 'style')
)


app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='handleSidePropsCollapse'
    ),
    [Output('side-props', 'style'),
     Output('fold-side-props-icon', 'icon')],
    Input('fold-side-props', 'nClicks'),
    Input('side-props-width', 'data'),
    State('side-props', 'style')
)


app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='handleSidePropsResize'
    ),
    [Output('side-props-width', 'data'),
     Output('side-props-width-plus', 'disabled'),
     Output('side-props-width-minus', 'disabled')],
    [Input('side-props-width-plus', 'nClicks'),
     Input('side-props-width-minus', 'nClicks')],
    State('side-props-width', 'data')
)

if __name__ == '__main__':
    app.run(debug=True)
