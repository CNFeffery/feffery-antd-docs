import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDatePicker(extraFooter=fac.AntdText('底部额外内容示例')),
            fac.AntdDatePicker(
                placeholder='请选择日期时间',
                showTime=True,
                extraFooter=fac.AntdText('底部额外内容示例'),
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
        fac.AntdDatePicker(extraFooter=fac.AntdText('底部额外内容示例')),
        fac.AntdDatePicker(
            placeholder='请选择日期时间',
            showTime=True,
            extraFooter=fac.AntdText('底部额外内容示例'),
        ),
    ],
    wrap=True,
)
"""
    }
]
