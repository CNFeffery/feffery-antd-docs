from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc


def docs_content(language: str = '中文'):

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(
                        duration=0.3
                    ),

                    fac.AntdBreadcrumb(
                        items=[
                            {
                                'title': '进阶使用'
                            },
                            {
                                'title': '属性持久化'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                'fac',
                                strong=True
                            ),
                            '中具有参数',
                            fac.AntdText(
                                'persistence',
                                code=True
                            ),
                            '、',
                            fac.AntdText(
                                'persisted_props',
                                code=True
                            ),
                            '、',
                            fac.AntdText(
                                'persistence_type',
                                code=True
                            ),
                            '的组件，可使用',
                            fac.AntdText(
                                '属性持久化',
                                strong=True
                            ),
                            '功能，开启后可分别在不同生命周期内对目标组件的属性进行记忆，这可能听起来比较抽象，让我们从下面的例子中了解更多：'
                        ],
                        style={
                            'textIndent': '2rem'
                        }
                    ),

                    fac.AntdParagraph(
                        [
                            '下面的示例输入框，已设置了',
                            fac.AntdText(
                                'persistence=True',
                                code=True
                            ),
                            '，即开启了默认的基于浏览器本地缓存的属性持久化功能，因此当我们在输入框内输入任意内容后，刷新页面，已输入的内容都会被记忆，因为',
                            fac.AntdText(
                                'value',
                                code=True
                            ),
                            '属性是输入框组件属性持久化默认作用的目标属性之一：'
                        ],
                        style={
                            'textIndent': '2rem'
                        }
                    ),

                    fac.AntdInput(
                        id='persistence-input-demo',
                        placeholder='请输入',
                        persistence=True,
                        style={
                            'width': 256
                        }
                    ),

                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString='''
fac.AntdInput(
    id='persistence-input-demo',
    placeholder='请输入',
    persistence=True,
    style={
        'width': 256
    }
)
'''
                    ),

                    fac.AntdParagraph(
                        [
                            '下面是支持属性持久化特性的全部组件，你可以在各自的文档页参数说明中了解更多：'
                        ]
                    ),

                    fac.AntdSpace(
                        [
                            fac.AntdCheckCard(
                                '持久化测试',
                                id='check-card-persistence-demo',
                                defaultChecked=True,
                                persistence=True
                            ),
                            fac.AntdCheckCardGroup(
                                [
                                    fac.AntdCheckCard(
                                        f'选项{i}',
                                        value=i
                                    )
                                    for i in range(1, 6)
                                ],
                                id='check-card-group-persistence-demo',
                                size='small',
                                multiple=True,
                                defaultValue=[1, 2],
                                persistence=True
                            ),

                            fac.AntdTabs(
                                id='tabs-persistence-demo',
                                items=[
                                    {
                                        'key': f'标签页{i}',
                                        'label': f'标签页{i}',
                                        'children': html.Div(
                                            f'这是标签页{i}的内容示例',
                                            style={
                                                'display': 'flex',
                                                'justifyContent': 'center',
                                                'alignItems': 'center',
                                                'fontSize': 18,
                                                'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                                                'height': 200
                                            }
                                        )
                                    }
                                    for i in range(1, 6)
                                ],
                                defaultActiveKey='标签页1',
                                persistence=True
                            ),
                            fac.AntdCalendar(
                                id='calendar-persistence-demo',
                                defaultValue='2023-01-01',
                                persistence=True,
                                style={
                                    'width': '300px'
                                }
                            ),
                            fac.AntdCascader(
                                id='cascader-persistence-demo',
                                placeholder='请选择',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'value': '节点2',
                                        'label': '节点2',
                                        'children': [
                                            {
                                                'value': '节点2-1',
                                                'label': '节点2-1'
                                            },
                                            {
                                                'value': '节点2-2',
                                                'label': '节点2-2'
                                            }
                                        ]
                                    }
                                ],
                                persistence=True,
                                style={
                                    'width': '200px'
                                }
                            ),
                            fac.AntdCheckbox(
                                id='checkbox-persistence-demo',
                                label='开启',
                                persistence=True
                            ),
                            fac.AntdCheckboxGroup(
                                id='checkbox-group-persistence-demo',
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': f'选项{i}'
                                    }
                                    for i in range(5)
                                ],
                                persistence=True
                            ),
                            fac.AntdCollapse(
                                fac.AntdParagraph(
                                    '内容示例'*20
                                ),
                                id='collapse-persistence-demo',
                                isOpen=True,
                                title='回调示例',
                                persistence=True,
                                style={
                                    'width': 300
                                }
                            ),
                            fac.AntdDatePicker(
                                id='date-picker-persistence-demo',
                                persistence=True,
                                style={
                                    'width': 175
                                },
                            ),
                            fac.AntdDateRangePicker(
                                id='date-range-picker-persistence-demo',
                                persistence=True,
                                style={
                                    'width': 300
                                },
                            ),
                            fac.AntdInput(
                                id='input-persistence-demo',
                                persistence=True,
                                style={
                                    'width': 150
                                }
                            ),
                            fac.AntdInput(
                                id='input-password-persistence-demo',
                                mode='password',
                                passwordUseMd5=True,
                                persistence=True,
                                style={
                                    'width': 150
                                }
                            ),
                            fac.AntdInputNumber(
                                id='input-number-persistence-demo',
                                persistence=True,
                                style={
                                    'width': 150
                                }
                            ),

                            html.Div(
                                fac.AntdMenu(
                                    id='menu-persistence-demo',
                                    persistence=True,
                                    defaultSelectedKey='图标antd-home',
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
                                            'antd-bar-chart'
                                        ]
                                    ],
                                    mode='inline'
                                ),
                                style={
                                    'width': '250px'
                                }
                            ),
                            fac.AntdPagination(
                                id='pagination-persistence-demo',
                                defaultPageSize=10,
                                total=100,
                                pageSizeOptions=[5, 10, 20],
                                showSizeChanger=True,
                                persistence=True
                            ),
                            fac.AntdRadioGroup(
                                id='radio-group-persistence-demo',
                                options=[
                                    {
                                        'label': f'选项{c}',
                                        'value': c
                                    }
                                    for c in list('abcdef')
                                ],
                                defaultValue='a',
                                persistence=True
                            ),
                            fac.AntdRate(
                                id='rate-persistence-demo',
                                count=10,
                                allowHalf=True,
                                defaultValue=1,
                                persistence=True
                            ),
                            fac.AntdSegmented(
                                id='segmented-persistence-demo',
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': i
                                    }
                                    for i in range(1, 6)
                                ],
                                defaultValue=2,
                                persistence=True
                            ),
                            fac.AntdSelect(
                                id='select-persistence-demo',
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': f'选项{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                persistence=True,
                                style={
                                    'width': 200
                                }
                            ),
                            fac.AntdSlider(
                                id='slider-persistence-demo',
                                min=0,
                                max=100,
                                defaultValue=33,
                                persistence=True,
                                style={
                                    'width': 300
                                }
                            ),
                            fac.AntdSlider(
                                id='slider-range-persistence-demo',
                                range=True,
                                min=0,
                                max=100,
                                defaultValue=[10, 90],
                                persistence=True,
                                style={
                                    'width': 300
                                }
                            ),
                            fac.AntdSwitch(
                                id='switch-persistence-demo',
                                persistence=True
                            ),
                            fac.AntdTimePicker(
                                id='time-picker-persistence-demo',
                                defaultValue='06:00:00',
                                persistence=True
                            ),
                            fac.AntdTimeRangePicker(
                                id='time-range-picker-persistence-demo',
                                defaultValue=[
                                    '12:00:00',
                                    '13:00:00'
                                ],
                                persistence=True
                            ),
                            fac.AntdTransfer(
                                id='transfer-persistence-demo',
                                dataSource=[
                                    {
                                        'key': i,
                                        'title': f'选项{i}'
                                    }
                                    for i in range(1, 10)
                                ],
                                targetKeys=[2, 3, 4],
                                persistence=True
                            ),
                            fac.AntdTree(
                                id='tree-persistence-demo',
                                treeData=[
                                    {
                                        'title': '四川省',
                                        'key': '四川省',
                                        'children': [
                                            {
                                                'title': '成都市',
                                                'key': '成都市'
                                            },
                                            {
                                                'title': '广安市',
                                                'key': '广安市'
                                            }
                                        ]
                                    },
                                    {
                                        'title': '重庆市',
                                        'key': '重庆市',
                                        'children': [
                                            {
                                                'title': '渝中区',
                                                'key': '渝中区',
                                                'children': [
                                                    {
                                                        'title': '解放碑街道',
                                                        'key': '解放碑街道'
                                                    }
                                                ]
                                            },
                                            {
                                                'title': '渝北区',
                                                'key': '渝北区'
                                            }
                                        ]
                                    }
                                ],
                                multiple=True,
                                checkable=True,
                                persistence=True
                            ),
                            fac.AntdTreeSelect(
                                id='tree-select-persistence-demo',
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                persistence=True,
                                style={
                                    'width': 256
                                }
                            ),
                            fac.AntdTreeSelect(
                                id='tree-select-multiple-persistence-demo',
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                multiple=True,
                                treeCheckable=True,
                                persistence=True,
                                style={
                                    'width': 256
                                }
                            )
                        ],
                        direction='vertical',
                        style={
                            'width': '100%'
                        }
                    ),

                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString='''
fac.AntdSpace(
    [
        fac.AntdCheckCard(
            '持久化测试',
            id='check-card-persistence-demo',
            defaultChecked=True,
            persistence=True
        ),
        fac.AntdCheckCardGroup(
            [
                fac.AntdCheckCard(
                    f'选项{i}',
                    value=i
                )
                for i in range(1, 6)
            ],
            id='check-card-group-persistence-demo',
            size='small',
            multiple=True,
            defaultValue=[1, 2],
            persistence=True
        ),

        fac.AntdTabs(
            id='tabs-persistence-demo',
            items=[
                {
                    'key': f'标签页{i}',
                    'label': f'标签页{i}',
                    'children': html.Div(
                        f'这是标签页{i}的内容示例',
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'fontSize': 18,
                            'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                            'height': 200
                        }
                    )
                }
                for i in range(1, 6)
            ],
            defaultActiveKey='标签页1',
            persistence=True
        ),
        fac.AntdCalendar(
            id='calendar-persistence-demo',
            defaultValue='2023-01-01',
            persistence=True,
            style={
                'width': '300px'
            }
        ),
        fac.AntdCascader(
            id='cascader-persistence-demo',
            placeholder='请选择',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                },
                {
                    'value': '节点2',
                    'label': '节点2',
                    'children': [
                        {
                            'value': '节点2-1',
                            'label': '节点2-1'
                        },
                        {
                            'value': '节点2-2',
                            'label': '节点2-2'
                        }
                    ]
                }
            ],
            persistence=True,
            style={
                'width': '200px'
            }
        ),
        fac.AntdCheckbox(
            id='checkbox-persistence-demo',
            label='开启',
            persistence=True
        ),
        fac.AntdCheckboxGroup(
            id='checkbox-group-persistence-demo',
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(5)
            ],
            persistence=True
        ),
        fac.AntdCollapse(
            fac.AntdParagraph(
                '内容示例'*20
            ),
            id='collapse-persistence-demo',
            isOpen=True,
            title='回调示例',
            persistence=True,
            style={
                'width': 300
            }
        ),
        fac.AntdDatePicker(
            id='date-picker-persistence-demo',
            persistence=True,
            style={
                'width': 175
            },
        ),
        fac.AntdDateRangePicker(
            id='date-range-picker-persistence-demo',
            persistence=True,
            style={
                'width': 300
            },
        ),
        fac.AntdInput(
            id='input-persistence-demo',
            persistence=True,
            style={
                'width': 150
            }
        ),
        fac.AntdInput(
            id='input-password-persistence-demo',
            mode='password',
            passwordUseMd5=True,
            persistence=True,
            style={
                'width': 150
            }
        ),
        fac.AntdInputNumber(
            id='input-number-persistence-demo',
            persistence=True,
            style={
                'width': 150
            }
        ),

        html.Div(
            fac.AntdMenu(
                id='menu-persistence-demo',
                persistence=True,
                defaultSelectedKey='图标antd-home',
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
                        'antd-bar-chart'
                    ]
                ],
                mode='inline'
            ),
            style={
                'width': '250px'
            }
        ),
        fac.AntdPagination(
            id='pagination-persistence-demo',
            defaultPageSize=10,
            total=100,
            pageSizeOptions=[5, 10, 20],
            showSizeChanger=True,
            persistence=True
        ),
        fac.AntdRadioGroup(
            id='radio-group-persistence-demo',
            options=[
                {
                    'label': f'选项{c}',
                    'value': c
                }
                for c in list('abcdef')
            ],
            defaultValue='a',
            persistence=True
        ),
        fac.AntdRate(
            id='rate-persistence-demo',
            count=10,
            allowHalf=True,
            defaultValue=1,
            persistence=True
        ),
        fac.AntdSegmented(
            id='segmented-persistence-demo',
            options=[
                {
                    'label': f'选项{i}',
                    'value': i
                }
                for i in range(1, 6)
            ],
            defaultValue=2,
            persistence=True
        ),
        fac.AntdSelect(
            id='select-persistence-demo',
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 6)
            ],
            persistence=True,
            style={
                'width': 200
            }
        ),
        fac.AntdSlider(
            id='slider-persistence-demo',
            min=0,
            max=100,
            defaultValue=33,
            persistence=True,
            style={
                'width': 300
            }
        ),
        fac.AntdSlider(
            id='slider-range-persistence-demo',
            range=True,
            min=0,
            max=100,
            defaultValue=[10, 90],
            persistence=True,
            style={
                'width': 300
            }
        ),
        fac.AntdSwitch(
            id='switch-persistence-demo',
            persistence=True
        ),
        fac.AntdTimePicker(
            id='time-picker-persistence-demo',
            defaultValue='06:00:00',
            persistence=True
        ),
        fac.AntdTimeRangePicker(
            id='time-range-picker-persistence-demo',
            defaultValue=[
                '12:00:00',
                '13:00:00'
            ],
            persistence=True
        ),
        fac.AntdTransfer(
            id='transfer-persistence-demo',
            dataSource=[
                {
                    'key': i,
                    'title': f'选项{i}'
                }
                for i in range(1, 10)
            ],
            targetKeys=[2, 3, 4],
            persistence=True
        ),
        fac.AntdTree(
            id='tree-persistence-demo',
            treeData=[
                {
                    'title': '四川省',
                    'key': '四川省',
                    'children': [
                        {
                            'title': '成都市',
                            'key': '成都市'
                        },
                        {
                            'title': '广安市',
                            'key': '广安市'
                        }
                    ]
                },
                {
                    'title': '重庆市',
                    'key': '重庆市',
                    'children': [
                        {
                            'title': '渝中区',
                            'key': '渝中区',
                            'children': [
                                {
                                    'title': '解放碑街道',
                                    'key': '解放碑街道'
                                }
                            ]
                        },
                        {
                            'title': '渝北区',
                            'key': '渝北区'
                        }
                    ]
                }
            ],
            multiple=True,
            checkable=True,
            persistence=True
        ),
        fac.AntdTreeSelect(
            id='tree-select-persistence-demo',
            treeData=[
                {
                    'key': '节点1',
                    'value': '1',
                    'title': '节点1',
                    'children': [
                        {
                            'key': f'节点1-{i}',
                            'value': f'1-{i}',
                            'title': f'节点1-{i}'
                        }
                        for i in range(1, 5)
                    ]
                },
                {
                    'key': '节点2',
                    'value': '2',
                    'title': '节点2'
                }
            ],
            placeholder='请选择',
            persistence=True,
            style={
                'width': 256
            }
        ),
        fac.AntdTreeSelect(
            id='tree-select-multiple-persistence-demo',
            treeData=[
                {
                    'key': '节点1',
                    'value': '1',
                    'title': '节点1',
                    'children': [
                        {
                            'key': f'节点1-{i}',
                            'value': f'1-{i}',
                            'title': f'节点1-{i}'
                        }
                        for i in range(1, 5)
                    ]
                },
                {
                    'key': '节点2',
                    'value': '2',
                    'title': '节点2'
                }
            ],
            placeholder='请选择',
            multiple=True,
            treeCheckable=True,
            persistence=True,
            style={
                'width': 256
            }
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)
'''
                    ),

                    html.Div(style={'height': '100px'})
                ],
                style={
                    'flex': 'auto',
                    'padding': '25px'
                }
            )
        ],
        style={
            'display': 'flex'
        }
    )
