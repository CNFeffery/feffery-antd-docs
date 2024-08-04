import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTabs(
            id='tabs-demo',
            items=[
                {'label': f'标签页{i}', 'key': f'标签页{i}'}
                for i in range(1, 6)
            ],
            defaultActiveKey='标签页3',
        ),
        fac.AntdText(id='tabs-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('tabs-demo-output', 'children'), Input('tabs-demo', 'activeKey')
)
def tabs_demo(activeKey):
    return f'activeKey: {activeKey}'


code_string = [
    {
        'code': """
[
    fac.AntdTabs(
        id='tabs-demo',
        items=[
            {'label': f'标签页{i}', 'key': f'标签页{i}'}
            for i in range(1, 6)
        ],
        defaultActiveKey='标签页3',
    ),
    fac.AntdText(id='tabs-demo-output'),
]

...

@app.callback(
    Output('tabs-demo-output', 'children'), Input('tabs-demo', 'activeKey')
)
def tabs_demo(activeKey):
    return f'activeKey: {activeKey}'
"""
    }
]
