import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdParagraph(
        [
            fac.AntdText('code示例', code=True),
            fac.AntdText('copyable示例', copyable=True),
            fac.AntdText('strikethrough示例', strikethrough=True),
            fac.AntdText('disabled示例', disabled=True),
            fac.AntdText('mark示例', mark=True),
            fac.AntdText('strong示例', strong=True),
            fac.AntdText('underline示例', underline=True),
            fac.AntdText('keyboard示例', keyboard=True),
            fac.AntdText('secondary示例', type='secondary'),
            fac.AntdText('success示例', type='success'),
            fac.AntdText('warning示例', type='warning'),
            fac.AntdText('danger示例', type='danger'),
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdParagraph(
    [
        fac.AntdText('code示例', code=True),
        fac.AntdText('copyable示例', copyable=True),
        fac.AntdText('strikethrough示例', strikethrough=True),
        fac.AntdText('disabled示例', disabled=True),
        fac.AntdText('mark示例', mark=True),
        fac.AntdText('strong示例', strong=True),
        fac.AntdText('underline示例', underline=True),
        fac.AntdText('keyboard示例', keyboard=True),
        fac.AntdText('secondary示例', type='secondary'),
        fac.AntdText('success示例', type='success'),
        fac.AntdText('warning示例', type='warning'),
        fac.AntdText('danger示例', type='danger'),
    ]
)
"""
    }
]
