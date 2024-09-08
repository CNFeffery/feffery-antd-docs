import json
import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdSpace(
                [
                    fac.AntdSpace(
                        [
                            fac.AntdText('是否开启选择结果排除指定菜单项：'),
                            fac.AntdSwitch(
                                id='dropdown-demo-selectable-switch',
                                checked=False,
                            ),
                        ]
                    ),
                    fac.AntdSpace(
                        [
                            fac.AntdDropdown(
                                id='dropdown-demo-selectable-single',
                                title='单选',
                                menuItems=[
                                    {
                                        'title': '单选子页面1',
                                        'key': '单选子页面1',
                                    },
                                    {
                                        'title': '单选子页面2',
                                        'key': '单选子页面2',
                                    },
                                    {'isDivider': True},
                                    {
                                        'title': '单选子页面3-1',
                                        'key': '单选子页面3-1',
                                    },
                                    {
                                        'title': '单选子页面3-2',
                                        'key': '单选子页面3-2',
                                    },
                                ],
                                selectable=True,
                            ),
                            fac.AntdDropdown(
                                id='dropdown-demo-selectable-multiple',
                                title='多选',
                                menuItems=[
                                    {
                                        'title': '多选子页面1',
                                        'key': '多选子页面1',
                                    },
                                    {
                                        'title': '多选子页面2',
                                        'key': '多选子页面2',
                                    },
                                    {'isDivider': True},
                                    {
                                        'title': '多选子页面3-1',
                                        'key': '多选子页面3-1',
                                    },
                                    {
                                        'title': '多选子页面3-2',
                                        'key': '多选子页面3-2',
                                    },
                                ],
                                selectable=True,
                                multiple=True,
                            ),
                        ],
                        size=20,
                    ),
                ],
                direction='vertical',
            ),
            html.Div(id='dropdown-demo-selectable-output'),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdSpace(
                [
                    fac.AntdSpace(
                        [
                            fac.AntdText(
                                'Whether to exclude the specified menu item when selecting results:'
                            ),
                            fac.AntdSwitch(
                                id='dropdown-demo-selectable-switch',
                                checked=False,
                            ),
                        ]
                    ),
                    fac.AntdSpace(
                        [
                            fac.AntdDropdown(
                                id='dropdown-demo-selectable-single',
                                title='Single',
                                menuItems=[
                                    {
                                        'title': 'Single page 1',
                                        'key': 'Single page 1',
                                    },
                                    {
                                        'title': 'Single page 2',
                                        'key': 'Single page 2',
                                    },
                                    {'isDivider': True},
                                    {
                                        'title': 'Single page 3-1',
                                        'key': 'Single page 3-1',
                                    },
                                    {
                                        'title': 'Single page 3-2',
                                        'key': 'Single page 3-2',
                                    },
                                ],
                                selectable=True,
                            ),
                            fac.AntdDropdown(
                                id='dropdown-demo-selectable-multiple',
                                title='Multiple',
                                menuItems=[
                                    {
                                        'title': 'Multiple page 1',
                                        'key': 'Multiple page 1',
                                    },
                                    {
                                        'title': 'Multiple page 2',
                                        'key': 'Multiple page 2',
                                    },
                                    {'isDivider': True},
                                    {
                                        'title': 'Multiple page 3-1',
                                        'key': 'Multiple page 3-1',
                                    },
                                    {
                                        'title': 'Multiple page 3-2',
                                        'key': 'Multiple page 3-2',
                                    },
                                ],
                                selectable=True,
                                multiple=True,
                            ),
                        ],
                        size=20,
                    ),
                ],
                direction='vertical',
            ),
            html.Div(id='dropdown-demo-selectable-output'),
        ]

    return demo_contents


@app.callback(
    [
        Output('dropdown-demo-selectable-single', 'nonSelectableKeys'),
        Output('dropdown-demo-selectable-multiple', 'nonSelectableKeys'),
    ],
    Input('dropdown-demo-selectable-switch', 'checked'),
)
def swtich_select_mode(checked):
    if checked:
        current_locale = get_current_locale()
        if current_locale == 'zh-cn':
            return [['单选子页面1'], ['多选子页面1']]
        elif current_locale == 'en-us':
            return [['Single page 1'], ['Multiple page 1']]
    return [[], []]


@app.callback(
    Output('dropdown-demo-selectable-output', 'children'),
    [
        Input('dropdown-demo-selectable-single', 'selectedKeys'),
        Input('dropdown-demo-selectable-multiple', 'selectedKeys'),
    ],
    prevent_initial_call=True,
)
def selectable_demo(single_selectedKeys, multiple_selectedKeys):
    trigger_id = dash.ctx.triggered_id
    if trigger_id == 'dropdown-demo-selectable-single':
        return json.dumps(
            dict(selectedKeys=single_selectedKeys), indent=4, ensure_ascii=False
        )
    elif trigger_id == 'dropdown-demo-selectable-multiple':
        return json.dumps(
            dict(selectedKeys=multiple_selectedKeys),
            indent=4,
            ensure_ascii=False,
        )
    return dash.no_update


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdText('是否开启选择结果排除指定菜单项：'),
                    fac.AntdSwitch(
                        id='dropdown-demo-selectable-switch',
                        checked=False,
                    ),
                ]
            ),
            fac.AntdSpace(
                [
                    fac.AntdDropdown(
                        id='dropdown-demo-selectable-single',
                        title='单选',
                        menuItems=[
                            {
                                'title': '单选子页面1',
                                'key': '单选子页面1',
                            },
                            {
                                'title': '单选子页面2',
                                'key': '单选子页面2',
                            },
                            {'isDivider': True},
                            {
                                'title': '单选子页面3-1',
                                'key': '单选子页面3-1',
                            },
                            {
                                'title': '单选子页面3-2',
                                'key': '单选子页面3-2',
                            },
                        ],
                        selectable=True,
                    ),
                    fac.AntdDropdown(
                        id='dropdown-demo-selectable-multiple',
                        title='多选',
                        menuItems=[
                            {
                                'title': '多选子页面1',
                                'key': '多选子页面1',
                            },
                            {
                                'title': '多选子页面2',
                                'key': '多选子页面2',
                            },
                            {'isDivider': True},
                            {
                                'title': '多选子页面3-1',
                                'key': '多选子页面3-1',
                            },
                            {
                                'title': '多选子页面3-2',
                                'key': '多选子页面3-2',
                            },
                        ],
                        selectable=True,
                        multiple=True,
                    ),
                ],
                size=20,
            ),
        ],
        direction='vertical',
    ),
    html.Div(id='dropdown-demo-selectable-output'),
]

...

@app.callback(
    [
        Output('dropdown-demo-selectable-single', 'nonSelectableKeys'),
        Output('dropdown-demo-selectable-multiple', 'nonSelectableKeys'),
    ],
    Input('dropdown-demo-selectable-switch', 'checked'),
)
def swtich_select_mode(checked):
    if checked:
        return [['单选子页面1'], ['多选子页面1']]
    return [[], []]


@app.callback(
    Output('dropdown-demo-selectable-output', 'children'),
    [
        Input('dropdown-demo-selectable-single', 'selectedKeys'),
        Input('dropdown-demo-selectable-multiple', 'selectedKeys'),
    ],
    prevent_initial_call=True,
)
def selectable_demo(single_selectedKeys, multiple_selectedKeys):
    trigger_id = dash.ctx.triggered_id
    if trigger_id == 'dropdown-demo-selectable-single':
        return json.dumps(
            dict(selectedKeys=single_selectedKeys), indent=4, ensure_ascii=False
        )
    elif trigger_id == 'dropdown-demo-selectable-multiple':
        return json.dumps(
            dict(selectedKeys=multiple_selectedKeys),
            indent=4,
            ensure_ascii=False,
        )
    return dash.no_update
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdText(
                        'Whether to exclude the specified menu item when selecting results:'
                    ),
                    fac.AntdSwitch(
                        id='dropdown-demo-selectable-switch',
                        checked=False,
                    ),
                ]
            ),
            fac.AntdSpace(
                [
                    fac.AntdDropdown(
                        id='dropdown-demo-selectable-single',
                        title='Single',
                        menuItems=[
                            {
                                'title': 'Single page 1',
                                'key': 'Single page 1',
                            },
                            {
                                'title': 'Single page 2',
                                'key': 'Single page 2',
                            },
                            {'isDivider': True},
                            {
                                'title': 'Single page 3-1',
                                'key': 'Single page 3-1',
                            },
                            {
                                'title': 'Single page 3-2',
                                'key': 'Single page 3-2',
                            },
                        ],
                        selectable=True,
                    ),
                    fac.AntdDropdown(
                        id='dropdown-demo-selectable-multiple',
                        title='Multiple',
                        menuItems=[
                            {
                                'title': 'Multiple page 1',
                                'key': 'Multiple page 1',
                            },
                            {
                                'title': 'Multiple page 2',
                                'key': 'Multiple page 2',
                            },
                            {'isDivider': True},
                            {
                                'title': 'Multiple page 3-1',
                                'key': 'Multiple page 3-1',
                            },
                            {
                                'title': 'Multiple page 3-2',
                                'key': 'Multiple page 3-2',
                            },
                        ],
                        selectable=True,
                        multiple=True,
                    ),
                ],
                size=20,
            ),
        ],
        direction='vertical',
    ),
    html.Div(id='dropdown-demo-selectable-output'),
]

...

@app.callback(
    [
        Output('dropdown-demo-selectable-single', 'nonSelectableKeys'),
        Output('dropdown-demo-selectable-multiple', 'nonSelectableKeys'),
    ],
    Input('dropdown-demo-selectable-switch', 'checked'),
)
def swtich_select_mode(checked):
    if checked:
        return [['Single page 1'], ['Multiple page 1']]
    return [[], []]


@app.callback(
    Output('dropdown-demo-selectable-output', 'children'),
    [
        Input('dropdown-demo-selectable-single', 'selectedKeys'),
        Input('dropdown-demo-selectable-multiple', 'selectedKeys'),
    ],
    prevent_initial_call=True,
)
def selectable_demo(single_selectedKeys, multiple_selectedKeys):
    trigger_id = dash.ctx.triggered_id
    if trigger_id == 'dropdown-demo-selectable-single':
        return json.dumps(
            dict(selectedKeys=single_selectedKeys), indent=4, ensure_ascii=False
        )
    elif trigger_id == 'dropdown-demo-selectable-multiple':
        return json.dumps(
            dict(selectedKeys=multiple_selectedKeys),
            indent=4,
            ensure_ascii=False,
        )
    return dash.no_update
"""
            }
        ]
