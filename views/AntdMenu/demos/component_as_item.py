from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdMenu(
        menuItems=[
            {
                'component': 'Item',
                'props': {
                    'title': '常规菜单项',
                    'key': '常规菜单项',
                },
            },
            {
                'component': 'Item',
                'props': {
                    'key': '带标签菜单项',
                },
            },
            {
                'component': 'Item',
                'props': {
                    'key': '带徽标菜单项',
                },
            },
            {
                'component': 'Item',
                'props': {
                    'key': '分离徽标菜单项',
                },
            },
            {
                'component': 'Item',
                'props': {
                    'key': '自定义图标',
                },
            },
            {
                'component': 'Item',
                'props': {
                    'key': '单独右对齐',
                },
            },
            {
                'component': 'Item',
                'props': {
                    'key': '单独居中',
                },
            },
        ],
        menuItemKeyToTitle={
            '带标签菜单项': fac.AntdSpace(
                ['带标签菜单项', fac.AntdTag(content='我是标签', color='green')]
            ),
            '带徽标菜单项': fac.AntdBadge(
                '带徽标菜单项', count=66, offset=[15, 0]
            ),
            '分离徽标菜单项': fac.AntdRow(
                [
                    fac.AntdCol('分离徽标菜单项'),
                    fac.AntdCol(fac.AntdBadge(count=8, color='#1a73e8')),
                ],
                justify='space-between',
            ),
            '自定义图标': fac.AntdSpace(
                [
                    *[
                        fac.AntdIcon(icon=icon)
                        for icon in [
                            'antd-build',
                            'antd-bug',
                            'antd-repair',
                            'antd-setting',
                        ]
                    ],
                    '自定义图标',
                ]
            ),
            '单独右对齐': html.Div('单独右对齐', style={'textAlign': 'end'}),
            '单独居中': html.Div('单独居中', style={'textAlign': 'center'}),
        },
        mode='inline',
        defaultSelectedKey='常规菜单项',
        style={'width': 220},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdMenu(
    menuItems=[
        {
            'component': 'Item',
            'props': {
                'title': '常规菜单项',
                'key': '常规菜单项',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': '带标签菜单项',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': '带徽标菜单项',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': '分离徽标菜单项',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': '自定义图标',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': '单独右对齐',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': '单独居中',
            },
        },
    ],
    menuItemKeyToTitle={
        '带标签菜单项': fac.AntdSpace(
            ['带标签菜单项', fac.AntdTag(content='我是标签', color='green')]
        ),
        '带徽标菜单项': fac.AntdBadge(
            '带徽标菜单项', count=66, offset=[15, 0]
        ),
        '分离徽标菜单项': fac.AntdRow(
            [
                fac.AntdCol('分离徽标菜单项'),
                fac.AntdCol(fac.AntdBadge(count=8, color='#1a73e8')),
            ],
            justify='space-between',
        ),
        '自定义图标': fac.AntdSpace(
            [
                *[
                    fac.AntdIcon(icon=icon)
                    for icon in [
                        'antd-build',
                        'antd-bug',
                        'antd-repair',
                        'antd-setting',
                    ]
                ],
                '自定义图标',
            ]
        ),
        '单独右对齐': html.Div('单独右对齐', style={'textAlign': 'end'}),
        '单独居中': html.Div('单独居中', style={'textAlign': 'center'}),
    },
    mode='inline',
    defaultSelectedKey='常规菜单项',
    style={'width': 220},
)
"""
    }
]
