from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    type,  # noqa: F401
    closable,  # noqa: F401
    description,  # noqa: F401
    icon,  # noqa: F401
    top_notice,  # noqa: F401
    loop,  # noqa: F401
    marquee,  # noqa: F401
    action,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from config import AppConfig
from components import mock_browser

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '最简单的用法，适用于简短的警告提示。'
        ),
    },
    {
        'path': 'type',
        'title': '四种样式',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('共有四种样式'),
                fac.AntdText('success', code=True),
                fac.AntdText('、'),
                fac.AntdText('warning', code=True),
                fac.AntdText('、'),
                fac.AntdText('error', code=True),
                fac.AntdText('、'),
                fac.AntdText('info', code=True),
                fac.AntdText('。'),
            ]
        ),
    },
    {
        'path': 'closable',
        'title': '可关闭的警告提示',
        'description': fac.AntdParagraph('显示关闭按钮，点击可关闭警告提示。'),
    },
    {
        'path': 'description',
        'title': '含有辅助性文字介绍',
        'description': fac.AntdParagraph('含有辅助性文字介绍的警告提示。'),
    },
    {
        'path': 'icon',
        'title': '图标',
        'description': fac.AntdParagraph('合适的图标让信息类型更加醒目。'),
    },
    {
        'path': 'top_notice',
        'title': '顶部公告',
        'description': fac.AntdParagraph('页面顶部通告形式。'),
        'iframe': True,
    },
    {
        'path': 'loop',
        'title': '轮播模式',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('当开启轮播模式时，参数'),
                fac.AntdText('meesage', code=True),
                fac.AntdText('需要传入数组型以便进行轮播。'),
            ]
        ),
    },
    {
        'path': 'marquee',
        'title': '走马灯模式',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('当开启走马灯模式时，参数'),
                fac.AntdText('meesage', code=True),
                fac.AntdText('需要传入数组型以便进行轮播。'),
            ]
        ),
    },
    {
        'path': 'action',
        'title': '操作',
        'description': fac.AntdParagraph('可以在右上角自定义操作项。'),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('组件型'),
                fac.AntdText('meesage', code=True),
                fac.AntdText('与'),
                fac.AntdText('description', code=True),
                fac.AntdText('。'),
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
                        (
                            fac.AntdSpace(
                                [
                                    mock_browser.render(),
                                    # 懒加载优化
                                    fuc.FefferyLazyLoad(
                                        html.Iframe(
                                            src='/~demo/{}/{}?padding=no'.format(
                                                component.__name__, item['path']
                                            ),
                                            style={
                                                'border': '1px solid #f0f0f0',
                                                'boxSizing': 'border-box',
                                                'width': '100%',
                                                'height': 350,
                                            },
                                        ),
                                        height=350,
                                        throttle=500,
                                    ),
                                ],
                                direction='vertical',
                                size=0,
                                style={'width': '100%'},
                            )
                            if item.get('iframe')
                            else getattr(
                                views.AntdAlert.demos, item['path']
                            ).render()
                        ),
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
                                        href='/~demo/{}/{}?padding=no'.format(
                                            component.__name__, item['path']
                                        )
                                        if item['path'] == 'top_notice'
                                        else '/~demo/{}/{}'.format(
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
                                        fac.AntdIcon(
                                            icon='si-gitee',
                                            style={'verticalAlign': '-0.3em'},
                                        ),
                                        href='{}/blob/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_gitee_library_repo,
                                            AppConfig.doc_library_branch,
                                            component.__name__,
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
                                views.AntdAlert.demos, item['path']
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
