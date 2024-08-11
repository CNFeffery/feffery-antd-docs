import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdCopyText(
                    text='AntdCopyText复制示例',
                    beforeIcon='点我复制',
                    afterIcon='复制成功',
                ),
                fac.AntdCopyText(
                    text='AntdCopyText复制示例',
                    beforeIcon=fac.AntdIcon(icon='antd-smile'),
                    afterIcon=fac.AntdIcon(icon='antd-like'),
                ),
            ],
            direction='vertical',
            style={
                'width': '100%',
            },
        )
    ]

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdCopyText(
            text='AntdCopyText复制示例',
            beforeIcon='点我复制',
            afterIcon='复制成功',
        ),
        fac.AntdCopyText(
            text='AntdCopyText复制示例',
            beforeIcon=fac.AntdIcon(icon='antd-smile'),
            afterIcon=fac.AntdIcon(icon='antd-like'),
        ),
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)
"""
    }
]
