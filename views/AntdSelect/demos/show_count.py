import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                mode='text-area',
                showCount=True,
                style={'width': 350},
            ),
            fac.AntdInput(
                mode='text-area',
                maxLength=10,
                showCount=True,
                placeholder='设置maxLength后，字符数将显示上限',
                style={'width': 350},
            ),
        ],
        direction='vertical',
        size='large',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(
            mode='text-area',
            showCount=True,
            style={'width': 350},
        ),
        fac.AntdInput(
            mode='text-area',
            maxLength=10,
            showCount=True,
            placeholder='设置maxLength后，字符数将显示上限',
            style={'width': 350},
        ),
    ],
    direction='vertical',
    size='large',
)
"""
    }
]
