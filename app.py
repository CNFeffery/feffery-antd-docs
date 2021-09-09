import dash
import time
import requests
import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

from server import app, server
from config import Config

from views import (
    what_is_fac,
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
    AntdMenu,
    AntdUpload,
    AntdSpin,
    AntdInput,
    AntdTabPane,
    AntdTabs
)

app.layout = fac.AntdSpin(
    fuc.FefferyWaterMark(
        html.Div(
            [
                # 注入路由
                dcc.Location(id='url'),

                # 页面结构
                fac.AntdLayout(
                    [
                        fac.AntdHeader(
                            [
                                fac.AntdRow(
                                    [
                                        fac.AntdCol(
                                            html.Img(
                                                src=app.get_asset_url(
                                                    'imgs/feffery-antd-components-logo-planB.svg'),
                                                style={
                                                    'height': '45px',
                                                    'paddingRight': '10px'
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
                                                            'fontSize': '30px'
                                                        }
                                                    ),
                                                    fac.AntdText(
                                                        'v0.0.1rc2',
                                                        style={
                                                            'fontSize': '10px',
                                                            'paddingLeft': '2px'
                                                        }
                                                    )
                                                ]
                                            )
                                        ),

                                        fac.AntdCol(
                                            html.Div(
                                                [
                                                    html.A(
                                                        html.Img(
                                                            alt='GitHub Repo stars',
                                                            src='https://img.shields.io/github/stars/CNFeffery/feffery-antd-components?style=social',
                                                            style={
                                                                'transform': 'scale(1.25)'
                                                            }
                                                        ),
                                                        href='https://github.com/CNFeffery/feffery-antd-components/stargazers/',
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
                                                            'paddingLeft': '50px',
                                                            'color': '#494f54'
                                                        }
                                                    )
                                                ],
                                                style={
                                                    'float': 'right',
                                                    'paddingRight': '20px'
                                                }
                                            ),
                                            flex='auto'
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
                                'paddingRight': '10px',
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
                                                        'key': '/',
                                                        'title': '快速入门'
                                                    },
                                                    'children': [
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/what-is-fac',
                                                                'href': '/what-is-fac',
                                                                'title': 'fac是什么？'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/getting-started',
                                                                'href': '/getting-started',
                                                                'title': '基础使用'
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
                                                                'href': '/AntdButton',
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
                                                                        'href': '/AntdTypography',
                                                                        'title': 'AntdTypography 排版',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdParagraph',
                                                                        'href': '/AntdParagraph',
                                                                        'title': 'AntdParagraph 段落',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdText',
                                                                        'href': '/AntdText',
                                                                        'title': 'AntdText 文字',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdTitle',
                                                                        'href': '/AntdTitle',
                                                                        'title': 'AntdTitle 标题',
                                                                        'disabled': True
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
                                                                'href': '/AntdDivider',
                                                                'title': 'AntdDivider 分割线'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdSpace',
                                                                'href': '/AntdSpace',
                                                                'title': 'AntdSpace 间距',
                                                                'disabled': True
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
                                                                        'href': '/AntdRow',
                                                                        'title': 'AntdRow 行',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdCol',
                                                                        'href': '/AntdCol',
                                                                        'title': 'AntdCol 列',
                                                                        'disabled': True
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
                                                                        'href': '/AntdLayout',
                                                                        'title': 'AntdLayout 布局',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdHeader',
                                                                        'href': '/AntdHeader',
                                                                        'title': 'AntdHeader 页首',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdSider',
                                                                        'href': '/AntdSider',
                                                                        'title': 'AntdSider 侧边栏',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdContent',
                                                                        'href': '/AntdContent',
                                                                        'title': 'AntdContent 内容区',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdFooter',
                                                                        'href': '/AntdFooter',
                                                                        'title': 'AntdFooter 页尾',
                                                                        'disabled': True
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
                                                                'href': '/AntdMenu',
                                                                'title': 'AntdMenu 导航菜单'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdPagination',
                                                                'href': '/AntdPagination',
                                                                'title': 'AntdPagination 分页',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdSteps',
                                                                'href': '/AntdSteps',
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
                                                                'href': '/AntdCascader',
                                                                'title': 'AntdCascader 级联选择',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdCheckbox',
                                                                'href': '/AntdCheckbox',
                                                                'title': 'AntdCheckbox 选择框',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdCheckboxGroup',
                                                                'href': '/AntdCheckboxGroup',
                                                                'title': 'AntdCheckboxGroup 组合选择框',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdDatePicker',
                                                                'href': '/AntdDatePicker',
                                                                'title': 'AntdDatePicker 日期选择'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdDateRangePicker',
                                                                'href': '/AntdDateRangePicker',
                                                                'title': 'AntdDateRangePicker 日期范围选择'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdInput',
                                                                'href': '/AntdInput',
                                                                'title': 'AntdInput 输入框'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdRadioGroup',
                                                                'href': '/AntdRadioGroup',
                                                                'title': 'AntdRadioGroup 单选框',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdSelect',
                                                                'href': '/AntdSelect',
                                                                'title': 'AntdSelect 下拉选择'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdSlider',
                                                                'href': '/AntdSlider',
                                                                'title': 'AntdSlider 滑动输入条'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdSwitch',
                                                                'href': '/AntdSwitch',
                                                                'title': 'AntdSwitch 开关',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdTransfer',
                                                                'href': '/AntdTransfer',
                                                                'title': 'AntdTransfer 穿梭框'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdTreeSelect',
                                                                'href': '/AntdTreeSelect',
                                                                'title': 'AntdTreeSelect 树选择',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdUpload',
                                                                'href': '/AntdUpload',
                                                                'title': 'AntdUpload 上传'
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
                                                                'href': '/AntdCollapse',
                                                                'title': 'AntdCollapse 折叠面板',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdEmpty',
                                                                'href': '/AntdEmpty',
                                                                'title': 'AntdEmpty 空状态',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdPopover',
                                                                'href': '/AntdPopover',
                                                                'title': 'AntdPopover 气泡卡片',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdTable',
                                                                'href': '/AntdTable',
                                                                'title': 'AntdTable 表格'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdTag',
                                                                'href': '/AntdTag',
                                                                'title': 'AntdTag 标签',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdTooltip',
                                                                'href': '/AntdTooltip',
                                                                'title': 'AntdTooltip 文字提示',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdTree',
                                                                'href': '/AntdTree',
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
                                                                        'href': '/AntdTabPane',
                                                                        'title': 'AntdTabPane 标签页面板'
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdTabs',
                                                                        'href': '/AntdTabs',
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
                                                                'href': '/AntdAlert',
                                                                'title': 'AntdAlert 警告提示',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdDrawer',
                                                                'href': '/AntdDrawer',
                                                                'title': 'AntdDrawer 抽屉',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdMessage',
                                                                'href': '/AntdMessage',
                                                                'title': 'AntdMessage 全局提示',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdModal',
                                                                'href': '/AntdModal',
                                                                'title': 'AntdModal 对话框',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdNotification',
                                                                'href': '/AntdNotification',
                                                                'title': 'AntdNotification 通知提醒框',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdResult',
                                                                'href': '/AntdResult',
                                                                'title': 'AntdResult 结果',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdSkeleton',
                                                                'href': '/AntdSkeleton',
                                                                'title': 'AntdSkeleton 骨架屏',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdSpin',
                                                                'href': '/AntdSpin',
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
                                                                'href': '/AntdAnchor',
                                                                'title': 'AntdAnchor 锚点'
                                                            }
                                                        }
                                                    ]
                                                }
                                            ],
                                            mode='inline',
                                            defaultOpenKeys=['tabs'],
                                            style={
                                                'height': '100%',
                                                'overflowX': 'hidden',
                                                'overflowY': 'auto',
                                                'paddingBottom': '50px'
                                            }
                                        )
                                    ],
                                    width=325
                                ),

                                fac.AntdContent(
                                    id='docs-content',
                                    style={
                                        'overflowY': 'auto',
                                        'padding': '50px 100px 50px 100px',
                                        'backgroundColor': 'rgb(255, 255, 255)',
                                        'position': 'relative'
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
        ),
        content='内容补全中',
        fontSize=20
    ),
    listenPropsMode='exclude',
    excludeProps=Config.exclude_props,
    size='large',
    text='文档加载中'
)


@app.callback(
    [Output('docs-content', 'children'),
     Output('router-menu', 'currentKey')],
    Input('url', 'pathname'),
    prevent_initial_call=True
)
def render_docs_content(pathname):
    '''
    路由回调
    '''

    if pathname == '/what-is-fac' or pathname == '/':
        pathname = '/what-is-fac'
        return what_is_fac.docs_content, pathname

    if pathname == '/AntdButton':
        return AntdButton.docs_content, pathname

    elif pathname == '/AntdTypography':
        return pathname, pathname

    elif pathname == '/AntdParagraph':
        return pathname, pathname

    elif pathname == '/AntdText':
        return pathname, pathname

    elif pathname == '/AntdTitle':
        return pathname, pathname

    elif pathname == '/AntdDivider':
        return AntdDivider.docs_content, pathname

    elif pathname == '/AntdSpace':
        return pathname, pathname

    elif pathname == '/AntdRow':
        return pathname, pathname

    elif pathname == '/AntdCol':
        return pathname, pathname

    elif pathname == '/AntdLayout':
        return pathname, pathname

    elif pathname == '/AntdHeader':
        return pathname, pathname

    elif pathname == '/AntdSider':
        return pathname, pathname

    elif pathname == '/AntdContent':
        return pathname, pathname

    elif pathname == '/AntdFooter':
        return pathname, pathname

    elif pathname == '/AntdMenu':
        return AntdMenu.docs_content, pathname

    elif pathname == '/AntdPagination':
        return pathname, pathname

    elif pathname == '/AntdSteps':
        return AntdSteps.docs_content, pathname

    elif pathname == '/AntdCascader':
        return pathname, pathname

    elif pathname == '/AntdCheckbox':
        return pathname, pathname

    elif pathname == '/AntdCheckboxGroup':
        return pathname, pathname

    elif pathname == '/AntdDatePicker':
        return AntdDatePicker.docs_content, pathname

    elif pathname == '/AntdDateRangePicker':
        return AntdDateRangePicker.docs_content, pathname

    elif pathname == '/AntdInput':
        return AntdInput.docs_content, pathname

    elif pathname == '/AntdRadioGroup':
        return pathname, pathname

    elif pathname == '/AntdSelect':
        return AntdSelect.docs_content, pathname

    elif pathname == '/AntdSlider':
        return AntdSlider.docs_content, pathname

    elif pathname == '/AntdSwitch':
        return pathname, pathname

    elif pathname == '/AntdTransfer':
        return AntdTransfer.docs_content, pathname

    elif pathname == '/AntdTreeSelect':
        return pathname, pathname

    elif pathname == '/AntdUpload':
        return AntdUpload.docs_content, pathname

    elif pathname == '/AntdCollapse':
        return pathname, pathname

    elif pathname == '/AntdEmpty':
        return pathname, pathname

    elif pathname == '/AntdPopover':
        return pathname, pathname

    elif pathname == '/AntdTable':
        return AntdTable.docs_content, pathname

    elif pathname == '/AntdTag':
        return pathname, pathname

    elif pathname == '/AntdTooltip':
        return pathname, pathname

    elif pathname == '/AntdTree':
        return AntdTree.docs_content, pathname

    elif pathname == '/AntdTabPane':
        return AntdTabPane.docs_content, pathname

    elif pathname == '/AntdTabs':
        return AntdTabs.docs_content, pathname

    elif pathname == '/AntdAlert':
        return pathname, pathname

    elif pathname == '/AntdDrawer':
        return pathname, pathname

    elif pathname == '/AntdMessage':
        return pathname, pathname

    elif pathname == '/AntdModal':
        return pathname, pathname

    elif pathname == '/AntdNotification':
        return pathname, pathname

    elif pathname == '/AntdResult':
        return pathname, pathname

    elif pathname == '/AntdSkeleton':
        return pathname, pathname

    elif pathname == '/AntdSpin':
        return AntdSpin.docs_content, pathname

    elif pathname == '/AntdAnchor':
        return AntdAnchor.docs_content, pathname

    return pathname, pathname


if __name__ == '__main__':
    app.run_server(debug=True)
