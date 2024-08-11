import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSegmented(
        options=[
            {'label': f'选项{i}', 'value': i, 'icon': icon}
            for i, icon in enumerate(
                [
                    'antd-carry-out',
                    'antd-branches',
                    'antd-team',
                    'antd-send',
                    'antd-setting',
                ]
            )
        ],
        defaultValue=0,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSegmented(
    options=[
        {'label': f'选项{i}', 'value': i, 'icon': icon}
        for i, icon in enumerate(
            [
                'antd-carry-out',
                'antd-branches',
                'antd-team',
                'antd-send',
                'antd-setting',
            ]
        )
    ],
    defaultValue=0,
)
"""
    }
]
