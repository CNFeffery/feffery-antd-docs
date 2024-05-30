import feffery_antd_components as fac
import json
import dash
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

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
                                {'title': '单选子页面1', 'key': '单选子页面1'},
                                {'title': '单选子页面2', 'key': '单选子页面2'},
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
                                {'title': '多选子页面1', 'key': '多选子页面1'},
                                {'title': '多选子页面2', 'key': '多选子页面2'},
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
            direction='vertical'
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


code_string = [
    {
        'code': """
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
                        {'title': '单选子页面1', 'key': '单选子页面1'},
                        {'title': '单选子页面2', 'key': '单选子页面2'},
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
                        {'title': '多选子页面1', 'key': '多选子页面1'},
                        {'title': '多选子页面2', 'key': '多选子页面2'},
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
    direction='vertical'
),

html.Div(id='dropdown-demo-selectable-output')

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
