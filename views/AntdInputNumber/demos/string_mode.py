import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdInputNumber(
        stringMode=True,
        defaultValue='0.1312312314124123124124123123123312312321312312312312',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdInputNumber(
    stringMode=True,
    defaultValue='0.1312312314124123124124123123123312312321312312312312',
    style={'width': '100%'},
)
"""
    }
]
