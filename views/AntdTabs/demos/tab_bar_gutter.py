import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSlider(
            id='tabs-gutter-demo-slider',
            min=20,
            max=60,
            step=5,
            defaultValue=20,
            tooltipVisible=False,
            marks={i * 5: f'{i * 5}px' for i in range(1, 13)},
        ),
        fac.AntdTabs(
            id='tabs-gutter-demo',
            items=[
                {'key': f'标签页{i}', 'label': f'标签页{i}'}
                for i in range(1, 6)
            ],
        ),
    ]

    return demo_contents


app.clientside_callback(
    """(value) => value""",
    Output('tabs-gutter-demo', 'tabBarGutter'),
    Input('tabs-gutter-demo-slider', 'value'),
)

code_string = [
    {
        'code': '''
[
    fac.AntdSlider(
        id='tabs-gutter-demo-slider',
        min=20,
        max=60,
        step=5,
        defaultValue=20,
        tooltipVisible=False,
        marks={i * 5: f'{i*5}px' for i in range(1, 13)},
    ),
    fac.AntdTabs(
        id='tabs-gutter-demo',
        items=[
            {'key': f'标签页{i}', 'label': f'标签页{i}'}
            for i in range(1, 6)
        ],
    ),
]

...

app.clientside_callback(
    """(value) => value""",
    Output('tabs-gutter-demo', 'tabBarGutter'),
    Input('tabs-gutter-demo-slider', 'value'),
)
'''
    }
]
