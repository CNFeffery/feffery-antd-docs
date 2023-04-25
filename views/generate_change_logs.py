from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc


def genarate_layout(pathname):
    '''
    生成更新日志相关页面内容
    '''

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(
                        duration=0.3
                    ),

                    fac.AntdBreadcrumb(
                        items=[
                            {
                                'title': '更新日志'
                            },
                            {
                                'title': pathname.split('-')[-1]
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fmc.FefferyMarkdown(
                        markdownStr=open(
                            './change_logs/'+pathname[1:]+'.md', encoding='utf-8').read()
                    ),

                    html.Div(style={'height': '100px'})
                ],
                style={
                    'flex': 'auto',
                    'padding': '25px'
                }
            )
        ],
        style={
            'minHeight': 'calc(100vh - 300px)'
        }
    )
