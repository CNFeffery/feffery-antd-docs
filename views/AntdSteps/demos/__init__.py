from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    with_more_info,  # noqa: F401
    custom_icon,  # noqa: F401
    set_current,  # noqa: F401
    vertical,  # noqa: F401
    vertical_info,  # noqa: F401
    dot,  # noqa: F401
    sizes,  # noqa: F401
    current_status,  # noqa: F401
    navigation,  # noqa: F401
    inline,  # noqa: F401
    click_switch,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('基础的静态步骤条。'),
    },
    {
        'path': 'with_more_info',
        'title': '带说明信息的步骤条',
        'description': fac.AntdParagraph(
            '步骤条节点可额外设置副标题及描述信息。'
        ),
    },
    {
        'path': 'custom_icon',
        'title': '自定义图标',
        'description': fac.AntdParagraph('步骤图标可传入任意组件型内容。'),
    },
    {
        'path': 'set_current',
        'title': '设置当前所在步骤',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('current', code=True),
                '可控制当前步骤条所在步骤。',
            ]
        ),
    },
    {
        'path': 'vertical',
        'title': '垂直步骤条',
        'description': fac.AntdParagraph('从上往下垂直展示步骤条信息。'),
    },
    {
        'path': 'vertical_info',
        'title': '垂直展示步骤条信息',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('labelPlacement', code=True),
                '可控制步骤条额外信息的展示形式。',
            ]
        ),
    },
    {
        'path': 'dot',
        'title': '点状步骤条',
        'description': fac.AntdParagraph('简洁风格的点状步骤条。'),
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': fac.AntdParagraph('不同尺寸的步骤条。'),
    },
    {
        'path': 'current_status',
        'title': '控制当前步骤状态',
        'description': None,
    },
    {
        'path': 'navigation',
        'title': '导航风格步骤条',
        'description': None,
    },
    {
        'path': 'inline',
        'title': '内联风格步骤条',
        'description': None,
    },
    {
        'path': 'click_switch',
        'title': '允许点击切换步骤',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('allowClick=True', code=True),
                '后可直接点击步骤进行步骤切换。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            ['通过回调函数监听并控制步骤条功能。']
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
                        getattr(views.AntdSteps.demos, item['path']).render(),
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
                                views.AntdSteps.demos, item['path']
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
