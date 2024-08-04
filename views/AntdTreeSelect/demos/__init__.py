from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    status,  # noqa: F401
    different_placement,  # noqa: F401
    multiple,  # noqa: F401
    multiple_checkable,  # noqa: F401
    flat_tree_data,  # noqa: F401
    tree_line,  # noqa: F401
    tree_check_strictly,  # noqa: F401
    show_checked_strategy,  # noqa: F401
    multiple_mode_search,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': None,
    },
    {
        'path': 'disabled',
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
        'path': 'read_only',
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
        'path': 'status',
        'title': '强制状态渲染',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('status', code=True),
                '进行强制状态渲染。',
            ]
        ),
    },
    {
        'path': 'different_placement',
        'title': '不同的悬浮层展开方位',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('placement', code=True),
                '控制悬浮层展开方位。',
            ]
        ),
    },
    {
        'path': 'multiple',
        'title': '多选模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('multiple=True', code=True),
                '开启多选模式。',
            ]
        ),
    },
    {
        'path': 'multiple_checkable',
        'title': '带勾选框的多选模式',
        'description': fac.AntdParagraph(
            [
                '多选模式下设置参数',
                fac.AntdText('treeCheckable=True', code=True),
                '为节点添加勾选框。',
            ]
        ),
    },
    {
        'path': 'flat_tree_data',
        'title': '扁平treeData模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('treeDataMode="flat"', code=True),
                '后可传入扁平结构',
                fac.AntdText('treeData', code=True),
                '进行树结构定义。',
            ]
        ),
    },
    {
        'path': 'tree_line',
        'title': '添加连接线',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('treeLine=True', code=True),
                '开启连接线。',
            ]
        ),
    },
    {
        'path': 'tree_check_strictly',
        'title': '父子节点独立选择',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('treeCheckStrictly=True', code=True),
                '后父子节点选择行为彼此独立。',
            ]
        ),
    },
    {
        'path': 'show_checked_strategy',
        'title': '已选项回填显示策略',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('showCheckedStrategy', code=True),
                '控制已选项回填显示策略。',
            ]
        ),
    },
    {
        'path': 'multiple_mode_search',
        'title': '多模式搜索',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('treeNodeFilterMode', code=True),
                '控制搜索模式。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': None,
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
                            views.AntdTreeSelect.demos, item['path']
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
                                fac.AntdTooltip(
                                    dcc.Link(
                                        fac.AntdIcon(icon='antd-github'),
                                        href='{}/tree/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_library_repo,
                                            AppConfig.doc_library_branch,
                                            component.__name__,
                                            item['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title='在Github中查看完整代码',
                                ),
                                fac.AntdTooltip(
                                    dcc.Link(
                                        html.Img(
                                            src='/assets/imgs/gitee-logo.svg',
                                            width=18,
                                            height=18,
                                            style={
                                                'display': 'block',
                                                'transform': 'translate(-0.05em, 0.05em)',
                                            },
                                        ),
                                        href='{}/blob/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_gitee_library_repo,
                                            AppConfig.doc_library_branch,
                                            component.__name__,
                                            item['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-img',
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
                                views.AntdTreeSelect.demos, item['path']
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
