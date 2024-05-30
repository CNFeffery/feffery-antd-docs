from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    button_mode,  # noqa: F401
    custom_button_style,  # noqa: F401
    free_position_mode,  # noqa: F401
    dropdown_trigger,  # noqa: F401
    dropdown_arrow,  # noqa: F401
    dropdown_placement,  # noqa: F401
    custom_children,  # noqa: F401
    dropdown_selectable,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最基础的下拉菜单。'),
    },
    {
        'path': 'button_mode',
        'title': '按钮模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('buttonMode=True', code=True),
                '后触发点显示为按钮样式。',
            ]
        ),
    },
    {
        'path': 'custom_button_style',
        'title': '自定义按钮样式',
        'description': fac.AntdParagraph('按钮模式时自定义按钮的样式。'),
    },
    {
        'path': 'free_position_mode',
        'title': '自由位置模式',
        'description': fac.AntdParagraph(
            [
                '自由位置模式的最典型应用场景是配合',
                fac.AntdText('fuc.FefferyDiv', code=True),
                '的右键事件监听功能，实现监听区域内鼠标右键触发自定义右键菜单。',
            ]
        ),
    },
    {
        'path': 'dropdown_trigger',
        'title': '点击触发方式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText("trigger='click'", code=True),
                '后通过点击才可触发下拉菜单。',
            ]
        ),
    },
    {
        'path': 'dropdown_arrow',
        'title': '添加箭头',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('arrow=True', code=True),
                '为展开的下拉菜单渲染连接箭头。',
            ]
        ),
    },
    {
        'path': 'dropdown_placement',
        'title': '不同的弹出方位',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('placement', code=True),
                '控制下拉菜单的展开方向。',
            ]
        ),
    },
    {
        'path': 'custom_children',
        'title': '自定义锚点元素',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('children', code=True),
                '自定义下拉菜单锚点元素，支持单个或多个组件。',
            ]
        ),
    },
    {
        'path': 'dropdown_selectable',
        'title': '菜单可选选择',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('selectable=True', code=True),
                '开启菜单选择能力，默认为单选模式。',
                '当额外设置参数',
                fac.AntdText('multiple=True', code=True),
                '可以开启多选模式。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                '通过',
                fac.AntdText('nClicks', code=True),
                '、',
                fac.AntdText('clickedKey', code=True),
                '进行下拉菜单项点击事件的监听。',
            ]
        ),
    },
]


def render(component: Component) -> Component:
    """渲染当前组件演示用例"""

    return fac.AntdSpace(
        [
            html.Div(
                [
                    html.Div(
                        getattr(
                            views.AntdDropdown.demos, item['path']
                        ).render(),
                        className='demo-box',
                    ),
                    html.Div(
                        [
                            fac.AntdText(
                                [
                                    item['title'],
                                    fac.AntdTooltip(
                                        html.A(
                                            fac.AntdIcon(
                                                icon='antd-edit',
                                                className='demo-github-link',
                                            ),
                                            href='{}/edit/{}/views/{}/demos/{}.py'.format(
                                                AppConfig.doc_library_repo,
                                                AppConfig.doc_library_branch,
                                                component.__name__,
                                                item['path'],
                                            ),
                                            target='_blank',
                                        ),
                                        title='在Github上编辑此示例',
                                    ),
                                ],
                                className='demo-title',
                            ),
                            html.Div(
                                item['description'],
                                style={'padding': '18px 24px 12px 28px'},
                            ),
                        ],
                        style={'position': 'relative'},
                    ),
                    fac.AntdCenter(
                        fac.AntdSpace(
                            [
                                fac.AntdTooltip(
                                    dcc.Link(
                                        fac.AntdIcon(icon='antd-export'),
                                        href='/~demo/{}/{}'.format(
                                            component.__name__, item['path']
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title='在新窗口打开',
                                ),
                                fac.AntdTooltip(
                                    fac.AntdIcon(
                                        id={
                                            'type': 'demo-code-toggle',
                                            'index': '{}/{}'.format(
                                                component.__name__, item['path']
                                            ),
                                        },
                                        icon='antd-code',
                                        className='demo-operations-icon',
                                    ),
                                    title='展开/收起代码',
                                ),
                            ],
                            size=12,
                        ),
                        className='demo-operations',
                    ),
                    fac.AntdTabs(
                        items=[
                            {
                                'label': item.get('language') or 'Python',
                                'key': item.get('language') or 'Python',
                                'children': fmc.FefferySyntaxHighlighter(
                                    codeString=item['code'],
                                    language=(
                                        item.get('language') or 'Python'
                                    ).lower(),
                                    codeTheme='coy-without-shadows',
                                    codeBlockStyle={'overflowX': 'auto'},
                                ),
                            }
                            for item in getattr(
                                views.AntdDropdown.demos, item['path']
                            ).code_string
                        ],
                        centered=True,
                        className='demo-code-tabs',
                        id={
                            'type': 'demo-code',
                            'index': '{}/{}'.format(
                                component.__name__, item['path']
                            ),
                        },
                        style={'display': 'none'},
                    ),
                ],
                className='demo-container',
                id='demo-container-' + item['path'],
            )
            for item in demos_config
        ],
        direction='vertical',
        size='large',
        style={'width': '100%'},
    )
