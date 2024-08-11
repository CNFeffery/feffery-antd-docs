import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCheckableTag(
                checkedContent='已选中',
                unCheckedContent='未选中',
            ),
            fac.AntdCheckableTag(
                checkedContent=fac.AntdSpace(
                    [
                        fac.AntdIcon(icon='antd-like'),
                        '取消',
                    ],
                    align='center',
                ),
                unCheckedContent=fac.AntdSpace(
                    [
                        fac.AntdIcon(icon='antd-like'),
                        '点赞',
                    ],
                    align='center',
                ),
            ),
        ],
        wrap=True,
        style={
            'width': '100%',
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdCheckableTag(
            checkedContent='已选中',
            unCheckedContent='未选中',
        ),
        fac.AntdCheckableTag(
            checkedContent=fac.AntdSpace(
                [
                    fac.AntdIcon(icon='antd-like'),
                    '取消',
                ],
                align='center',
            ),
            unCheckedContent=fac.AntdSpace(
                [
                    fac.AntdIcon(icon='antd-like'),
                    '点赞',
                ],
                align='center',
            ),
        ),
    ],
    wrap=True,
    style={
        'width': '100%',
    },
)
"""
    }
]
