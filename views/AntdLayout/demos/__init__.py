from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    right_sider,  # noqa: F401
    collapsible_sider,  # noqa: F401
    responsive_collapsible_sider,  # noqa: F401
    collapsible_sider_with_menu,  # noqa: F401
    collapsible_sider_custom_trigger,  # noqa: F401
)
from config import AppConfig
from components import mock_browser

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                '经典布局方案的重点在于用',
                fac.AntdText('AntdLayout', strong=True),
                '包裹嵌套其他经典布局组件，从而构建出常用的各种经典页面布局方案。',
            ]
        ),
    },
    {
        'path': 'right_sider',
        'title': '右侧侧边栏',
        'description': fac.AntdParagraph('侧边栏方位可调整。'),
    },
    {
        'path': 'collapsible_sider',
        'title': '可折叠侧边栏',
        'description': fac.AntdParagraph(
            [
                '为',
                fac.AntdText('AntdSider', strong=True),
                '设置',
                fac.AntdText('collapsible=True', code=True),
                '开启自带的侧边栏折叠功能。',
            ]
        ),
        'iframe': True,
        'no_padding': True,
    },
    {
        'path': 'responsive_collapsible_sider',
        'title': '响应式可折叠侧边栏',
        'description': fac.AntdParagraph(
            '侧边栏可以指定屏幕宽度断点为阈值进行自动折叠及展开。'
        ),
        'iframe': True,
        'no_padding': True,
    },
    {
        'path': 'collapsible_sider_with_menu',
        'title': '可折叠侧边栏+导航菜单',
        'description': fac.AntdParagraph(
            '侧边栏折叠可联动内部的导航菜单组件。'
        ),
        'iframe': True,
        'no_padding': True,
    },
    {
        'path': 'collapsible_sider_custom_trigger',
        'title': '自定义折叠触发控件',
        'description': fac.AntdParagraph(
            [
                '设置',
                fac.AntdText('trigger=None', code=True),
                '后可自定义控件配合回调函数控制侧边栏折叠状态。',
            ]
        ),
        'iframe': True,
        'no_padding': True,
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
                                            src='/~demo/{}/{}{}'.format(
                                                component.__name__,
                                                item['path'],
                                                (
                                                    '?padding=no'
                                                    if item.get('no_padding')
                                                    else ''
                                                ),
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
                                views.AntdLayout.demos, item['path']
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
                                        href='/~demo/{}/{}{}'.format(
                                            component.__name__,
                                            item['path'],
                                            (
                                                '?padding=no'
                                                if item.get('no_padding')
                                                else ''
                                            ),
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
                                views.AntdLayout.demos, item['path']
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
