import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTransfer(
            id='transfer-demo',
            dataSource=[{'key': i, 'title': f'选项{i}'} for i in range(1, 10)],
            targetKeys=[2, 3, 4],
        ),
        fac.AntdSpace(id='transfer-demo-output', direction='vertical'),
    ]

    return demo_contents


@app.callback(
    Output('transfer-demo-output', 'children'),
    [
        Input('transfer-demo', 'targetKeys'),
        Input('transfer-demo', 'moveDirection'),
        Input('transfer-demo', 'moveKeys'),
    ],
)
def transfer_demo(targetKeys, moveDirection, moveKeys):
    return [
        fac.AntdText(f'targetKeys: {targetKeys}'),
        fac.AntdText(f'moveDirection: {moveDirection}'),
        fac.AntdText(f'moveKeys: {moveKeys}'),
    ]


code_string = [
    {
        'code': """
[
    fac.AntdTransfer(
        id='transfer-demo',
        dataSource=[{'key': i, 'title': f'选项{i}'} for i in range(1, 10)],
        targetKeys=[2, 3, 4],
    ),
    fac.AntdSpace(id='transfer-demo-output', direction='vertical'),
]

...

@app.callback(
    Output('transfer-demo-output', 'children'),
    [Input('transfer-demo', 'targetKeys'),
     Input('transfer-demo', 'moveDirection'),
     Input('transfer-demo', 'moveKeys')]
)
def transfer_demo(targetKeys, moveDirection, moveKeys):

    return [
        fac.AntdText(f'targetKeys: {targetKeys}'),
        fac.AntdText(f'moveDirection: {moveDirection}'),
        fac.AntdText(f'moveKeys: {moveKeys}')
    ]
"""
    }
]
