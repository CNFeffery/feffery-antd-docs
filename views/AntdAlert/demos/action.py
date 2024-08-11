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
                closable=True,
                action=fac.AntdButton('UNDO', size='small', type='text'),
            ),
            fac.AntdAlert(
                message='Error Text',
                description='Error Description Error Description Error Description Error Description',
                type='error',
                showIcon=True,
                action=fac.AntdButton('Detail', size='small', danger=True),
            ),
            fac.AntdAlert(
                message='Warning Text',
                type='warning',
                closable=True,
                action=fac.AntdButton(
                    'Done', size='small', type='text', ghost=True
                ),
            ),
            fac.AntdAlert(
                message='Info Text',
                description='Info Description Info Description Info Description Info Description',
                type='info',
                closable=True,
                action=fac.AntdSpace(
                    [
                        fac.AntdButton('Accept', size='small', type='primary'),
                        fac.AntdButton(
                            'Decline', size='small', danger=True, ghost=True
                        ),
                    ],
                    direction='vertical',
                ),
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
            closable=True,
            action=fac.AntdButton('UNDO', size='small', type='text'),
        ),
        fac.AntdAlert(
            message='Error Text',
            description='Error Description Error Description Error Description Error Description',
            type='error',
            showIcon=True,
            action=fac.AntdButton('Detail', size='small', danger=True),
        ),
        fac.AntdAlert(
            message='Warning Text',
            type='warning',
            closable=True,
            action=fac.AntdButton(
                'Done', size='small', type='text', ghost=True
            ),
        ),
        fac.AntdAlert(
            message='Info Text',
            description='Info Description Info Description Info Description Info Description',
            type='info',
            closable=True,
            action=fac.AntdSpace(
                [
                    fac.AntdButton('Accept', size='small', type='primary'),
                    fac.AntdButton(
                        'Decline', size='small', danger=True, ghost=True
                    ),
                ],
                direction='vertical',
            ),
        ),
    ],
    direction='vertical',
    size='middle',
    style={'width': '100%'},
)
"""
    }
]
