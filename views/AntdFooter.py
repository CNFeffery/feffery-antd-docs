from dash import dcc
from dash import html
import feffery_antd_components as fac

docs_content = html.Div(
    [
        html.H2(
            'AntdFooter(id, className, style, *args, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),

        html.Span(
            '主要参数说明：',
            id='主要参数说明',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        dcc.Markdown(open('documents/AntdFooter.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

        html.Ul(
            [
                html.Li(
                    fac.AntdParagraph(
                        [
                            fac.AntdText('有关'),
                            fac.AntdText('AntdFooter', strong=True),
                            fac.AntdText('的使用示例请移步'),
                            fac.AntdText('AntdLayout', strong=True),
                            fac.AntdText('对应的文档'),
                        ],
                        style={
                            'paddingTop': '20px'
                        }
                    ),
                    style={'listStyleType': 'circle'}
                )
            ]
        ),

        html.Div(style={'height': '100px'})
    ]
)
