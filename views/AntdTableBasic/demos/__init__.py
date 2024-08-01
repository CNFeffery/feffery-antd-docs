from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    percentage_column_width,  # noqa: F401
    numeric_column_width,  # noqa: F401
    css_column_width,  # noqa: F401
    max_height_usage,  # noqa: F401
    max_width_usage,  # noqa: F401
    fixed_columns,  # noqa: F401
    bordered,  # noqa: F401
    column_content_align,  # noqa: F401
    editable,  # noqa: F401
    listen_edit_event,  # noqa: F401
    sizes,  # noqa: F401
    group_columns,  # noqa: F401
)
from config import AppConfig

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('基础数据表格。'),
    },
    {
        'path': 'percentage_column_width',
        'title': '百分比列宽',
        'description': fac.AntdParagraph('使用百分比形式控制列宽。'),
    },
    {
        'path': 'numeric_column_width',
        'title': '数值型列宽',
        'description': fac.AntdParagraph(
            '默认情况下，为各字段设置数值型列宽后，会自动计算转换为比例，作为各个字段的百分比列宽。'
        ),
    },
    {
        'path': 'css_column_width',
        'title': 'css控制列宽',
        'description': fac.AntdParagraph(
            [
                '基于',
                fac.AntdText('CSS', strong=True),
                '实现更为灵活的列宽控制。',
            ]
        ),
    },
    {
        'path': 'max_height_usage',
        'title': 'maxHeight的使用',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('maxHeight', code=True),
                '后，当表格实际像素高度超出',
                fac.AntdText('maxHeight', code=True),
                '所设定值时，会自动渲染垂直滚动条。',
            ]
        ),
    },
    {
        'path': 'max_width_usage',
        'title': 'maxWidth的使用',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('maxWidth', code=True),
                '后，当表格实际像素宽度超出',
                fac.AntdText('maxWidth', code=True),
                '所设定值时，会自动渲染水平滚动条。',
            ]
        ),
    },
    {
        'path': 'fixed_columns',
        'title': '冻结部分列',
        'description': fac.AntdParagraph(
            [
                '在参数',
                fac.AntdText('columns', code=True),
                '中控制字段的',
                fac.AntdText('fixed', code=True),
                '以实现冻结部分列的功能。',
            ]
        ),
    },
    {
        'path': 'bordered',
        'title': '添加边框线',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('bordered=True', code=True),
                '为表格添加边框线。',
            ]
        ),
    },
    {
        'path': 'column_content_align',
        'title': '字段内容对齐方式',
        'description': fac.AntdParagraph(
            [
                '在参数',
                fac.AntdText('columns', code=True),
                '中控制字段的',
                fac.AntdText('align', code=True),
                '以控制字段内容对齐方式。',
            ]
        ),
    },
    {
        'path': 'editable',
        'title': '可编辑单元格',
        'description': fac.AntdParagraph(
            [
                '在参数',
                fac.AntdText('columns', code=True),
                '中控制字段的',
                fac.AntdText('editable', code=True),
                '以开启字段单元格可编辑功能。',
            ]
        ),
    },
    {
        'path': 'listen_edit_event',
        'title': '监听单元格编辑事件',
        'description': fac.AntdParagraph(
            [
                '在回调函数中监听属性',
                fac.AntdText('recentlyChangedRow', code=True),
                '、',
                fac.AntdText('recentlyChangedColumn', code=True),
                '获知最近一次单元格编辑事件相关信息。',
            ]
        ),
    },
    {
        'path': 'sizes',
        'title': '表格尺寸规格',
        'description': fac.AntdParagraph(
            ['设置参数', fac.AntdText('size', code=True), '控制表格尺寸规格。']
        ),
    },
    {
        'path': 'group_columns',
        'title': '多层表头',
        'description': fac.AntdParagraph(
            [
                '在参数',
                fac.AntdText('columns', code=True),
                '中控制字段的',
                fac.AntdText('group', code=True),
                '以渲染具有相应多层表头的表格。',
            ]
        ),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return fac.AntdSpace(
        [
            html.Div(
                [
                    html.Div(
                        getattr(
                            views.AntdTableBasic.demos, item['path']
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
                                                section_name
                                                or component.__name__,
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
                                            section_name or component.__name__,
                                            item['path'],
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
                                views.AntdTableBasic.demos, item['path']
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
