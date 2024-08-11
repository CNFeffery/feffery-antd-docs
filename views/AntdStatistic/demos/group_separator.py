import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdFlex(
        [
            fac.AntdDivider(
                fac.AntdText('showGroupSeparator=True', code=True),
                innerTextOrientation='left',
            ),
            fac.AntdStatistic(
                title='数值型统计数值示例',
                value=1321321.3213,
                showGroupSeparator=True,
            ),
            fac.AntdDivider(
                fac.AntdText('showGroupSeparator=False', code=True),
                innerTextOrientation='left',
            ),
            fac.AntdStatistic(
                title='数值型统计数值示例',
                value=1321321.3213,
                showGroupSeparator=False,
            ),
        ],
        gap='small',
        align='flex-start',
        vertical=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdFlex(
    [
        fac.AntdDivider(
            fac.AntdText('showGroupSeparator=True', code=True),
            innerTextOrientation='left',
        ),
        fac.AntdStatistic(
            title='数值型统计数值示例',
            value=1321321.3213,
            showGroupSeparator=True,
        ),
        fac.AntdDivider(
            fac.AntdText('showGroupSeparator=False', code=True),
            innerTextOrientation='left',
        ),
        fac.AntdStatistic(
            title='数值型统计数值示例',
            value=1321321.3213,
            showGroupSeparator=False,
        ),
    ],
    gap='small',
    align='flex-start',
    vertical=True,
)
"""
    }
]
