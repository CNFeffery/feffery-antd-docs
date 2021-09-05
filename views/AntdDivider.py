import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

docs_content = html.Div(
    [
        html.H2(
            'AntdDivider(id, className, *args, **kwargs)',
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
            ],
            containerId='docs-content',
            targetOffset=200
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

        html.Div(
            html.Span(
                '使用示例',
                id='使用示例',
                style={
                    'borderLeft': '4px solid grey',
                    'padding': '3px 0 3px 10px',
                    'backgroundColor': '#f5f5f5',
                    'fontWeight': 'bold',
                    'fontSize': '1.2rem'
                }
            ),
            style={
                'marginBottom': '10px'
            }
        ),

        html.Div(
            [
                fac.AntdDivider(),

                fac.AntdDivider(isDashed=True),

                fac.AntdDivider(
                    '常规的实线与虚线分割线',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdDivider(),

                                fac.AntdDivider(isDashed=True)
                                ```
                                '''),
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )

            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='常规的实线与虚线分割线',
            className='div-highlight'
        ),

        html.Div(
            [
                # 默认居中
                fac.AntdDivider('AntdDivider'),

                # 左对齐
                fac.AntdDivider('AntdDivider', innerTextOrientation='left'),

                # 右对齐且设置内嵌文字样式
                fac.AntdDivider('AntdDivider', innerTextOrientation='right', fontStyle='oblique'),

                fac.AntdDivider(
                    '内嵌文字及文字位置设置',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                # 默认居中
                                fac.AntdDivider('AntdDivider'),

                                # 左对齐
                                fac.AntdDivider('AntdDivider', innerTextOrientation='left'),

                                # 右对齐且设置内嵌文字样式
                                fac.AntdDivider('AntdDivider', innerTextOrientation='right', fontStyle='oblique')
                                ```
                                '''),
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )
            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='内嵌文字及文字位置设置',
            className='div-highlight'
        ),

        html.Div(
            [
                html.Div(
                    [
                        '项目1',
                        fac.AntdDivider(direction='vertical', lineColor='black'),
                        '项目2',
                        fac.AntdDivider(direction='vertical', lineColor='red'),
                        '项目3'
                    ]
                ),

                fac.AntdDivider(
                    '竖直分割线',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                html.Div(
                                    [
                                        '项目1',
                                        fac.AntdDivider(direction='vertical', lineColor='black'),
                                        '项目2',
                                        fac.AntdDivider(direction='vertical', lineColor='red'),
                                        '项目3'
                                    ]
                                )
                                ```
                                '''),
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )
            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='竖直分割线',
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)
