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
    AntdUpload
)

app.layout = fac.AntdSpin(
    fuc.FefferyWaterMark(
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
                                                        'v0.0.1rc1稳定版',
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
                                                        'key': '/getting-started',
                                                        'title': '快速入门'
                                                    },
                                                    'children': [
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/what-is-fac',
                                                                'title': 'fac是什么？'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/getting-started',
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
                                                                        'title': 'AntdTypography 排版',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdParagraph',
                                                                        'title': 'AntdParagraph 段落',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdText',
                                                                        'title': 'AntdText 文字',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdTitle',
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
                                                                'title': 'AntdDivider 分割线'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdSpace',
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
                                                                        'title': 'AntdRow 行',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdCol',
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
                                                                        'title': 'AntdLayout 布局',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdHeader',
                                                                        'title': 'AntdHeader 页首',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdSider',
                                                                        'title': 'AntdSider 侧边栏',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdContent',
                                                                        'title': 'AntdContent 内容区',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdFooter',
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
                                                                'title': 'AntdMenu 导航菜单'
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdPagination',
                                                                'title': 'AntdPagination 分页',
                                                                'disabled': True
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
                                                                'title': 'AntdCascader 级联选择',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdCheckbox',
                                                                'title': 'AntdCheckbox 选择框',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdCheckboxGroup',
                                                                'title': 'AntdCheckboxGroup 组合选择框',
                                                                'disabled': True
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
                                                                'title': 'AntdInput 输入框',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdRadioGroup',
                                                                'title': 'AntdRadioGroup 单选框',
                                                                'disabled': True
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
                                                                'title': 'AntdSwitch 开关',
                                                                'disabled': True
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
                                                                'title': 'AntdTreeSelect 树选择',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdUpload',
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
                                                                'title': 'AntdCollapse 折叠面板',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdEmpty',
                                                                'title': 'AntdEmpty 空状态',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdPopover',
                                                                'title': 'AntdPopover 气泡卡片',
                                                                'disabled': True
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
                                                                'title': 'AntdTag 标签',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdTooltip',
                                                                'title': 'AntdTooltip 文字提示',
                                                                'disabled': True
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
                                                                        'title': 'AntdTabPane 标签页面板',
                                                                        'disabled': True
                                                                    }
                                                                },
                                                                {
                                                                    'component': 'Item',
                                                                    'props': {
                                                                        'key': '/AntdTabs',
                                                                        'title': 'AntdTabs 标签页',
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
                                                        'key': 'feedback',
                                                        'title': '反馈'
                                                    },
                                                    'children': [
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdAlert',
                                                                'title': 'AntdAlert 警告提示',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdDrawer',
                                                                'title': 'AntdDrawer 抽屉',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdMessage',
                                                                'title': 'AntdMessage 全局提示',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdModal',
                                                                'title': 'AntdModal 对话框',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdNotification',
                                                                'title': 'AntdNotification 通知提醒框',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdResult',
                                                                'title': 'AntdResult 结果',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdSkeleton',
                                                                'title': 'AntdSkeleton 骨架屏',
                                                                'disabled': True
                                                            }
                                                        },
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': '/AntdSpin',
                                                                'title': 'AntdSpin 加载动画',
                                                                'disabled': True
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
        content='最新稳定版本（内容补全中）',
        fontSize=18
    ),
    listenPropsMode='exclude',
    excludeProps=Config.exclude_props,
    size='large',
    text='文档加载中'
)


@app.callback(
    Output('docs-content', 'children'),
    Input('router-menu', 'currentKey'),
    prevent_initial_call=True
)
def render_docs_content(currentKey):
    '''
    路由回调
    :param currentKey: 当前被点击的侧边栏菜单项
    :return:
    '''

    if currentKey == '/what-is-fac':
        return what_is_fac.docs_content

    if currentKey == '/AntdButton':
        return AntdButton.docs_content

    elif currentKey == '/AntdTypography':
        return currentKey

    elif currentKey == '/AntdParagraph':
        return currentKey

    elif currentKey == '/AntdText':
        return currentKey

    elif currentKey == '/AntdTitle':
        return currentKey

    elif currentKey == '/AntdDivider':
        return AntdDivider.docs_content

    elif currentKey == '/AntdSpace':
        return currentKey

    elif currentKey == '/AntdRow':
        return currentKey

    elif currentKey == '/AntdCol':
        return currentKey

    elif currentKey == '/AntdLayout':
        return currentKey

    elif currentKey == '/AntdHeader':
        return currentKey

    elif currentKey == '/AntdSider':
        return currentKey

    elif currentKey == '/AntdContent':
        return currentKey

    elif currentKey == '/AntdFooter':
        return currentKey

    elif currentKey == '/AntdMenu':
        return AntdMenu.docs_content

    elif currentKey == '/AntdPagination':
        return currentKey

    elif currentKey == '/AntdSteps':
        return AntdSteps.docs_content

    elif currentKey == '/AntdCascader':
        return currentKey

    elif currentKey == '/AntdCheckbox':
        return currentKey

    elif currentKey == '/AntdCheckboxGroup':
        return currentKey

    elif currentKey == '/AntdDatePicker':
        return AntdDatePicker.docs_content

    elif currentKey == '/AntdDateRangePicker':
        return AntdDateRangePicker.docs_content

    elif currentKey == '/AntdInput':
        return currentKey

    elif currentKey == '/AntdRadioGroup':
        return currentKey

    elif currentKey == '/AntdSelect':
        return AntdSelect.docs_content

    elif currentKey == '/AntdSlider':
        return AntdSlider.docs_content

    elif currentKey == '/AntdSwitch':
        return currentKey

    elif currentKey == '/AntdTransfer':
        return AntdTransfer.docs_content

    elif currentKey == '/AntdTreeSelect':
        return currentKey

    elif currentKey == '/AntdUpload':
        return AntdUpload.docs_content

    elif currentKey == '/AntdCollapse':
        return currentKey

    elif currentKey == '/AntdEmpty':
        return currentKey

    elif currentKey == '/AntdPopover':
        return currentKey

    elif currentKey == '/AntdTable':
        return AntdTable.docs_content

    elif currentKey == '/AntdTag':
        return currentKey

    elif currentKey == '/AntdTooltip':
        return currentKey

    elif currentKey == '/AntdTree':
        return AntdTree.docs_content

    elif currentKey == '/AntdTabPane':
        return currentKey

    elif currentKey == '/AntdTabs':
        return currentKey

    elif currentKey == '/AntdAlert':
        return currentKey

    elif currentKey == '/AntdDrawer':
        return currentKey

    elif currentKey == '/AntdMessage':
        return currentKey

    elif currentKey == '/AntdModal':
        return currentKey

    elif currentKey == '/AntdNotification':
        return currentKey

    elif currentKey == '/AntdResult':
        return currentKey

    elif currentKey == '/AntdSkeleton':
        return currentKey

    elif currentKey == '/AntdSpin':
        return currentKey

    elif currentKey == '/AntdAnchor':
        return AntdAnchor.docs_content

    return currentKey


if __name__ == '__main__':
    app.run_server(debug=True)
