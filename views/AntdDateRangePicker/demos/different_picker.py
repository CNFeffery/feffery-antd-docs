import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDateRangePicker(
                picker=picker, placeholder=['picker:', picker]
            )
            for picker in ['date', 'week', 'month', 'quarter', 'year']
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
        [
            fac.AntdDateRangePicker(
                picker=picker, placeholder=['picker:', picker]
            )
            for picker in ['date', 'week', 'month', 'quarter', 'year']
        ],
        direction='vertical',
    )
"""
    }
]
