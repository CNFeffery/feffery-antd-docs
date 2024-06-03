import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                'autoSize=False（默认）', innerTextOrientation='left'
            ),
            fac.AntdInput(
                mode='text-area',
                defaultValue='示例内容' * 20,
                style={'width': 350},
            ),
            fac.AntdDivider(
                'autoSize=True（跟随行数扩展高度）', innerTextOrientation='left'
            ),
            fac.AntdInput(
                mode='text-area',
                defaultValue='示例内容' * 20,
                autoSize=True,
                style={'width': 350},
            ),
            fac.AntdDivider(
                '配置minRows、maxRows参数',
                innerTextOrientation='left',
            ),
            fac.AntdInput(
                mode='text-area',
                defaultValue='示例内容' * 20,
                autoSize={'minRows': 2, 'maxRows': 3},
                style={'width': 350},
            ),
        ],
        direction='vertical',
        style={'width': '350px'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider(
            'autoSize=False（默认）', innerTextOrientation='left'
        ),
        fac.AntdInput(
            mode='text-area',
            defaultValue='示例内容' * 20,
            style={'width': 350},
        ),
        fac.AntdDivider(
            'autoSize=True（跟随行数扩展高度）', innerTextOrientation='left'
        ),
        fac.AntdInput(
            mode='text-area',
            defaultValue='示例内容' * 20,
            autoSize=True,
            style={'width': 350},
        ),
        fac.AntdDivider(
            '配置minRows、maxRows参数',
            innerTextOrientation='left',
        ),
        fac.AntdInput(
            mode='text-area',
            defaultValue='示例内容' * 20,
            autoSize={'minRows': 2, 'maxRows': 3},
            style={'width': 350},
        ),
    ],
    direction='vertical',
    style={'width': '350px'},
)
"""
    }
]
