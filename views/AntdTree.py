from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdTree
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
                            'title': '数据展示'
                        },
                        {
                            'title': 'AntdTree 树形控件'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于渲染展示树形数据结构，并支持丰富的交互功能。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdTree(
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
                            ]
                        ),

                        fac.AntdDivider(
                            '基础使用',
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
fac.AntdTree(
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
    ]
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
                        fac.AntdTree(
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
                            defaultExpandAll=True
                        ),

                        fac.AntdDivider(
                            '初始化展开全部节点',
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
fac.AntdTree(
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
    defaultExpandAll=True
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
                    id='初始化展开全部节点',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
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
                            showLine=False
                        ),

                        fac.AntdDivider(
                            '关闭连接线',
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
fac.AntdTree(
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
    showLine=False
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
                    id='关闭连接线',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
                            treeData=[
                                {
                                    'title': '四川省',
                                    'key': '四川省',
                                    'icon': 'antd-cloud',
                                    'children': [
                                        {
                                            'title': '成都市',
                                            'key': '成都市',
                                            'icon': 'antd-cloud-server',
                                        },
                                        {
                                            'title': '广安市',
                                            'key': '广安市',
                                            'icon': 'antd-cloud-server',
                                        }
                                    ]
                                },
                                {
                                    'title': '重庆市',
                                    'key': '重庆市',
                                    'icon': 'antd-cloud',
                                    'children': [
                                        {
                                            'title': '渝中区',
                                            'key': '渝中区',
                                            'icon': 'antd-cloud-server',
                                            'children': [
                                                {
                                                    'title': '解放碑街道',
                                                    'key': '解放碑街道',
                                                    'icon': 'antd-cloud-server',
                                                }
                                            ]
                                        },
                                        {
                                            'title': '渝北区',
                                            'key': '渝北区',
                                            'icon': 'antd-cloud-server'
                                        }
                                    ]
                                }
                            ],
                            showIcon=True,
                            defaultExpandAll=True
                        ),

                        fac.AntdDivider(
                            '节点前缀展示图标',
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
fac.AntdTree(
    treeData=[
        {
            'title': '四川省',
            'key': '四川省',
            'icon': 'antd-cloud',
            'children': [
                {
                    'title': '成都市',
                    'key': '成都市',
                    'icon': 'antd-cloud-server',
                },
                {
                    'title': '广安市',
                    'key': '广安市',
                    'icon': 'antd-cloud-server',
                }
            ]
        },
        {
            'title': '重庆市',
            'key': '重庆市',
            'icon': 'antd-cloud',
            'children': [
                {
                    'title': '渝中区',
                    'key': '渝中区',
                    'icon': 'antd-cloud-server',
                    'children': [
                        {
                            'title': '解放碑街道',
                            'key': '解放碑街道',
                            'icon': 'antd-cloud-server',
                        }
                    ]
                },
                {
                    'title': '渝北区',
                    'key': '渝北区',
                    'icon': 'antd-cloud-server'
                }
            ]
        }
    ],
    showIcon=True,
    defaultExpandAll=True
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
                    id='节点前缀展示图标',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        # 动态样式
                        fuc.FefferyStyle(
                            rawStyle='''
.tree-node-style-demo1 {
    color: #2f9e44;
}

.tree-node-style-demo1:hover {
    color: #b2f2bb;
}

.tree-node-style-demo2 {
    color: #fd7e14;
}
'''
                        ),
                        fac.AntdTree(
                            treeData=[
                                {
                                    'title': '四川省',
                                    'key': '四川省',
                                    'className': 'tree-node-style-demo1',
                                    'children': [
                                        {
                                            'title': '成都市',
                                            'key': '成都市',
                                            'className': 'tree-node-style-demo1',
                                        },
                                        {
                                            'title': '广安市',
                                            'key': '广安市',
                                            'className': 'tree-node-style-demo1',
                                        }
                                    ]
                                },
                                {
                                    'title': '重庆市',
                                    'key': '重庆市',
                                    'className': 'tree-node-style-demo2',
                                    'children': [
                                        {
                                            'title': '渝中区',
                                            'key': '渝中区',
                                            'className': 'tree-node-style-demo2',
                                            'children': [
                                                {
                                                    'title': '解放碑街道',
                                                    'key': '解放碑街道',
                                                    'className': 'tree-node-style-demo2',
                                                }
                                            ]
                                        },
                                        {
                                            'title': '渝北区',
                                            'key': '渝北区',
                                            'className': 'tree-node-style-demo2',
                                        }
                                    ]
                                }
                            ],
                            defaultExpandAll=True
                        ),

                        fac.AntdDivider(
                            '自定义节点样式',
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
# 动态样式
fuc.FefferyStyle(
    rawStyle='''
.tree-node-style-demo1 {
    color: #2f9e44;
}

.tree-node-style-demo1:hover {
    color: #b2f2bb;
}

.tree-node-style-demo2 {
    color: #fd7e14;
}
'''
),
fac.AntdTree(
    treeData=[
        {
            'title': '四川省',
            'key': '四川省',
            'className': 'tree-node-style-demo1',
            'children': [
                {
                    'title': '成都市',
                    'key': '成都市',
                    'className': 'tree-node-style-demo1',
                },
                {
                    'title': '广安市',
                    'key': '广安市',
                    'className': 'tree-node-style-demo1',
                }
            ]
        },
        {
            'title': '重庆市',
            'key': '重庆市',
            'className': 'tree-node-style-demo2',
            'children': [
                {
                    'title': '渝中区',
                    'key': '渝中区',
                    'className': 'tree-node-style-demo2',
                    'children': [
                        {
                            'title': '解放碑街道',
                            'key': '解放碑街道',
                            'className': 'tree-node-style-demo2',
                        }
                    ]
                },
                {
                    'title': '渝北区',
                    'key': '渝北区',
                    'className': 'tree-node-style-demo2',
                }
            ]
        }
    ],
    defaultExpandAll=True
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
                    id='自定义节点样式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
                            treeData=[
                                {
                                    'title': '四川省',
                                    'key': '四川省',
                                    'tooltipProps': {
                                        'title': 'tooltip示例😀'
                                    },
                                    'children': [
                                        {
                                            'title': '成都市',
                                            'key': '成都市',
                                            'tooltipProps': {
                                                'title': 'tooltip示例😉'
                                            },
                                        },
                                        {
                                            'title': '广安市',
                                            'key': '广安市',
                                            'tooltipProps': {
                                                'title': 'tooltip示例😉'
                                            },
                                        }
                                    ]
                                },
                                {
                                    'title': '重庆市',
                                    'key': '重庆市',
                                    'tooltipProps': {
                                        'title': 'tooltip示例😀',
                                        'placement': 'right'
                                    },
                                    'children': [
                                        {
                                            'title': '渝中区',
                                            'key': '渝中区',
                                            'tooltipProps': {
                                                'title': 'tooltip示例😉',
                                                'placement': 'bottom'
                                            },
                                            'children': [
                                                {
                                                    'title': '解放碑街道',
                                                    'key': '解放碑街道',
                                                    'tooltipProps': {
                                                        'title': 'tooltip示例😉',
                                                        'placement': 'left'
                                                    },
                                                }
                                            ]
                                        },
                                        {
                                            'title': '渝北区',
                                            'key': '渝北区',
                                            'tooltipProps': {
                                                'title': 'tooltip示例😉',
                                                'placement': 'bottom'
                                            },
                                        }
                                    ]
                                }
                            ],
                            defaultExpandAll=True
                        ),

                        fac.AntdDivider(
                            '为节点添加tooltip',
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
fac.AntdTree(
    treeData=[
        {
            'title': '四川省',
            'key': '四川省',
            'tooltipProps': {
                'title': 'tooltip示例😀'
            },
            'children': [
                {
                    'title': '成都市',
                    'key': '成都市',
                    'tooltipProps': {
                        'title': 'tooltip示例😉'
                    },
                },
                {
                    'title': '广安市',
                    'key': '广安市',
                    'tooltipProps': {
                        'title': 'tooltip示例😉'
                    },
                }
            ]
        },
        {
            'title': '重庆市',
            'key': '重庆市',
            'tooltipProps': {
                'title': 'tooltip示例😀',
                'placement': 'right'
            },
            'children': [
                {
                    'title': '渝中区',
                    'key': '渝中区',
                    'tooltipProps': {
                        'title': 'tooltip示例😉',
                        'placement': 'bottom'
                    },
                    'children': [
                        {
                            'title': '解放碑街道',
                            'key': '解放碑街道',
                            'tooltipProps': {
                                'title': 'tooltip示例😉',
                                'placement': 'left'
                            },
                        }
                    ]
                },
                {
                    'title': '渝北区',
                    'key': '渝北区',
                    'tooltipProps': {
                        'title': 'tooltip示例😉',
                        'placement': 'bottom'
                    },
                }
            ]
        }
    ],
    defaultExpandAll=True
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
                    id='为节点添加tooltip',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
                            treeData=[
                                {
                                    'title': '四川省',
                                    'key': '四川省',
                                    'children': [
                                        {
                                            'title': '成都市',
                                            'key': '成都市',
                                        },
                                        {
                                            'title': '广安市',
                                            'key': '广安市',
                                        }
                                    ],
                                    'contextMenu': [
                                        {
                                            'key': f'四川省-操作选项{i}',
                                            'label': f'操作选项{i}'
                                        }
                                        for i in range(1, 6)
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
                                                    'key': '解放碑街道',
                                                }
                                            ]
                                        },
                                        {
                                            'title': '渝北区',
                                            'key': '渝北区',
                                        }
                                    ],
                                    'contextMenu': [
                                        {
                                            'key': f'重庆市-操作选项{i}',
                                            'label': f'操作选项{i}',
                                            'icon': 'antd-function'
                                        }
                                        for i in range(1, 6)
                                    ]
                                }
                            ],
                            defaultExpandAll=True
                        ),

                        fac.AntdDivider(
                            '为节点添加自定义右键菜单',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '本例中为节点',
                                fac.AntdText(
                                    '四川省',
                                    strong=True
                                ),
                                '和',
                                fac.AntdText(
                                    '重庆市',
                                    strong=True
                                ),
                                '添加了自定义右键菜单功能'
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
fac.AntdTree(
    treeData=[
        {
            'title': '四川省',
            'key': '四川省',
            'children': [
                {
                    'title': '成都市',
                    'key': '成都市',
                },
                {
                    'title': '广安市',
                    'key': '广安市',
                }
            ],
            'contextMenu': [
                {
                    'key': f'四川省-操作选项{i}',
                    'label': f'操作选项{i}'
                }
                for i in range(1, 6)
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
                            'key': '解放碑街道',
                        }
                    ]
                },
                {
                    'title': '渝北区',
                    'key': '渝北区',
                }
            ],
            'contextMenu': [
                {
                    'key': f'重庆市-操作选项{i}',
                    'label': f'操作选项{i}',
                    'icon': 'antd-function'
                }
                for i in range(1, 6)
            ]
        }
    ],
    defaultExpandAll=True
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
                    id='为节点添加自定义右键菜单',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
                            treeData=[
                                {
                                    'title': f'节点{i}',
                                    'key': f'节点{i}',
                                    'children': [
                                        {
                                            'title': f'节点{i}-{j}',
                                            'key': f'节点{i}-{j}',
                                        }
                                        for j in range(1, 10)
                                    ]
                                }
                                for i in range(1, 101)
                            ],
                            height=200,
                            style={
                                'border': '1px dashed #ced4da'
                            }
                        ),

                        fac.AntdDivider(
                            '大数据量时开启虚拟滚动优化',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '在设置参数',
                                fac.AntdText(
                                    'height',
                                    code=True
                                ),
                                '后，树形控件会在对应固定高度区域内开启虚拟滚动渲染，从而大幅度提升渲染交互性能'
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
fac.AntdTree(
    treeData=[
        {
            'title': f'节点{i}',
            'key': f'节点{i}',
            'children': [
                {
                    'title': f'节点{i}-{j}',
                    'key': f'节点{i}-{j}',
                }
                for j in range(1, 10)
            ]
        }
        for i in range(1, 101)
    ],
    height=200,
    style={
        'border': '1px dashed #ced4da'
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
                    id='大数据量时开启虚拟滚动优化',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
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
                            multiple=True
                        ),

                        fac.AntdDivider(
                            '多选模式',
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
fac.AntdTree(
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
    multiple=True
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
                    id='多选模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
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
                            checkable=True
                        ),

                        fac.AntdDivider(
                            '带勾选框的多选模式',
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
fac.AntdTree(
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
    checkable=True
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
                    id='带勾选框的多选模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
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
                            checkStrictly=True
                        ),

                        fac.AntdDivider(
                            '父子节点独立选择',
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
fac.AntdTree(
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
    checkStrictly=True
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
                    id='父子节点独立选择',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
                            treeData=[
                                {
                                    'title': '四川省',
                                    'key': '四川省'
                                },
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'parent': '四川省'
                                },
                                {
                                    'title': '广安市',
                                    'key': '广安市',
                                    'parent': '四川省'
                                },
                                {
                                    'title': '重庆市',
                                    'key': '重庆市'
                                },
                                {
                                    'title': '渝中区',
                                    'key': '渝中区',
                                    'parent': '重庆市'
                                },
                                {
                                    'title': '渝北区',
                                    'key': '渝北区',
                                    'parent': '重庆市'
                                },
                                {
                                    'title': '解放碑街道',
                                    'key': '解放碑街道',
                                    'parent': '渝中区'
                                },
                            ],
                            treeDataMode='flat'
                        ),

                        fac.AntdDivider(
                            '扁平treeData模式',
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
fac.AntdTree(
    treeData=[
        {
            'title': '四川省',
            'key': '四川省'
        },
        {
            'title': '成都市',
            'key': '成都市',
            'parent': '四川省'
        },
        {
            'title': '广安市',
            'key': '广安市',
            'parent': '四川省'
        },
        {
            'title': '重庆市',
            'key': '重庆市'
        },
        {
            'title': '渝中区',
            'key': '渝中区',
            'parent': '重庆市'
        },
        {
            'title': '渝北区',
            'key': '渝北区',
            'parent': '重庆市'
        },
        {
            'title': '解放碑街道',
            'key': '解放碑街道',
            'parent': '渝中区'
        },
    ],
    treeDataMode='flat'
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
                    id='扁平treeData模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
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
                            draggable=True,
                            defaultExpandAll=True
                        ),

                        fac.AntdDivider(
                            '节点可拖拽',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '在参数',
                                fac.AntdText(
                                    'treeDataMode="tree"',
                                    code=True
                                ),
                                '的前提下，通过设置参数',
                                fac.AntdText(
                                    'draggable=True',
                                    code=True
                                ),
                                '可开启树节点拖拽功能'
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
fac.AntdTree(
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
    draggable=True,
    defaultExpandAll=True
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
                    id='节点可拖拽',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
                            id='tree-demo',
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
                            checkable=True
                        ),

                        html.Pre(
                            id='tree-demo-output'
                        ),

                        fac.AntdDivider(
                            '节点选择回调示例',
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
fac.AntdTree(
    id='tree-demo',
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
    checkable=True
),

html.Pre(
    id='tree-demo-output'
)

...

import json

...

@app.callback(
    Output('tree-demo-output', 'children'),
    [Input('tree-demo', 'selectedKeys'),
     Input('tree-demo', 'checkedKeys'),
     Input('tree-demo', 'halfCheckedKeys'),
     Input('tree-demo', 'expandedKeys')]
)
def tree_demo(selectedKeys, checkedKeys, halfCheckedKeys, expandedKeys):

    return json.dumps(
        dict(
            selectedKeys=selectedKeys,
            checkedKeys=checkedKeys,
            halfCheckedKeys=halfCheckedKeys,
            expandedKeys=expandedKeys
        ),
        indent=4,
        ensure_ascii=False
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
                    id='节点选择回调示例',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
                            id='tree-drag-demo',
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
                            draggable=True
                        ),

                        html.Pre(
                            id='tree-drag-demo-output'
                        ),

                        fac.AntdDivider(
                            '节点拖拽回调示例',
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
fac.AntdTree(
    id='tree-drag-demo',
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
    draggable=True
),

html.Pre(
    id='tree-drag-demo-output'
)

...

import json

...

@app.callback(
    Output('tree-drag-demo-output', 'children'),
    [Input('tree-drag-demo', 'treeData'),
     Input('tree-drag-demo', 'draggedNodeKey')]
)
def tree_drag_demo(treeData, draggedNodeKey):

    return json.dumps(
        dict(
            treeData=treeData,
            draggedNodeKey=draggedNodeKey
        ),
        indent=4,
        ensure_ascii=False
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
                    id='节点拖拽回调示例',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
                            id='tree-context-menu-demo',
                            treeData=[
                                {
                                    'title': '四川省',
                                    'key': '四川省',
                                    'children': [
                                        {
                                            'title': '成都市',
                                            'key': '成都市',
                                        },
                                        {
                                            'title': '广安市',
                                            'key': '广安市',
                                        }
                                    ],
                                    'contextMenu': [
                                        {
                                            'key': f'四川省-操作选项{i}',
                                            'label': f'操作选项{i}'
                                        }
                                        for i in range(1, 6)
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
                                                    'key': '解放碑街道',
                                                }
                                            ]
                                        },
                                        {
                                            'title': '渝北区',
                                            'key': '渝北区',
                                        }
                                    ],
                                    'contextMenu': [
                                        {
                                            'key': f'重庆市-操作选项{i}',
                                            'label': f'操作选项{i}',
                                            'icon': 'antd-function'
                                        }
                                        for i in range(1, 6)
                                    ]
                                }
                            ]
                        ),

                        html.Pre(
                            id='tree-context-menu-demo-output'
                        ),

                        fac.AntdDivider(
                            '节点右键菜单回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '本例中为节点',
                                fac.AntdText(
                                    '四川省',
                                    strong=True
                                ),
                                '和',
                                fac.AntdText(
                                    '重庆市',
                                    strong=True
                                ),
                                '添加了自定义右键菜单功能'
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
fac.AntdTree(
    id='tree-context-menu-demo',
    treeData=[
        {
            'title': '四川省',
            'key': '四川省',
            'children': [
                {
                    'title': '成都市',
                    'key': '成都市',
                },
                {
                    'title': '广安市',
                    'key': '广安市',
                }
            ],
            'contextMenu': [
                {
                    'key': f'四川省-操作选项{i}',
                    'label': f'操作选项{i}'
                }
                for i in range(1, 6)
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
                            'key': '解放碑街道',
                        }
                    ]
                },
                {
                    'title': '渝北区',
                    'key': '渝北区',
                }
            ],
            'contextMenu': [
                {
                    'key': f'重庆市-操作选项{i}',
                    'label': f'操作选项{i}',
                    'icon': 'antd-function'
                }
                for i in range(1, 6)
            ]
        }
    ]
),

html.Pre(
    id='tree-context-menu-demo-output'
)

...

import json

...

@app.callback(
    Output('tree-context-menu-demo-output', 'children'),
    Input('tree-context-menu-demo', 'clickedContextMenu')
)
def tree_context_menu_demo(clickedContextMenu):

    return json.dumps(
        dict(
            treeData=clickedContextMenu
        ),
        indent=4,
        ensure_ascii=False
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
                    id='节点右键菜单回调示例',
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
                    {'title': '初始化展开全部节点', 'href': '#初始化展开全部节点'},
                    {'title': '关闭连接线', 'href': '#关闭连接线'},
                    {'title': '节点前缀展示图标', 'href': '#节点前缀展示图标'},
                    {'title': '自定义节点样式', 'href': '#自定义节点样式'},
                    {'title': '为节点添加tooltip', 'href': '#为节点添加tooltip'},
                    {'title': '为节点添加自定义右键菜单', 'href': '#为节点添加自定义右键菜单'},
                    {'title': '大数据量时开启虚拟滚动优化', 'href': '#大数据量时开启虚拟滚动优化'},
                    {'title': '多选模式', 'href': '#多选模式'},
                    {'title': '带勾选框的多选模式', 'href': '#带勾选框的多选模式'},
                    {'title': '父子节点独立选择', 'href': '#父子节点独立选择'},
                    {'title': '扁平treeData模式', 'href': '#扁平treeData模式'},
                    {'title': '节点可拖拽', 'href': '#节点可拖拽'},
                    {'title': '节点选择回调示例', 'href': '#节点选择回调示例'},
                    {'title': '节点拖拽回调示例', 'href': '#节点拖拽回调示例'},
                    {'title': '节点右键菜单回调示例', 'href': '#节点右键菜单回调示例'},
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
            component_name='AntdTree'
        )
    ],
    style={
        'display': 'flex'
    }
)
