import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdInput(name=f'表单项{i}'), label=f'表单项{i}'
                    )
                    for i in range(1, 6)
                ],
                id='callback-listen-value-form-demo',
                enableBatchControl=True,
                layout='vertical',
                values={
                    f'表单项{i}': f'这是表单项{i}的设定值' for i in range(1, 6)
                },
            ),
            html.Pre(id='callback-listen-value-form-demo-output'),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('callback-listen-value-form-demo-output', 'children'),
    Input('callback-listen-value-form-demo', 'values'),
)
def callback_listen_value_demo(values):
    return json.dumps(values, ensure_ascii=False, indent=4)


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInput(name=f'表单项{i}'), label=f'表单项{i}'
                )
                for i in range(1, 6)
            ],
            id='callback-listen-value-form-demo',
            enableBatchControl=True,
            layout='vertical',
            values={
                f'表单项{i}': f'这是表单项{i}的设定值' for i in range(1, 6)
            },
        ),
        html.Pre(id='callback-listen-value-form-demo-output'),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('callback-listen-value-form-demo-output', 'children'),
    Input('callback-listen-value-form-demo', 'values'),
)
def callback_listen_value_demo(values):
    return json.dumps(values, ensure_ascii=False, indent=4)
"""
    }
]
