import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

docs_content = html.Div(
    [
        html.H2(
            'AntdDivider(id, className, style, *args, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),
        fac.AntdAnchor(
            linkDict=[
                {'title': '主要参数说明', 'href': '#主要参数说明'},
                {
                    'title': '使用示例',
                    'href': '#使用示例',
                    'children': [
                        {'title': '常规的实线与虚线分割线', 'href': '#常规的实线与虚线分割线'},
                        {'title': '内嵌文字及文字位置设置', 'href': '#内嵌文字及文字位置设置'},
                        {'title': '竖直分割线', 'href': '#竖直分割线'},
                    ]
                },
            ]
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

        dcc.Markdown(open('documents/AntdDivider.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

        html.Span(
            '使用示例：',
            id='使用示例',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        html.Hr(),

        html.Div(
            [
                html.Strong(
                    '常规的实线与虚线分割线：',
                    id='常规的实线与虚线分割线',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                # 水平分割线使用border-top相关css属性自定义样式
                fac.AntdDivider(style={'borderTopColor': 'black'}),
                
                fac.AntdDivider(isDashed=True, style={'borderTopColor': 'black'})
                ```
                '''),

                # 水平分割线使用border-top相关css属性自定义样式
                fac.AntdDivider(style={'borderTopColor': 'black'}),

                fac.AntdDivider(isDashed=True, style={'borderTopColor': 'black'}),
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '内嵌文字及文字位置设置：',
                    id='内嵌文字及文字位置设置',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                # 默认居中
                fac.AntdDivider('AntdDivider'),

                # 左对齐
                fac.AntdDivider('AntdDivider', innerTextOrientation='left'),

                # 右对齐且设置内嵌文字样式
                fac.AntdDivider('AntdDivider', innerTextOrientation='right', style={'fontStyle': 'oblique'})
                ```
                '''),

                # 默认居中
                fac.AntdDivider('AntdDivider'),

                # 左对齐
                fac.AntdDivider('AntdDivider', innerTextOrientation='left'),

                # 右对齐且设置内嵌文字样式
                fac.AntdDivider('AntdDivider', innerTextOrientation='right', style={'fontStyle': 'oblique'}),
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '竖直分割线：',
                    id='竖直分割线',
                    style={'paddingTop': '5px'},
                ),

                dcc.Markdown('''
                ```Python
                # 默认居中
                fac.AntdDivider('AntdDivider'),

                # 左对齐
                fac.AntdDivider('AntdDivider', innerTextOrientation='left'),

                # 右对齐且设置内嵌文字样式
                fac.AntdDivider('AntdDivider', innerTextOrientation='right', style={'fontStyle': 'oblique'})
                ```
                '''),

                # 竖直分割线使用border-left相关css属性自定义样式
                html.Div(
                    [
                        '项目1',
                        fac.AntdDivider(direction='vertical', style={'borderLeftColor': 'black'}),
                        '项目2',
                        fac.AntdDivider(direction='vertical', style={'borderLeftColor': 'red'}),
                        '项目3'
                    ]
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
