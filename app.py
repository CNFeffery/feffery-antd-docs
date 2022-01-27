import feffery_antd_components as fac
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from config import Config
from server import app, server
from views import (
    what_is_fac,
    getting_started,
    AntdDatePicker,
    AntdDateRangePicker,
    AntdDivider,
    AntdIcon,
    AntdBackTop,
    AntdButton,
    AntdSelect,
    AntdRate,
    AntdTree,
    AntdTable,
    AntdAnchor,
    AntdSlider,
    AntdTransfer,
    AntdSteps,
    AntdMenu,
    AntdUpload,
    AntdDraggerUpload,
    AntdSpin,
    AntdInput,
    AntdTabPane,
    AntdTabs,
    AntdRow,
    AntdCol,
    AntdParagraph,
    AntdText,
    AntdTitle,
    AntdSpace,
    AntdAlert,
    AntdNotification,
    AntdMessage,
    AntdLayout,
    AntdHeader,
    AntdSider,
    AntdContent,
    AntdFooter,
    AntdPagination,
    AntdCascader,
    AntdCheckbox,
    AntdCheckboxGroup,
    AntdRadioGroup,
    AntdSwitch,
    AntdTreeSelect,
    AntdCollapse,
    AntdEmpty,
    AntdTooltip,
    AntdPopover,
    AntdStatistic,
    AntdCountdown,
    AntdTag,
    AntdDrawer,
    AntdModal,
    AntdPopconfirm,
    AntdResult,
    AntdSkeleton,
    AntdAffix,
    AntdBreadcrumb,
    AntdDropdown,
    AntdInputNumber,
    AntdTimeline,
    AntdProgress,
    AntdAvatar,
    AntdBadge,
    AntdRibbon,
    AntdTimePicker,
    AntdTimeRangePicker,
    AntdCarousel,
    AntdForm,
    AntdFormItem,
    AntdCardGrid,
    AntdCard,
    AntdMentions,
    AntdImage,
    AntdPageHeader,
    AntdCalendar,
    AntdComment,
    AntdDescriptions,
    AntdDescriptionItem
)

app.layout = fac.AntdSpin(
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
                                                'imgs/fac-logo.svg'),
                                            style={
                                                'height': '50px',
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
                                                        'fontSize': '35px'
                                                    }
                                                ),
                                                fac.AntdText(
                                                    'v0.0.1rc8',
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
                                                    fac.AntdImage(
                                                        alt='fac源码仓库，欢迎star',
                                                        src='https://img.shields.io/github/stars/CNFeffery/feffery-antd-components?style=social',
                                                        preview=False,
                                                        style={
                                                            'transform': 'translateY(5px) scale(1.25)'
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
                                                            'key': '/AntdIcon',
                                                            'href': '/AntdIcon',
                                                            'title': 'AntdIcon 图标'
                                                        }
                                                    },
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
                                                                    'key': '/AntdParagraph',
                                                                    'href': '/AntdParagraph',
                                                                    'title': 'AntdParagraph 段落'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdText',
                                                                    'href': '/AntdText',
                                                                    'title': 'AntdText 文字'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdTitle',
                                                                    'href': '/AntdTitle',
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
                                                            'href': '/AntdDivider',
                                                            'title': 'AntdDivider 分割线'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdSpace',
                                                            'href': '/AntdSpace',
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
                                                                    'key': '/AntdCol',
                                                                    'href': '/AntdCol',
                                                                    'title': 'AntdCol 列'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdRow',
                                                                    'href': '/AntdRow',
                                                                    'title': 'AntdRow 行'
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
                                                                    'title': 'AntdLayout 布局'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdHeader',
                                                                    'href': '/AntdHeader',
                                                                    'title': 'AntdHeader 页首'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdSider',
                                                                    'href': '/AntdSider',
                                                                    'title': 'AntdSider 侧边栏'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdContent',
                                                                    'href': '/AntdContent',
                                                                    'title': 'AntdContent 内容区'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdFooter',
                                                                    'href': '/AntdFooter',
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
                                                            'key': '/AntdAffix',
                                                            'href': '/AntdAffix',
                                                            'title': 'AntdAffix 固钉'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdBreadcrumb',
                                                            'href': '/AntdBreadcrumb',
                                                            'title': 'AntdBreadcrumb 面包屑'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdDropdown',
                                                            'href': '/AntdDropdown',
                                                            'title': 'AntdDropdown 下拉菜单'
                                                        }
                                                    },
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
                                                            'key': '/AntdPageHeader',
                                                            'href': '/AntdPageHeader',
                                                            'title': 'AntdPageHeader 页头'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdPagination',
                                                            'href': '/AntdPagination',
                                                            'title': 'AntdPagination 分页'
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
                                                            'title': 'AntdCascader 级联选择'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdCheckbox',
                                                            'href': '/AntdCheckbox',
                                                            'title': 'AntdCheckbox 选择框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdCheckboxGroup',
                                                            'href': '/AntdCheckboxGroup',
                                                            'title': 'AntdCheckboxGroup 组合选择框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdDatePicker',
                                                            'href': '/AntdDatePicker',
                                                            'title': 'AntdDatePicker 日期选择框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'key': 'Form',
                                                            'title': '表单'
                                                        },
                                                        'children': [
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdFormItem',
                                                                    'href': '/AntdFormItem',
                                                                    'title': 'AntdFormItem 表单项'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdForm',
                                                                    'href': '/AntdForm',
                                                                    'title': 'AntdForm 表单'
                                                                }
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdDateRangePicker',
                                                            'href': '/AntdDateRangePicker',
                                                            'title': 'AntdDateRangePicker 日期范围选择框'
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
                                                            'key': '/AntdInputNumber',
                                                            'href': '/AntdInputNumber',
                                                            'title': 'AntdInputNumber 数字输入框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdMentions',
                                                            'href': '/AntdMentions',
                                                            'title': 'AntdMentions 提及'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdRadioGroup',
                                                            'href': '/AntdRadioGroup',
                                                            'title': 'AntdRadioGroup 单选框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdRate',
                                                            'href': '/AntdRate',
                                                            'title': 'AntdRate 评分'
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
                                                            'title': 'AntdSwitch 开关'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdTimePicker',
                                                            'href': '/AntdTimePicker',
                                                            'title': 'AntdTimePicker 时间选择框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdTimeRangePicker',
                                                            'href': '/AntdTimeRangePicker',
                                                            'title': 'AntdTimeRangePicker 时间范围选择框'
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
                                                            'title': 'AntdTreeSelect 树选择'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdUpload',
                                                            'href': '/AntdUpload',
                                                            'title': 'AntdUpload 上传'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdDraggerUpload',
                                                            'href': '/AntdDraggerUpload',
                                                            'title': 'AntdDraggerUpload 拖拽上传'
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
                                                            'key': '/AntdAvatar',
                                                            'href': '/AntdAvatar',
                                                            'title': 'AntdAvatar 头像'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdBadge',
                                                            'href': '/AntdBadge',
                                                            'title': 'AntdBadge 徽标数'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdCalendar',
                                                            'href': '/AntdCalendar',
                                                            'title': 'AntdCalendar 日历'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdRibbon',
                                                            'href': '/AntdRibbon',
                                                            'title': 'AntdRibbon 缎带'
                                                        }
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'key': 'Card',
                                                            'title': '卡片'
                                                        },
                                                        'children': [
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdCardGrid',
                                                                    'href': '/AntdCardGrid',
                                                                    'title': 'AntdCardGrid 卡片网格'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdCard',
                                                                    'href': '/AntdCard',
                                                                    'title': 'AntdCard 卡片'
                                                                }
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdCarousel',
                                                            'href': '/AntdCarousel',
                                                            'title': 'AntdCarousel 走马灯'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdCollapse',
                                                            'href': '/AntdCollapse',
                                                            'title': 'AntdCollapse 折叠面板'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdComment',
                                                            'href': '/AntdComment',
                                                            'title': 'AntdComment 评论'
                                                        }
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'key': 'Descriptions',
                                                            'title': '描述列表'
                                                        },
                                                        'children': [
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdDescriptions',
                                                                    'href': '/AntdDescriptions',
                                                                    'title': 'AntdDescriptions 描述列表'
                                                                }
                                                            },
                                                            {
                                                                'component': 'Item',
                                                                'props': {
                                                                    'key': '/AntdDescriptionItem',
                                                                    'href': '/AntdDescriptionItem',
                                                                    'title': 'AntdDescriptionItem 描述列表子项'
                                                                }
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdEmpty',
                                                            'href': '/AntdEmpty',
                                                            'title': 'AntdEmpty 空状态'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdImage',
                                                            'href': '/AntdImage',
                                                            'title': 'AntdImage 图片'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdPopover',
                                                            'href': '/AntdPopover',
                                                            'title': 'AntdPopover 气泡卡片'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdStatistic',
                                                            'href': '/AntdStatistic',
                                                            'title': 'AntdStatistic 统计数值'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdCountdown',
                                                            'href': '/AntdCountdown',
                                                            'title': 'AntdCountdown 倒计时'
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
                                                            'title': 'AntdTag 标签'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdTimeline',
                                                            'href': '/AntdTimeline',
                                                            'title': 'AntdTimeline 时间轴'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdTooltip',
                                                            'href': '/AntdTooltip',
                                                            'title': 'AntdTooltip 文字提示'
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
                                                            'key': 'Tabs',
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
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdDrawer',
                                                            'href': '/AntdDrawer',
                                                            'title': 'AntdDrawer 抽屉'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdMessage',
                                                            'href': '/AntdMessage',
                                                            'title': 'AntdMessage 全局提示'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdModal',
                                                            'href': '/AntdModal',
                                                            'title': 'AntdModal 对话框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdNotification',
                                                            'href': '/AntdNotification',
                                                            'title': 'AntdNotification 通知提醒框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdPopconfirm',
                                                            'href': '/AntdPopconfirm',
                                                            'title': 'AntdPopconfirm 气泡确认框'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdProgress',
                                                            'href': '/AntdProgress',
                                                            'title': 'AntdProgress 进度条'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdResult',
                                                            'href': '/AntdResult',
                                                            'title': 'AntdResult 结果'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdSkeleton',
                                                            'href': '/AntdSkeleton',
                                                            'title': 'AntdSkeleton 骨骼屏'
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
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': '/AntdBackTop',
                                                            'href': '/AntdBackTop',
                                                            'title': 'AntdBackTop 回到顶部'
                                                        }
                                                    }
                                                ]
                                            }
                                        ],
                                        mode='inline',
                                        defaultOpenKeys=[
                                            'Card', 'Descriptions', 'Form', 'Tabs', 'Grid', 'Typography', 'Layout'
                                        ],
                                        style={
                                            'height': '100%',
                                            'overflow': 'hidden',
                                            'paddingBottom': '50px'
                                        }
                                    )
                                ],
                                width=300,
                                breakpoint='xxl',
                                collapsedWidth=0,
                                theme='light'
                            ),

                            fac.AntdContent(
                                id='docs-content',
                                style={
                                    'overflowY': 'auto',
                                    'padding': '25px',
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
    listenPropsMode='exclude',
    excludeProps=Config.exclude_props,
    size='large',
    text='文档加载中，请稍候',
    debug=True
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

    elif pathname == '/getting-started':
        return getting_started.docs_content, pathname

    elif pathname == '/AntdIcon':
        return AntdIcon.docs_content, pathname

    elif pathname == '/AntdButton':
        return AntdButton.docs_content, pathname

    elif pathname == '/AntdParagraph':
        return AntdParagraph.docs_content, pathname

    elif pathname == '/AntdText':
        return AntdText.docs_content, pathname

    elif pathname == '/AntdTitle':
        return AntdTitle.docs_content, pathname

    elif pathname == '/AntdDivider':
        return AntdDivider.docs_content, pathname

    elif pathname == '/AntdSpace':
        return AntdSpace.docs_content, pathname

    elif pathname == '/AntdRow':
        return AntdRow.docs_content, pathname

    elif pathname == '/AntdCol':
        return AntdCol.docs_content, pathname

    elif pathname == '/AntdLayout':
        return AntdLayout.docs_content, pathname

    elif pathname == '/AntdHeader':
        return AntdHeader.docs_content, pathname

    elif pathname == '/AntdSider':
        return AntdSider.docs_content, pathname

    elif pathname == '/AntdContent':
        return AntdContent.docs_content, pathname

    elif pathname == '/AntdFooter':
        return AntdFooter.docs_content, pathname

    elif pathname == '/AntdAffix':
        return AntdAffix.docs_content, pathname

    elif pathname == '/AntdBreadcrumb':
        return AntdBreadcrumb.docs_content, pathname

    elif pathname == '/AntdDropdown':
        return AntdDropdown.docs_content, pathname

    elif pathname == '/AntdMenu':
        return AntdMenu.docs_content, pathname

    elif pathname == '/AntdPagination':
        return AntdPagination.docs_content, pathname

    elif pathname == '/AntdSteps':
        return AntdSteps.docs_content, pathname

    elif pathname == '/AntdCascader':
        return AntdCascader.docs_content, pathname

    elif pathname == '/AntdCheckbox':
        return AntdCheckbox.docs_content, pathname

    elif pathname == '/AntdCheckboxGroup':
        return AntdCheckboxGroup.docs_content, pathname

    elif pathname == '/AntdDatePicker':
        return AntdDatePicker.docs_content, pathname

    elif pathname == '/AntdDateRangePicker':
        return AntdDateRangePicker.docs_content, pathname

    elif pathname == '/AntdInput':
        return AntdInput.docs_content, pathname

    elif pathname == '/AntdInputNumber':
        return AntdInputNumber.docs_content, pathname

    elif pathname == '/AntdRadioGroup':
        return AntdRadioGroup.docs_content, pathname

    elif pathname == '/AntdSelect':
        return AntdSelect.docs_content, pathname

    elif pathname == '/AntdRate':
        return AntdRate.docs_content, pathname

    elif pathname == '/AntdSlider':
        return AntdSlider.docs_content, pathname

    elif pathname == '/AntdSwitch':
        return AntdSwitch.docs_content, pathname

    elif pathname == '/AntdTransfer':
        return AntdTransfer.docs_content, pathname

    elif pathname == '/AntdTreeSelect':
        return AntdTreeSelect.docs_content, pathname

    elif pathname == '/AntdUpload':
        return AntdUpload.docs_content, pathname

    elif pathname == '/AntdDraggerUpload':
        return AntdDraggerUpload.docs_content, pathname

    elif pathname == '/AntdCollapse':
        return AntdCollapse.docs_content, pathname

    elif pathname == '/AntdEmpty':
        return AntdEmpty.docs_content, pathname

    elif pathname == '/AntdPopover':
        return AntdPopover.docs_content, pathname

    elif pathname == '/AntdStatistic':
        return AntdStatistic.docs_content, pathname

    elif pathname == '/AntdCountdown':
        return AntdCountdown.docs_content, pathname

    elif pathname == '/AntdTable':
        return AntdTable.docs_content, pathname

    elif pathname == '/AntdTag':
        return AntdTag.docs_content, pathname

    elif pathname == '/AntdTimeline':
        return AntdTimeline.docs_content, pathname

    elif pathname == '/AntdTooltip':
        return AntdTooltip.docs_content, pathname

    elif pathname == '/AntdTree':
        return AntdTree.docs_content, pathname

    elif pathname == '/AntdTabPane':
        return AntdTabPane.docs_content, pathname

    elif pathname == '/AntdTabs':
        return AntdTabs.docs_content, pathname

    elif pathname == '/AntdAlert':
        return AntdAlert.docs_content, pathname

    elif pathname == '/AntdDrawer':
        return AntdDrawer.docs_content, pathname

    elif pathname == '/AntdMessage':
        return AntdMessage.docs_content, pathname

    elif pathname == '/AntdModal':
        return AntdModal.docs_content, pathname

    elif pathname == '/AntdNotification':
        return AntdNotification.docs_content, pathname

    elif pathname == '/AntdResult':
        return AntdResult.docs_content, pathname

    elif pathname == '/AntdSkeleton':
        return AntdSkeleton.docs_content, pathname

    elif pathname == '/AntdSpin':
        return AntdSpin.docs_content, pathname

    elif pathname == '/AntdAnchor':
        return AntdAnchor.docs_content, pathname

    elif pathname == '/AntdBackTop':
        return AntdBackTop.docs_content, pathname

    elif pathname == '/AntdPopconfirm':
        return AntdPopconfirm.docs_content, pathname

    elif pathname == '/AntdProgress':
        return AntdProgress.docs_content, pathname

    elif pathname == '/AntdAvatar':
        return AntdAvatar.docs_content, pathname

    elif pathname == '/AntdBadge':
        return AntdBadge.docs_content, pathname

    elif pathname == '/AntdRibbon':
        return AntdRibbon.docs_content, pathname

    elif pathname == '/AntdTimePicker':
        return AntdTimePicker.docs_content, pathname

    elif pathname == '/AntdTimeRangePicker':
        return AntdTimeRangePicker.docs_content, pathname

    elif pathname == '/AntdCarousel':
        return AntdCarousel.docs_content, pathname

    elif pathname == '/AntdForm':
        return AntdForm.docs_content, pathname

    elif pathname == '/AntdFormItem':
        return AntdFormItem.docs_content, pathname

    elif pathname == '/AntdCardGrid':
        return AntdCardGrid.docs_content, pathname

    elif pathname == '/AntdCard':
        return AntdCard.docs_content, pathname

    elif pathname == '/AntdMentions':
        return AntdMentions.docs_content, pathname

    elif pathname == '/AntdImage':
        return AntdImage.docs_content, pathname

    elif pathname == '/AntdPageHeader':
        return AntdPageHeader.docs_content, pathname

    elif pathname == '/AntdCalendar':
        return AntdCalendar.docs_content, pathname

    elif pathname == '/AntdComment':
        return AntdComment.docs_content, pathname

    elif pathname == '/AntdDescriptions':
        return AntdDescriptions.docs_content, pathname

    elif pathname == '/AntdDescriptionItem':
        return AntdDescriptionItem.docs_content, pathname

    return pathname, pathname


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
