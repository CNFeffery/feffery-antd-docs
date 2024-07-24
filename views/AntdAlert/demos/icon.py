import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdAlert(
                message='Success Tips',
                type='success',
                showIcon=True,
            ),
            fac.AntdAlert(
                message='Informational Notes',
                type='info',
                showIcon=True,
            ),
            fac.AntdAlert(
                message='Warning', type='warning', showIcon=True, closable=True
            ),
            fac.AntdAlert(
                message='Error',
                type='error',
                showIcon=True,
            ),
            fac.AntdAlert(
                message='Success Tips',
                description='Detailed description and advice about successful copywriting.',
                type='success',
                showIcon=True,
            ),
            fac.AntdAlert(
                message='Informational Notes',
                description='Additional description and information about copywriting.',
                type='info',
                showIcon=True,
            ),
            fac.AntdAlert(
                message='Warning',
                description='This is a warning notice about copywriting.',
                type='warning',
                showIcon=True,
                closable=True,
            ),
            fac.AntdAlert(
                message='Error',
                description='This is an error message about copywriting.',
                type='error',
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
            message='Success Tips',
            type='success',
            showIcon=True,
        ),
        fac.AntdAlert(
            message='Informational Notes',
            type='info',
            showIcon=True,
        ),
        fac.AntdAlert(
            message='Warning', type='warning', showIcon=True, closable=True
        ),
        fac.AntdAlert(
            message='Error',
            type='error',
            showIcon=True,
        ),
        fac.AntdAlert(
            message='Success Tips',
            description='Detailed description and advice about successful copywriting.',
            type='success',
            showIcon=True,
        ),
        fac.AntdAlert(
            message='Informational Notes',
            description='Additional description and information about copywriting.',
            type='info',
            showIcon=True,
        ),
        fac.AntdAlert(
            message='Warning',
            description='This is a warning notice about copywriting.',
            type='warning',
            showIcon=True,
            closable=True,
        ),
        fac.AntdAlert(
            message='Error',
            description='This is an error message about copywriting.',
            type='error',
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
