from dash import html
import feffery_antd_components as fac

from .side_props import render_side_props_layout

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(
                    duration=0.3
                ),

                fac.AntdBreadcrumb(
                    items=[
                        {
                            'title': '组件介绍'
                        },
                        {
                            'title': '数据展示'
                        },
                        {
                            'title': '标签页'
                        },
                        {
                            'title': 'AntdTabPane 标签页面板'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('用于在标签页中构建每个标签页面板，'),
                        fac.AntdText('有关'),
                        fac.AntdText('AntdTabPane', strong=True),
                        fac.AntdText('的使用示例请移步'),
                        fac.AntdText('AntdTabs', strong=True),
                        fac.AntdText('对应的文档。')
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                fac.AntdParagraph(
                    [
                        '此组件从下一个大版本（0.3.x）开始将会被移除，建议使用更推荐的',
                        fac.AntdText(
                            'items',
                            code=True
                        ),
                        '方式构造标签页。'
                    ],
                    type='secondary',
                    style={
                        'textIndent': '2rem'
                    }
                ),
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        # 侧边参数栏
        render_side_props_layout(
            component_name='AntdTabPane'
        )
    ],
    style={
        'display': 'flex'
    }
)
