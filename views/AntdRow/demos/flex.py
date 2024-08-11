import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRow(
        [
            fac.AntdCol(
                fac.AntdCenter(
                    f'{flex} / 7',
                    style={
                        'backgroundColor': '#1677ff',
                        'color': 'white',
                        'height': 100,
                    },
                ),
                flex=flex,
            )
            for i, flex in enumerate(['1', '2', '4'])
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
                f'{flex} / 7',
                style={
                    'backgroundColor': '#1677ff',
                    'color': 'white',
                    'height': 100,
                },
            ),
            flex=flex,
        )
        for i, flex in enumerate(['1', '2', '4'])
    ],
    gutter=10,
)
"""
    }
]
