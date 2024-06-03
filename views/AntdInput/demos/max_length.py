import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                mode=mode,
                maxLength=10,
                showCount=True if mode == 'text-area' else False,
                placeholder='请输入'
                if mode != 'text-area'
                else '请输入字符并注意下方计数',
                style={'width': 350},
            )
            for mode in [
                'default',
                'search',
                'password',
                'text-area',
            ]
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(
            mode=mode,
            maxLength=10,
            showCount=True if mode == 'text-area' else False,
            placeholder='请输入',
            style={'width': 350},
        )
        for mode in [
            'default',
            'search',
            'password',
            'text-area',
        ]
    ],
    direction='vertical',
)
"""
    }
]
