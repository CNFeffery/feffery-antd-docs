import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCheckCardGroup(
        [fac.AntdCheckCard(f'选项{i}', value=i) for i in range(1, 6)],
        defaultValue=3,
        readOnly=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdCheckCardGroup(
    [fac.AntdCheckCard(f'选项{i}', value=i) for i in range(1, 6)],
    defaultValue=3,
    readOnly=True,
)
"""
    }
]
