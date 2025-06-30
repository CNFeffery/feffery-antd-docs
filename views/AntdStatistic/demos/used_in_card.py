import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRow(
        [
            fac.AntdCol(
                fac.AntdCard(
                    fac.AntdStatistic(
                        title='Active',
                        value=11.28,
                        precision=2,
                        valueStyle={
                            'color': '#3f8600',
                        },
                        prefix=fac.AntdIcon(icon='antd-arrow-up'),
                        suffix='%',
                    ),
                    title='Card One',
                    variant='borderless',
                ),
                span=12,
            ),
            fac.AntdCol(
                fac.AntdCard(
                    fac.AntdStatistic(
                        title='Idle',
                        value=9.3,
                        precision=2,
                        valueStyle={
                            'color': '#cf1322',
                        },
                        prefix=fac.AntdIcon(icon='antd-arrow-down'),
                        suffix='%',
                    ),
                    title='Card Two',
                    variant='borderless',
                ),
                span=12,
            ),
        ],
        gutter=16,
        style={'backgroundColor': '#f0f2f5', 'padding': '16px'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdRow(
    [
        fac.AntdCol(
            fac.AntdCard(
                fac.AntdStatistic(
                    title='Active',
                    value=11.28,
                    precision=2,
                    valueStyle={
                        'color': '#3f8600',
                    },
                    prefix=fac.AntdIcon(icon='antd-arrow-up'),
                    suffix='%',
                ),
                title='Card One',
                variant='borderless',
            ),
            span=12,
        ),
        fac.AntdCol(
            fac.AntdCard(
                fac.AntdStatistic(
                    title='Idle',
                    value=9.3,
                    precision=2,
                    valueStyle={
                        'color': '#cf1322',
                    },
                    prefix=fac.AntdIcon(icon='antd-arrow-down'),
                    suffix='%',
                ),
                title='Card Two',
                variant='borderless',
            ),
            span=12,
        ),
    ],
    gutter=16,
    style={
        'backgroundColor': '#f0f2f5',
        'padding': '16px'
    }
)
"""
    }
]
