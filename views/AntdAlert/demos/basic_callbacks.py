import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdAlert(
        showIcon=True,
        message=fac.AntdSpace(
            [
                fac.AntdText('这是组件型message参数示例，'),
                fac.AntdButton(
                    '点我试试',
                    id='alert-message-button-input',
                    type='primary',
                    size='small',
                ),
            ],
            size=0,
        ),
        description=fac.AntdText(
            '这是组件型description参数示例，上面的按钮被点了0次',
            id='alert-description-output',
        ),
    )

    return demo_contents


@app.callback(
    Output('alert-description-output', 'children'),
    Input('alert-message-button-input', 'nClicks'),
    prevent_initial_call=True,
)
def alert_message_description_callback_demo(nClicks):
    return f'这是组件型description参数示例，上面的按钮被点了{nClicks}次'


code_string = [
    {
        'code': """
fac.AntdAlert(
    showIcon=True,
    message=fac.AntdSpace(
        [
            fac.AntdText('这是组件型message参数示例，'),
            fac.AntdButton(
                '点我试试',
                id='alert-message-button-input',
                type='primary',
                size='small',
            ),
        ],
        size=0,
    ),
    description=fac.AntdText(
        '这是组件型description参数示例，上面的按钮被点了0次',
        id='alert-description-output',
    ),
)

...

@app.callback(
    Output('alert-description-output', 'children'),
    Input('alert-message-button-input', 'nClicks'),
    prevent_initial_call=True,
)
def alert_message_description_callback_demo(nClicks):
    return f'这是组件型description参数示例，上面的按钮被点了{nClicks}次'
"""
    }
]
