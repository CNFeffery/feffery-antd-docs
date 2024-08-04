import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRow(
        [
            fac.AntdCol(
                fac.AntdStatistic(
                    title='Active Users',
                    value=fuc.FefferyCountUp(end=112893, duration=3),
                ),
                span=12,
            ),
            fac.AntdCol(
                fac.AntdStatistic(
                    title='Account Balance (CNY)',
                    value=fuc.FefferyCountUp(end=112893, duration=3),
                ),
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
                title='Active Users',
                value=fuc.FefferyCountUp(end=112893, duration=3),
            ),
            span=12,
        ),
        fac.AntdCol(
            fac.AntdStatistic(
                title='Account Balance (CNY)',
                value=fuc.FefferyCountUp(end=112893, duration=3),
            ),
            span=12,
        ),
    ],
    gutter=16,
)
"""
    }
]
