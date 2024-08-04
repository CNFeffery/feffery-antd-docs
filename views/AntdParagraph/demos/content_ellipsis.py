import feffery_antd_components as fac
from dash.dependencies import Component


paragraph_demo = '　　君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。'


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = (
        fac.AntdSpace(
            [
                fac.AntdParagraph(paragraph_demo, ellipsis=True),
                fac.AntdParagraph(
                    paragraph_demo, ellipsis={'expandable': True}
                ),
                fac.AntdParagraph(
                    paragraph_demo, ellipsis={'expandable': True, 'rows': 3}
                ),
                fac.AntdParagraph(paragraph_demo, ellipsis={'suffix': '👉'}),
                fac.AntdParagraph(
                    paragraph_demo,
                    ellipsis={
                        'expandable': True,
                        'rows': 3,
                        'symbol': fac.AntdText('点我展开', type='secondary'),
                    },
                ),
                fac.AntdParagraph(
                    paragraph_demo,
                    ellipsis={
                        'expandable': 'collapsible',
                        'rows': 3
                    },
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        ),
    )

    return demo_contents


code_string = [
    {
        'code': """
paragraph_demo = '　　君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。'

...

fac.AntdSpace(
    [
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis=True
        ),
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis={
                'expandable': True
            }
        ),
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis={
                'expandable': True,
                'rows': 3
            }
        ),
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis={
                'suffix': '👉'
            }
        ),
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis={
                'expandable': True,
                'rows': 3,
                'symbol': fac.AntdText(
                    '点我展开',
                    type='secondary'
                )
            }
        ),
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis={
                'expandable': 'collapsible',
                'rows': 3
            },
        ),
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)
"""
    }
]
