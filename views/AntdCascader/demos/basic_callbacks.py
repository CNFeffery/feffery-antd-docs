import feffery_antd_components as fac
import json
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider(
            'changeOnSelect=False（默认）', innerTextOrientation='left'
        ),
        fac.AntdSpace(
            [
                fac.AntdCascader(
                    id='cascader-demo1',
                    placeholder='请选择',
                    options=[
                        {
                            'value': '节点1',
                            'label': '节点1',
                            'children': [
                                {'value': '节点1-1', 'label': '节点1-1'},
                                {
                                    'value': '节点1-2',
                                    'label': '节点1-2',
                                    'children': [
                                        {
                                            'value': '节点1-2-1',
                                            'label': '节点1-2-1',
                                        },
                                        {
                                            'value': '节点1-2-2',
                                            'label': '节点1-2-2',
                                        },
                                    ],
                                },
                            ],
                        },
                        {
                            'value': '节点2',
                            'label': '节点2',
                            'children': [
                                {'value': '节点2-1', 'label': '节点2-1'},
                                {'value': '节点2-2', 'label': '节点2-2'},
                            ],
                        },
                    ],
                    style={'width': '200px'},
                ),
                fac.AntdText(id='cascader-demo1-output'),
            ]
        ),
        fac.AntdDivider('changeOnSelect=True', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                fac.AntdCascader(
                    id='cascader-demo2',
                    placeholder='请选择',
                    options=[
                        {
                            'value': '节点1',
                            'label': '节点1',
                            'children': [
                                {'value': '节点1-1', 'label': '节点1-1'},
                                {
                                    'value': '节点1-2',
                                    'label': '节点1-2',
                                    'children': [
                                        {
                                            'value': '节点1-2-1',
                                            'label': '节点1-2-1',
                                        },
                                        {
                                            'value': '节点1-2-2',
                                            'label': '节点1-2-2',
                                        },
                                    ],
                                },
                            ],
                        },
                        {
                            'value': '节点2',
                            'label': '节点2',
                            'children': [
                                {'value': '节点2-1', 'label': '节点2-1'},
                                {'value': '节点2-2', 'label': '节点2-2'},
                            ],
                        },
                    ],
                    changeOnSelect=True,
                    style={'width': '200px'},
                ),
                fac.AntdText(id='cascader-demo2-output'),
            ]
        ),
        fac.AntdDivider('多选模式', innerTextOrientation='left'),
        fac.AntdCascader(
            id='cascader-demo3',
            placeholder='请选择',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {'value': '节点1-1', 'label': '节点1-1'},
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {'value': '节点1-2-1', 'label': '节点1-2-1'},
                                {'value': '节点1-2-2', 'label': '节点1-2-2'},
                            ],
                        },
                    ],
                },
                {
                    'value': '节点2',
                    'label': '节点2',
                    'children': [
                        {'value': '节点2-1', 'label': '节点2-1'},
                        {'value': '节点2-2', 'label': '节点2-2'},
                    ],
                },
            ],
            multiple=True,
            placement='topLeft',
            style={'width': '200px'},
        ),
        html.Pre(id='cascader-demo3-output'),
    ]

    return demo_contents


@app.callback(
    Output('cascader-demo1-output', 'children'),
    Input('cascader-demo1', 'value'),
    prevent_initial_call=True,
)
def cascader_demo1(value):
    return str(value)


@app.callback(
    Output('cascader-demo2-output', 'children'),
    Input('cascader-demo2', 'value'),
    prevent_initial_call=True,
)
def cascader_demo2(value):
    return str(value)


@app.callback(
    Output('cascader-demo3-output', 'children'),
    Input('cascader-demo3', 'value'),
    prevent_initial_call=True,
)
def cascader_demo3(value):
    return json.dumps(value, indent=4, ensure_ascii=False)


code_string = [
    {
        'code': """
fac.AntdDivider(
    'changeOnSelect=False（默认）',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdCascader(
            id='cascader-demo1',
            placeholder='请选择',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                },
                {
                    'value': '节点2',
                    'label': '节点2',
                    'children': [
                        {
                            'value': '节点2-1',
                            'label': '节点2-1'
                        },
                        {
                            'value': '节点2-2',
                            'label': '节点2-2'
                        }
                    ]
                }
            ],
            style={
                'width': '200px'
            }
        ),
        fac.AntdText(id='cascader-demo1-output')
    ]
),

fac.AntdDivider(
    'changeOnSelect=True',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdCascader(
            id='cascader-demo2',
            placeholder='请选择',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                },
                {
                    'value': '节点2',
                    'label': '节点2',
                    'children': [
                        {
                            'value': '节点2-1',
                            'label': '节点2-1'
                        },
                        {
                            'value': '节点2-2',
                            'label': '节点2-2'
                        }
                    ]
                }
            ],
            changeOnSelect=True,
            style={
                'width': '200px'
            }
        ),
        fac.AntdText(id='cascader-demo2-output')
    ]
),

fac.AntdDivider(
    '多选模式',
    innerTextOrientation='left'
),
fac.AntdCascader(
    id='cascader-demo3',
    placeholder='请选择',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    multiple=True,
    placement='topLeft',
    style={
        'width': '200px'
    }
),
html.Pre(id='cascader-demo3-output')

...

@app.callback(
    Output('cascader-demo1-output', 'children'),
    Input('cascader-demo1', 'value'),
    prevent_initial_call=True
)
def cascader_demo1(value):

    return str(value)


@app.callback(
    Output('cascader-demo2-output', 'children'),
    Input('cascader-demo2', 'value'),
    prevent_initial_call=True
)
def cascader_demo2(value):

    return str(value)


@app.callback(
    Output('cascader-demo3-output', 'children'),
    Input('cascader-demo3', 'value'),
    prevent_initial_call=True
)
def cascader_demo3(value):

    return json.dumps(
        value,
        indent=4,
        ensure_ascii=False
    )
"""
    }
]
