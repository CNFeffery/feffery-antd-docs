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
                        'comment-demo.children',
                        'icon-demo.children',
                        'input-md5-demo-output.children',
                        'collapse-demo.children',
                        'collapse-demo.is_open',
                        'upload-demo.multiple',
                        'dragger-upload-demo.multiple',
                        'side-menu.style',
                        'fold-side-menu-icon.icon',
                        'segmented-demo-output.children',
                        'check-card-demo-output.children',
                        'check-card-group-demo1-output.children',
                        'check-card-group-demo2-output.children',
                        'accordion-demo-output.children'
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
                        'title': 'Dash+fac 快速上手'
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
                        'key': '/AntdSegmented',
                        'href': '/AntdSegmented',
                        'title': 'AntdSegmented 分段控制器'
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
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': 'CheckCard',
                        'title': '选择卡片'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCheckCard',
                                'href': '/AntdCheckCard',
                                'title': 'AntdCheckCard 选择卡片'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCheckCardGroup',
                                'href': '/AntdCheckCardGroup',
                                'title': 'AntdCheckCardGroup 组合选择卡片'
                            }
                        }
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': 'Accordion',
                        'title': '手风琴'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAccordionItem',
                                'href': '/AntdAccordionItem',
                                'title': 'AntdAccordionItem 手风琴项'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAccordion',
                                'href': '/AntdAccordion',
                                'title': 'AntdAccordion 手风琴'
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
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/AntdWatermark',
                        'href': '/AntdWatermark',
                        'title': 'AntdWatermark 水印'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/AntdPasteImage',
                        'href': '/AntdPasteImage',
                        'title': 'AntdPasteImage 图片粘贴'
                    }
                }
            ]
        },
        {
            'component': 'ItemGroup',
            'props': {
                'key': 'change log',
                'title': '更新日志'
            },
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': 'v0.1.10',
                        'title': 'v0.1.10',
                        'href': '/change-log-v0.1.10'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'v0.1.9',
                        'title': 'v0.1.9',
                        'href': '/change-log-v0.1.9'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'v0.1.8',
                        'title': 'v0.1.8',
                        'href': '/change-log-v0.1.8'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'v0.1.7',
                        'title': 'v0.1.7',
                        'href': '/change-log-v0.1.7'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'v0.1.6',
                        'title': 'v0.1.6',
                        'href': '/change-log-v0.1.6'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'v0.1.5',
                        'title': 'v0.1.5',
                        'href': '/change-log-v0.1.5'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'v0.1.4',
                        'title': 'v0.1.4',
                        'href': '/change-log-v0.1.4'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'v0.1.3',
                        'title': 'v0.1.3',
                        'href': '/change-log-v0.1.3'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'v0.1.2',
                        'title': 'v0.1.2',
                        'href': '/change-log-v0.1.2'
                    }
                }
            ]
        }
    ]

    all_icons = ['md-star-half', 'md-star-border', 'md-star', 'md-people', 'md-plus-one', 'md-notifications',
                 'md-pin-drop', 'md-layers-clear', 'md-layers', 'md-edit-location', 'md-tune', 'md-transform',
                 'md-timer-off', 'md-timer', 'md-file-upload', 'md-file-download', 'md-create-new-folder',
                 'md-cloud-upload', 'md-cloud-queue', 'md-cloud-download', 'md-cloud-done', 'md-insert-chart',
                 'md-functions', 'md-format-quote', 'md-attach-file', 'md-storage', 'md-save',
                 'md-remove-circle-outline', 'md-remove-circle', 'md-remove', 'md-low-priority', 'md-link',
                 'md-gesture', 'md-forward', 'md-flag', 'md-drafts', 'md-create', 'md-content-paste', 'md-content-cut',
                 'md-content-copy', 'md-clear', 'md-block', 'md-backspace', 'md-add-box', 'md-add',
                 'md-add-circle-outline', 'md-add-circle', 'md-location-on', 'md-mail-outline', 'md-email',
                 'md-not-interested', 'md-library-books', 'md-library-add', 'md-equalizer', 'md-add-alert',
                 'md-visibility-off', 'md-visibility', 'md-verified-user', 'md-update', 'md-trending-up',
                 'md-trending-flat', 'md-trending-down', 'md-translate', 'md-toc', 'md-timeline', 'md-thumb-up',
                 'md-thumb-down', 'md-swap-vert', 'md-swap-horiz', 'md-supervisor-account', 'md-subject', 'md-settings',
                 'md-search', 'md-schedule', 'md-restore', 'md-query-builder', 'md-power-settings-new', 'md-opacity',
                 'md-note-add', 'md-lock-outline', 'md-lock-open', 'md-list', 'md-lightbulb-outline', 'md-launch',
                 'md-label-outline', 'md-label', 'md-input', 'md-info-outline', 'md-info', 'md-hourglass', 'md-home',
                 'md-history', 'md-highlight-off', 'md-help-outline', 'md-help', 'md-get-app', 'md-translate',
                 'md-fingerprint', 'md-findIn-page', 'md-favorite-border', 'md-favorite', 'md-extension', 'md-explore',
                 'md-exit-to-app', 'md-event', 'md-description', 'md-delete-forever', 'md-delete', 'md-dashboard',
                 'md-code', 'md-build', 'md-bug-report', 'md-assignment', 'md-assessment', 'md-alarm-on',
                 'md-alarm-off', 'md-alarm-add', 'md-alarm', 'md-account-circle', 'fc-vlc', 'fc-view-details',
                 'fc-upload', 'fc-tree-structure', 'fc-timeline', 'fc-template', 'fc-survey', 'fc-signature',
                 'fc-share', 'fc-services', 'fc-rules', 'fc-questions', 'fc-process', 'fc-plus', 'fc-overtime',
                 'fc-organization', 'fc-numerical-sorting21', 'fc-numerical-sorting12', 'fc-multiple-inputs',
                 'fc-mind-map', 'fc-menu', 'fc-list', 'fc-like', 'fc-like-placeholder', 'fc-info', 'fc-import',
                 'fc-image-file', 'fc-idea', 'fc-home', 'fc-high-priority', 'fc-low-priority', 'fc-genealogy',
                 'fc-full-trash', 'fc-document-search', 'fc-file', 'fc-faq', 'fc-export', 'fc-empty-trash',
                 'fc-download', 'fc-document', 'fc-deployment', 'fc-delete-database', 'fc-conference-call',
                 'fc-database', 'fc-data-protection', 'fc-data-encryption', 'fc-data-configuration', 'fc-data-backup',
                 'fc-checkmark', 'fc-cancel', 'fc-briefcase', 'fc-binoculars', 'fc-automatic',
                 'fc-alphabetical-sorting-za', 'fc-alphabetical-sorting-az', 'fc-add-database', 'fc-accept-database',
                 'fc-about', 'fc-radar-chart', 'fc-scatter-chart', 'fc-pie-chart', 'fc-line-chart', 'fc-flow-chart',
                 'fc-doughnut-chart', 'fc-bar-chart', 'fc-area-chart', 'fc-line-bar-chart', 'fc-workflow',
                 'fc-todo-list', 'fc-synchronize', 'fc-repair', 'fc-statistics', 'fc-settings', 'fc-search',
                 'fc-serial-tasks', 'fc-safe', 'fc-negative-dynamic', 'fc-positive-dynamic', 'fc-planner',
                 'fc-parallel-tasks', 'fc-org-unit', 'fc-opened-folder', 'fc-ok', 'fc-inspection', 'fc-globe',
                 'fc-folder', 'fc-electronics', 'fc-data-sheet', 'fc-command-line', 'fc-calendar', 'fc-calculator',
                 'fc-bullish', 'fc-bearish', 'fc-bookmark', 'fc-approval', 'fc-advertising', 'di-linux', 'di-python',
                 'bi-table', 'bi-analyse', 'bs-list-task', 'bs-list-check', 'bs-link', 'bs-link-45-deg',
                 'bs-envelope-open', 'bs-envelope', 'bs-alarm', 'antd-carry-out', 'antd-car', 'antd-bulb', 'antd-build',
                 'antd-bug', 'antd-bar-code', 'antd-branches', 'antd-aim', 'antd-issues-close', 'antd-ellipsis',
                 'antd-user', 'antd-unlock', 'antd-repair', 'antd-team', 'antd-sync', 'antd-setting', 'antd-send',
                 'antd-schedule', 'antd-save', 'antd-rocket', 'antd-reload', 'antd-read', 'antd-qrcode',
                 'antd-power-off', 'antd-number', 'antd-notification', 'antd-menu', 'antd-mail', 'antd-lock',
                 'antd-loading', 'antd-key', 'antd-hourglass', 'antd-global', 'antd-function', 'antd-import',
                 'antd-export', 'antd-dashboard', 'antd-control', 'antd-console-sql', 'antd-compass', 'antd-comment',
                 'antd-code', 'antd-cluster', 'antd-clear', 'antd-camera', 'antd-book', 'antd-catalog', 'antd-api',
                 'antd-alert', 'antd-account-book', 'antd-alipay', 'antd-alipay-circle', 'antd-weibo', 'antd-github',
                 'antd-fall', 'antd-rise', 'antd-stock', 'antd-home', 'antd-fund', 'antd-area-chart',
                 'antd-radar-chart', 'antd-bar-chart', 'antd-pie-chart', 'antd-box-plot', 'antd-dot-chart',
                 'antd-line-chart', 'antd-field-binary', 'antd-field-number', 'antd-field-string', 'antd-field-time',
                 'antd-file-add', 'antd-file-done', 'antd-file', 'antd-file-image', 'antd-file-markdown',
                 'antd-file-pdf', 'antd-file-protect', 'antd-file-sync', 'antd-file-text', 'antd-file-word',
                 'antd-file-zip', 'antd-filter', 'antd-fire', 'antd-woman', 'antd-arrow-up', 'antd-arrow-down',
                 'antd-arrow-left', 'antd-arrow-right', 'antd-flag', 'antd-user-add', 'antd-folder-add', 'antd-man',
                 'antd-tag', 'antd-folder', 'antd-user-delete', 'antd-trophy', 'antd-shopping-cart', 'antd-folder-open',
                 'antd-fork', 'antd-select', 'antd-tags', 'antd-thunderbolt', 'antd-sound',
                 'antd-fund-projection-screen', 'antd-funnel-plot', 'antd-gift', 'antd-robot', 'antd-pushpin',
                 'antd-printer', 'antd-phone', 'antd-picture', 'antd-idcard', 'antd-partition', 'antd-monitor',
                 'antd-more', 'antd-apartment', 'antd-money-collect', 'antd-experiment', 'antd-link', 'antd-mobile',
                 'antd-coffee', 'antd-layout', 'antd-eye', 'antd-eye-invisible', 'antd-exception', 'antd-dollar',
                 'antd-euro', 'antd-download', 'antd-environment', 'antd-deployment-unit', 'antd-crown', 'antd-desktop',
                 'antd-like', 'antd-dislike', 'antd-disconnect', 'antd-app-store', 'antd-app-store-add', 'antd-bell',
                 'antd-calculator', 'antd-calendar', 'antd-database', 'antd-history', 'antd-search', 'antd-file-search',
                 'antd-cloud', 'antd-cloud-upload', 'antd-cloud-download', 'antd-cloud-server', 'antd-cloud-sync',
                 'antd-swap', 'im-earth', 'gi-mesh-network', 'antd-rollback', 'antd-login', 'antd-logout',
                 'antd-menu-fold', 'antd-menu-unfold', 'antd-full-screen', 'antd-full-screen-exit',
                 'antd-question-circle', 'antd-plus-circle', 'antd-minus-circle', 'antd-info-circle',
                 'antd-exclamation-circle', 'antd-close-circle', 'antd-check-circle', 'antd-clock-circle', 'antd-stop',
                 'antd-edit', 'antd-delete', 'antd-highlight', 'antd-redo', 'antd-undo', 'antd-zoom-in',
                 'antd-zoom-out', 'antd-sort-ascending', 'antd-sort-descending', 'antd-table']
