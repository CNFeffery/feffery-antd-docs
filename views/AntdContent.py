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
                            'title': '经典布局'
                        },
                        {
                            'title': 'AntdContent 主体内容'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在经典布局方案中构建主体内容部分，'),
                        fac.AntdText('有关'),
                        fac.AntdText('AntdContent', strong=True),
                        fac.AntdText('的使用示例请移步'),
                        fac.AntdText('AntdLayout', strong=True),
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
            component_name='AntdContent'
        )
    ],
    style={
        'display': 'flex'
    }
)
