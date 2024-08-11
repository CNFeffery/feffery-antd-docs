import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRow(
        [
            fac.AntdCol(
                fac.AntdStatistic(
                    title='Feedback',
                    value=1128,
                    prefix=fac.AntdIcon(icon='antd-like'),
                ),
                span=12,
            ),
            fac.AntdCol(
                fac.AntdStatistic(title='Unmerged', value=93, suffix='/ 100'),
                span=12,
            ),
        ],
        gutter=16,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdRow(
    [
        fac.AntdCol(
            fac.AntdStatistic(
                title='Feedback',
                value=1128,
                prefix=fac.AntdIcon(icon='antd-like'),
            ),
            span=12,
        ),
        fac.AntdCol(
            fac.AntdStatistic(title='Unmerged', value=93, suffix='/ 100'),
            span=12,
        ),
    ],
    gutter=16,
)
"""
    }
]
