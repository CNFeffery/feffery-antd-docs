import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRadioGroup(
        options=[
            {
                'label': fac.AntdText([fac.AntdIcon(icon=icon), f'选项{i}']),
                'value': f'选项{i}',
            }
            for i, icon in enumerate(
                ['antd-carry-out', 'antd-car', 'antd-bulb', 'antd-build']
            )
        ],
        defaultValue='选项1',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdRadioGroup(
    options=[
        {
            'label': fac.AntdText([fac.AntdIcon(icon=icon), f'选项{i}']),
            'value': f'选项{i}',
        }
        for i, icon in enumerate(
            ['antd-carry-out', 'antd-car', 'antd-bulb', 'antd-build']
        )
    ],
    defaultValue='选项1',
)
"""
    }
]
