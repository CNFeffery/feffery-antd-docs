import json
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
                        f'表单项{i}': f'这是表单项{i}的设定值'
                        for i in range(1, 6)
                    },
                ),
                html.Pre(id='callback-listen-value-form-demo-output'),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdForm(
                    [
                        fac.AntdFormItem(
                            fac.AntdInput(name=f'FormItem{i}'),
                            label=f'FormItem{i}',
                        )
                        for i in range(1, 6)
                    ],
                    id='callback-listen-value-form-demo',
                    enableBatchControl=True,
                    layout='vertical',
                    values={
                        f'FormItem{i}': f'This is the preset value for FormItem{i}'
                        for i in range(1, 6)
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInput(name=f'FormItem{i}'),
                    label=f'FormItem{i}',
                )
                for i in range(1, 6)
            ],
            id='callback-listen-value-form-demo',
            enableBatchControl=True,
            layout='vertical',
            values={
                f'FormItem{i}': f'This is the preset value for FormItem{i}'
                for i in range(1, 6)
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
