import os


class Config:

    caches_path = 'caches'

    # 顶端进度条需要纳入的监听目标
    include_props = [
        'docs-content.children'
    ]

    # 定义侧边菜单树状结构数据
    menuItems = [
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
                        'name': '/what-is-fac',
                        'href': '/what-is-fac',
                        'title': 'fac是什么？'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/getting-started',
                        'name': '/getting-started',
                        'href': '/getting-started',
                        'title': 'Dash+fac 快速上手'
                    }
                }
            ]
        },
        {
            'component': 'Divider',
            'props': {
                'dashed': True
            }
        },
        {
            'component': 'ItemGroup',
            'props': {
                'key': '组件介绍',
                'title': '组件介绍'
            },
            'children': [
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '通用',
                        'title': '通用'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdIcon',
                                'name': '/AntdIcon',
                                'title': 'AntdIcon 图标',
                                'href': '/AntdIcon'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdButton',
                                'name': '/AntdButton',
                                'title': 'AntdButton 按钮',
                                'href': '/AntdButton'
                            }
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '通用/排版相关',
                                'title': '排版相关'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdParagraph',
                                        'name': '/AntdParagraph',
                                        'title': 'AntdParagraph 段落',
                                        'href': '/AntdParagraph'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdText',
                                        'name': '/AntdText',
                                        'title': 'AntdText 文字',
                                        'href': '/AntdText'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTitle',
                                        'name': '/AntdTitle',
                                        'title': 'AntdTitle 标题',
                                        'href': '/AntdTitle'
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '布局',
                        'title': '布局'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCenter',
                                'name': '/AntdCenter',
                                'title': 'AntdCenter 居中',
                                'href': '/AntdCenter'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDivider',
                                'name': '/AntdDivider',
                                'title': 'AntdDivider 分割线',
                                'href': '/AntdDivider'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSpace',
                                'name': '/AntdSpace',
                                'title': 'AntdSpace 排列',
                                'href': '/AntdSpace'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCompact',
                                'name': '/AntdCompact',
                                'title': 'AntdCompact 紧凑排列',
                                'href': '/AntdCompact'
                            }
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '布局/网格系统',
                                'title': '网格系统'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCol',
                                        'name': '/AntdCol',
                                        'title': 'AntdCol 列',
                                        'href': '/AntdCol'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdRow',
                                        'name': '/AntdRow',
                                        'title': 'AntdRow 行',
                                        'href': '/AntdRow'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '布局/经典布局',
                                'title': '经典布局'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdLayout',
                                        'name': '/AntdLayout',
                                        'title': 'AntdLayout 布局容器',
                                        'href': '/AntdLayout'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdHeader',
                                        'name': '/AntdHeader',
                                        'title': 'AntdHeader 页首',
                                        'href': '/AntdHeader'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSider',
                                        'name': '/AntdSider',
                                        'title': 'AntdSider 侧边栏',
                                        'href': '/AntdSider'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdContent',
                                        'name': '/AntdContent',
                                        'title': 'AntdContent 内容区',
                                        'href': '/AntdContent'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdFooter',
                                        'name': '/AntdFooter',
                                        'title': 'AntdFooter 页尾',
                                        'href': '/AntdFooter'
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '导航',
                        'title': '导航'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAffix',
                                'name': '/AntdAffix',
                                'title': 'AntdAffix 固钉',
                                'href': '/AntdAffix'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdBreadcrumb',
                                'name': '/AntdBreadcrumb',
                                'title': 'AntdBreadcrumb 面包屑',
                                'href': '/AntdBreadcrumb'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDropdown',
                                'name': '/AntdDropdown',
                                'title': 'AntdDropdown 下拉菜单',
                                'href': '/AntdDropdown'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdMenu',
                                'name': '/AntdMenu',
                                'title': 'AntdMenu 导航菜单',
                                'href': '/AntdMenu'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdPageHeader',
                                'name': '/AntdPageHeader',
                                'title': 'AntdPageHeader 页头',
                                'href': '/AntdPageHeader'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdPagination',
                                'name': '/AntdPagination',
                                'title': 'AntdPagination 分页',
                                'href': '/AntdPagination'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSteps',
                                'name': '/AntdSteps',
                                'title': 'AntdSteps 步骤条',
                                'href': '/AntdSteps'
                            }
                        }
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '数据录入',
                        'title': '数据录入'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCascader',
                                'name': '/AntdCascader',
                                'title': 'AntdCascader 级联选择',
                                'href': '/AntdCascader'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCheckbox',
                                'name': '/AntdCheckbox',
                                'title': 'AntdCheckbox 选择框',
                                'href': '/AntdCheckbox'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCheckboxGroup',
                                'name': '/AntdCheckboxGroup',
                                'title': 'AntdCheckboxGroup 组合选择框',
                                'href': '/AntdCheckboxGroup'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDatePicker',
                                'name': '/AntdDatePicker',
                                'title': 'AntdDatePicker 日期选择框',
                                'href': '/AntdDatePicker'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDateRangePicker',
                                'name': '/AntdDateRangePicker',
                                'title': 'AntdDateRangePicker 日期范围选择框',
                                'href': '/AntdDateRangePicker'
                            }
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据录入/表单',
                                'title': '表单'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdFormItem',
                                        'name': '/AntdFormItem',
                                        'title': 'AntdFormItem 表单项',
                                        'href': '/AntdFormItem'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdForm',
                                        'name': '/AntdForm',
                                        'title': 'AntdForm 表单',
                                        'href': '/AntdForm'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdInput',
                                'name': '/AntdInput',
                                'title': 'AntdInput 输入框',
                                'href': '/AntdInput'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdInputNumber',
                                'name': '/AntdInputNumber',
                                'title': 'AntdInputNumber 数字输入框',
                                'href': '/AntdInputNumber'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSegmentedColoring',
                                'name': '/AntdSegmentedColoring',
                                'title': 'AntdSegmentedColoring 分段着色',
                                'href': '/AntdSegmentedColoring'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdMentions',
                                'name': '/AntdMentions',
                                'title': 'AntdMentions 提及',
                                'href': '/AntdMentions'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdRadioGroup',
                                'name': '/AntdRadioGroup',
                                'title': 'AntdRadioGroup 单选框',
                                'href': '/AntdRadioGroup'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdRate',
                                'name': '/AntdRate',
                                'title': 'AntdRate 评分',
                                'href': '/AntdRate'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSelect',
                                'name': '/AntdSelect',
                                'title': 'AntdSelect 下拉选择',
                                'href': '/AntdSelect'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSlider',
                                'name': '/AntdSlider',
                                'title': 'AntdSlider 滑动输入条',
                                'href': '/AntdSlider'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSwitch',
                                'name': '/AntdSwitch',
                                'title': 'AntdSwitch 开关',
                                'href': '/AntdSwitch'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTimePicker',
                                'name': '/AntdTimePicker',
                                'title': 'AntdTimePicker 时间选择框',
                                'href': '/AntdTimePicker'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTimeRangePicker',
                                'name': '/AntdTimeRangePicker',
                                'title': 'AntdTimeRangePicker 时间范围选择框',
                                'href': '/AntdTimeRangePicker'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTransfer',
                                'name': '/AntdTransfer',
                                'title': 'AntdTransfer 穿梭框',
                                'href': '/AntdTransfer'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTreeSelect',
                                'name': '/AntdTreeSelect',
                                'title': 'AntdTreeSelect 树选择',
                                'href': '/AntdTreeSelect'
                            }
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据录入/文件上传',
                                'title': '文件上传'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdUpload',
                                        'name': '/AntdUpload',
                                        'title': 'AntdUpload 上传',
                                        'href': '/AntdUpload'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdDraggerUpload',
                                        'name': '/AntdDraggerUpload',
                                        'title': 'AntdDraggerUpload 拖拽上传',
                                        'href': '/AntdDraggerUpload'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdPictureUpload',
                                        'name': '/AntdPictureUpload',
                                        'title': 'AntdPictureUpload 图片上传',
                                        'href': '/AntdPictureUpload'
                                    }
                                }
                            ]
                        },
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '数据展示',
                        'title': '数据展示'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAvatar',
                                'name': '/AntdAvatar',
                                'title': 'AntdAvatar 头像',
                                'href': '/AntdAvatar'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAvatarGroup',
                                'name': '/AntdAvatarGroup',
                                'title': 'AntdAvatarGroup 头像组',
                                'href': '/AntdAvatarGroup'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdBadge',
                                'name': '/AntdBadge',
                                'title': 'AntdBadge 徽标数',
                                'href': '/AntdBadge'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCalendar',
                                'name': '/AntdCalendar',
                                'title': 'AntdCalendar 日历',
                                'href': '/AntdCalendar'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdRibbon',
                                'name': '/AntdRibbon',
                                'title': 'AntdRibbon 缎带',
                                'href': '/AntdRibbon'
                            }
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据展示/卡片',
                                'title': '卡片'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCardGrid',
                                        'name': '/AntdCardGrid',
                                        'title': 'AntdCardGrid 卡片网格',
                                        'href': '/AntdCardGrid'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCard',
                                        'name': '/AntdCard',
                                        'title': 'AntdCard 卡片',
                                        'href': '/AntdCard'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCarousel',
                                'name': '/AntdCarousel',
                                'title': 'AntdCarousel 走马灯',
                                'href': '/AntdCarousel'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCollapse',
                                'name': '/AntdCollapse',
                                'title': 'AntdCollapse 折叠面板',
                                'href': '/AntdCollapse'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdComment',
                                'name': '/AntdComment',
                                'title': 'AntdComment 评论',
                                'href': '/AntdComment'
                            }
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据展示/描述列表',
                                'title': '描述列表'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdDescriptionItem',
                                        'name': '/AntdDescriptionItem',
                                        'title': 'AntdDescriptionItem 描述列表项',
                                        'href': '/AntdDescriptionItem'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdDescriptions',
                                        'name': '/AntdDescriptions',
                                        'title': 'AntdDescriptions 描述列表',
                                        'href': '/AntdDescriptions'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdEmpty',
                                'name': '/AntdEmpty',
                                'title': 'AntdEmpty 空状态',
                                'href': '/AntdEmpty'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdImage',
                                'name': '/AntdImage',
                                'title': 'AntdImage 图片',
                                'href': '/AntdImage'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdPopover',
                                'name': '/AntdPopover',
                                'title': 'AntdPopover 气泡卡片',
                                'href': '/AntdPopover'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdPopupCard',
                                'name': '/AntdPopupCard',
                                'title': 'AntdPopupCard 弹出式卡片',
                                'href': '/AntdPopupCard'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSegmented',
                                'name': '/AntdSegmented',
                                'title': 'AntdSegmented 分段控制器',
                                'href': '/AntdSegmented'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSpoiler',
                                'name': '/AntdSpoiler',
                                'title': 'AntdSpoiler 展开收起',
                                'href': '/AntdSpoiler'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdStatistic',
                                'name': '/AntdStatistic',
                                'title': 'AntdStatistic 统计数值',
                                'href': '/AntdStatistic'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCountdown',
                                'name': '/AntdCountdown',
                                'title': 'AntdCountdown 倒计时',
                                'href': '/AntdCountdown'
                            }
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据展示/表格',
                                'title': 'AntdTable 表格'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTable-basic',
                                        'name': '/AntdTable-basic',
                                        'title': '基础功能',
                                        'href': '/AntdTable-basic'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTable-advanced',
                                        'name': '/AntdTable-advanced',
                                        'title': '进阶功能',
                                        'href': '/AntdTable-advanced'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTable-server-side-mode',
                                        'name': '/AntdTable-server-side-mode',
                                        'title': '服务端数据加载模式',
                                        'href': '/AntdTable-server-side-mode'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTable-rerender',
                                        'name': '/AntdTable-rerender',
                                        'title': '再渲染模式',
                                        'href': '/AntdTable-rerender'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTag',
                                'name': '/AntdTag',
                                'title': 'AntdTag 标签',
                                'href': '/AntdTag'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTimeline',
                                'name': '/AntdTimeline',
                                'title': 'AntdTimeline 时间轴',
                                'href': '/AntdTimeline'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTooltip',
                                'name': '/AntdTooltip',
                                'title': 'AntdTooltip 文字提示',
                                'href': '/AntdTooltip'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTree',
                                'name': '/AntdTree',
                                'title': 'AntdTree 树形控件',
                                'href': '/AntdTree'
                            }
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据展示/标签页',
                                'title': '标签页'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTabPane',
                                        'name': '/AntdTabPane',
                                        'title': 'AntdTabPane 标签页面板',
                                        'href': '/AntdTabPane'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTabs',
                                        'name': '/AntdTabs',
                                        'title': 'AntdTabs 标签页',
                                        'href': '/AntdTabs'
                                    }
                                },
                            ]
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据展示/选择卡片',
                                'title': '选择卡片'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCheckCard',
                                        'name': '/AntdCheckCard',
                                        'title': 'AntdCheckCard 选择卡片',
                                        'href': '/AntdCheckCard'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCheckCardGroup',
                                        'name': '/AntdCheckCardGroup',
                                        'title': 'AntdCheckCardGroup 组合选择卡片',
                                        'href': '/AntdCheckCardGroup'
                                    }
                                },
                            ]
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAccordion',
                                'name': '/AntdAccordion',
                                'title': 'AntdAccordion 手风琴',
                                'href': '/AntdAccordion'
                            }
                        }
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '反馈',
                        'title': '反馈'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAlert',
                                'name': '/AntdAlert',
                                'title': 'AntdAlert 警告提示',
                                'href': '/AntdAlert'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDrawer',
                                'name': '/AntdDrawer',
                                'title': 'AntdDrawer 抽屉',
                                'href': '/AntdDrawer'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdMessage',
                                'name': '/AntdMessage',
                                'title': 'AntdMessage 全局提示',
                                'href': '/AntdMessage'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdModal',
                                'name': '/AntdModal',
                                'title': 'AntdModal 对话框',
                                'href': '/AntdModal'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdNotification',
                                'name': '/AntdNotification',
                                'title': 'AntdNotification 通知提醒框',
                                'href': '/AntdNotification'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdPopconfirm',
                                'name': '/AntdPopconfirm',
                                'title': 'AntdPopconfirm 气泡确认框',
                                'href': '/AntdPopconfirm'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdProgress',
                                'name': '/AntdProgress',
                                'title': 'AntdProgress 进度条',
                                'href': '/AntdProgress'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdResult',
                                'name': '/AntdResult',
                                'title': 'AntdResult 结果',
                                'href': '/AntdResult'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSkeleton',
                                'name': '/AntdSkeleton',
                                'title': 'AntdSkeleton 骨架屏',
                                'href': '/AntdSkeleton'
                            }
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '反馈/自定义骨架屏',
                                'title': '自定义骨架屏'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCustomSkeleton',
                                        'name': '/AntdCustomSkeleton',
                                        'title': 'AntdCustomSkeleton 自定义骨架屏',
                                        'href': '/AntdCustomSkeleton'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSkeletonAvatar',
                                        'name': '/AntdSkeletonAvatar',
                                        'title': 'AntdSkeletonAvatar 头像占位图',
                                        'href': '/AntdSkeletonAvatar'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSkeletonButton',
                                        'name': '/AntdSkeletonButton',
                                        'title': 'AntdSkeletonButton 按钮占位图',
                                        'href': '/AntdSkeletonButton'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSkeletonImage',
                                        'name': '/AntdSkeletonImage',
                                        'title': 'AntdSkeletonImage 图片占位图',
                                        'href': '/AntdSkeletonImage'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSkeletonInput',
                                        'name': '/AntdSkeletonInput',
                                        'title': 'AntdSkeletonInput 输入框占位图',
                                        'href': '/AntdSkeletonInput'
                                    }
                                },
                            ]
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSpin',
                                'name': '/AntdSpin',
                                'title': 'AntdSpin 加载动画',
                                'href': '/AntdSpin'
                            }
                        },
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '其他',
                        'title': '其他'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAnchor',
                                'name': '/AntdAnchor',
                                'title': 'AntdAnchor 锚点',
                                'href': '/AntdAnchor'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdBackTop',
                                'name': '/AntdBackTop',
                                'title': 'AntdBackTop 回到顶部',
                                'href': '/AntdBackTop'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdConfigProvider',
                                'name': '/AntdConfigProvider',
                                'title': 'AntdConfigProvider 全局配置',
                                'href': '/AntdConfigProvider'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCopyText',
                                'name': '/AntdCopyText',
                                'title': 'AntdCopyText 文本复制',
                                'href': '/AntdCopyText'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdWatermark',
                                'name': '/AntdWatermark',
                                'title': 'AntdWatermark 水印',
                                'href': '/AntdWatermark'
                            }
                        },
                    ]
                }
            ]
        },
        {
            'component': 'Divider',
            'props': {
                'dashed': True
            }
        },
        {
            'component': 'ItemGroup',
            'props': {
                'key': '进阶使用',
                'title': '进阶使用'
            },
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': '/advanced-classname',
                        'name': '/advanced-classname',
                        'title': '进阶className的使用',
                        'href': '/advanced-classname'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/popup-container',
                        'name': '/popup-container',
                        'title': '弹出层容器设置',
                        'href': '/popup-container'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/internationalization',
                        'name': '/internationalization',
                        'title': '国际化',
                        'href': '/internationalization'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/prop-persistence',
                        'name': '/prop-persistence',
                        'title': '属性持久化',
                        'href': '/prop-persistence'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/use-key-to-refresh',
                        'name': '/use-key-to-refresh',
                        'title': '强制刷新组件',
                        'href': '/use-key-to-refresh'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/batch-props-values',
                        'name': '/batch-props-values',
                        'title': '属性批量监听',
                        'href': '/batch-props-values'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/import-alias',
                        'name': '/import-alias',
                        'title': '组件按别名导入',
                        'href': '/import-alias'
                    }
                }
            ]
        },
        {
            'component': 'ItemGroup',
            'props': {
                'key': '更新日志',
                'title': '更新日志'
            },
            'children': [
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': 'v0.2.x',
                        'title': 'v0.2.x'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/change-log-v0.2.10',
                                'title': 'v0.2.10',
                                'href': '/change-log-v0.2.10'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/change-log-v0.2.9',
                                'title': 'v0.2.9',
                                'href': '/change-log-v0.2.9'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/change-log-v0.2.8',
                                'title': 'v0.2.8',
                                'href': '/change-log-v0.2.8'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/change-log-v0.2.7',
                                'title': 'v0.2.7',
                                'href': '/change-log-v0.2.7'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/change-log-v0.2.6',
                                'title': 'v0.2.6',
                                'href': '/change-log-v0.2.6'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/change-log-v0.2.5',
                                'title': 'v0.2.5',
                                'href': '/change-log-v0.2.5'
                            }
                        }
                    ]
                }
            ]
        }
    ]

    # 定义位于折叠菜单中的菜单项默认需展开菜单key值列表
    key2open_keys = {
        '/AntdIcon': ['通用'],
        '/AntdButton': ['通用'],
        '/AntdParagraph': ['通用', '通用/排版相关'],
        '/AntdText': ['通用', '通用/排版相关'],
        '/AntdTitle': ['通用', '通用/排版相关'],
        '/AntdCenter': ['布局'],
        '/AntdDivider': ['布局'],
        '/AntdSpace': ['布局'],
        '/AntdCompact': ['布局'],
        '/AntdCol': ['布局', '布局/网格系统'],
        '/AntdRow': ['布局', '布局/网格系统'],
        '/AntdLayout': ['布局', '布局/经典布局'],
        '/AntdHeader': ['布局', '布局/经典布局'],
        '/AntdSider': ['布局', '布局/经典布局'],
        '/AntdContent': ['布局', '布局/经典布局'],
        '/AntdFooter': ['布局', '布局/经典布局'],
        '/AntdAffix': ['导航'],
        '/AntdBreadcrumb': ['导航'],
        '/AntdDropdown': ['导航'],
        '/AntdMenu': ['导航'],
        '/AntdPageHeader': ['导航'],
        '/AntdPagination': ['导航'],
        '/AntdSteps': ['导航'],
        '/AntdCascader': ['数据录入'],
        '/AntdCheckbox': ['数据录入'],
        '/AntdCheckboxGroup': ['数据录入'],
        '/AntdDatePicker': ['数据录入'],
        '/AntdDateRangePicker': ['数据录入'],
        '/AntdFormItem': ['数据录入', '数据录入/表单'],
        '/AntdForm': ['数据录入', '数据录入/表单'],
        '/AntdInput': ['数据录入'],
        '/AntdInputNumber': ['数据录入'],
        '/AntdSegmentedColoring': ['数据录入'],
        '/AntdMentions': ['数据录入'],
        '/AntdRadioGroup': ['数据录入'],
        '/AntdRate': ['数据录入'],
        '/AntdSelect': ['数据录入'],
        '/AntdSlider': ['数据录入'],
        '/AntdSwitch': ['数据录入'],
        '/AntdTimePicker': ['数据录入'],
        '/AntdTimeRangePicker': ['数据录入'],
        '/AntdTransfer': ['数据录入'],
        '/AntdTreeSelect': ['数据录入'],
        '/AntdUpload': ['数据录入', '数据录入/文件上传'],
        '/AntdDraggerUpload': ['数据录入', '数据录入/文件上传'],
        '/AntdPictureUpload': ['数据录入', '数据录入/文件上传'],
        '/AntdAvatar': ['数据展示'],
        '/AntdAvatarGroup': ['数据展示'],
        '/AntdBadge': ['数据展示'],
        '/AntdCalendar': ['数据展示'],
        '/AntdRibbon': ['数据展示'],
        '/AntdCardGrid': ['数据展示', '数据展示/卡片'],
        '/AntdCard': ['数据展示', '数据展示/卡片'],
        '/AntdCarousel': ['数据展示'],
        '/AntdCollapse': ['数据展示'],
        '/AntdComment': ['数据展示'],
        '/AntdDescriptionItem': ['数据展示', '数据展示/描述列表'],
        '/AntdDescriptions': ['数据展示', '数据展示/描述列表'],
        '/AntdEmpty': ['数据展示'],
        '/AntdImage': ['数据展示'],
        '/AntdPopover': ['数据展示'],
        '/AntdPopupCard': ['数据展示'],
        '/AntdSegmented': ['数据展示'],
        '/AntdSpoiler': ['数据展示'],
        '/AntdStatistic': ['数据展示'],
        '/AntdCountdown': ['数据展示'],
        '/AntdTable-basic': ['数据展示', '数据展示/表格'],
        '/AntdTable-advanced': ['数据展示', '数据展示/表格'],
        '/AntdTable-server-side-mode': ['数据展示', '数据展示/表格'],
        '/AntdTable-rerender': ['数据展示', '数据展示/表格'],
        '/AntdTag': ['数据展示'],
        '/AntdTimeline': ['数据展示'],
        '/AntdTooltip': ['数据展示'],
        '/AntdTree': ['数据展示'],
        '/AntdTabPane': ['数据展示', '数据展示/标签页'],
        '/AntdTabs': ['数据展示', '数据展示/标签页'],
        '/AntdCheckCard': ['数据展示', '数据展示/选择卡片'],
        '/AntdCheckCardGroup': ['数据展示', '数据展示/选择卡片'],
        '/AntdAccordion': ['数据展示'],
        '/AntdAlert': ['反馈'],
        '/AntdDrawer': ['反馈'],
        '/AntdMessage': ['反馈'],
        '/AntdModal': ['反馈'],
        '/AntdNotification': ['反馈'],
        '/AntdPopconfirm': ['反馈'],
        '/AntdProgress': ['反馈'],
        '/AntdResult': ['反馈'],
        '/AntdSkeleton': ['反馈'],
        '/AntdCustomSkeleton': ['反馈', '反馈/自定义骨架屏'],
        '/AntdSkeletonAvatar': ['反馈', '反馈/自定义骨架屏'],
        '/AntdSkeletonButton': ['反馈', '反馈/自定义骨架屏'],
        '/AntdSkeletonImage': ['反馈', '反馈/自定义骨架屏'],
        '/AntdSkeletonInput': ['反馈', '反馈/自定义骨架屏'],
        '/AntdSpin': ['反馈'],
        '/AntdAnchor': ['其他'],
        '/AntdBackTop': ['其他'],
        '/AntdConfigProvider': ['其他'],
        '/AntdCopyText': ['其他'],
        '/AntdWatermark': ['其他'],
    }

    # 注入侧边菜单栏默认展开子菜单
    side_menu_open_keys = [
        # '通用',
        # '通用/排版相关',
        # '布局',
        # '布局/网格系统',
        # '布局/经典布局',
        # '导航',
        # '数据录入',
        # '数据录入/表单',
        # '数据录入/文件上传',
        # '数据展示',
        # '数据展示/卡片',
        # '数据展示/描述列表',
        # '数据展示/标签页',
        # '数据展示/选择卡片',
        # '数据展示/手风琴',
        # '反馈',
        # '反馈/自定义骨架屏',
    ]

    # AntdIcon中所有类型图标的名称
    icon_map_dict = {
        'antd': [
            'antd-carry-out',
            'antd-car',
            'antd-bulb',
            'antd-build',
            'antd-bug',
            'antd-bar-code',
            'antd-branches',
            'antd-aim',
            'antd-issues-close',
            'antd-ellipsis',
            'antd-user',
            'antd-unlock',
            'antd-repair',
            'antd-team',
            'antd-sync',
            'antd-setting',
            'antd-send',
            'antd-schedule',
            'antd-save',
            'antd-rocket',
            'antd-reload',
            'antd-read',
            'antd-qrcode',
            'antd-power-off',
            'antd-number',
            'antd-notification',
            'antd-menu',
            'antd-mail',
            'antd-lock',
            'antd-loading',
            'antd-key',
            'antd-hourglass',
            'antd-global',
            'antd-function',
            'antd-import',
            'antd-export',
            'antd-dashboard',
            'antd-control',
            'antd-console-sql',
            'antd-compass',
            'antd-comment',
            'antd-code',
            'antd-cluster',
            'antd-clear',
            'antd-camera',
            'antd-book',
            'antd-catalog',
            'antd-api',
            'antd-alert',
            'antd-account-book',
            'antd-alipay',
            'antd-alipay-circle',
            'antd-weibo',
            'antd-github',
            'antd-fall',
            'antd-rise',
            'antd-stock',
            'antd-home',
            'antd-fund',
            'antd-area-chart',
            'antd-radar-chart',
            'antd-bar-chart',
            'antd-pie-chart',
            'antd-box-plot',
            'antd-dot-chart',
            'antd-line-chart',
            'antd-field-binary',
            'antd-field-number',
            'antd-field-string',
            'antd-field-time',
            'antd-file-add',
            'antd-file-done',
            'antd-file',
            'antd-file-image',
            'antd-file-markdown',
            'antd-file-pdf',
            'antd-file-protect',
            'antd-file-sync',
            'antd-file-text',
            'antd-file-word',
            'antd-file-zip',
            'antd-filter',
            'antd-fire',
            'antd-woman',
            'antd-arrow-up',
            'antd-arrow-down',
            'antd-arrow-left',
            'antd-arrow-right',
            'antd-flag',
            'antd-user-add',
            'antd-folder-add',
            'antd-man',
            'antd-tag',
            'antd-folder',
            'antd-user-delete',
            'antd-trophy',
            'antd-shopping-cart',
            'antd-folder-open',
            'antd-fork',
            'antd-select',
            'antd-tags',
            'antd-thunderbolt',
            'antd-sound',
            'antd-fund-projection-screen',
            'antd-funnel-plot',
            'antd-gift',
            'antd-robot',
            'antd-pushpin',
            'antd-printer',
            'antd-phone',
            'antd-picture',
            'antd-idcard',
            'antd-partition',
            'antd-monitor',
            'antd-more',
            'antd-apartment',
            'antd-money-collect',
            'antd-experiment',
            'antd-link',
            'antd-mobile',
            'antd-coffee',
            'antd-layout',
            'antd-eye',
            'antd-eye-invisible',
            'antd-exception',
            'antd-dollar',
            'antd-euro',
            'antd-download',
            'antd-environment',
            'antd-deployment-unit',
            'antd-crown',
            'antd-desktop',
            'antd-like',
            'antd-dislike',
            'antd-disconnect',
            'antd-app-store',
            'antd-app-store-add',
            'antd-bell',
            'antd-calculator',
            'antd-calendar',
            'antd-database',
            'antd-history',
            'antd-search',
            'antd-file-search',
            'antd-cloud',
            'antd-cloud-upload',
            'antd-cloud-download',
            'antd-cloud-server',
            'antd-cloud-sync',
            'antd-swap',
            'antd-rollback',
            'antd-login',
            'antd-logout',
            'antd-menu-fold',
            'antd-menu-unfold',
            'antd-full-screen',
            'antd-full-screen-exit',
            'antd-question-circle',
            'antd-plus-circle',
            'antd-minus-circle',
            'antd-info-circle',
            'antd-exclamation-circle',
            'antd-close-circle',
            'antd-check-circle',
            'antd-clock-circle',
            'antd-stop',
            'antd-edit',
            'antd-delete',
            'antd-highlight',
            'antd-redo',
            'antd-undo',
            'antd-zoom-in',
            'antd-zoom-out',
            'antd-sort-ascending',
            'antd-sort-descending',
            'antd-table',
            'antd-question',
            'antd-plus',
            'antd-minus',
            'antd-close',
            'antd-check',
            'antd-sketch',
            'antd-bank',
            'antd-block',
            'antd-insurance',
            'antd-smile',
            'antd-skin',
            'antd-star',
            'antd-right-circle-two-tone',
            'antd-left-circle-two-tone',
            'antd-up-circle-two-tone',
            'antd-down-circle-two-tone',
            'antd-up-square-two-tone',
            'antd-down-square-two-tone',
            'antd-left-square-two-tone',
            'antd-right-square-two-tone',
            'antd-question-circle-two-tone',
            'antd-plus-circle-two-tone',
            'antd-minus-circle-two-tone',
            'antd-plus-square-two-tone',
            'antd-minus-square-two-tone',
            'antd-info-circle-two-tone',
            'antd-exclamation-circle-two-tone',
            'antd-close-circle-two-tone',
            'antd-close-square-two-tone',
            'antd-check-circle-two-tone',
            'antd-check-square-two-tone',
            'antd-edit-two-tone',
            'antd-delete-two-tone',
            'antd-highlight-two-tone',
            'antd-pie-chart-two-tone',
            'antd-box-chart-two-tone',
            'antd-fund-two-tone',
            'antd-sliders-two-tone',
            'antd-api-two-tone',
            'antd-cloud-two-tone',
            'antd-hourglass-two-tone',
            'antd-notification-two-tone',
            'antd-tool-two-tone',
            'antd-down',
            'antd-up',
            'antd-left',
            'antd-right',
            'antd-caret-up',
            'antd-caret-down',
            'antd-caret-left',
            'antd-caret-right',
            'antd-up-circle',
            'antd-down-circle',
            'antd-left-circle',
            'antd-right-circle',
            'antd-enter',
            'antd-retweet',
            'antd-warning',
            'antd-form',
            'antd-copy',
            'antd-scissor',
            'antd-snippets',
            'antd-diff',
            'antd-ordered-list',
            'antd-unordered-list',
            'antd-sliders',
            'antd-audit',
            'antd-border',
            'antd-contacts',
            'antd-container',
            'antd-delivered-procedure'
        ],
        'md': [
            'md-star-half',
            'md-star-border',
            'md-star',
            'md-people',
            'md-plus-one',
            'md-notifications',
            'md-pin-drop',
            'md-layers-clear',
            'md-layers',
            'md-edit-location',
            'md-tune',
            'md-transform',
            'md-timer-off',
            'md-timer',
            'md-file-upload',
            'md-file-download',
            'md-create-new-folder',
            'md-cloud-upload',
            'md-cloud-queue',
            'md-cloud-download',
            'md-cloud-done',
            'md-insert-chart',
            'md-functions',
            'md-format-quote',
            'md-attach-file',
            'md-storage',
            'md-save',
            'md-remove-circle-outline',
            'md-remove-circle',
            'md-remove',
            'md-low-priority',
            'md-link',
            'md-gesture',
            'md-forward',
            'md-flag',
            'md-drafts',
            'md-create',
            'md-content-paste',
            'md-content-cut',
            'md-content-copy',
            'md-clear',
            'md-block',
            'md-backspace',
            'md-add-box',
            'md-add',
            'md-add-circle-outline',
            'md-add-circle',
            'md-location-on',
            'md-mail-outline',
            'md-email',
            'md-not-interested',
            'md-library-books',
            'md-library-add',
            'md-equalizer',
            'md-add-alert',
            'md-visibility-off',
            'md-visibility',
            'md-verified-user',
            'md-update',
            'md-trending-up',
            'md-trending-flat',
            'md-trending-down',
            'md-translate',
            'md-toc',
            'md-timeline',
            'md-thumb-up',
            'md-thumb-down',
            'md-swap-vert',
            'md-swap-horiz',
            'md-supervisor-account',
            'md-subject',
            'md-settings',
            'md-search',
            'md-schedule',
            'md-restore',
            'md-query-builder',
            'md-power-settings-new',
            'md-opacity',
            'md-note-add',
            'md-lock-outline',
            'md-lock-open',
            'md-list',
            'md-lightbulb-outline',
            'md-launch',
            'md-label-outline',
            'md-label',
            'md-input',
            'md-info-outline',
            'md-info',
            'md-hourglass',
            'md-home',
            'md-history',
            'md-highlight-off',
            'md-help-outline',
            'md-help',
            'md-get-app',
            'md-translate',
            'md-fingerprint',
            'md-findIn-page',
            'md-favorite-border',
            'md-favorite',
            'md-extension',
            'md-explore',
            'md-exit-to-app',
            'md-event',
            'md-description',
            'md-delete-forever',
            'md-delete',
            'md-dashboard',
            'md-code',
            'md-build',
            'md-bug-report',
            'md-assignment',
            'md-assessment',
            'md-alarm-on',
            'md-alarm-off',
            'md-alarm-add',
            'md-alarm',
            'md-account-circle',
        ],
        'fc': [
            'fc-vlc',
            'fc-view-details',
            'fc-upload',
            'fc-tree-structure',
            'fc-timeline',
            'fc-template',
            'fc-survey',
            'fc-signature',
            'fc-share',
            'fc-services',
            'fc-rules',
            'fc-questions',
            'fc-process',
            'fc-plus',
            'fc-overtime',
            'fc-organization',
            'fc-numerical-sorting21',
            'fc-numerical-sorting12',
            'fc-multiple-inputs',
            'fc-mind-map',
            'fc-menu',
            'fc-list',
            'fc-like',
            'fc-like-placeholder',
            'fc-info',
            'fc-import',
            'fc-image-file',
            'fc-idea',
            'fc-home',
            'fc-high-priority',
            'fc-low-priority',
            'fc-genealogy',
            'fc-full-trash',
            'fc-document-search',
            'fc-file',
            'fc-faq',
            'fc-export',
            'fc-empty-trash',
            'fc-download',
            'fc-document',
            'fc-deployment',
            'fc-delete-database',
            'fc-conference-call',
            'fc-database',
            'fc-data-protection',
            'fc-data-encryption',
            'fc-data-configuration',
            'fc-data-backup',
            'fc-checkmark',
            'fc-cancel',
            'fc-briefcase',
            'fc-binoculars',
            'fc-automatic',
            'fc-alphabetical-sorting-za',
            'fc-alphabetical-sorting-az',
            'fc-add-database',
            'fc-accept-database',
            'fc-about',
            'fc-radar-chart',
            'fc-scatter-chart',
            'fc-pie-chart',
            'fc-line-chart',
            'fc-flow-chart',
            'fc-doughnut-chart',
            'fc-bar-chart',
            'fc-area-chart',
            'fc-line-bar-chart',
            'fc-workflow',
            'fc-todo-list',
            'fc-synchronize',
            'fc-repair',
            'fc-statistics',
            'fc-settings',
            'fc-search',
            'fc-serial-tasks',
            'fc-safe',
            'fc-negative-dynamic',
            'fc-positive-dynamic',
            'fc-planner',
            'fc-parallel-tasks',
            'fc-org-unit',
            'fc-opened-folder',
            'fc-ok',
            'fc-inspection',
            'fc-globe',
            'fc-folder',
            'fc-electronics',
            'fc-data-sheet',
            'fc-command-line',
            'fc-calendar',
            'fc-calculator',
            'fc-bullish',
            'fc-bearish',
            'fc-bookmark',
            'fc-approval',
            'fc-advertising',
        ],
        'di': [
            'di-linux',
            'di-python',
            'di-chrome',
            'di-database',
            'di-firefox',
            'di-markdown',
            'di-postgresql',
            'di-terminal',
            'di-windows',
        ],
        'bi': [
            'bi-table',
            'bi-analyse',
            'bi-layer',
            'bi-layer-minus',
            'bi-layer-plus',
        ],
        'bs': [
            'bs-list-task',
            'bs-list-check',
            'bs-link',
            'bs-link-45-deg',
            'bs-envelope-open',
            'bs-envelope',
            'bs-alarm',
        ],
        'gi': [
            'gi-mesh-network'
        ],
        'im': [
            'im-earth',
            'im-sphere'
        ]
    }
