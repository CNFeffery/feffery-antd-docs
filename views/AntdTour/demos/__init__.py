from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    arrow_placement,  # noqa: F401
    basic_usage,  # noqa: F401
    mask,  # noqa: F401,
    buttons,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最简单的用法。'),
    },
    {
        'path': 'mask',
        'title': '设置遮罩层',
        'description': fac.AntdParagraph(
            [
                '可对遮罩层的样式进行修改，或设置为非模态引导（即无遮罩，同时为了强调引导本身，建议与',
                fac.AntdText('type="primary"', code=True),
                '配合使用）。',
            ]
        ),
    },
    {
        'path': 'arrow_placement',
        'title': '设置引导弹框位置和箭头',
        'description': fac.AntdParagraph(
            '可设置引导弹框相对于元素的位置，以及箭头的方向及是否指向中心。'
        ),
    },
    {
        'path': 'buttons',
        'title': '设置上一步和下一步按钮',
        'description': fac.AntdParagraph(
            '可传入任意Dash组件设置为上一步和下一步按钮。'
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
                        getattr(views.AntdTour.demos, item['path']).render(),
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
                                views.AntdTour.demos, item['path']
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
