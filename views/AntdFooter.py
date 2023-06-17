from dash import html
import feffery_antd_components as fac

from .side_props import render_side_props_layout


def docs_content(language: str = '中文'):

    return html.Div(
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
                                'title': 'AntdFooter 页尾'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于在经典布局方案中构建页尾部分，'),
                            fac.AntdText('有关'),
                            fac.AntdText('AntdFooter', strong=True),
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
                component_name='AntdFooter',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
