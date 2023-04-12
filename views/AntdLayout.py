from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdLayout
from .side_props import render_side_props_layout

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(
                    duration=0.3
                ),

                fac.AntdBreadcrumb(
                    items=[
                        {
                            'title': '组件介绍'
                        },
                        {
                            'title': '布局'
                        },
                        {
                            'title': '经典布局'
                        },
                        {
                            'title': 'AntdLayout 布局容器'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在经典布局方案中作为容器。')
                    ]
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdLayout(
                                    [
                                        fac.AntdHeader(
                                            fac.AntdTitle(
                                                '页首示例',
                                                level=2,
                                                style={
                                                    'color': 'white',
                                                    'margin': '0'
                                                }
                                            ),
                                            style={
                                                'display': 'flex',
                                                'justifyContent': 'center',
                                                'alignItems': 'center'
                                            }
                                        ),
                                        fac.AntdLayout(
                                            [
                                                fac.AntdSider(
                                                    html.Div(
                                                        fac.AntdTitle(
                                                            '侧边栏示例',
                                                            level=2,
                                                            style={
                                                                'margin': '0'
                                                            }
                                                        ),
                                                        style={
                                                            'alignItems': 'center',
                                                            'display': 'flex',
                                                            'height': '100%'
                                                        }
                                                    ),
                                                    style={
                                                        'backgroundColor': 'rgb(240, 242, 245)',
                                                        'display': 'flex',
                                                        'justifyContent': 'center'
                                                    }
                                                ),
                                                fac.AntdLayout(
                                                    [
                                                        fac.AntdContent(
                                                            html.Div(
                                                                fac.AntdTitle(
                                                                    '内容区示例',
                                                                    level=2,
                                                                    style={
                                                                        'margin': '0'
                                                                    }
                                                                ),
                                                                style={
                                                                    'display': 'flex',
                                                                    'height': '100%',
                                                                    'justifyContent': 'center',
                                                                    'alignItems': 'center'
                                                                }
                                                            ),
                                                            style={
                                                                'backgroundColor': 'white'
                                                            }
                                                        ),
                                                        fac.AntdFooter(
                                                            html.Div(
                                                                fac.AntdTitle(
                                                                    '页尾示例',
                                                                    level=2,
                                                                    style={
                                                                        'margin': '0'
                                                                    }
                                                                ),
                                                                style={
                                                                    'display': 'flex',
                                                                    'height': '100%',
                                                                    'justifyContent': 'center',
                                                                    'alignItems': 'center'
                                                                }
                                                            ),
                                                            style={
                                                                'backgroundColor': 'rgb(193, 193, 193)',
                                                                'height': '40px'
                                                            }
                                                        )
                                                    ]
                                                )
                                            ],
                                            style={
                                                'height': '536px'
                                            }
                                        )
                                    ]
                                )
                            ],
                            style={
                                'height': '600px',
                                'border': '1px solid rgb(241, 241, 241)'
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '经典布局方案的重点在于用',
                                fac.AntdText(
                                    'AntdLayout',
                                    strong=True
                                ),
                                '包裹嵌套其他经典布局组件，从而构建出常用的各种经典页面布局方案'
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    [
        fac.AntdLayout(
            [
                fac.AntdHeader(
                    fac.AntdTitle(
                        '页首示例',
                        level=2,
                        style={
                            'color': 'white',
                            'margin': '0'
                        }
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center'
                    }
                ),
                fac.AntdLayout(
                    [
                        fac.AntdSider(
                            html.Div(
                                fac.AntdTitle(
                                    '侧边栏示例',
                                    level=2,
                                    style={
                                        'margin': '0'
                                    }
                                ),
                                style={
                                    'alignItems': 'center',
                                    'display': 'flex',
                                    'height': '100%'
                                }
                            ),
                            style={
                                'backgroundColor': 'rgb(240, 242, 245)',
                                'display': 'flex',
                                'justifyContent': 'center'
                            }
                        ),
                        fac.AntdLayout(
                            [
                                fac.AntdContent(
                                    html.Div(
                                        fac.AntdTitle(
                                            '内容区示例',
                                            level=2,
                                            style={
                                                'margin': '0'
                                            }
                                        ),
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    style={
                                        'backgroundColor': 'white'
                                    }
                                ),
                                fac.AntdFooter(
                                    html.Div(
                                        fac.AntdTitle(
                                            '页尾示例',
                                            level=2,
                                            style={
                                                'margin': '0'
                                            }
                                        ),
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    style={
                                        'backgroundColor': 'rgb(193, 193, 193)',
                                        'height': '40px'
                                    }
                                )
                            ]
                        )
                    ],
                    style={
                        'height': '536px'
                    }
                )
            ]
        )
    ],
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
    }
)
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdLayout(
                                    [
                                        fac.AntdContent(
                                            html.Div(
                                                fac.AntdTitle(
                                                    '内容区示例',
                                                    level=2,
                                                    style={
                                                        'margin': '0'
                                                    }
                                                ),
                                                style={
                                                    'display': 'flex',
                                                    'height': '100%',
                                                    'justifyContent': 'center',
                                                    'alignItems': 'center'
                                                }
                                            ),
                                            style={
                                                'backgroundColor': 'white'
                                            }
                                        ),

                                        fac.AntdSider(
                                            html.Div(
                                                fac.AntdTitle(
                                                    '右侧侧边栏',
                                                    level=2,
                                                    style={
                                                        'margin': '0'
                                                    }
                                                ),
                                                style={
                                                    'display': 'flex',
                                                    'height': '100%',
                                                    'justifyContent': 'center',
                                                    'alignItems': 'center'
                                                }
                                            ),
                                            style={
                                                'backgroundColor': 'rgb(240, 242, 245)'
                                            }
                                        )
                                    ],
                                    style={
                                        'height': '600px'
                                    }
                                )
                            ],
                            style={
                                'height': '600px',
                                'border': '1px solid rgb(241, 241, 241)'
                            }
                        ),

                        fac.AntdDivider(
                            '右侧侧边栏',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    [
        fac.AntdLayout(
            [
                fac.AntdContent(
                    html.Div(
                        fac.AntdTitle(
                            '内容区示例',
                            level=2,
                            style={
                                'margin': '0'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'height': '100%',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    style={
                        'backgroundColor': 'white'
                    }
                ),

                fac.AntdSider(
                    html.Div(
                        fac.AntdTitle(
                            '右侧侧边栏',
                            level=2,
                            style={
                                'margin': '0'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'height': '100%',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    style={
                        'backgroundColor': 'rgb(240, 242, 245)'
                    }
                )
            ],
            style={
                'height': '600px'
            }
        )
    ],
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
    }
)
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='右侧侧边栏',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        # 侧边栏自带折叠触发区域默认会紧贴页面下边界
                        # 这里为方便局部展示示例，基于fuc.FefferyStyle强制覆盖默认样式
                        fuc.FefferyStyle(
                            rawStyle='''
.sider-demo .ant-layout-sider-trigger {
  position: absolute !important;
}
'''
                        ),

                        html.Div(
                            [
                                fac.AntdLayout(
                                    [
                                        fac.AntdSider(
                                            collapsible=True,
                                            style={
                                                'backgroundColor': 'rgb(240, 242, 245)'
                                            }
                                        ),

                                        fac.AntdContent(
                                            html.Div(
                                                fac.AntdTitle(
                                                    '内容区示例',
                                                    level=2,
                                                    style={
                                                        'margin': '0'
                                                    }
                                                ),
                                                style={
                                                    'display': 'flex',
                                                    'height': '100%',
                                                    'justifyContent': 'center',
                                                    'alignItems': 'center'
                                                }
                                            ),
                                            style={
                                                'backgroundColor': 'white'
                                            }
                                        )
                                    ],
                                    style={
                                        'height': '600px'
                                    }
                                )
                            ],
                            className='sider-demo',
                            style={
                                'height': '600px',
                                'border': '1px solid rgb(241, 241, 241)'
                            }
                        ),

                        fac.AntdDivider(
                            '可折叠侧边栏',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
# 侧边栏自带折叠触发区域默认会紧贴页面下边界
# 这里为方便局部展示示例，基于fuc.FefferyStyle强制覆盖默认样式
fuc.FefferyStyle(
    rawStyle='''
.sider-demo .ant-layout-sider-trigger {
  position: absolute !important;
}
'''
    ),

html.Div(
    [
        fac.AntdLayout(
            [
                fac.AntdSider(
                    collapsible=True,
                    style={
                        'backgroundColor': 'rgb(240, 242, 245)'
                    }
                ),

                fac.AntdContent(
                    html.Div(
                        fac.AntdTitle(
                            '内容区示例',
                            level=2,
                            style={
                                'margin': '0'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'height': '100%',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    style={
                        'backgroundColor': 'white'
                    }
                )
            ],
            style={
                'height': '600px'
            }
        )
    ],
    className='sider-demo',
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
    }
)
"""
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='可折叠侧边栏',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdLayout(
                                    [
                                        fac.AntdSider(
                                            breakpoint='xl',
                                            collapsible=True,
                                            style={
                                                'backgroundColor': 'rgb(240, 242, 245)'
                                            }
                                        ),

                                        fac.AntdContent(
                                            html.Div(
                                                fac.AntdTitle(
                                                    '内容区示例',
                                                    level=2,
                                                    style={
                                                        'margin': '0'
                                                    }
                                                ),
                                                style={
                                                    'display': 'flex',
                                                    'height': '100%',
                                                    'justifyContent': 'center',
                                                    'alignItems': 'center'
                                                }
                                            ),
                                            style={
                                                'backgroundColor': 'white'
                                            }
                                        )
                                    ],
                                    style={
                                        'height': '600px'
                                    }
                                )
                            ],
                            className='sider-demo',
                            style={
                                'height': '600px',
                                'border': '1px solid rgb(241, 241, 241)'
                            }
                        ),

                        fac.AntdDivider(
                            '侧边栏响应式折叠',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    [
        fac.AntdLayout(
            [
                fac.AntdSider(
                    breakpoint='xl',
                    collapsible=True,
                    style={
                        'backgroundColor': 'rgb(240, 242, 245)'
                    }
                ),

                fac.AntdContent(
                    html.Div(
                        fac.AntdTitle(
                            '内容区示例',
                            level=2,
                            style={
                                'margin': '0'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'height': '100%',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    style={
                        'backgroundColor': 'white'
                    }
                )
            ],
            style={
                'height': '600px'
            }
        )
    ],
    className='sider-demo',
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
    }
)
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='侧边栏响应式折叠',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdLayout(
                                    [
                                        fac.AntdSider(
                                            [
                                                fac.AntdMenu(
                                                    menuItems=[
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': f'图标{icon}',
                                                                'title': f'图标{icon}',
                                                                'icon': icon
                                                            }
                                                        }
                                                        for icon in [
                                                            'antd-home',
                                                            'antd-cloud-upload',
                                                            'antd-bar-chart',
                                                            'antd-pie-chart',
                                                            'antd-dot-chart',
                                                            'antd-line-chart',
                                                            'antd-apartment',
                                                            'antd-app-store',
                                                            'antd-app-store-add',
                                                            'antd-bell',
                                                            'antd-calculator',
                                                            'antd-calendar',
                                                            'antd-database',
                                                            'antd-history'
                                                        ]
                                                    ],
                                                    mode='inline',
                                                    style={
                                                        'height': '100%',
                                                        'overflow': 'hidden auto'
                                                    }
                                                )
                                            ],
                                            collapsible=True,
                                            collapsedWidth=60,
                                            style={
                                                'backgroundColor': 'rgb(240, 242, 245)'
                                            }
                                        ),

                                        fac.AntdContent(
                                            html.Div(
                                                fac.AntdTitle(
                                                    '内容区示例',
                                                    level=2,
                                                    style={
                                                        'margin': '0'
                                                    }
                                                ),
                                                style={
                                                    'display': 'flex',
                                                    'height': '100%',
                                                    'justifyContent': 'center',
                                                    'alignItems': 'center'
                                                }
                                            ),
                                            style={
                                                'backgroundColor': 'white'
                                            }
                                        )
                                    ],
                                    style={
                                        'height': '600px'
                                    }
                                )
                            ],
                            className='sider-demo',
                            style={
                                'height': '600px',
                                'border': '1px solid rgb(241, 241, 241)'
                            }
                        ),

                        fac.AntdDivider(
                            '侧边栏联动菜单组件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    [
        fac.AntdLayout(
            [
                fac.AntdSider(
                    [
                        fac.AntdMenu(
                            menuItems=[
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': f'图标{icon}',
                                        'title': f'图标{icon}',
                                        'icon': icon
                                    }
                                }
                                for icon in [
                                    'antd-home',
                                    'antd-cloud-upload',
                                    'antd-bar-chart',
                                    'antd-pie-chart',
                                    'antd-dot-chart',
                                    'antd-line-chart',
                                    'antd-apartment',
                                    'antd-app-store',
                                    'antd-app-store-add',
                                    'antd-bell',
                                    'antd-calculator',
                                    'antd-calendar',
                                    'antd-database',
                                    'antd-history'
                                ]
                            ],
                            mode='inline',
                            style={
                                'height': '100%',
                                'overflow': 'hidden auto'
                            }
                        )
                    ],
                    collapsible=True,
                    collapsedWidth=60,
                    style={
                        'backgroundColor': 'rgb(240, 242, 245)'
                    }
                ),

                fac.AntdContent(
                    html.Div(
                        fac.AntdTitle(
                            '内容区示例',
                            level=2,
                            style={
                                'margin': '0'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'height': '100%',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    style={
                        'backgroundColor': 'white'
                    }
                )
            ],
            style={
                'height': '600px'
            }
        )
    ],
    className='sider-demo',
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
    }
)
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='侧边栏联动菜单组件',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdLayout(
                                    [
                                        fac.AntdSider(
                                            id='sider-custom-trigger-demo',
                                            collapsible=True,
                                            trigger=None,
                                            style={
                                                'backgroundColor': 'rgb(240, 242, 245)'
                                            }
                                        ),

                                        fac.AntdContent(
                                            fac.AntdButton(
                                                '折叠/展开',
                                                id='sider-custom-trigger-button-demo',
                                                type='primary'
                                            ),
                                            style={
                                                'backgroundColor': 'white'
                                            }
                                        )
                                    ],
                                    style={
                                        'height': '600px'
                                    }
                                )
                            ],
                            style={
                                'height': '600px',
                                'border': '1px solid rgb(241, 241, 241)'
                            }
                        ),

                        fac.AntdDivider(
                            '自定义侧边栏折叠触发器',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    [
        fac.AntdLayout(
            [
                fac.AntdSider(
                    id='sider-custom-trigger-demo',
                    collapsible=True,
                    trigger=None,
                    style={
                        'backgroundColor': 'rgb(240, 242, 245)'
                    }
                ),

                fac.AntdContent(
                    fac.AntdButton(
                        '折叠/展开',
                        id='sider-custom-trigger-button-demo',
                        type='primary'
                    ),
                    style={
                        'backgroundColor': 'white'
                    }
                )
            ],
            style={
                'height': '600px'
            }
        )
    ],
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
    }
)

...

@app.callback(
    Output('sider-custom-trigger-demo', 'collapsed'),
    Input('sider-custom-trigger-button-demo', 'nClicks'),
    State('sider-custom-trigger-demo', 'collapsed'),
    prevent_initial_call=True
)
def sider_custom_trigger_demo(nClicks, collapsed):
    if nClicks:
        return not collapsed

    return dash.no_update
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='自定义侧边栏折叠触发器',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '基础使用', 'href': '#基础使用'},
                    {'title': '右侧侧边栏', 'href': '#右侧侧边栏'},
                    {'title': '可折叠侧边栏', 'href': '#可折叠侧边栏'},
                    {'title': '侧边栏响应式折叠', 'href': '#侧边栏响应式折叠'},
                    {'title': '侧边栏联动菜单组件', 'href': '#侧边栏联动菜单组件'},
                    {'title': '自定义侧边栏折叠触发器', 'href': '#自定义侧边栏折叠触发器'},
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'padding': '25px'
            }
        ),
        # 侧边参数栏
        render_side_props_layout(
            component_name='AntdLayout'
        )
    ],
    style={
        'display': 'flex'
    }
)
