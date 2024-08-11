import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCheckboxGroup(
        options=[{'label': f'选项{i}', 'value': f'选项{i}'} for i in range(5)],
        value=['选项1', '选项3'],
        readOnly=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdCheckboxGroup(
    options=[{'label': f'选项{i}', 'value': f'选项{i}'} for i in range(5)],
    value=['选项1', '选项3'],
    readOnly=True,
)
"""
    }
]
