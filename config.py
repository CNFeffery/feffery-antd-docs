class Config:
    exclude_props = [
                        'button-demo-output.children',
                        'menu-demo-output.children',
                        'steps-demo.current',
                        'steps-demo-current.children',
                        'date-picker-demo-output.children',
                        'date-range-picker-demo-output.children',
                        'select-demo-output.children',
                        'slider-demo-output.children',
                        'transfer-demo-output.children',
                        'table-demo-output.children',
                        'table-server-side-demo.data',
                        'table-server-side-demo.pagination',
                        'tree-demo-output.children',
                        'upload-demo-output.children',
                        'github-stars.children',
                        'spin-basic-demo-output.children',
                        'spin-delay-demo-output1.children',
                        'spin-delay-demo-output2.children',
                        'spin-include-demo-output1.children',
                        'spin-include-demo-output2.children',
                        'spin-exclude-demo-output1.children',
                        'spin-exclude-demo-output2.children',
                        'input-value-demo-output.children',
                        'input-nSubmit-demo-output.children',
                        'input-nClicksSearch-demo-output.children',
                        'tabs-demo.children',
                        'tabs-demo.activeKey',
                        'getting-started-notification-demo.children',
                        'notification-container-demo1.children',
                        'notification-container-demo2.children',
                        'notification-container-demo3.children',
                        'notification-container-demo4.children',
                        'message-container-demo1.children',
                        'message-container-demo2.children',
                        'sider-custom-trigger-demo.collapsed',
                        'pagination-demo-output.children',
                        'cascader-demo-output.children',
                        'cascader-multiple-demo-output.children',
                        'checkbox-demo-output.children',
                        'checkbox-group-demo-output.children',
                        'checkbox-demo-client-side.checked',
                        'checkbox-group-demo-client-side.value',
                        'radio-group-demo-output.children',
                        'switch-demo-output.children',
                        'tree-select-demo-output.children',
                        'drawer-demo-1.visible',
                        'drawer-demo-2-top.visible',
                        'drawer-demo-2-left.visible',
                        'drawer-demo-2-bottom.visible',
                        'modal-demo-1.visible',
                        'modal-demo-2.visible',
                        'modal-demo-2-output-1.children',
                        'modal-demo-2-output-2.children',
                        'modal-demo-2-output-3.children',
                        'popconfirm-demo-output-1.children',
                        'popconfirm-demo-output-2.children',
                        'table-button-click-demo-recentlyButtonClickedRow-output.children',
                        'table-button-click-demo-nClicksButton-output.children',
                        'table-button-click-demo-clickedContent-output.children',
                        'table-row-select-demo-selectedRowKeys-output.children',
                        'table-row-select-demo-selectedRows-output.children',
                        'table-mouse-event-demo-output.children',
                        'dragger-upload-demo-output.children',
                        'skeleton-basic-demo-output.children',
                        'skeleton-custom-demo-output.children',
                        'dropdown-demo-output.children',
                        'input-number-demo-output.children',
                        'rate-demo-output.children',
                        'statistic-demo.value',
                        'statistic-demo.prefix',
                        'statistic-demo.valueStyle',
                        'badge-demo-1.count',
                        'badge-demo-2.count'
                    ] + [
                        '{"index":%s,"type":"badge-click-demo"}.count' % i
                        for i in range(10)
                    ] + [
                        'badges-area.children',
                        'badge-click-demo-score.children',
                        'badge-click-demo-start-time.data',
                        'time-picker-demo-output.children',
                        'time-range-picker-demo-output.children',
                        'form-demo-1.validateStatus',
                        'form-demo-1.help',
                        'form-item-validate-demo-username.validateStatus',
                        'mentions-demo-output-value.children',
                        'mentions-demo-output-selectedOptions.children',
                        'page-header-demo.children',
                        'calendar-demo-output.children',
                        'comment-demo.children'
                    ]

    caches_path = './caches'

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
                    'component': 'Item',
                    'props': {
                        'key': '/AntdDateRangePicker',
                        'href': '/AntdDateRangePicker',
                        'title': 'AntdDateRangePicker 日期范围选择框'
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
    ]
