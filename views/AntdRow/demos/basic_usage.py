import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRow(
        [
            fac.AntdCol(
                fac.AntdCenter(
                    f'col{i}',
                    style={
                        'backgroundColor': '#1677ff'
                        if i % 2 == 0
                        else '#1677ffbf',
                        'color': 'white',
                        'height': 100,
                    },
                ),
                span=6,
            )
            for i in range(1, 5)
        ],
        gutter=10,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdRow(
    [
        fac.AntdCol(
            fac.AntdCenter(
                f'col{i}',
                style={
                    'backgroundColor': '#1677ff'
                    if i % 2 == 0
                    else '#1677ffbf',
                    'color': 'white',
                    'height': 100,
                },
            ),
            span=6,
        )
        for i in range(1, 5)
    ],
    gutter=10,
)
"""
    }
]
