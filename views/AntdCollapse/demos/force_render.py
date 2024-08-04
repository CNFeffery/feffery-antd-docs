import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider(
            'forceRender=False（默认）', innerTextOrientation='left'
        ),
        fac.AntdSpace(
            [
                fac.AntdCollapse(
                    fac.AntdInput(
                        id='collapse-child-demo1',
                        defaultValue='内容测试',
                        style={'width': '100%'},
                    ),
                    isOpen=False,
                    style={'width': 300},
                ),
                fac.AntdText(id='collapse-child-demo1-output'),
            ]
        ),
        fac.AntdDivider('forceRender=True', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                fac.AntdCollapse(
                    fac.AntdInput(
                        id='collapse-child-demo2',
                        defaultValue='内容测试',
                        style={'width': '100%'},
                    ),
                    isOpen=False,
                    forceRender=True,
                    style={'width': 300},
                ),
                fac.AntdText(id='collapse-child-demo2-output'),
            ]
        ),
    ]

    return demo_contents


@app.callback(
    Output('collapse-child-demo1-output', 'children'),
    Input('collapse-child-demo1', 'value'),
)
def collapse_child_demo1(value):
    return value


@app.callback(
    Output('collapse-child-demo2-output', 'children'),
    Input('collapse-child-demo2', 'value'),
)
def collapse_child_demo2(value):
    return value


code_string = [
    {
        'code': """
[
    fac.AntdDivider(
        'forceRender=False（默认）', innerTextOrientation='left'
    ),
    fac.AntdSpace(
        [
            fac.AntdCollapse(
                fac.AntdInput(
                    id='collapse-child-demo1',
                    defaultValue='内容测试',
                    style={'width': '100%'},
                ),
                isOpen=False,
                style={'width': 300},
            ),
            fac.AntdText(id='collapse-child-demo1-output'),
        ]
    ),
    fac.AntdDivider('forceRender=True', innerTextOrientation='left'),
    fac.AntdSpace(
        [
            fac.AntdCollapse(
                fac.AntdInput(
                    id='collapse-child-demo2',
                    defaultValue='内容测试',
                    style={'width': '100%'},
                ),
                isOpen=False,
                forceRender=True,
                style={'width': 300},
            ),
            fac.AntdText(id='collapse-child-demo2-output'),
        ]
    ),
]

...

@app.callback(
    Output('collapse-child-demo1-output', 'children'),
    Input('collapse-child-demo1', 'value'),
)
def collapse_child_demo1(value):
    return value


@app.callback(
    Output('collapse-child-demo2-output', 'children'),
    Input('collapse-child-demo2', 'value'),
)
def collapse_child_demo2(value):
    return value
"""
    }
]
