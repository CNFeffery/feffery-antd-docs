import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('连续型色带', innerTextOrientation='left'),
            fac.AntdSelect(
                defaultValue='色系1',
                options=[
                    {
                        'label': '色系1',
                        'value': '色系1',
                        'colors': ['#fff5f5', '#ff8787', '#c92a2a'],
                    },
                    {
                        'label': '色系2',
                        'value': '色系2',
                        'colors': ['#f8f0fc', '#da77f2', '#862e9c'],
                    },
                    {
                        'label': '色系3',
                        'value': '色系3',
                        'colors': ['#e7f5ff', '#4dabf7', '#1864ab'],
                    },
                ],
                colorsMode='sequential',
                style={'width': '100%'},
            ),
            fac.AntdDivider('离散型色带', innerTextOrientation='left'),
            fac.AntdSelect(
                defaultValue='色系1',
                options=[
                    {
                        'label': '色系1',
                        'value': '色系1',
                        'colors': ['#fff5f5', '#ff8787', '#c92a2a'],
                    },
                    {
                        'label': '色系2',
                        'value': '色系2',
                        'colors': ['#f8f0fc', '#da77f2', '#862e9c'],
                    },
                    {
                        'label': '色系3',
                        'value': '色系3',
                        'colors': ['#e7f5ff', '#4dabf7', '#1864ab'],
                    },
                ],
                colorsMode='diverging',
                style={'width': '100%'},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('连续型色带', innerTextOrientation='left'),
        fac.AntdSelect(
            defaultValue='色系1',
            options=[
                {
                    'label': '色系1',
                    'value': '色系1',
                    'colors': ['#fff5f5', '#ff8787', '#c92a2a'],
                },
                {
                    'label': '色系2',
                    'value': '色系2',
                    'colors': ['#f8f0fc', '#da77f2', '#862e9c'],
                },
                {
                    'label': '色系3',
                    'value': '色系3',
                    'colors': ['#e7f5ff', '#4dabf7', '#1864ab'],
                },
            ],
            colorsMode='sequential',
            style={'width': '100%'},
        ),
        fac.AntdDivider('离散型色带', innerTextOrientation='left'),
        fac.AntdSelect(
            defaultValue='色系1',
            options=[
                {
                    'label': '色系1',
                    'value': '色系1',
                    'colors': ['#fff5f5', '#ff8787', '#c92a2a'],
                },
                {
                    'label': '色系2',
                    'value': '色系2',
                    'colors': ['#f8f0fc', '#da77f2', '#862e9c'],
                },
                {
                    'label': '色系3',
                    'value': '色系3',
                    'colors': ['#e7f5ff', '#4dabf7', '#1864ab'],
                },
            ],
            colorsMode='diverging',
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
    }
]
