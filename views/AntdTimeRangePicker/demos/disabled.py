import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTimeRangePicker(
                placeholder=['开始时间', '结束时间'], disabled=[True, True]
            ),
            fac.AntdTimeRangePicker(
                placeholder=['开始时间', '结束时间'],
                disabled=[True, False],
                defaultValue=['12:00:00', ''],
            ),
            fac.AntdTimeRangePicker(
                placeholder=['开始时间', '结束时间'],
                disabled=[False, True],
                defaultValue=['', '12:00:00'],
            ),
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdTimeRangePicker(
            placeholder=['开始时间', '结束时间'], disabled=[True, True]
        ),
        fac.AntdTimeRangePicker(
            placeholder=['开始时间', '结束时间'],
            disabled=[True, False],
            defaultValue=['12:00:00', ''],
        ),
        fac.AntdTimeRangePicker(
            placeholder=['开始时间', '结束时间'],
            disabled=[False, True],
            defaultValue=['', '12:00:00'],
        ),
    ],
    direction='vertical',
)
"""
    }
]
