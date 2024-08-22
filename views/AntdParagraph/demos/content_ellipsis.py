import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale

paragraph_demo = '　　君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。'
paragraph_demo_en_us = """To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause—there's the respect
That makes calamity of so long life.
"""


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdSpace(
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
                    ellipsis={'expandable': 'collapsible', 'rows': 3},
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdParagraph(
                    paragraph_demo_en_us, ellipsis=True, locale='en-us'
                ),
                fac.AntdParagraph(
                    paragraph_demo_en_us,
                    ellipsis={'expandable': True},
                    locale='en-us',
                ),
                fac.AntdParagraph(
                    paragraph_demo_en_us,
                    ellipsis={'expandable': True, 'rows': 3},
                    locale='en-us',
                ),
                fac.AntdParagraph(
                    paragraph_demo_en_us,
                    ellipsis={'suffix': '👉'},
                    locale='en-us',
                ),
                fac.AntdParagraph(
                    paragraph_demo_en_us,
                    ellipsis={
                        'expandable': True,
                        'rows': 3,
                        'symbol': fac.AntdText('点我展开', type='secondary'),
                    },
                    locale='en-us',
                ),
                fac.AntdParagraph(
                    paragraph_demo_en_us,
                    ellipsis={'expandable': 'collapsible', 'rows': 3},
                    locale='en-us',
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
paragraph_demo = '　　君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。'

...

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
            ellipsis={'expandable': 'collapsible', 'rows': 3},
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': '''
paragraph_demo_en_us = """To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause—there's the respect
That makes calamity of so long life.
"""
...

fac.AntdSpace(
    [
        fac.AntdParagraph(
            paragraph_demo_en_us, ellipsis=True, locale='en-us'
        ),
        fac.AntdParagraph(
            paragraph_demo_en_us,
            ellipsis={'expandable': True},
            locale='en-us',
        ),
        fac.AntdParagraph(
            paragraph_demo_en_us,
            ellipsis={'expandable': True, 'rows': 3},
            locale='en-us',
        ),
        fac.AntdParagraph(
            paragraph_demo_en_us,
            ellipsis={'suffix': '👉'},
            locale='en-us',
        ),
        fac.AntdParagraph(
            paragraph_demo_en_us,
            ellipsis={
                'expandable': True,
                'rows': 3,
                'symbol': fac.AntdText('点我展开', type='secondary'),
            },
            locale='en-us',
        ),
        fac.AntdParagraph(
            paragraph_demo_en_us,
            ellipsis={'expandable': 'collapsible', 'rows': 3},
            locale='en-us',
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
'''
            }
        ]
