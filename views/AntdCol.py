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
                            'title': '布局'
                        },
                        {
                            'title': '网格系统'
                        },
                        {
                            'title': 'AntdCol 列'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在网格系统中构建每个列，'),
                        fac.AntdText('有关'),
                        fac.AntdText('AntdCol', strong=True),
                        fac.AntdText('的使用示例请移步'),
                        fac.AntdText('AntdRow', strong=True),
                        fac.AntdText('对应的文档。')
                    ]
                )
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        # 侧边参数栏
        render_side_props_layout(
            component_name='AntdCol'
        )
    ],
    style={
        'display': 'flex'
    }
)
