from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
from dash.dependencies import Component


def render() -> Component:
    """渲染“弹出层容器设置”文档页"""

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(duration=0.3),
                    fac.AntdBreadcrumb(
                        items=[
                            {'title': '进阶使用'},
                            {'title': '弹出层容器设置'},
                        ]
                    ),
                    fac.AntdDivider(isDashed=True),
                    fac.AntdParagraph(
                        [
                            fac.AntdText('fac', code=True),
                            '对所有具有悬浮弹出层元素的组件的显示稳定性进行了优化，对于所有设计有参数',
                            fac.AntdText('popupContainer', code=True),
                            '的组件，默认',
                            fac.AntdText('popupContainer="body"', code=True),
                            '，在此默认设定下相关组件悬浮弹出层的位置计算参照容器为页面根节点，此时如果我们在带有滚动条的局部容器内放置具有悬浮弹出层的组件，',
                            '当悬浮弹出层处于显示状态时，在对应局部容器内进行滚动时，这些悬浮弹出层会出现不跟随滚动的问题，就像下面的例子一样：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    html.Div(
                        [
                            html.Div(style={'height': 100}),
                            fac.AntdPopover(
                                fac.AntdButton('点我展开，接着滚动试试'),
                                title='悬浮弹出层局部滚动不跟随示例',
                                content='默认popupContainer="body"',
                                trigger='focus',
                            ),
                            html.Div(style={'height': 600}),
                        ],
                        style={
                            'height': 300,
                            'overflowY': 'auto',
                            'background': '#f1f3f5',
                            'padding': 25,
                        },
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
html.Div(
    [
        html.Div(
            style={
                'height': 100
            }
        ),
        fac.AntdPopover(
            fac.AntdButton(
                '点我展开，接着滚动试试'
            ),
            title='悬浮弹出层局部滚动不跟随示例',
            content='默认popupContainer="body"',
            trigger='focus'
        ),
        html.Div(
            style={
                'height': 600
            }
        ),
    ],
    style={
        'height': 300,
        'overflowY': 'auto',
        'background': '#f1f3f5',
        'padding': 25
    }
)
""",
                    ),
                    fac.AntdParagraph(
                        [
                            '面对这种情况，我们可以在悬浮弹出层所在的组件中，设置参数',
                            fac.AntdText('popupContainer="parent"', code=True),
                            '，同时确保对应容器css样式中的position为relative或absolute，从而将对应组件的悬浮弹出层参照容器从页面根节点，切换为这些组件各自的父容器，',
                            '从而确保相关悬浮弹出层可以被正确计算位置变化：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    html.Div(
                        [
                            html.Div(style={'height': 100}),
                            fac.AntdPopover(
                                fac.AntdButton('点我展开，接着滚动试试'),
                                title='悬浮弹出层局部滚动不跟随示例',
                                content='默认popupContainer="parent"',
                                trigger='focus',
                                popupContainer='parent',
                            ),
                            html.Div(style={'height': 600}),
                        ],
                        style={
                            'height': 300,
                            'overflowY': 'auto',
                            'background': '#f1f3f5',
                            'padding': 25,
                            'position': 'relative',
                        },
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
html.Div(
    [
        html.Div(
            style={
                'height': 100
            }
        ),
        fac.AntdPopover(
            fac.AntdButton(
                '点我展开，接着滚动试试'
            ),
            title='悬浮弹出层局部滚动不跟随示例',
            content='默认popupContainer="parent"',
            trigger='focus',
            popupContainer='parent'
        ),
        html.Div(
            style={
                'height': 600
            }
        ),
    ],
    style={
        'height': 300,
        'overflowY': 'auto',
        'background': '#f1f3f5',
        'padding': 25,
        'position': 'relative'
    }
)
""",
                    ),
                    fac.AntdParagraph(
                        [
                            '除了上面介绍的局部滚动场景以外，其他与悬浮弹出层锚点相关的场景下，妥善使用参数',
                            fac.AntdText('popupContainer', code=True),
                            '可以有效解决一些相关的显示问题，譬如在下面的“相对-绝对”经典布局中，由于其中的绝对定位容器设置了z-index，',
                            '导致其内部放置的',
                            fac.AntdText('AntdDropdown', strong=True),
                            '组件附带的悬浮展开层显示异常：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    html.Div(
                        [
                            fuc.FefferyDiv(
                                fac.AntdDropdown(
                                    title='下拉菜单测试',
                                    menuItems=[
                                        {'title': f'下拉子项{i}'}
                                        for i in range(1, 6)
                                    ],
                                ),
                                style={
                                    'position': 'absolute',
                                    'top': 25,
                                    'left': 25,
                                    'width': 200,
                                    'padding': '25px',
                                    'background': 'white',
                                    'borderRadius': 6,
                                    'zIndex': 99999,
                                },
                                shadow='always-shadow',
                            )
                        ],
                        style={
                            'height': 300,
                            'background': '#f8f9fa',
                            'position': 'relative',
                        },
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
html.Div(
    [
        fuc.FefferyDiv(
            fac.AntdDropdown(
                title='下拉菜单测试',
                menuItems=[
                    {
                        'title': f'下拉子项{i}'
                    }
                    for i in range(1, 6)
                ]
            ),
            style={
                'position': 'absolute',
                'top': 25,
                'left': 25,
                'width': 200,
                'padding': '25px',
                'background': 'white',
                'borderRadius': 6,
                'zIndex': 99999
            },
            shadow='always-shadow'
        )
    ],
    style={
        'height': 300,
        'background': '#f8f9fa',
        'position': 'relative'
    }
)
""",
                    ),
                    fac.AntdParagraph(
                        [
                            '而对上面例子中的',
                            fac.AntdText('AntdDropdown', strong=True),
                            '设置',
                            fac.AntdText('popupContainer="parent"', code=True),
                            '后，即可在这个场景下保证下拉展开菜单显示正常：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    html.Div(
                        [
                            fuc.FefferyDiv(
                                fac.AntdDropdown(
                                    title='下拉菜单测试',
                                    menuItems=[
                                        {'title': f'下拉子项{i}'}
                                        for i in range(1, 6)
                                    ],
                                    popupContainer='parent',
                                ),
                                style={
                                    'position': 'absolute',
                                    'top': 25,
                                    'left': 25,
                                    'width': 200,
                                    'padding': '25px',
                                    'background': 'white',
                                    'borderRadius': 6,
                                    'zIndex': 99999,
                                },
                                shadow='always-shadow',
                            )
                        ],
                        style={
                            'height': 300,
                            'background': '#f8f9fa',
                            'position': 'relative',
                        },
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
html.Div(
    [
        fuc.FefferyDiv(
            fac.AntdDropdown(
                title='下拉菜单测试',
                menuItems=[
                    {
                        'title': f'下拉子项{i}'
                    }
                    for i in range(1, 6)
                ],
                popupContainer='parent'
            ),
            style={
                'position': 'absolute',
                'top': 25,
                'left': 25,
                'width': 200,
                'padding': '25px',
                'background': 'white',
                'borderRadius': 6,
                'zIndex': 99999
            },
            shadow='always-shadow'
        )
    ],
    style={
        'height': 300,
        'background': '#f8f9fa',
        'position': 'relative'
    }
)
""",
                    ),
                    html.Div(style={'height': '100px'}),
                ],
                style={'flex': 'auto', 'padding': '25px'},
            )
        ],
        style={'display': 'flex', 'paddingRight': 40},
    )
