import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('隐藏内容区示例', innerTextOrientation='left'),
            fac.AntdCard(
                '隐藏内容区示例',
                title='标题',
                bodyStyle={'display': 'none'},
            ),
            fac.AntdDivider('设置内容区背景示例', innerTextOrientation='left'),
            fac.AntdCard(
                '设置内容区背景示例',
                title='标题',
                bodyStyle={'background': 'rgba(0, 0, 0, 0.3)'},
            ),
        ],
        direction='vertical',
        style={'width': 300},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('隐藏内容区示例', innerTextOrientation='left'),
        fac.AntdCard(
            '隐藏内容区示例',
            title='标题',
            bodyStyle={'display': 'none'},
        ),
        fac.AntdDivider('设置内容区背景示例', innerTextOrientation='left'),
        fac.AntdCard(
            '设置内容区背景示例',
            title='标题',
            bodyStyle={'background': 'rgba(0, 0, 0, 0.3)'},
        ),
    ],
    direction='vertical',
    style={'width': 300},
)
"""
    }
]
