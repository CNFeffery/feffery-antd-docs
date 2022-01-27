from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

docs_content = html.Div(
    [
        html.H2(
            'AntdDescriptionItem(children, id, className, style, *args, **kwargs)',
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

        fmc.FefferyMarkdown(
            markdownStr=open('documents/AntdDescriptionItem.md', encoding='utf-8').read()
        ),

        html.Ul(
            [
                html.Li(
                    fac.AntdParagraph(
                        [
                            fac.AntdText('有关'),
                            fac.AntdText('AntdDescriptionItem', strong=True),
                            fac.AntdText('的使用示例请移步'),
                            fac.AntdText('AntdDescriptions', strong=True),
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
