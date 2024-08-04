import feffery_antd_components as fac
from dash.dependencies import Component

def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdResult(
        status='success',
        title='任务创建成功',
        subTitle=fac.AntdSpace(
            [
                fac.AntdText(
                    '创建时间：2023-01-01 12:00:00',
                    type='secondary'
                ),
                fac.AntdSpace(
                    [
                        fac.AntdButton(
                            '查看详情',
                            type='primary'
                        ),
                        fac.AntdButton(
                            '回到首页'
                        )
                    ]
                )
            ],
            direction='vertical',
            align='center'
            )   
    )
    return demo_contents               

code_string = [ 
    {
       'code':"""
fac.AntdResult(
    status='success',
    title='任务创建成功',
    subTitle=fac.AntdSpace(
        [
            fac.AntdText(
                '创建时间：2023-01-01 12:00:00',
                type='secondary'
            ),
            fac.AntdSpace(
                [
                    fac.AntdButton(
                        '查看详情',
                        type='primary'
                    ),
                    fac.AntdButton(
                        '回到首页'
                    )
                ]
            )
        ],
        direction='vertical',
        align='center'
    )
)
"""
    }
]