import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdAlert(message='Demo Text', showIcon=True, icon='😎'),
            fac.AntdAlert(
                message='Demo Text',
                showIcon=True,
                icon=fac.AntdIcon(icon='antd-user'),
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdAlert(message='Demo Text', showIcon=True, icon='😎'),
        fac.AntdAlert(
            message='Demo Text',
            showIcon=True,
            icon=fac.AntdIcon(icon='antd-user'),
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
