import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                'AntdCardGrid基础使用', innerTextOrientation='left'
            ),
            fac.AntdCard(
                [fac.AntdCardGrid(f'内容{i}') for i in range(1, 16)],
                title='AntdCardGrid基础使用',
            ),
            fac.AntdDivider(
                '调整浏览器窗口尺寸以观察换行效果', innerTextOrientation='left'
            ),
            fac.AntdCard(
                [
                    fac.AntdCardGrid(f'内容{i}', style={'width': 95})
                    for i in range(1, 16)
                ],
                title='固定AntdCardGrid宽度以支持自动换行',
            ),
            fac.AntdDivider('紧凑的网格内容区', innerTextOrientation='left'),
            fac.AntdCard(
                [fac.AntdCardGrid(f'内容{i}') for i in range(1, 16)],
                title='调整各类样式以实现紧凑的网格内容区',
                bordered=False,
                bodyStyle={'padding': '0px 1px 0px 0px', 'border': 0},
                headStyle={'border': '1px solid #f0f0f0'},
                style={'borderRadius': '8px 8px 0 0'},
            ),
            fac.AntdDivider('关闭悬停阴影效果', innerTextOrientation='left'),
            fac.AntdCard(
                [
                    fac.AntdCardGrid(f'内容{i}', hoverable=False)
                    for i in range(1, 16)
                ],
                title='关闭悬停阴影效果',
            ),
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider(
            'AntdCardGrid基础使用', innerTextOrientation='left'
        ),
        fac.AntdCard(
            [fac.AntdCardGrid(f'内容{i}') for i in range(1, 16)],
            title='AntdCardGrid基础使用',
        ),
        fac.AntdDivider(
            '调整浏览器窗口尺寸以观察换行效果', innerTextOrientation='left'
        ),
        fac.AntdCard(
            [
                fac.AntdCardGrid(f'内容{i}', style={'width': 95})
                for i in range(1, 16)
            ],
            title='固定AntdCardGrid宽度以支持自动换行',
        ),
        fac.AntdDivider('紧凑的网格内容区', innerTextOrientation='left'),
        fac.AntdCard(
            [fac.AntdCardGrid(f'内容{i}') for i in range(1, 16)],
            title='调整各类样式以实现紧凑的网格内容区',
            bordered=False,
            bodyStyle={'padding': '0px 1px 0px 0px', 'border': 0},
            headStyle={'border': '1px solid #f0f0f0'},
            style={'borderRadius': '8px 8px 0 0'},
        ),
        fac.AntdDivider('关闭悬停阴影效果', innerTextOrientation='left'),
        fac.AntdCard(
            [
                fac.AntdCardGrid(f'内容{i}', hoverable=False)
                for i in range(1, 16)
            ],
            title='关闭悬停阴影效果',
        ),
    ],
    direction='vertical',
)
"""
    }
]
