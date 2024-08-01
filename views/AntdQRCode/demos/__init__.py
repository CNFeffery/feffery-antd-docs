from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    qrcode_icon,  # noqa: F401
    icon_size,  # noqa: F401
    border,  # noqa: F401
    qrcode_status,  # noqa: F401
    custom_render_type,  # noqa: F401
    custom_color,  # noqa: F401
    custom_size,  # noqa: F401
    error_level,  # noqa: F401
    download_qrcode,  # noqa: F401
    high_usage,  # noqa: F401
    auto_spin,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('基本用法。'),
    },
    {
        'path': 'qrcode_icon',
        'title': '带图片的例子',
        'description': fac.AntdParagraph('带图片的二维码。'),
    },
    {
        'path': 'icon_size',
        'title': '二维码中图片大小',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('iconSize', code=True),
                fac.AntdText('调整二维码中图片的大小。'),
            ]
        ),
    },
    {
        'path': 'border',
        'title': '边框',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('bordered', code=True),
                fac.AntdText('显示或隐藏边框。'),
            ]
        ),
    },
    {
        'path': 'qrcode_status',
        'title': '不同的状态',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('可以通过'),
                fac.AntdText('status', code=True),
                fac.AntdText('的值控制二维码的状态，提供了'),
                fac.AntdText('active', code=True),
                fac.AntdText('、'),
                fac.AntdText('expired', code=True),
                fac.AntdText('、'),
                fac.AntdText('loading', code=True),
                fac.AntdText('、'),
                fac.AntdText('scanned', code=True),
                fac.AntdText('四个值。'),
            ]
        ),
    },
    {
        'path': 'custom_render_type',
        'title': '自定义渲染类型',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('type', code=True),
                fac.AntdText('自定义渲染结果，提供'),
                fac.AntdText('canvas', code=True),
                fac.AntdText('和'),
                fac.AntdText('svg', code=True),
                fac.AntdText('两个选项。'),
            ]
        ),
    },
    {
        'path': 'custom_color',
        'title': '自定义颜色',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('color', code=True),
                fac.AntdText('自定义二维码颜色，通过设置'),
                fac.AntdText('bgColor', code=True),
                fac.AntdText('自定义背景颜色。'),
            ]
        ),
    },
    {
        'path': 'custom_size',
        'title': '自定义尺寸',
        'description': fac.AntdParagraph('自定义尺寸。'),
    },
    {
        'path': 'error_level',
        'title': '纠错比例',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('errorLevel', code=True),
                fac.AntdText('调整不同的容错等级。'),
            ]
        ),
    },
    {
        'path': 'download_qrcode',
        'title': '下载二维码',
        'description': fac.AntdParagraph('下载二维码的简单实现。'),
    },
    {
        'path': 'auto_spin',
        'title': '自动进入加载中状态',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('autoSpin', code=True),
                fac.AntdText('控制在'),
                fac.AntdText('value', code=True),
                fac.AntdText('处于回调更新中时，是否自动切换为'),
                fac.AntdText('loading', code=True),
                fac.AntdText('状态。'),
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('监听当前"点击刷新"按钮累计点击次数，仅在'),
                fac.AntdText('status', code=True),
                fac.AntdText('为'),
                fac.AntdText("'expired'", code=True),
                fac.AntdText('时有效。'),
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
                        getattr(views.AntdQRCode.demos, item['path']).render(),
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
                                views.AntdQRCode.demos, item['path']
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
