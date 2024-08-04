import feffery_antd_components as fac
from dash.dependencies import Component

def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
                                [
                                    fac.AntdResult(
                                        title='标题示例',
                                        subTitle=f'status="{status}"',
                                        status=status
                                    )
                                    for status in [
                                        'info', 'success', 'warning', 'error',
                                        '404', '403', '500', 'loading'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            )
    return demo_contents               

code_string = [ 
    {
       'code':"""
fac.AntdSpace(
    [
        fac.AntdResult(
            title='标题示例',
            subTitle=f'status="{status}"',
            status=status
        )
        for status in [
            'info', 'success', 'warning', 'error',
            '404', '403', '500', 'loading'
        ]
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)
"""
    }
]