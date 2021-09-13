import dash_core_components as dcc
import dash_html_components as html
import feffery_antd_components as fac

paragraph_demo = '　　君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。'

docs_content = html.Div(
    [
        html.H2(
            'AntdParagraph(children, id, className, style, *args, **kwargs)',
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
                        {'title': '不同的渲染模式', 'href': '#不同的渲染模式'},
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

        dcc.Markdown(open('documents/AntdParagraph.md', encoding='utf-8').read(),
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
                html.Div(
                    [
                        fac.AntdDivider('默认模式', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo
                        ),
                        fac.AntdDivider('code=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            code=True
                        ),
                        fac.AntdDivider('copyable=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            copyable=True
                        ),
                        fac.AntdDivider('strikethrough=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            strikethrough=True
                        ),
                        fac.AntdDivider('disabled=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            disabled=True
                        ),
                        fac.AntdDivider('mark=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            mark=True
                        ),
                        fac.AntdDivider('strong=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            strong=True
                        ),
                        fac.AntdDivider('italic=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            italic=True
                        ),
                        fac.AntdDivider('underline=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            underline=True
                        ),
                        fac.AntdDivider('type="secondary"', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            type="secondary"
                        ),
                        fac.AntdDivider('type="success"', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            type="success"
                        ),
                        fac.AntdDivider('type="warning"', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            type="warning"
                        ),
                        fac.AntdDivider('type="danger"', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            type="danger"
                        )
                    ]
                ),

                fac.AntdDivider(
                    '不同的渲染模式',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdDivider('默认模式', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo
                        ),
                        fac.AntdDivider('code=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            code=True
                        ),
                        fac.AntdDivider('copyable=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            copyable=True
                        ),
                        fac.AntdDivider('strikethrough=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            strikethrough=True
                        ),
                        fac.AntdDivider('disabled=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            disabled=True
                        ),
                        fac.AntdDivider('mark=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            mark=True
                        ),
                        fac.AntdDivider('strong=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            strong=True
                        ),
                        fac.AntdDivider('italic=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            italic=True
                        ),
                        fac.AntdDivider('underline=True', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            underline=True
                        ),
                        fac.AntdDivider('type="secondary"', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            type="secondary"
                        ),
                        fac.AntdDivider('type="success"', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            type="success"
                        ),
                        fac.AntdDivider('type="warning"', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            type="warning"
                        ),
                        fac.AntdDivider('type="danger"', innerTextOrientation='left'),
                        fac.AntdParagraph(
                            paragraph_demo,
                            type="danger"
                        )
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
            id='不同的渲染模式',
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)
