import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdAlert(
                message='Warning text',
                type='warning',
                banner=True,
                showIcon=True,
            ),
            fac.AntdAlert(
                message='Very long warning text warning text text text text text text text',
                type='warning',
                banner=True,
                showIcon=True,
                closable=True,
            ),
            fac.AntdAlert(
                message='Warning text without icon',
                type='warning',
                banner=True,
                showIcon=False,
            ),
            fac.AntdAlert(
                message='Error text',
                type='error',
                banner=True,
                showIcon=True,
            ),
        ],
        direction='vertical',
        size='middle',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdAlert(
            message='Warning text',
            type='warning',
            banner=True,
            showIcon=True,
        ),
        fac.AntdAlert(
            message='Very long warning text warning text text text text text text text',
            type='warning',
            banner=True,
            showIcon=True,
            closable=True,
        ),
        fac.AntdAlert(
            message='Warning text without icon',
            type='warning',
            banner=True,
            showIcon=False,
        ),
        fac.AntdAlert(
            message='Error text',
            type='error',
            banner=True,
            showIcon=True,
        ),
    ],
    direction='vertical',
    size='middle',
    style={'width': '100%'},
)
"""
    }
]
