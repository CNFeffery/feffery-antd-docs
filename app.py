import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from server import app, server

from views import (
    AntdDatePicker,
    AntdDateRangePicker,
    AntdDivider,
    AntdButton,
    AntdSelect,
    AntdTree,
    AntdTable,
    AntdAnchor
)

app.layout = html.Div(
    [
        dcc.Location(id='url'),

        html.Div(
            html.Div(
                [
                    html.P(
                        [html.Span('feffery-antd-components', style={'fontSize': '1.75rem'}),
                         html.Em('0.0.1a24',
                                 style={'fontFamily': 'Times New Romer', 'color': '#ff2c6d', 'fontSize': '0.4rem'}),
                         html.Br(),
                         html.Span('交互式说明文档', style={'fontSize': '2rem'})],
                        style={
                            'fontStyle': 'italic',
                            'fontWeight': 'bold',
                            'padding': '0 10px 0 10px'
                        }
                    ),

                    dcc.Markdown('''
                    本文档基于`Dash`编写，完整源码地址：
                    [https://github.com/CNFeffery/feffery-antd-docs](https://github.com/CNFeffery/feffery-antd-docs)
                    ''', style={
                        'padding': '0 5px 0 5px'
                    }),

                    html.Hr(),
                    dbc.Nav(
                        [
                            dbc.NavItem(
                                dbc.NavLink(
                                    '首页',
                                    href='/feffery-antd-docs/index',
                                    active='exact'
                                ),
                            ),
                            dbc.NavLink(
                                '日期选择框：AntdDatePicker',
                                href='/feffery-antd-docs/AntdDatePicker',
                                active='exact'
                            ),
                            dbc.NavLink(
                                '日期范围选择框：AntdDateRangePicker',
                                href='/feffery-antd-docs/AntdDateRangePicker',
                                active='exact'
                            ),
                            dbc.NavLink(
                                '分割线：AntdDivider',
                                href='/feffery-antd-docs/AntdDivider',
                                active='exact'
                            ),
                            dbc.NavLink(
                                '按钮：AntdButton',
                                href='/feffery-antd-docs/AntdButton',
                                active='exact'
                            ),
                            dbc.NavLink(
                                '下拉选择：AntdSelect',
                                href='/feffery-antd-docs/AntdSelect',
                                active='exact'
                            ),
                            dbc.NavLink(
                                '树形控件：AntdTree',
                                href='/feffery-antd-docs/AntdTree',
                                active='exact'
                            ),
                            dbc.NavLink(
                                '表格：AntdTable',
                                href='/feffery-antd-docs/AntdTable',
                                active='exact'
                            ),
                            dbc.NavLink(
                                '锚点：AntdAnchor',
                                href='/feffery-antd-docs/AntdAnchor',
                                active='exact'
                            ),
                        ],
                        vertical=True,
                        pills=True,
                        style={
                            'padding': '20px 20px 0 20px'
                        }
                    )
                ],
                style={
                    'borderRight': '1px solid #e0e0e0',
                    'width': '400px',
                    'position': 'sticky',
                    'top': '0',
                    'height': '100vh'
                }
            ),
            style={
                'flex': 'none'
            }
        ),

        dbc.Container(
            html.Div(
                dcc.Loading(
                    html.Div(id='docs-content', style={'padding': '50px 50px 0 50px'}),
                    fullscreen=True,
                    type='circle'
                ),
                style={
                    'width': '100%'
                },
                className='loader-wrapper'
            ),
            fluid=True,
            style={
                'width': '100%',
                'overflowY': 'auto'
            }
        )

    ],
    style={
        'display': 'flex'
    }
)


# 路由
@app.callback(
    Output('docs-content', 'children'),
    Input('url', 'pathname')
)
def render_docs_content(pathname):
    if pathname.startswith('/feffery-antd-docs/index'):

        return dcc.Markdown(open('documents/index.md', encoding='utf-8').read(), className='markdown')

    elif pathname.startswith('/feffery-antd-docs/AntdDatePicker'):

        return AntdDatePicker.docs_content


    elif pathname.startswith('/feffery-antd-docs/AntdDateRangePicker'):

        return AntdDateRangePicker.docs_content


    elif pathname.startswith('/feffery-antd-docs/AntdDivider'):

        return AntdDivider.docs_content

    elif pathname.startswith('/feffery-antd-docs/AntdButton'):

        return AntdButton.docs_content

    elif pathname.startswith('/feffery-antd-docs/AntdSelect'):

        return AntdSelect.docs_content

    elif pathname.startswith('/feffery-antd-docs/AntdTree'):

        return AntdTree.docs_content

    elif pathname.startswith('/feffery-antd-docs/AntdTable'):

        return AntdTable.docs_content

    elif pathname.startswith('/feffery-antd-docs/AntdAnchor'):

        return AntdAnchor.docs_content


if __name__ == '__main__':
    app.run_server(debug=True)
