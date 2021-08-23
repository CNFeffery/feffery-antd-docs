import dash
import time
import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app, server

from views import (
    AntdDatePicker,
    AntdDateRangePicker,
    AntdDivider,
    AntdButton,
    AntdSelect,
    AntdTree,
    AntdTable,
    AntdAnchor,
    AntdSlider,
    AntdTransfer,
    AntdSteps,
    AntdMenu
)

app.layout = fac.AntdSpin(
    html.Div(
        [
            # 注入路由
            dcc.Location(id='url'),

            # 注入重定向容器
            html.Div(id='redirect-url-container'),

            # 页面结构
            fac.AntdLayout(
                [
                    fac.AntdHeader(
                        [
                            fac.AntdRow(
                                [
                                    fac.AntdCol(
                                        html.Img(
                                            src=app.get_asset_url('imgs/feffery-antd-components-logo-planB.svg'),
                                            style={
                                                'height': '40px',
                                                'paddingRight': '10px'
                                            }
                                        )
                                    ),
                                    fac.AntdCol(
                                        fac.AntdParagraph(
                                            [
                                                fac.AntdText(
                                                    'feffery-antd-components',
                                                    strong=True,
                                                    style={
                                                        'fontSize': '28px'
                                                    }
                                                ),
                                                fac.AntdText(
                                                    'v0.0.1rc1',
                                                    style={
                                                        'fontSize': '10px',
                                                        'paddingLeft': '2px'
                                                    }
                                                )
                                            ]
                                        )
                                    )
                                ],
                                style={
                                    'paddingLeft': '30px'
                                }
                            )
                        ],
                        style={
                            'backgroundColor': 'rgb(255, 255, 255)',
                            'boxShadow': '0 2px 14px #f0f1f2',
                            'zIndex': '999',
                            'paddingLeft': '10px',
                            'height': '65px'
                        }
                    ),
                    fac.AntdLayout(
                        [
                            fac.AntdSider(
                                [

                                    fac.AntdMenu(
                                        id='router-menu',
                                        menuItems=[
                                            {
                                                'component': 'ItemGroup',
                                                'props': {
                                                    'key': 'getting-started',
                                                    'title': '快速入门'
                                                },
                                                'children': [
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/what-is-fac',
                                                            'title': 'fac是什么'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/getting-started',
                                                            'title': '安装及基础使用'
                                                        }
                                                    }
                                                ]
                                            },
                                            {
                                                'component': 'ItemGroup',
                                                'props': {
                                                    'key': 'general',
                                                    'title': '通用'
                                                },
                                                'children': [
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdButton',
                                                            'title': 'AntdButton 按钮'
                                                        }
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'key': 'Typography',
                                                            'title': '排版相关'
                                                        },
                                                        'children': [
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdTypography',
                                                                    'title': 'AntdTypography 排版'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdParagraph',
                                                                    'title': 'AntdParagraph 段落'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdText',
                                                                    'title': 'AntdText 文字'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdTitle',
                                                                    'title': 'AntdTitle 标题'
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                'component': 'ItemGroup',
                                                'props': {
                                                    'key': 'layout',
                                                    'title': '布局'
                                                },
                                                'children': [
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdDivider',
                                                            'title': 'AntdDivider 分割线'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdSpace',
                                                            'title': 'AntdSpace 间距'
                                                        }
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'key': 'Grid',
                                                            'title': '网格系统'
                                                        },
                                                        'children': [
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdRow',
                                                                    'title': 'AntdRow 行'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdCol',
                                                                    'title': 'AntdCol 列'
                                                                }
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'key': 'Layout',
                                                            'title': '布局'
                                                        },
                                                        'children': [
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdLayout',
                                                                    'title': 'AntdLayout 布局'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdHeader',
                                                                    'title': 'AntdHeader 页首'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdSider',
                                                                    'title': 'AntdSider 侧边栏'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdContent',
                                                                    'title': 'AntdContent 内容区'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdFooter',
                                                                    'title': 'AntdFooter 页尾'
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                'component': 'ItemGroup',
                                                'props': {
                                                    'key': 'navigation',
                                                    'title': '导航'
                                                },
                                                'children': [
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdMenu',
                                                            'title': 'AntdMenu 导航菜单'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdPagination',
                                                            'title': 'AntdPagination 分页'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdSteps',
                                                            'title': 'AntdSteps 步骤条'
                                                        }
                                                    }
                                                ]
                                            },
                                            {
                                                'component': 'ItemGroup',
                                                'props': {
                                                    'key': 'data-entry',
                                                    'title': '数据录入'
                                                },
                                                'children': [
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdCascader',
                                                            'title': 'AntdCascader 级联选择'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdCheckbox',
                                                            'title': 'AntdCheckbox 选择框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdCheckboxGroup',
                                                            'title': 'AntdCheckboxGroup 组合选择框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdDatePicker',
                                                            'title': 'AntdDatePicker 日期选择'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdDateRangePicker',
                                                            'title': 'AntdDateRangePicker 日期范围选择'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdInput',
                                                            'title': 'AntdInput 输入框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdRadioGroup',
                                                            'title': 'AntdRadioGroup 单选框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdSelect',
                                                            'title': 'AntdSelect 下拉选择'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdSlider',
                                                            'title': 'AntdSlider 滑动输入条'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdSwitch',
                                                            'title': 'AntdSwitch 开关'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdTransfer',
                                                            'title': 'AntdTransfer 穿梭框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdTreeSelect',
                                                            'title': 'AntdTreeSelect 树选择'
                                                        }
                                                    }
                                                ]
                                            },

                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': 'data-display',
                                                    'title': '数据展示'
                                                },
                                                'children': [
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdCollapse',
                                                            'title': 'AntdCollapse 折叠面板'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdEmpty',
                                                            'title': 'AntdEmpty 空状态'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdPopover',
                                                            'title': 'AntdPopover 气泡卡片'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdTable',
                                                            'title': 'AntdTable 表格'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdTag',
                                                            'title': 'AntdTag 标签'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdTooltip',
                                                            'title': 'AntdTooltip 文字提示'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdTree',
                                                            'title': 'AntdTree 树形控件'
                                                        }
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'key': 'tabs',
                                                            'title': '标签页'
                                                        },
                                                        'children': [
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdTabPane',
                                                                    'title': 'AntdTabPane 标签页面板'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdTabs',
                                                                    'title': 'AntdTabs 标签页'
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },

                                            {
                                                'component': 'ItemGroup',
                                                'props': {
                                                    'key': 'feedback',
                                                    'title': '反馈'
                                                },
                                                'children': [
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdAlert',
                                                            'title': 'AntdAlert 警告提示'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdDrawer',
                                                            'title': 'AntdDrawer 抽屉'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdMessage',
                                                            'title': 'AntdMessage 全局提示'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdModal',
                                                            'title': 'AntdModal 对话框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdNotification',
                                                            'title': 'AntdNotification 通知提醒框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdResult',
                                                            'title': 'AntdResult 结果'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdSkeleton',
                                                            'title': 'AntdSkeleton 骨架屏'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdSpin',
                                                            'title': 'AntdSpin 加载动画'
                                                        }
                                                    }
                                                ]
                                            },
                                            {
                                                'component': 'ItemGroup',
                                                'props': {
                                                    'key': 'other',
                                                    'title': '其他'
                                                },
                                                'children': [
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdAnchor',
                                                            'title': 'AntdAnchor 锚点'
                                                        }
                                                    }
                                                ]
                                            }
                                        ],
                                        mode='inline',
                                        defaultSelectedKey='/what-is-fac',
                                        style={
                                            'height': '100%',
                                            'overflowX': 'hidden',
                                            'overflowY': 'auto',
                                            'paddingBottom': '50px'
                                        }
                                    )
                                ],
                                width=350
                            ),

                            fac.AntdContent(
                                id='docs-content',
                                style={
                                    'overflowY': 'auto',
                                    'padding': '50px'
                                }
                            )
                        ]
                    )
                ],
                style={
                    'height': '100%'
                }
            )
        ],
        style={
            'width': '100vw',
            'height': '100vh'
        }
    )
)


# 路由
@app.callback(
    Output('docs-content', 'children'),
    Input('router-menu', 'currentKey'),
    prevent_initial_call=True
)
def render_docs_content(currentKey):
    time.sleep(0.5)

    if currentKey == '/AntdButton':
        return AntdButton.docs_content

    return currentKey

    # return dcc.Location(id='redirect-url', href=currentKey)

    #
    # if pathname.startswith('/feffery-antd-docs/index'):
    #
    #     return dcc.Markdown(open('documents/index.md', encoding='utf-8').read(), className='markdown')
    #
    # else:
    #     return dcc.Location(id='redirect-url', href='/feffery-antd-docs/index')


if __name__ == '__main__':
    app.run_server(debug=True)
