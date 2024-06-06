from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    vertical_mode,  # noqa: F401
    custom_step,  # noqa: F401
    custom_marks,  # noqa: F401
    tooltip_visible,  # noqa: F401
    tooltip_prefix_suffix,  # noqa: F401
    disabled_status,  # noqa: F401
    read_only_status,  # noqa: F401
    rail_style,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                '基本滑动条。当',
                fac.AntdText('range=True', code=True),
                '时，渲染为双滑块。',
            ]
        ),
    },
    {
        'path': 'vertical_mode',
        'title': '垂直模式',
        'description': fac.AntdParagraph('垂直方向的滑动条。'),
    },
    {
        'path': 'custom_step',
        'title': '滑动步长',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('step', code=True),
                '自定义滑动步长。',
            ]
        ),
    },
    {
        'path': 'custom_marks',
        'title': '刻度标签',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('marks', code=True),
                '自定义刻度标签。',
            ]
        ),
    },
    {
        'path': 'tooltip_visible',
        'title': '滑动提示内容显示策略',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('tooltipVisible', code=True),
                '显示或者隐藏滑动提示内容。',
            ]
        ),
    },
    {
        'path': 'tooltip_prefix_suffix',
        'title': '滑动提示内容前后缀',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('tooltipPrefix', code=True),
                '控制滑动提示内容前缀。',
                '设置参数',
                fac.AntdText('tooltipSuffix', code=True),
                '控制滑动提示内容后缀。',
            ]
        ),
    },
    {
        'path': 'disabled_status',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('disabled=True', code=True),
                '开启禁用状态。',
            ]
        ),
    },
    {
        'path': 'read_only_status',
        'title': '只读状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('readOnly=True', code=True),
                '开启只读状态。',
            ]
        ),
    },
    {
        'path': 'rail_style',
        'title': '滑轨样式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('railStyle', code=True),
                '自定义滑轨样式。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('可用于监听滑动条滑动事件。'),
    },
]


def render(component: Component) -> Component:
    """渲染当前组件演示用例"""

    return fac.AntdSpace(
        [
            html.Div(
                [
                    html.Div(
                        getattr(views.AntdSlider.demos, item['path']).render(),
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
                                views.AntdSlider.demos, item['path']
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
