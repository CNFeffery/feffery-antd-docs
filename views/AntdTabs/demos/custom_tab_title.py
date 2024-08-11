import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTabs(
        items=[
            {
                'key': f'标签页{i}',
                'label': fac.AntdSpace(
                    [
                        fac.AntdText(f'标签页{i}'),
                        fac.AntdTooltip(
                            fac.AntdIcon(
                                icon='antd-question-circle',
                                style={'color': '#9b9b9b'},
                            ),
                            title=f'这是标签页{i}balabalabala',
                            placement='right',
                        ),
                    ]
                ),
            }
            for i in range(1, 6)
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTabs(
    items=[
        {
            'key': f'标签页{i}',
            'label': fac.AntdSpace(
                [
                    fac.AntdText(f'标签页{i}'),
                    fac.AntdTooltip(
                        fac.AntdIcon(
                            icon='antd-question-circle',
                            style={'color': '#9b9b9b'},
                        ),
                        title=f'这是标签页{i}balabalabala',
                        placement='right',
                    ),
                ]
            ),
        }
        for i in range(1, 6)
    ]
)
"""
    }
]
