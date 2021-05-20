import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdButton

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

        html.Span(
            '主要参数说明：',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        dcc.Markdown(open('documents/AntdButton.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

        html.Span(
            '使用示例：',
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
                html.Strong('不同type对应按钮样式风格：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdButton('default'),
                        fac.AntdButton('primary', type='primary'),
                        fac.AntdButton('dashed', type='dashed'),
                        fac.AntdButton('link', type='link'),
                        fac.AntdButton('text', type='text')
                    ]
                )
                ```
                '''),

                html.Div(
                    [
                        fac.AntdButton('default'),
                        fac.AntdButton('primary', type='primary'),
                        fac.AntdButton('dashed', type='dashed'),
                        fac.AntdButton('link', type='link'),
                        fac.AntdButton('text', type='text')
                    ]
                ),

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('充当跳转功能使用：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                fac.AntdButton(href='https://github.com/CNFeffery/feffery-antd-components',
                               target='_blank')
                ```
                '''),

                fac.AntdButton('feffery-antd-components',
                               href='https://github.com/CNFeffery/feffery-antd-components',
                               target='_blank',
                               type='primary')

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('撑满父级元素宽度：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                fac.AntdButton('feffery-antd-components',
                               block=True,
                               type='primary')
                ```
                '''),

                fac.AntdButton('feffery-antd-components',
                               block=True,
                               type='primary')

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('显示为危险警告状态：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdButton('default', danger=True),
                        fac.AntdButton('primary', type='primary', danger=True),
                        fac.AntdButton('dashed', type='dashed', danger=True),
                        fac.AntdButton('link', type='link', danger=True),
                        fac.AntdButton('text', type='text', danger=True)
                    ]
                )
                ```
                '''),

                html.Div(
                    [
                        fac.AntdButton('default', danger=True),
                        fac.AntdButton('primary', type='primary', danger=True),
                        fac.AntdButton('dashed', type='dashed', danger=True),
                        fac.AntdButton('link', type='link', danger=True),
                        fac.AntdButton('text', type='text', danger=True)
                    ]
                ),

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('显示为不可点击状态：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdButton('default', disabled=True),
                        fac.AntdButton('primary', type='primary', disabled=True),
                        fac.AntdButton('dashed', type='dashed', disabled=True),
                        fac.AntdButton('link', type='link', disabled=True),
                        fac.AntdButton('text', type='text', disabled=True)
                    ]
                )
                ```
                '''),

                html.Div(
                    [
                        fac.AntdButton('default', disabled=True),
                        fac.AntdButton('primary', type='primary', disabled=True),
                        fac.AntdButton('dashed', type='dashed', disabled=True),
                        fac.AntdButton('link', type='link', disabled=True),
                        fac.AntdButton('text', type='text', disabled=True)
                    ]
                ),

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('修改按钮形状：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdButton('默认'),
                        fac.AntdButton('circle', shape='circle'),
                        fac.AntdButton('round', shape='round')
                    ]
                )
                ```
                '''),

                html.Div(
                    [
                        fac.AntdButton('默认', type='primary'),
                        fac.AntdButton('circle', shape='circle', type='primary'),
                        fac.AntdButton('round', shape='round', type='primary')
                    ]
                ),

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('回调示例：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdButton('默认'),
                        fac.AntdButton('circle', shape='circle'),
                        fac.AntdButton('round', shape='round')
                    ]
                )
                ```
                '''),

                fac.AntdButton('点我点我', type='primary', id='button-demo'),
                html.Br(),
                html.Em(id='button-demo-output')

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
