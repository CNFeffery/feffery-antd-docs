import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyHexColorPicker(
                id='config-provider-primary-color', color='#1890ff'
            ),
            fac.AntdConfigProvider(
                fac.AntdButton('按钮示例', type='primary'),
                id='config-provider-primary-color-demo',
            ),
        ],
        direction='vertical',
    )

    return demo_contents


app.clientside_callback(
    '(color) => color',
    Output('config-provider-primary-color-demo', 'primaryColor'),
    Input('config-provider-primary-color', 'color'),
)

code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fuc.FefferyHexColorPicker(
            id='config-provider-primary-color', color='#1890ff'
        ),
        fac.AntdConfigProvider(
            fac.AntdButton('按钮示例', type='primary'),
            id='config-provider-primary-color-demo',
        ),
    ],
    direction='vertical',
)

...

app.clientside_callback(
    '(color) => color',
    Output('config-provider-primary-color-demo', 'primaryColor'),
    Input('config-provider-primary-color', 'color'),
)
"""
    }
]
