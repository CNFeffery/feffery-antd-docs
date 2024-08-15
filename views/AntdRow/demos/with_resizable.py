import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRow(
        [
            fac.AntdCol(
                [
                    fuc.FefferyStyle(
                        rawStyle="""
.custom-right-resize-handle:hover, .custom-right-resize-handle:active {
    background: #007fd4;
    transition: 0.3s background;
}

.custom-right-resize-handle {
    background: #f0f0f0;
    transition: 0.3s background;
    width: 4px !important;
    right: -2px !important;
}
"""
                    ),
                    fuc.FefferyResizable(
                        fac.AntdCenter('left', style={'height': '100%'}),
                        defaultSize={'width': 100, 'height': '100%'},
                        direction=['right'],
                        handleClassNames={
                            'right': 'custom-right-resize-handle'
                        },
                        maxWidth=500,
                        minWidth=50,
                    ),
                ],
                flex='none',
            ),
            fac.AntdCol(
                fac.AntdCenter('right', style={'height': '100%'}), flex='auto'
            ),
        ],
        style={'height': 400, 'border': '1px dashed #8c8c8c'},
    )

    return demo_contents


code_string = [
    {
        'code': '''
fac.AntdRow(
    [
        fac.AntdCol(
            [
                fuc.FefferyStyle(
                    rawStyle="""
.custom-right-resize-handle:hover, .custom-right-resize-handle:active {
    background: #007fd4;
    transition: 0.3s background;
}

.custom-right-resize-handle {
    background: #f0f0f0;
    transition: 0.3s background;
    width: 4px !important;
    right: -2px !important;
}
"""
                ),
                fuc.FefferyResizable(
                    fac.AntdCenter('left', style={'height': '100%'}),
                    defaultSize={'width': 100, 'height': '100%'},
                    direction=['right'],
                    handleClassNames={
                        'right': 'custom-right-resize-handle'
                    },
                    maxWidth=500,
                    minWidth=50,
                ),
            ],
            flex='none',
        ),
        fac.AntdCol(
            fac.AntdCenter('right', style={'height': '100%'}), flex='auto'
        ),
    ],
    style={'height': 400, 'border': '1px dashed #8c8c8c'},
)
'''
    }
]
