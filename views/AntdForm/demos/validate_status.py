import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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

    elif current_locale == 'en-us':
        # construct demo contents
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
                        label='Switch status',
                    ),
                    fac.AntdFormItem(
                        fac.AntdInput(),
                        id='form-item-status-demo',
                        label='Username',
                        hasFeedback=True,
                    ),
                ],
                labelCol={'span': 5},
                wrapperCol={'span': 19},
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
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
                label='Switch status',
            ),
            fac.AntdFormItem(
                fac.AntdInput(),
                id='form-item-status-demo',
                label='Username',
                hasFeedback=True,
            ),
        ],
        labelCol={'span': 5},
        wrapperCol={'span': 19},
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
