import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdRadioGroup(
                        id='form-item-status-switch',
                        options=[
                            {'label': 'None', 'value': 'None'},
                            {
                                'label': 'success',
                                'value': 'success',
                            },
                            {
                                'label': 'warning',
                                'value': 'warning',
                            },
                            {
                                'label': 'error',
                                'value': 'error',
                            },
                            {
                                'label': 'validating',
                                'value': 'validating',
                            },
                        ],
                        optionType='button',
                        defaultValue='None',
                    ),
                    label='切换状态',
                ),
                fac.AntdFormItem(
                    fac.AntdInput(),
                    id='form-item-status-demo',
                    label='用户名',
                    hasFeedback=True,
                ),
            ],
            labelCol={'span': 4},
            wrapperCol={'span': 20},
            style={'width': 500},
        )
    )

    return demo_contents


@app.callback(
    [
        Output('form-item-status-demo', 'validateStatus'),
        Output('form-item-status-demo', 'help'),
    ],
    Input('form-item-status-switch', 'value'),
)
def form_item_status_demo(value):
    if not value or value == 'None':
        return None, None

    return value, f'validateStatus="{value}"'


code_string = [
    {
        'code': """
fac.AntdCenter(
    fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdRadioGroup(
                    id='form-item-status-switch',
                    options=[
                        {'label': 'None', 'value': 'None'},
                        {
                            'label': 'success',
                            'value': 'success',
                        },
                        {
                            'label': 'warning',
                            'value': 'warning',
                        },
                        {
                            'label': 'error',
                            'value': 'error',
                        },
                        {
                            'label': 'validating',
                            'value': 'validating',
                        },
                    ],
                    optionType='button',
                    defaultValue='None',
                ),
                label='切换状态',
            ),
            fac.AntdFormItem(
                fac.AntdInput(),
                id='form-item-status-demo',
                label='用户名',
                hasFeedback=True,
            ),
        ],
        labelCol={'span': 4},
        wrapperCol={'span': 20},
        style={'width': 500},
    )
)

...

@app.callback(
    [
        Output('form-item-status-demo', 'validateStatus'),
        Output('form-item-status-demo', 'help'),
    ],
    Input('form-item-status-switch', 'value'),
)
def form_item_status_demo(value):
    if not value or value == 'None':
        return None, None

    return value, f'validateStatus="{value}"'
"""
    }
]
