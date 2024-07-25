from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    custom_tab_title,  # noqa: F401
    disabled_tabs,  # noqa: F401
    different_tab_position,  # noqa: F401
    sizes,  # noqa: F401
    centered,  # noqa: F401
    tab_bar_gutter,  # noqa: F401
    tab_animation,  # noqa: F401
    different_type,  # noqa: F401
    extra_content,  # noqa: F401
    basic_callbacks,  # noqa: F401
    tab_add_delete,  # noqa: F401
    tab_context_menu,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            ['使用参数', fac.AntdText('items', code=True), '构造各标签页。']
        ),
    },
    {
        'path': 'custom_tab_title',
        'title': '自定义标签页标题',
        'description': fac.AntdParagraph(
            '标签页标题内容支持自由的组件型定义。'
        ),
    },
    {
        'path': 'disabled_tabs',
        'title': '禁用部分标签页',
        'description': fac.AntdParagraph('对各标签页进行禁用的不同方式。'),
    },
    {
        'path': 'different_tab_position',
        'title': '不同的标签页显示方位',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('tabPosition', code=True),
                '控制标签页显示方位。',
            ]
        ),
    },
    {
        'path': 'sizes',
        'title': '标签页尺寸规格',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('size', code=True),
                '控制标签页尺寸规格。',
            ]
        ),
    },
    {
        'path': 'centered',
        'title': '标签栏居中',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('centered=True', code=True),
                '令标签栏居中。',
            ]
        ),
    },
    {
        'path': 'tab_bar_gutter',
        'title': '控制标签栏间距',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('tabBarGutter', code=True),
                '控制标签栏之间的间距。',
            ]
        ),
    },
    {
        'path': 'tab_animation',
        'title': '控制标签页动画',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('inkBarAnimated', code=True),
                '、',
                fac.AntdText('tabPaneAnimated', code=True),
                '控制标签页切换动画效果。',
            ]
        ),
    },
    {
        'path': 'different_type',
        'title': '标签页类型',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('type', code=True),
                '控制标签页类型。',
            ]
        ),
    },
    {
        'path': 'extra_content',
        'title': '添加额外内容',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('tabBarLeftExtraContent', code=True),
                '、',
                fac.AntdText('tabBarRightExtraContent', code=True),
                '添加额外内容。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                '属性',
                fac.AntdText('activeKey', code=True),
                '对应当前激活的标签页。',
            ]
        ),
    },
    {
        'path': 'tab_add_delete',
        'title': '标签页增删控制',
        'description': fac.AntdParagraph('通过回调函数控制标签页的增删。'),
    },
    {
        'path': 'tab_context_menu',
        'title': '标签页右键菜单交互',
        'description': fac.AntdParagraph(
            '通过回调函数响应标签页标题的右键菜单交互事件。'
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
                        getattr(views.AntdTabs.demos, item['path']).render(),
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
                                views.AntdTabs.demos, item['path']
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
