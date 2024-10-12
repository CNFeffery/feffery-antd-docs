import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSplitter(
                items=[
                    {
                        'children': fac.AntdCenter(
                            f'item{i}', style={'height': '100%'}
                        ),
                        'collapsible': True,
                    }
                    for i in range(1, 3)
                ],
                style={
                    'height': 200,
                    'boxShadow': '0 0 10px rgba(0, 0, 0, 0.1)',
                },
            ),
            fac.AntdSplitter(
                items=[
                    {
                        'children': fac.AntdCenter(
                            f'item{i}', style={'height': '100%'}
                        ),
                        'collapsible': True,
                    }
                    for i in range(1, 3)
                ],
                layout='vertical',
                style={
                    'height': 300,
                    'boxShadow': '0 0 10px rgba(0, 0, 0, 0.1)',
                },
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fac.AntdSplitter(
            items=[
                {
                    'children': fac.AntdCenter(
                        f'item{i}', style={'height': '100%'}
                    ),
                    'collapsible': True,
                }
                for i in range(1, 3)
            ],
            style={
                'height': 200,
                'boxShadow': '0 0 10px rgba(0, 0, 0, 0.1)',
            },
        ),
        fac.AntdSplitter(
            items=[
                {
                    'children': fac.AntdCenter(
                        f'item{i}', style={'height': '100%'}
                    ),
                    'collapsible': True,
                }
                for i in range(1, 3)
            ],
            layout='vertical',
            style={
                'height': 300,
                'boxShadow': '0 0 10px rgba(0, 0, 0, 0.1)',
            },
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
        }
    ]
