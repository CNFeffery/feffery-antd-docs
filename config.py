import json
import feffery_antd_components as fac


class DeployConfig:
    """
    应用部署相关参数
    """

    # CDN模块名列表
    cdn_modules = [
        'DashRenderer',
        'dash_html_components',
        'dash_core_components',
        'feffery_antd_components',
        'feffery_utils_components',
        'feffery_markdown_components',
    ]


class AppConfig:
    """
    应用常规参数配置
    """

    # 应用默认标签页标题
    title = 'feffery-antd-components在线文档'

    # 应用logo地址
    logo_path = 'imgs/fac-logo.svg'

    # 页首标题
    page_header_title = 'feffery-antd-components'

    # 当前组件版本
    library_version = fac.__version__

    # 组件仓库地址
    library_repo = 'https://github.com/CNFeffery/feffery-antd-components'

    # 文档仓库地址
    doc_library_repo = 'https://github.com/CNFeffery/feffery-antd-docs'

    # 文档Gitee仓库地址
    doc_gitee_library_repo = 'https://gitee.com/cnfeffery/feffery-antd-docs'

    # 文档仓库分支名称
    doc_library_branch = 'fac0.3.x'

    # 当前应用是否为正式发布模式
    is_release = False

    # 文档贡献者信息
    doc_contributors = json.load(open('./public/contributors.json'))

    # 侧边菜单栏数据结构
    side_menu_items = [
        {
            'component': 'ItemGroup',
            'props': {'key': '快速入门', 'title': '快速入门'},
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': '/what-is-fac',
                        'name': '/what-is-fac',
                        'href': '/what-is-fac',
                        'title': 'fac是什么',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/getting-started',
                        'name': '/getting-started',
                        'href': '/getting-started',
                        'title': 'Dash+fac快速上手',
                    },
                },
            ],
        },
        {'component': 'Divider', 'props': {'dashed': True}},
        {
            'component': 'ItemGroup',
            'props': {'key': '组件介绍', 'title': '组件介绍'},
            'children': [
                {
                    'component': 'SubMenu',
                    'props': {'key': '通用', 'title': '通用'},
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdButton',
                                'name': '/AntdButton',
                                'title': 'AntdButton 按钮',
                                'href': '/AntdButton',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdFloatButton',
                                'name': '/AntdFloatButton',
                                'title': 'AntdFloatButton 悬浮按钮',
                                'href': '/AntdFloatButton',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdFloatButtonGroup',
                                'name': '/AntdFloatButtonGroup',
                                'title': 'AntdFloatButtonGroup 悬浮按钮组',
                                'href': '/AntdFloatButtonGroup',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdIcon',
                                'name': '/AntdIcon',
                                'title': 'AntdIcon 图标',
                                'href': '/AntdIcon',
                            },
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '通用/排版相关',
                                'title': '排版相关',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdParagraph',
                                        'name': '/AntdParagraph',
                                        'title': 'AntdParagraph 段落',
                                        'href': '/AntdParagraph',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdText',
                                        'name': '/AntdText',
                                        'title': 'AntdText 文字',
                                        'href': '/AntdText',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTitle',
                                        'name': '/AntdTitle',
                                        'title': 'AntdTitle 标题',
                                        'href': '/AntdTitle',
                                    },
                                },
                            ],
                        },
                    ],
                },
                {
                    'component': 'SubMenu',
                    'props': {'key': '布局', 'title': '布局'},
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCenter',
                                'name': '/AntdCenter',
                                'title': 'AntdCenter 居中',
                                'href': '/AntdCenter',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDivider',
                                'name': '/AntdDivider',
                                'title': 'AntdDivider 分割线',
                                'href': '/AntdDivider',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdFlex',
                                'name': '/AntdFlex',
                                'title': 'AntdFlex 弹性布局',
                                'href': '/AntdFlex',
                            },
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '布局/网格系统',
                                'title': '网格系统',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdRow',
                                        'name': '/AntdRow',
                                        'title': 'AntdRow 行',
                                        'href': '/AntdRow',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCol',
                                        'name': '/AntdCol',
                                        'title': 'AntdCol 列',
                                        'href': '/AntdCol',
                                    },
                                },
                            ],
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSpace',
                                'name': '/AntdSpace',
                                'title': 'AntdSpace 排列',
                                'href': '/AntdSpace',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCompact',
                                'name': '/AntdCompact',
                                'title': 'AntdCompact 紧凑排列',
                                'href': '/AntdCompact',
                            },
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '布局/经典布局',
                                'title': '经典布局',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdLayout',
                                        'name': '/AntdLayout',
                                        'title': 'AntdLayout 布局容器',
                                        'href': '/AntdLayout',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdHeader',
                                        'name': '/AntdHeader',
                                        'title': 'AntdHeader 页首',
                                        'href': '/AntdHeader',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdContent',
                                        'name': '/AntdContent',
                                        'title': 'AntdContent 内容区',
                                        'href': '/AntdContent',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdFooter',
                                        'name': '/AntdFooter',
                                        'title': 'AntdFooter 页尾',
                                        'href': '/AntdFooter',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSider',
                                        'name': '/AntdSider',
                                        'title': 'AntdSider 侧边栏',
                                        'href': '/AntdSider',
                                    },
                                },
                            ],
                        },
                    ],
                },
                {
                    'component': 'SubMenu',
                    'props': {'key': '导航', 'title': '导航'},
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAnchor',
                                'name': '/AntdAnchor',
                                'title': 'AntdAnchor 锚点',
                                'href': '/AntdAnchor',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdBreadcrumb',
                                'name': '/AntdBreadcrumb',
                                'title': 'AntdBreadcrumb 面包屑',
                                'href': '/AntdBreadcrumb',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDropdown',
                                'name': '/AntdDropdown',
                                'title': 'AntdDropdown 下拉菜单',
                                'href': '/AntdDropdown',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdMenu',
                                'name': '/AntdMenu',
                                'title': 'AntdMenu 导航菜单',
                                'href': '/AntdMenu',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdPageHeader',
                                'name': '/AntdPageHeader',
                                'title': 'AntdPageHeader 页头',
                                'href': '/AntdPageHeader',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdPagination',
                                'name': '/AntdPagination',
                                'title': 'AntdPagination 分页',
                                'href': '/AntdPagination',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSteps',
                                'name': '/AntdSteps',
                                'title': 'AntdSteps 步骤条',
                                'href': '/AntdSteps',
                            },
                        },
                    ],
                },
                {
                    'component': 'SubMenu',
                    'props': {'key': '数据录入', 'title': '数据录入'},
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCalendar',
                                'name': '/AntdCalendar',
                                'title': 'AntdCalendar 日历',
                                'href': '/AntdCalendar',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCascader',
                                'name': '/AntdCascader',
                                'title': 'AntdCascader 级联选择',
                                'href': '/AntdCascader',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCheckbox',
                                'name': '/AntdCheckbox',
                                'title': 'AntdCheckbox 选择框',
                                'href': '/AntdCheckbox',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCheckboxGroup',
                                'name': '/AntdCheckboxGroup',
                                'title': 'AntdCheckboxGroup 组合选择框',
                                'href': '/AntdCheckboxGroup',
                            },
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据录入/选择卡片',
                                'title': '选择卡片',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCheckCard',
                                        'name': '/AntdCheckCard',
                                        'title': 'AntdCheckCard 选择卡片',
                                        'href': '/AntdCheckCard',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCheckCardGroup',
                                        'name': '/AntdCheckCardGroup',
                                        'title': 'AntdCheckCardGroup 组合选择卡片',
                                        'href': '/AntdCheckCardGroup',
                                    },
                                },
                            ],
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdColorPicker',
                                'name': '/AntdColorPicker',
                                'title': 'AntdColorPicker 颜色选择',
                                'href': '/AntdColorPicker',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDatePicker',
                                'name': '/AntdDatePicker',
                                'title': 'AntdDatePicker 日期选择',
                                'href': '/AntdDatePicker',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDateRangePicker',
                                'name': '/AntdDateRangePicker',
                                'title': 'AntdDateRangePicker 日期范围选择',
                                'href': '/AntdDateRangePicker',
                            },
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据录入/表单',
                                'title': '表单',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdForm',
                                        'name': '/AntdForm',
                                        'title': 'AntdForm 表单',
                                        'href': '/AntdForm',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdFormItem',
                                        'name': '/AntdFormItem',
                                        'title': 'AntdFormItem 表单项',
                                        'href': '/AntdFormItem',
                                    },
                                },
                            ],
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdInput',
                                'name': '/AntdInput',
                                'title': 'AntdInput 输入框',
                                'href': '/AntdInput',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdOTP',
                                'name': '/AntdOTP',
                                'title': 'AntdOTP 一次性密码框',
                                'href': '/AntdOTP',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdInputNumber',
                                'name': '/AntdInputNumber',
                                'title': 'AntdInputNumber 数值输入框',
                                'href': '/AntdInputNumber',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdMentions',
                                'name': '/AntdMentions',
                                'title': 'AntdMentions 提及',
                                'href': '/AntdMentions',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdRadioGroup',
                                'name': '/AntdRadioGroup',
                                'title': 'AntdRadioGroup 单选框',
                                'href': '/AntdRadioGroup',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdRate',
                                'name': '/AntdRate',
                                'title': 'AntdRate 评分',
                                'href': '/AntdRate',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSegmentedColoring',
                                'name': '/AntdSegmentedColoring',
                                'title': 'AntdSegmentedColoring 分段着色',
                                'href': '/AntdSegmentedColoring',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSelect',
                                'name': '/AntdSelect',
                                'title': 'AntdSelect 下拉选择',
                                'href': '/AntdSelect',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSlider',
                                'name': '/AntdSlider',
                                'title': 'AntdSlider 滑动输入条',
                                'href': '/AntdSlider',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSwitch',
                                'name': '/AntdSwitch',
                                'title': 'AntdSwitch 开关',
                                'href': '/AntdSwitch',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTimePicker',
                                'name': '/AntdTimePicker',
                                'title': 'AntdTimePicker 时间选择',
                                'href': '/AntdTimePicker',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTimeRangePicker',
                                'name': '/AntdTimeRangePicker',
                                'title': 'AntdTimeRangePicker 时间范围选择',
                                'href': '/AntdTimeRangePicker',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTransfer',
                                'name': '/AntdTransfer',
                                'title': 'AntdTransfer 穿梭框',
                                'href': '/AntdTransfer',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTreeSelect',
                                'name': '/AntdTreeSelect',
                                'title': 'AntdTreeSelect 树选择',
                                'href': '/AntdTreeSelect',
                            },
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据录入/文件上传',
                                'title': '文件上传',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdUpload',
                                        'name': '/AntdUpload',
                                        'title': 'AntdUpload 上传',
                                        'href': '/AntdUpload',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdDraggerUpload',
                                        'name': '/AntdDraggerUpload',
                                        'title': 'AntdDraggerUpload 拖拽上传',
                                        'href': '/AntdDraggerUpload',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdPictureUpload',
                                        'name': '/AntdPictureUpload',
                                        'title': 'AntdPictureUpload 图片上传',
                                        'href': '/AntdPictureUpload',
                                    },
                                },
                            ],
                        },
                    ],
                },
                {
                    'component': 'SubMenu',
                    'props': {'key': '数据展示', 'title': '数据展示'},
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAccordion',
                                'name': '/AntdAccordion',
                                'title': 'AntdAccordion 手风琴',
                                'href': '/AntdAccordion',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAvatar',
                                'name': '/AntdAvatar',
                                'title': 'AntdAvatar 头像',
                                'href': '/AntdAvatar',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAvatarGroup',
                                'name': '/AntdAvatarGroup',
                                'title': 'AntdAvatarGroup 头像组合',
                                'href': '/AntdAvatarGroup',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdBadge',
                                'name': '/AntdBadge',
                                'title': 'AntdBadge 徽标',
                                'href': '/AntdBadge',
                            },
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据展示/卡片',
                                'title': '卡片',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCard',
                                        'name': '/AntdCard',
                                        'title': 'AntdCard 卡片',
                                        'href': '/AntdCard',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCardGrid',
                                        'name': '/AntdCardGrid',
                                        'title': 'AntdCardGrid 卡片网格',
                                        'href': '/AntdCardGrid',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCardMeta',
                                        'name': '/AntdCardMeta',
                                        'title': 'AntdCardMeta 结构化卡片',
                                        'href': '/AntdCardMeta',
                                    },
                                },
                            ],
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCarousel',
                                'name': '/AntdCarousel',
                                'title': 'AntdCarousel 走马灯',
                                'href': '/AntdCarousel',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCheckableTag',
                                'name': '/AntdCheckableTag',
                                'title': 'AntdCheckableTag 可选择标签',
                                'href': '/AntdCheckableTag',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCollapse',
                                'name': '/AntdCollapse',
                                'title': 'AntdCollapse 折叠面板',
                                'href': '/AntdCollapse',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdComment',
                                'name': '/AntdComment',
                                'title': 'AntdComment 评论',
                                'href': '/AntdComment',
                            },
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '数据展示/描述列表',
                                'title': '描述列表',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdDescriptions',
                                        'name': '/AntdDescriptions',
                                        'title': 'AntdDescriptions 描述列表',
                                        'href': '/AntdDescriptions',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdDescriptionItem',
                                        'name': '/AntdDescriptionItem',
                                        'title': 'AntdDescriptionItem 描述列表子项',
                                        'href': '/AntdDescriptionItem',
                                    },
                                },
                            ],
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdEmpty',
                                'name': '/AntdEmpty',
                                'title': 'AntdEmpty 空状态',
                                'href': '/AntdEmpty',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdImage',
                                'name': '/AntdImage',
                                'title': 'AntdImage 图片',
                                'href': '/AntdImage',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdImageGroup',
                                'name': '/AntdImageGroup',
                                'title': 'AntdImageGroup 图片组合',
                                'href': '/AntdImageGroup',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdPopover',
                                'name': '/AntdPopover',
                                'title': 'AntdPopover 气泡卡片',
                                'href': '/AntdPopover',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdQRCode',
                                'name': '/AntdQRCode',
                                'title': 'AntdQRCode 二维码',
                                'href': '/AntdQRCode',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdRibbon',
                                'name': '/AntdRibbon',
                                'title': 'AntdRibbon 缎带',
                                'href': '/AntdRibbon',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSegmented',
                                'name': '/AntdSegmented',
                                'title': 'AntdSegmented 分段控制器',
                                'href': '/AntdSegmented',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSpoiler',
                                'name': '/AntdSpoiler',
                                'title': 'AntdSpoiler 展开收起',
                                'href': '/AntdSpoiler',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdStatistic',
                                'name': '/AntdStatistic',
                                'title': 'AntdStatistic 统计数值',
                                'href': '/AntdStatistic',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCountdown',
                                'name': '/AntdCountdown',
                                'title': 'AntdCountdown 倒计时',
                                'href': '/AntdCountdown',
                            },
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '/AntdTable',
                                'title': 'AntdTable 表格',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTable-basic',
                                        'name': '/AntdTable-basic',
                                        'title': '基础功能',
                                        'href': '/AntdTable-basic',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTable-advanced',
                                        'name': '/AntdTable-advanced',
                                        'title': '进阶功能',
                                        'href': '/AntdTable-advanced',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdTable-server-side-mode',
                                        'name': '/AntdTable-server-side-mode',
                                        'title': '服务端数据加载模式',
                                        'href': '/AntdTable-server-side-mode',
                                    },
                                },
                            ],
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTabs',
                                'name': '/AntdTabs',
                                'title': 'AntdTabs 标签页',
                                'href': '/AntdTabs',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTag',
                                'name': '/AntdTag',
                                'title': 'AntdTag 标签',
                                'href': '/AntdTag',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTimeline',
                                'name': '/AntdTimeline',
                                'title': 'AntdTimeline 时间轴',
                                'href': '/AntdTimeline',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTooltip',
                                'name': '/AntdTooltip',
                                'title': 'AntdTooltip 文字提示',
                                'href': '/AntdTooltip',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTree',
                                'name': '/AntdTree',
                                'title': 'AntdTree 树形控件',
                                'href': '/AntdTree',
                            },
                        },
                    ],
                },
                {
                    'component': 'SubMenu',
                    'props': {'key': '反馈', 'title': '反馈'},
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAlert',
                                'name': '/AntdAlert',
                                'title': 'AntdAlert 警告提示',
                                'href': '/AntdAlert',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDrawer',
                                'name': '/AntdDrawer',
                                'title': 'AntdDrawer 抽屉',
                                'href': '/AntdDrawer',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdMessage',
                                'name': '/AntdMessage',
                                'title': 'AntdMessage 全局提示',
                                'href': '/AntdMessage',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdModal',
                                'name': '/AntdModal',
                                'title': 'AntdModal 对话框',
                                'href': '/AntdModal',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdNotification',
                                'name': '/AntdNotification',
                                'title': 'AntdNotification 通知提醒框',
                                'href': '/AntdNotification',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdPopconfirm',
                                'name': '/AntdPopconfirm',
                                'title': 'AntdPopconfirm 气泡确认框',
                                'href': '/AntdPopconfirm',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdPopupCard',
                                'name': '/AntdPopupCard',
                                'title': 'AntdPopupCard 弹出式卡片',
                                'href': '/AntdPopupCard',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdProgress',
                                'name': '/AntdProgress',
                                'title': 'AntdProgress 进度条',
                                'href': '/AntdProgress',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdResult',
                                'name': '/AntdResult',
                                'title': 'AntdResult 结果',
                                'href': '/AntdResult',
                            },
                        },
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '反馈/骨架屏',
                                'title': '骨架屏',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSkeleton',
                                        'name': '/AntdSkeleton',
                                        'title': 'AntdSkeleton 骨架屏',
                                        'href': '/AntdSkeleton',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdCustomSkeleton',
                                        'name': '/AntdCustomSkeleton',
                                        'title': 'AntdCustomSkeleton 自定义骨架屏',
                                        'href': '/AntdCustomSkeleton',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSkeletonAvatar',
                                        'name': '/AntdSkeletonAvatar',
                                        'title': 'AntdSkeletonAvatar 头像占位图',
                                        'href': '/AntdSkeletonAvatar',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSkeletonButton',
                                        'name': '/AntdSkeletonButton',
                                        'title': 'AntdSkeletonButton 按钮占位图',
                                        'href': '/AntdSkeletonButton',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSkeletonInput',
                                        'name': '/AntdSkeletonInput',
                                        'title': 'AntdSkeletonInput 输入框占位图',
                                        'href': '/AntdSkeletonInput',
                                    },
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/AntdSkeletonImage',
                                        'name': '/AntdSkeletonImage',
                                        'title': 'AntdSkeletonImage 图片占位图',
                                        'href': '/AntdSkeletonImage',
                                    },
                                },
                            ],
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdSpin',
                                'name': '/AntdSpin',
                                'title': 'AntdSpin 加载动画',
                                'href': '/AntdSpin',
                            },
                        },
                    ],
                },
                {
                    'component': 'SubMenu',
                    'props': {'key': '其他', 'title': '其他'},
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdAffix',
                                'name': '/AntdAffix',
                                'title': 'AntdAffix 固钉',
                                'href': '/AntdAffix',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdBackTop',
                                'name': '/AntdBackTop',
                                'title': 'AntdBackTop 回到顶部',
                                'href': '/AntdBackTop',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdCopyText',
                                'name': '/AntdCopyText',
                                'title': 'AntdCopyText 文本复制',
                                'href': '/AntdCopyText',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdTour',
                                'name': '/AntdTour',
                                'title': 'AntdTour 漫游式引导',
                                'href': '/AntdTour',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdWatermark',
                                'name': '/AntdWatermark',
                                'title': 'AntdWatermark 水印',
                                'href': '/AntdWatermark',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdConfigProvider',
                                'name': '/AntdConfigProvider',
                                'title': 'AntdConfigProvider 参数配置',
                                'href': '/AntdConfigProvider',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/Fragment',
                                'name': '/Fragment',
                                'title': 'Fragment 空节点',
                                'href': '/Fragment',
                            },
                        },
                    ],
                },
                {
                    'component': 'SubMenu',
                    'props': {'key': '复杂交互', 'title': '复杂交互'},
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdDraggablePanel',
                                'name': '/AntdDraggablePanel',
                                'title': 'AntdDraggablePanel 可拖拽面板',
                                'href': '/AntdDraggablePanel',
                            },
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/AntdEditorLayout',
                                'name': '/AntdEditorLayout',
                                'title': 'AntdEditorLayout 编辑器布局',
                                'href': '/AntdEditorLayout',
                            },
                        },
                    ],
                },
            ],
        },
        {
            'component': 'ItemGroup',
            'props': {'key': '进阶使用', 'title': '进阶使用'},
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': '/advanced-classname',
                        'name': '/advanced-classname',
                        'title': '进阶className的使用',
                        'href': '/advanced-classname',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/popup-container',
                        'name': '/popup-container',
                        'title': '弹出层容器设置',
                        'href': '/popup-container',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/internationalization',
                        'name': '/internationalization',
                        'title': '国际化',
                        'href': '/internationalization',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/prop-persistence',
                        'name': '/prop-persistence',
                        'title': '属性持久化',
                        'href': '/prop-persistence',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/use-key-to-refresh',
                        'name': '/use-key-to-refresh',
                        'title': '强制刷新组件',
                        'href': '/use-key-to-refresh',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/batch-props-values',
                        'name': '/batch-props-values',
                        'title': '属性批量监听',
                        'href': '/batch-props-values',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/import-alias',
                        'name': '/import-alias',
                        'title': '组件按别名导入',
                        'href': '/import-alias',
                    },
                },
            ],
        },
    ]

    # 侧边菜单栏key值 -> 展开项节点key值数组
    side_menu_expand_keys = {
        '/AntdButton': ['通用'],
        '/AntdFloatButton': ['通用'],
        '/AntdFloatButtonGroup': ['通用'],
        '/AntdIcon': ['通用'],
        '/AntdParagraph': ['通用', '通用/排版相关'],
        '/AntdText': ['通用', '通用/排版相关'],
        '/AntdTitle': ['通用', '通用/排版相关'],
        '/AntdCenter': ['布局'],
        '/AntdDivider': ['布局'],
        '/AntdFlex': ['布局'],
        '/AntdRow': ['布局', '布局/网格系统'],
        '/AntdCol': ['布局', '布局/网格系统'],
        '/AntdSpace': ['布局'],
        '/AntdCompact': ['布局'],
        '/AntdLayout': ['布局', '布局/经典布局'],
        '/AntdHeader': ['布局', '布局/经典布局'],
        '/AntdContent': ['布局', '布局/经典布局'],
        '/AntdFooter': ['布局', '布局/经典布局'],
        '/AntdSider': ['布局', '布局/经典布局'],
        '/AntdAnchor': ['导航'],
        '/AntdBreadcrumb': ['导航'],
        '/AntdDropdown': ['导航'],
        '/AntdMenu': ['导航'],
        '/AntdPageHeader': ['导航'],
        '/AntdPagination': ['导航'],
        '/AntdSteps': ['导航'],
        '/AntdCalendar': ['数据录入'],
        '/AntdCascader': ['数据录入'],
        '/AntdCheckbox': ['数据录入'],
        '/AntdCheckboxGroup': ['数据录入'],
        '/AntdCheckCard': ['数据录入', '数据录入/选择卡片'],
        '/AntdCheckCardGroup': ['数据录入', '数据录入/选择卡片'],
        '/AntdColorPicker': ['数据录入'],
        '/AntdDatePicker': ['数据录入'],
        '/AntdDateRangePicker': ['数据录入'],
        '/AntdForm': ['数据录入', '数据录入/表单'],
        '/AntdFormItem': ['数据录入', '数据录入/表单'],
        '/AntdInput': ['数据录入'],
        '/AntdOTP': ['数据录入'],
        '/AntdInputNumber': ['数据录入'],
        '/AntdMentions': ['数据录入'],
        '/AntdRadioGroup': ['数据录入'],
        '/AntdRate': ['数据录入'],
        '/AntdSegmentedColoring': ['数据录入'],
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
        '/AntdAccordion': ['数据展示'],
        '/AntdAvatar': ['数据展示'],
        '/AntdAvatarGroup': ['数据展示'],
        '/AntdBadge': ['数据展示'],
        '/AntdCard': ['数据展示', '数据展示/卡片'],
        '/AntdCardGrid': ['数据展示', '数据展示/卡片'],
        '/AntdCardMeta': ['数据展示', '数据展示/卡片'],
        '/AntdCarousel': ['数据展示'],
        '/AntdCheckableTag': ['数据展示'],
        '/AntdCollapse': ['数据展示'],
        '/AntdComment': ['数据展示'],
        '/AntdDescriptions': ['数据展示', '数据展示/描述列表'],
        '/AntdDescriptionItem': ['数据展示', '数据展示/描述列表'],
        '/AntdEmpty': ['数据展示'],
        '/AntdImage': ['数据展示'],
        '/AntdImageGroup': ['数据展示'],
        '/AntdPopover': ['数据展示'],
        '/AntdQRCode': ['数据展示'],
        '/AntdRibbon': ['数据展示'],
        '/AntdSegmented': ['数据展示'],
        '/AntdSpoiler': ['数据展示'],
        '/AntdStatistic': ['数据展示'],
        '/AntdCountdown': ['数据展示'],
        '/AntdTable-basic': ['数据展示', '/AntdTable'],
        '/AntdTable-advanced': ['数据展示', '/AntdTable'],
        '/AntdTable-server-side-mode': ['数据展示', '/AntdTable'],
        '/AntdTabs': ['数据展示'],
        '/AntdTag': ['数据展示'],
        '/AntdTimeline': ['数据展示'],
        '/AntdTooltip': ['数据展示'],
        '/AntdTree': ['数据展示'],
        '/AntdAlert': ['反馈'],
        '/AntdDrawer': ['反馈'],
        '/AntdMessage': ['反馈'],
        '/AntdModal': ['反馈'],
        '/AntdNotification': ['反馈'],
        '/AntdPopconfirm': ['反馈'],
        '/AntdPopupCard': ['反馈'],
        '/AntdProgress': ['反馈'],
        '/AntdResult': ['反馈'],
        '/AntdSkeleton': ['反馈', '反馈/骨架屏'],
        '/AntdCustomSkeleton': ['反馈', '反馈/骨架屏'],
        '/AntdSkeletonAvatar': ['反馈', '反馈/骨架屏'],
        '/AntdSkeletonButton': ['反馈', '反馈/骨架屏'],
        '/AntdSkeletonInput': ['反馈', '反馈/骨架屏'],
        '/AntdSkeletonImage': ['反馈', '反馈/骨架屏'],
        '/AntdSpin': ['反馈'],
        '/AntdAffix': ['其他'],
        '/AntdBackTop': ['其他'],
        '/AntdCopyText': ['其他'],
        '/AntdTour': ['其他'],
        '/AntdWatermark': ['其他'],
        '/AntdConfigProvider': ['其他'],
        '/Fragment': ['其他'],
        '/AntdDraggablePanel': ['复杂交互'],
        '/AntdEditorLayout': ['复杂交互'],
    }


class DemosConfig:
    """
    示例所需特殊参数配置
    """

    all_icons = json.load(open('./public/icons.json'))
