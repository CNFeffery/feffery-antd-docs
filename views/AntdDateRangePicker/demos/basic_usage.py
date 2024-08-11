import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDateRangePicker(),
            fac.AntdDateRangePicker(
                placeholder=['开始日期时间', '结束日期时间'],
                showTime=True,
                needConfirm=True,
            ),
        ],
        wrap=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDateRangePicker(),
        fac.AntdDateRangePicker(
            placeholder=['开始日期时间', '结束日期时间'],
            showTime=True,
            needConfirm=True,
        ),
    ],
    wrap=True,
)
"""
    }
]
