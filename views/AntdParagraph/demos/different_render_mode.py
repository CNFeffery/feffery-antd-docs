import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component


paragraph_demo = '　　君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。'


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            fac.AntdDivider('默认模式', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo),
            fac.AntdDivider('code=True', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, code=True),
            fac.AntdDivider('copyable=True', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, copyable=True),
            fac.AntdDivider('strikethrough=True', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, strikethrough=True),
            fac.AntdDivider('disabled=True', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, disabled=True),
            fac.AntdDivider('mark=True', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, mark=True),
            fac.AntdDivider('strong=True', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, strong=True),
            fac.AntdDivider('italic=True', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, italic=True),
            fac.AntdDivider('underline=True', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, underline=True),
            fac.AntdDivider('type="secondary"', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, type='secondary'),
            fac.AntdDivider('type="success"', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, type='success'),
            fac.AntdDivider('type="warning"', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, type='warning'),
            fac.AntdDivider('type="danger"', innerTextOrientation='left'),
            fac.AntdParagraph(paragraph_demo, type='danger'),
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
paragraph_demo = '　　君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。'

...

html.Div(
    [
        fac.AntdDivider(
            '默认模式',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo
        ),
        fac.AntdDivider(
            'code=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            code=True
        ),
        fac.AntdDivider(
            'copyable=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            copyable=True
        ),
        fac.AntdDivider(
            'strikethrough=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            strikethrough=True
        ),
        fac.AntdDivider(
            'disabled=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            disabled=True
        ),
        fac.AntdDivider(
            'mark=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            mark=True
        ),
        fac.AntdDivider(
            'strong=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            strong=True
        ),
        fac.AntdDivider(
            'italic=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            italic=True
        ),
        fac.AntdDivider(
            'underline=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            underline=True
        ),
        fac.AntdDivider(
            'type="secondary"',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            type="secondary"
        ),
        fac.AntdDivider(
            'type="success"',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            type="success"
        ),
        fac.AntdDivider(
            'type="warning"',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            type="warning"
        ),
        fac.AntdDivider(
            'type="danger"',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            type="danger"
        )
    ]
)
"""
    }
]
