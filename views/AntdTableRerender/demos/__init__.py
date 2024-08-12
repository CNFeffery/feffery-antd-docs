from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    link_mode,  # noqa: F401
    ellipsis_mode,  # noqa: F401
    copyable_mode,  # noqa: F401
    ellipsis_copyable_mode,  # noqa: F401
    tags_mode,  # noqa: F401
    status_badge_mode,  # noqa: F401
    image_mode,  # noqa: F401
    custom_format_mode,  # noqa: F401
    corner_mark_mode,  # noqa: F401
    row_merge_mode,  # noqa: F401
    dropdown_links_mode,  # noqa: F401
    image_avatar_mode,  # noqa: F401
    mini_line_mode,  # noqa: F401
    mini_bar_mode,  # noqa: F401
    mini_area_mode,  # noqa: F401
    mini_progress_mode,  # noqa: F401
    mini_ring_progress_mode,  # noqa: F401
    button_mode_and_callbacks,  # noqa: F401
    checkbox_mode_and_callbacks,  # noqa: F401
    switch_mode_and_callbacks,  # noqa: F401
    dropdown_mode_and_callbacks,  # noqa: F401
    select_mode_and_callbacks,  # noqa: F401
    custom_component_cell_render,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'link_mode',
        'title': 'link链接模式',
        'description': fac.AntdParagraph('将单元格内容快捷渲染为链接形式。'),
    },
    {
        'path': 'ellipsis_mode',
        'title': 'ellipsis长内容省略模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为长内容省略形式。'
        ),
    },
    {
        'path': 'copyable_mode',
        'title': 'copyable可复制模式',
        'description': fac.AntdParagraph('将单元格内容快捷渲染为可复制形式。'),
    },
    {
        'path': 'ellipsis_copyable_mode',
        'title': 'ellipsis-copyable长内容省略+可复制模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为长内容省略+可复制形式。'
        ),
    },
    {
        'path': 'tags_mode',
        'title': 'tags标签模式',
        'description': fac.AntdParagraph('将单元格内容快捷渲染为标签形式。'),
    },
    {
        'path': 'status_badge_mode',
        'title': 'status-badge状态徽标模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为状态徽标形式。'
        ),
    },
    {
        'path': 'image_mode',
        'title': 'image图片模式',
        'description': fac.AntdParagraph('将单元格内容快捷渲染为图片形式。'),
    },
    {
        'path': 'custom_format_mode',
        'title': 'custom-format自定义格式模式',
        'description': fac.AntdParagraph(
            [
                '在这个例子中，数值测试1与数值测试2字段本质上都是数值型，但在',
                fac.AntdText("'custom-format'", code=True),
                '模式下，可通过参数',
                fac.AntdText('customFormatFuncs', code=True),
                '自定义的js函数来改变单元格中表面上所渲染出的内容格式。',
            ]
        ),
    },
    {
        'path': 'corner_mark_mode',
        'title': 'corner-mark角标模式',
        'description': fac.AntdParagraph('将单元格内容快捷渲染为角标形式。'),
    },
    {
        'path': 'row_merge_mode',
        'title': 'row-merge跨行单元格合并模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为跨行单元格合并形式。'
        ),
    },
    {
        'path': 'dropdown_links_mode',
        'title': 'dropdown-links下拉链接菜单模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为下拉链接菜单形式。'
        ),
    },
    {
        'path': 'image_avatar_mode',
        'title': 'image-avatar图片型头像模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为图片型头像形式。'
        ),
    },
    {
        'path': 'mini_line_mode',
        'title': 'mini-line迷你折线图模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为迷你折线图形式。'
        ),
    },
    {
        'path': 'mini_bar_mode',
        'title': 'mini-bar迷你柱状图模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为迷你柱状图形式。'
        ),
    },
    {
        'path': 'mini_area_mode',
        'title': 'mini-area迷你面积图模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为迷你面积图形式。'
        ),
    },
    {
        'path': 'mini_progress_mode',
        'title': 'mini-progress迷你进度图模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为迷你进度图形式。'
        ),
    },
    {
        'path': 'mini_ring_progress_mode',
        'title': 'mini-ring-progress迷你环形进度图模式',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为迷你环形进度图形式。'
        ),
    },
    {
        'path': 'button_mode_and_callbacks',
        'title': 'button按钮模式及回调监听',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为按钮形式，并通过回调监听相关事件。'
        ),
    },
    {
        'path': 'checkbox_mode_and_callbacks',
        'title': 'checkbox勾选框模式及回调监听',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为勾选框形式，并通过回调监听相关事件。'
        ),
    },
    {
        'path': 'switch_mode_and_callbacks',
        'title': 'switch开关模式及回调监听',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为开关形式，并通过回调监听相关事件。'
        ),
    },
    {
        'path': 'dropdown_mode_and_callbacks',
        'title': 'dropdown下拉菜单模式及回调监听',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为下拉菜单形式，并通过回调监听相关事件。'
        ),
    },
    {
        'path': 'select_mode_and_callbacks',
        'title': 'select下拉选择模式及回调监听',
        'description': fac.AntdParagraph(
            '将单元格内容快捷渲染为下拉选择形式，并通过回调监听相关事件。'
        ),
    },
    {
        'path': 'custom_component_cell_render',
        'title': '自定义单元格元素',
        'description': fac.AntdParagraph(
            '目前已有的快捷再渲染模式满足不了你的需求？没关系，任何组件元素都可以作为单元格值被传入😉！（此特性建议仅用作静态展示使用）'
        ),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return fac.AntdSpace(
        [
            html.Div(
                [
                    html.Div(
                        getattr(
                            views.AntdTableRerender.demos, item['path']
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
                                                section_name
                                                or component.__name__,
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
                                            section_name or component.__name__,
                                            item['path'],
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
                                fac.AntdTooltip(
                                    dcc.Link(
                                        fac.AntdIcon(icon='antd-github'),
                                        href='{}/tree/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_library_repo,
                                            AppConfig.doc_library_branch,
                                            section_name or component.__name__,
                                            item['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title='在Github中查看完整代码',
                                ),
                                fac.AntdTooltip(
                                    dcc.Link(
                                        fac.AntdIcon(
                                            icon='si-gitee',
                                            style={'verticalAlign': '-0.3em'},
                                        ),
                                        href='{}/blob/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_gitee_library_repo,
                                            AppConfig.doc_library_branch,
                                            section_name or component.__name__,
                                            item['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title='在Gitee中查看完整代码',
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
                                views.AntdTableRerender.demos, item['path']
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
