import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTag(
                content='Loading...',
                icon=fac.AntdIcon(icon='antd-loading'),
                color='#0086ff',
            ),
            fac.AntdTag(
                content='Warning!',
                icon=fac.AntdIcon(
                    icon='fc-high-priority',
                    style={'position': 'relative', 'top': 1},
                ),
                color='red',
            ),
            fac.AntdTag(
                content='Stars',
                icon=fac.AntdIcon(icon='antd-github'),
                style={
                    'fontSize': '14px',
                    'fontWeight': 'bold',
                    'background': 'linear-gradient(to bottom, #fcfcfc, #e4e4e4)',
                },
            ),
        ],
        wrap=True,
        style={
            'width': '100%',
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdTag(
            content='Loading...',
            icon=fac.AntdIcon(icon='antd-loading'),
            color='#0086ff',
        ),
        fac.AntdTag(
            content='Warning!',
            icon=fac.AntdIcon(
                icon='fc-high-priority',
                style={'position': 'relative', 'top': 1},
            ),
            color='red',
        ),
        fac.AntdTag(
            content='Stars',
            icon=fac.AntdIcon(icon='antd-github'),
            style={
                'fontSize': '14px',
                'fontWeight': 'bold',
                'background': 'linear-gradient(to bottom, #fcfcfc, #e4e4e4)',
            },
        ),
    ],
    wrap=True,
    style={
        'width': '100%',
    },
)
"""
    }
]
