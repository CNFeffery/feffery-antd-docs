import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('默认分段宽度', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    fac.AntdProgress(percent=40, steps=10),
                    fac.AntdProgress(
                        percent=100, steps=5, strokeColor='#52c41a'
                    ),
                    fac.AntdProgress(percent=80, steps=10, size='small'),
                ],
                direction='vertical',
                style={'width': '100%'},
            ),
            fac.AntdDivider('自定义分段宽度', innerTextOrientation='left'),
            fuc.FefferyStyle(
                rawStyle="""
#progress-custom-step-width .ant-progress-steps-item {
    width: 30px !important;
}
"""
            ),
            fac.AntdSpace(
                [
                    fac.AntdProgress(percent=40, steps=10),
                    fac.AntdProgress(
                        percent=100, steps=5, strokeColor='#52c41a'
                    ),
                ],
                id='progress-custom-step-width',
                direction='vertical',
                style={'width': '100%'},
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': '''
fac.AntdSpace(
    [
        fac.AntdDivider('默认分段宽度', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                fac.AntdProgress(percent=40, steps=10),
                fac.AntdProgress(
                    percent=100, steps=5, strokeColor='#52c41a'
                ),
                fac.AntdProgress(percent=80, steps=10, size='small'),
            ],
            direction='vertical',
            style={'width': '100%'},
        ),
        fac.AntdDivider('自定义分段宽度', innerTextOrientation='left'),
        fuc.FefferyStyle(
            rawStyle="""
#progress-custom-step-width .ant-progress-steps-item {
    width: 30px !important;
}
"""
        ),
        fac.AntdSpace(
            [
                fac.AntdProgress(percent=40, steps=10),
                fac.AntdProgress(
                    percent=100, steps=5, strokeColor='#52c41a'
                ),
            ],
            id='progress-custom-step-width',
            direction='vertical',
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
'''
    }
]
