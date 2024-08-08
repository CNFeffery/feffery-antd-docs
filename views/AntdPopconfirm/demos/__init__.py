from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    custom_description,  # noqa: F401
    custom_icon,  # noqa: F401
    hide_arrow,  # noqa: F401
    placement,  # noqa: F401
    custom_style,  # noqa: F401
    control_open,  # noqa: F401
    basic_callbacks,  # noqa: F401
    question_with_absolute_position,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('为子元素添加气泡确认框。'),
    },
    {
        'path': 'custom_description',
        'title': '自定义描述信息',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('description', code=True),
                '控制描述信息内容。',
            ]
        ),
    },
    {
        'path': 'custom_icon',
        'title': '自定义图标',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('icon', code=True),
                '控制图标内容。',
            ]
        ),
    },
    {
        'path': 'hide_arrow',
        'title': '隐藏附带箭头',
        'description': fac.AntdParagraph(
            [
                '控制参数',
                fac.AntdText('arrow', code=True),
                '隐藏气泡确认框附带的箭头。',
            ]
        ),
    },
    {
        'path': 'placement',
        'title': '悬浮层展开方向',
        'description': fac.AntdParagraph(
            [
                '控制参数',
                fac.AntdText('placement', code=True),
                '设置不同的悬浮层展开方向。',
            ]
        ),
    },
    {
        'path': 'custom_style',
        'title': '自定义样式',
        'description': fac.AntdParagraph('控制不用部分的样式。'),
    },
    {
        'path': 'control_open',
        'title': '展开状态受控',
        'description': fac.AntdParagraph(
            '气泡确认框的展开状态可通过回调进行控制。'
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            '通过回调函数监听确认、取消按钮的点击事件。'
        ),
    },
    {
        'path': 'question_with_absolute_position',
        'title': '常见问题：配合绝对定位',
        'description': fac.AntdParagraph(
            [
                '当直接将',
                fac.AntdText('AntdPopconfirm', strong=True),
                '施加于具有绝对定位样式的元素之上时，可能会遇到悬浮层位置显示异常的问题，推荐的稳定做法是为对应的',
                fac.AntdText('AntdPopconfirm', strong=True),
                '添加一层',
                fac.AntdText('Span', strong=True),
                '父元素，并将原先的绝对定位相关样式转而施加于此父元素之上。',
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
                            views.AntdPopconfirm.demos, item['path']
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
                                views.AntdPopconfirm.demos, item['path']
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