from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDescriptions(
        items=[
            {'label': fac.AntdText('姓名'), 'children': '费弗里'},
            {
                'label': fac.AntdText('个人Github地址'),
                'children': html.A(
                    'https://github.com/CNFeffery',
                    href='https://github.com/CNFeffery',
                ),
            },
            {
                'label': fac.AntdText('个人博客地址'),
                'children': html.A(
                    'https://www.cnblogs.com/feffery/',
                    href='https://www.cnblogs.com/feffery/',
                ),
            },
            {
                'label': fac.AntdText('fac框架官网'),
                'children': html.A(
                    'http://fac.feffery.tech/', href='http://fac.feffery.tech/'
                ),
            },
        ],
        title='描述列表示例',
        styles={'label': {'fontWeight': 'bold'}},
        bordered=True,
        extra=fac.AntdButton(
            '额外内容',
            type='primary',
        ),
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDescriptions(
    items=[
        {'label': fac.AntdText('姓名'), 'children': '费弗里'},
        {
            'label': fac.AntdText('个人Github地址'),
            'children': html.A(
                'https://github.com/CNFeffery',
                href='https://github.com/CNFeffery',
            ),
        },
        {
            'label': fac.AntdText('个人博客地址'),
            'children': html.A(
                'https://www.cnblogs.com/feffery/',
                href='https://www.cnblogs.com/feffery/',
            ),
        },
        {
            'label': fac.AntdText('fac框架官网'),
            'children': html.A(
                'http://fac.feffery.tech/', href='http://fac.feffery.tech/'
            ),
        },
    ],
    title='描述列表示例',
    styles={'label': {'fontWeight': 'bold'}},
    bordered=True,
    extra=fac.AntdButton(
        '额外内容',
        type='primary',
    ),
)
"""
    }
]
