import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTimeRangePicker(
        placeholder=['开始时间', '结束时间'],
        extraFooter=fac.AntdText('底部额外内容示例'),
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTimeRangePicker(
    placeholder=['开始时间', '结束时间'],
    extraFooter=fac.AntdText('底部额外内容示例'),
)
"""
    }
]
