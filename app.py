import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import feffery_antd_components as fac

from server import app, server

from views import (
    AntdDatePicker,
    AntdDivider,
    AntdButton
)

app.layout = html.Div(
    [
        dcc.Location(id='url'),

        html.Div(
            html.Div(
                [
                    html.P(
                        [html.Span('feffery-antd-components', style={'fontSize': '1.75rem'}),
                         html.Em('v0.0.1a6',
                                 style={'fontFamily': 'Times New Romer', 'color': '#ff2c6d', 'fontSize': '0.4rem'}),
                         html.Br(),
                         html.Span('交互式说明文档', style={'fontSize': '2rem'})],
                        style={
                            'fontStyle': 'italic',
                            'fontWeight': 'bold',
                            'padding': '0 10px 0 10px'
                        }
                    ),

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
                                '分割线：AntdDivider',
                                href='/feffery-antd-docs/AntdDivider',
                                active='exact'
                            ),
                            dbc.NavLink(
                                '按钮：AntdButton',
                                href='/feffery-antd-docs/AntdButton',
                                active='exact'
                            )
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
                    html.Div(id='docs-content', style={'padding': '100px 100px 0 100px'}),
                    fullscreen=True
                ),
                style={
                    'width': '100%'
                }
            ),
            fluid=True,
            style={
                'width': 'calc(100% - 20px)',
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
    if pathname == '/feffery-antd-docs/index':

        return dcc.Markdown(open('documents/index.md', encoding='utf-8').read(), className='markdown')

    elif pathname == '/feffery-antd-docs/AntdDatePicker':

        return AntdDatePicker.docs_content


    elif pathname == '/feffery-antd-docs/AntdDivider':

        return AntdDivider.docs_content

    elif pathname == '/feffery-antd-docs/AntdButton':

        return AntdButton.docs_content


if __name__ == '__main__':
    app.run_server(debug=True)
