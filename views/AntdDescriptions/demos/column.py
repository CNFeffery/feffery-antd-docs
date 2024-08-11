from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('column=2', innerTextOrientation='left'),
        fac.AntdDescriptions(
            [
                fac.AntdDescriptionItem('费弗里', label='姓名'),
                fac.AntdDescriptionItem(
                    html.A(
                        'https://github.com/CNFeffery',
                        href='https://github.com/CNFeffery',
                    ),
                    label='个人Github地址',
                ),
                fac.AntdDescriptionItem(
                    html.A(
                        'https://www.cnblogs.com/feffery/',
                        href='https://www.cnblogs.com/feffery/',
                    ),
                    label='个人博客地址',
                ),
                fac.AntdDescriptionItem(
                    html.A(
                        'http://fac.feffery.tech/',
                        href='http://fac.feffery.tech/',
                    ),
                    label='fac框架官网',
                ),
            ],
            title='描述列表示例',
            bordered=True,
            column=2,
            labelStyle={'fontWeight': 'bold'},
        ),
        fac.AntdDivider('column=4', innerTextOrientation='left'),
        fac.AntdDescriptions(
            [
                fac.AntdDescriptionItem('费弗里', label='姓名'),
                fac.AntdDescriptionItem(
                    html.A(
                        'https://github.com/CNFeffery',
                        href='https://github.com/CNFeffery',
                    ),
                    label='个人Github地址',
                ),
                fac.AntdDescriptionItem(
                    html.A(
                        'https://www.cnblogs.com/feffery/',
                        href='https://www.cnblogs.com/feffery/',
                    ),
                    label='个人博客地址',
                ),
                fac.AntdDescriptionItem(
                    html.A(
                        'http://fac.feffery.tech/',
                        href='http://fac.feffery.tech/',
                    ),
                    label='fac框架官网',
                ),
            ],
            title='描述列表示例',
            bordered=True,
            column=4,
            labelStyle={'fontWeight': 'bold'},
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider('column=2', innerTextOrientation='left'),
    fac.AntdDescriptions(
        [
            fac.AntdDescriptionItem('费弗里', label='姓名'),
            fac.AntdDescriptionItem(
                html.A(
                    'https://github.com/CNFeffery',
                    href='https://github.com/CNFeffery',
                ),
                label='个人Github地址',
            ),
            fac.AntdDescriptionItem(
                html.A(
                    'https://www.cnblogs.com/feffery/',
                    href='https://www.cnblogs.com/feffery/',
                ),
                label='个人博客地址',
            ),
            fac.AntdDescriptionItem(
                html.A(
                    'http://fac.feffery.tech/',
                    href='http://fac.feffery.tech/',
                ),
                label='fac框架官网',
            ),
        ],
        title='描述列表示例',
        bordered=True,
        column=2,
        labelStyle={'fontWeight': 'bold'},
    ),
    fac.AntdDivider('column=4', innerTextOrientation='left'),
    fac.AntdDescriptions(
        [
            fac.AntdDescriptionItem('费弗里', label='姓名'),
            fac.AntdDescriptionItem(
                html.A(
                    'https://github.com/CNFeffery',
                    href='https://github.com/CNFeffery',
                ),
                label='个人Github地址',
            ),
            fac.AntdDescriptionItem(
                html.A(
                    'https://www.cnblogs.com/feffery/',
                    href='https://www.cnblogs.com/feffery/',
                ),
                label='个人博客地址',
            ),
            fac.AntdDescriptionItem(
                html.A(
                    'http://fac.feffery.tech/',
                    href='http://fac.feffery.tech/',
                ),
                label='fac框架官网',
            ),
        ],
        title='描述列表示例',
        bordered=True,
        column=4,
        labelStyle={'fontWeight': 'bold'},
    ),
]
"""
    }
]
