from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

from server import app

docs_content = html.Div(
    [
        fac.AntdBackTop(
            containerId='docs-content',
            duration=0.6
        ),

        html.Div(
            [
                fac.AntdTitle(
                    '1 Dash+fac开发环境的准备',
                    id='1 Dash+fac开发环境的准备',
                    level=2
                ),
                fmc.FefferyMarkdown(
                     codeTheme='a11y-dark',
                    markdownStr=open('./documents/1 Dash+fac开发环境的准备.md', encoding='utf-8').read()
                ),
                fac.AntdTitle(
                    '2 用Dash开发静态页面',
                    id='2 用Dash开发静态页面',
                    level=2
                ),
                fmc.FefferyMarkdown(
                     codeTheme='a11y-dark',
                    markdownStr=open('./documents/2 用Dash开发静态页面.md', encoding='utf-8').read(),
                    renderHtml=True
                ),
                fac.AntdTitle(
                    '3 用Dash开发交互应用',
                    id='3 用Dash开发交互应用',
                    level=2
                ),
                fmc.FefferyMarkdown(
                     codeTheme='a11y-dark',
                    markdownStr=open('./documents/3 用Dash开发交互应用.md', encoding='utf-8').read(),
                    renderHtml=True
                ),
                html.Div(
                    fac.AntdImage(
                        src=app.get_asset_url('imgs/玩转dash星球二维码.jpg'),
                        style={
                            'height': '400px',
                            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                            'borderRadius': '5px'
                        }
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center'
                    }
                )
            ],
            style={
                'flex': 'auto',
                'marginBottom': '200px'
            }
        ),

        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '1 Dash+fac开发环境的准备', 'href': '#1 Dash+fac开发环境的准备'},
                    {'title': '2 用Dash开发静态页面', 'href': '#2 用Dash开发静态页面'},
                    {'title': '3 用Dash开发交互应用', 'href': '#3 用Dash开发交互应用'},
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'margin': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
