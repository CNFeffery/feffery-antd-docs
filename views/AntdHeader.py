from dash import dcc
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.H2(
            'AntdHeader(id, className, style, *args, **kwargs)',
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

        fuc.FefferyMarkdown(
            markdownStr=open('documents/AntdHeader.md', encoding='utf-8').read()
        ),

        html.Ul(
            [
                html.Li(
                    fac.AntdParagraph(
                        [
                            fac.AntdText('有关'),
                            fac.AntdText('AntdHeader', strong=True),
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
