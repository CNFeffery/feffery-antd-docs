from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    disabled,  # noqa: F401
    list_max_length,  # noqa: F401
    file_types,  # noqa: F401
    multiple_upload,  # noqa: F401
    directory_upload,  # noqa: F401
    failed_tooltip,  # noqa: F401
    confirm_before_delete,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '点击目标区域或拖拽文件至目标区域触发文件上传功能。'
        ),
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
        'path': 'list_max_length',
        'title': '限制上传列表记录数量',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('fileListMaxLength', code=True),
                '限制上传列表中的文件上传记录最大数量。',
            ]
        ),
    },
    {
        'path': 'file_types',
        'title': '限制上传文件类型',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('fileTypes', code=True),
                '限制可上传的文件类型。',
            ]
        ),
    },
    {
        'path': 'multiple_upload',
        'title': '多文件上传',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('multiple=True', code=True),
                '后可一次性上传多个文件。',
            ]
        ),
    },
    {
        'path': 'directory_upload',
        'title': '文件夹上传',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('directory=True', code=True),
                '后可选择文件夹进行内部文件的批量上传。',
            ]
        ),
    },
    {
        'path': 'failed_tooltip',
        'title': '自定义失败文件提示',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('failedTooltipInfo', code=True),
                '进行上传失败文件的错误提示信息自定义。',
            ]
        ),
    },
    {
        'path': 'confirm_before_delete',
        'title': '删除前确认',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('confirmBeforeDelete=True', code=True),
                '为已上传文件记录的删除操作添加二次确认功能。',
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
                            views.AntdDraggerUpload.demos, item['path']
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
                                views.AntdDraggerUpload.demos, item['path']
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
