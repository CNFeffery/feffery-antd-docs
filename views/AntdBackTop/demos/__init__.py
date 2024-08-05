from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from config import AppConfig
from components import mock_browser

from . import (
    basic_usage,  # noqa: F401
    duration,  # noqa: F401
    visibility_height,  # noqa: F401
    container,  # noqa: F401
    basic_callback,  # noqa: F401
)

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '滚动一定距离后出现按钮，点击可回到顶部。'
        ),
        'iframe': True,
    },
    {
        'path': 'duration',
        'title': '设置滚动耗时',
        'description': fac.AntdParagraph(
            '设置回到顶部动作的持续时间，单位为秒。'
        ),
        'iframe': True,
    },
    {
        'path': 'visibility_height',
        'title': '设置组件出现的滚动高度阈值',
        'description': fac.AntdParagraph(
            '设置当滚动高度超过该阈值时，才会显示回到顶部按钮。',
        ),
        'iframe': True,
    },
    {
        'path': 'container',
        'title': '绑定在局部容器中',
        'description': fac.AntdParagraph(
            [
                '可使用',
                fac.AntdText('containerId', strong=True),
                '和',
                fac.AntdText('containerSelector', strong=True),
                '两种参数的方式设置绑定的局部容器，',
                fac.AntdText('containerId', strong=True),
                '接受组件的id，',
                fac.AntdText('containerSelector', strong=True),
                '接受完整的JS代码，如',
                fac.AntdText('document.querySelector("#container")', code=True),
                '。',
            ]
        ),
        'iframe': True,
    },
    {
        'path': 'basic_callback',
        'title': '基础回调',
        'description': fac.AntdParagraph(
            [
                '监听',
                fac.AntdText('BackTop', strong=True),
                '组件的点击事件。',
            ]
        ),
        'iframe': True,
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
                                            src='/~demo/{}/{}'.format(
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
                                views.AntdBackTop.demos, item['path']
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
                                views.AntdBackTop.demos, item['path']
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
