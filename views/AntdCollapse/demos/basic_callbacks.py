import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCollapse(
                fac.AntdParagraph('内容示例' * 20),
                id='collapse-demo',
                isOpen=True,
                title='回调示例',
                style={'width': 300},
            ),
            fac.AntdText(id='collapse-demo-output'),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('collapse-demo-output', 'children'), Input('collapse-demo', 'isOpen')
)
def collapse_demo(isOpen):
    return f'isOpen={isOpen}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdCollapse(
            fac.AntdParagraph('内容示例' * 20),
            id='collapse-demo',
            isOpen=True,
            title='回调示例',
            style={'width': 300},
        ),
        fac.AntdText(id='collapse-demo-output'),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('collapse-demo-output', 'children'), Input('collapse-demo', 'isOpen')
)
def collapse_demo(isOpen):
    return f'isOpen={isOpen}'
"""
    }
]
