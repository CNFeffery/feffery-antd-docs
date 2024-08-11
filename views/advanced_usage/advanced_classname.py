from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
from dash.dependencies import Component


def render() -> Component:
    """渲染“进阶className的使用”文档页"""

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(duration=0.3),
                    fac.AntdBreadcrumb(
                        items=[
                            {'title': '进阶使用'},
                            {'title': '进阶className的使用'},
                        ]
                    ),
                    fac.AntdDivider(isDashed=True),
                    fac.AntdParagraph(
                        [
                            '从',
                            fac.AntdText('0.2.x', code=True),
                            '版本开始，',
                            fac.AntdText('fac', strong=True),
                            '为常用的',
                            fac.AntdText('className', code=True),
                            '类参数全新引入“动态css类”的概念，使得我们可以以更加自由灵活的方式为组件配置css样式，具体用法说明如下：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdParagraph(
                        '注：此特性针对所有可接受dict型输入的className相关参数均可用',
                        type='secondary',
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdParagraph(
                        [
                            '在之前版本的',
                            fac.AntdText('fac', strong=True),
                            '中，参数',
                            fac.AntdText('className', code=True),
                            '只接受字符型输入，从而配合外部真实存在的css样式文件，或由',
                            fac.AntdText('fuc.FefferyStyle', code=True),
                            '定义的临时css样式代码中所定义的css类名，实现更复杂丰富的样式效果。',
                            '但从',
                            fac.AntdText('fac', strong=True),
                            fac.AntdText('0.2.x', code=True),
                            '版本开始，',
                            fac.AntdText('className', code=True),
                            '参数新增字典型输入支持，最基础的用法可以像参数',
                            fac.AntdText('style', code=True),
                            '一样直接设置css键值对属性，譬如我们如果想要为按钮添加渐变背景色：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    # 动态css类基础使用示例
                    fac.AntdButton(
                        '按钮示例',
                        size='large',
                        className={
                            'background': 'linear-gradient(135deg,#6b73ff,#000dff)',
                            'color': 'white',
                        },
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
# 动态css类基础使用示例
fac.AntdButton(
    '按钮示例',
    size='large',
    className={
        'background': 'linear-gradient(135deg,#6b73ff,#000dff)',
        'color': 'white'
    }
)
""",
                    ),
                    fac.AntdParagraph(
                        [
                            '如果想要在上面按钮示例的基础上，对按钮处于鼠标悬停、聚焦、点击等状态下的样式同样进行一些自定义覆盖，沿用传统的做法就比较繁琐，为方便演示，以配合组件',
                            fac.AntdText('fuc.FefferyStyle', code=True),
                            '为例，我们需要写好原生的css样式代码：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    fuc.FefferyStyle(
                        rawStyle="""
.demo-button {
    background: linear-gradient(135deg,#6b73ff,#000dff);
    color: white;
    transition: transform 0.2s ease;
}

/* 覆盖悬停状态样式 */
.demo-button:hover {
    background: linear-gradient(135deg,#6b73ff,#000dff);
    color: white;
    border-color: white;
}

/* 覆盖聚焦状态样式 */
.demo-button:focus {
    background: linear-gradient(135deg,#6b73ff,#000dff);
    color: white;
    border-color: white;
}

/* 覆盖点击状态样式 */
.demo-button:active {
    background: linear-gradient(135deg,#6b73ff,#000dff);
    color: white;
    border-color: white;
    transform: translateY(3px);
}
"""
                    ),
                    fac.AntdButton(
                        '按钮示例', size='large', className='demo-button'
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
fuc.FefferyStyle(
    rawStyle='''
.demo-button {
    background: linear-gradient(135deg,#6b73ff,#000dff);
    color: white;
    transition: transform 0.2s ease;
}

/* 覆盖悬停状态样式 */
.demo-button:hover {
    background: linear-gradient(135deg,#6b73ff,#000dff);
    color: white;
    border-color: white;
}

/* 覆盖聚焦状态样式 */
.demo-button:focus {
    background: linear-gradient(135deg,#6b73ff,#000dff);
    color: white;
    border-color: white;
}

/* 覆盖点击状态样式 */
.demo-button:active {
    background: linear-gradient(135deg,#6b73ff,#000dff);
    color: white;
    border-color: white;
    transform: translateY(3px);
}
'''
),
fac.AntdButton(
    '按钮示例',
    size='large',
    className='demo-button'
)
""",
                    ),
                    fac.AntdParagraph(
                        [
                            '下面我们换成“动态css类”的方式😉，其中',
                            fac.AntdText('&', code=True),
                            '表示当前组件自身：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdButton(
                        '按钮示例',
                        size='large',
                        className={
                            'background': 'linear-gradient(135deg,#6b73ff,#000dff)',
                            'color': 'white',
                            'transition': 'transform 0.2s ease',
                            # 悬停状态
                            '&:hover': {
                                'background': 'linear-gradient(135deg,#6b73ff,#000dff)',
                                'color': 'white',
                                'borderColor': 'white',
                            },
                            # 聚焦状态
                            '&:focus': {
                                'background': 'linear-gradient(135deg,#6b73ff,#000dff)',
                                'color': 'white',
                                'borderColor': 'white',
                            },
                            # 点击状态
                            '&:active': {
                                'background': 'linear-gradient(135deg,#6b73ff,#000dff)',
                                'color': 'white',
                                'borderColor': 'white',
                                'transform': 'translateY(3px)',
                            },
                        },
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
fac.AntdButton(
    '按钮示例',
    size='large',
    className={
        'background': 'linear-gradient(135deg,#6b73ff,#000dff)',
        'color': 'white',
        'transition': 'transform 0.2s ease',
        # 悬停状态
        '&:hover': {
            'background': 'linear-gradient(135deg,#6b73ff,#000dff)',
            'color': 'white',
            'borderColor': 'white'
        },
        # 聚焦状态
        '&:focus': {
            'background': 'linear-gradient(135deg,#6b73ff,#000dff)',
            'color': 'white',
            'borderColor': 'white'
        },
        # 点击状态
        '&:active': {
            'background': 'linear-gradient(135deg,#6b73ff,#000dff)',
            'color': 'white',
            'borderColor': 'white',
            'transform': 'translateY(3px)'
        },
    }
)
""",
                    ),
                    fac.AntdParagraph(
                        [
                            '通过这种方式，我们也可以非常方便灵活地修改复杂组件内部某些构件元素的样式，以',
                            fac.AntdText('AntdTable', strong=True),
                            '的复杂定制化样式为例（表格组件本身由于底层原因暂不支持动态css类，但我们可以为其包裹其他支持动态css类的容器组件实现需要的效果）：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    # fuc.FefferyDiv支持动态css类
                    fuc.FefferyDiv(
                        fac.AntdTable(
                            columns=[
                                {'dataIndex': f'字段{i}', 'title': f'字段{i}'}
                                for i in range(1, 6)
                            ],
                            data=[{f'字段{i}': 999 for i in range(1, 6)}] * 8,
                            pagination={'pageSize': 5},
                            bordered=True,
                            style={'width': '80%', 'margin': '0 auto'},
                        ),
                        className={
                            '.ant-pagination-total-text': {'color': '#c92a2a'},
                            '.ant-table-thead .ant-table-cell': {
                                'fontWeight': 'bold'
                            },
                            # 修改偶数行背景色
                            'tr:nth-child(even)': {'background': '#c3fae8'},
                            # 覆盖表格行鼠标悬停状态背景色
                            '.ant-table-tbody>tr.ant-table-row:hover>td, .ant-table-tbody>tr>td.ant-table-cell-row-hover': {
                                'background': '#ffec99'
                            },
                        },
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
# fuc.FefferyDiv支持动态css类
fuc.FefferyDiv(
    fac.AntdTable(
        columns=[
            {
                'dataIndex': f'字段{i}',
                'title': f'字段{i}'
            }
            for i in range(1, 6)
        ],
        data=[
            {
                f'字段{i}': 999
                for i in range(1, 6)
            }
        ] * 8,
        pagination={
            'pageSize': 5
        },
        bordered=True,
        style={
            'width': '80%',
            'margin': '0 auto'
        }
    ),
    className={
        '.ant-pagination-total-text': {
            'color': '#c92a2a'
        },
        '.ant-table-thead .ant-table-cell': {
            'fontWeight': 'bold'
        },
        # 修改偶数行背景色
        'tr:nth-child(even)': {
            'background': '#c3fae8'
        },
        # 覆盖表格行鼠标悬停状态背景色
        '.ant-table-tbody>tr.ant-table-row:hover>td, .ant-table-tbody>tr>td.ant-table-cell-row-hover': {
            'background': '#ffec99'
        }
    }
)
""",
                    ),
                    html.Div(style={'height': '100px'}),
                ],
                style={'flex': 'auto', 'padding': '25px'},
            )
        ],
        style={'display': 'flex', 'paddingRight': 40},
    )
