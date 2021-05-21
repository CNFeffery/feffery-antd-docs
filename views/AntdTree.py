import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdSelect

docs_content = html.Div(
    [
        html.H2(
            'AntdTree(id, className, style, *args, **kwargs)',
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

        dcc.Markdown(open('documents/AntdTree.md', encoding='utf-8').read(),
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
                html.Strong('基础的下拉选择：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                fac.AntdSelect(
                    placeholder='请选择国家：',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国', 'disabled': True},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
                ```
                '''),

                fac.AntdSelect(
                    placeholder='请选择国家：',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国', 'disabled': True},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
