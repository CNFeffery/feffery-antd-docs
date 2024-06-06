import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTransfer(
        dataSource=[{'key': i, 'title': f'选项{i}'} for i in range(1, 10)],
        targetKeys=[2, 3, 4],
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTransfer(
    dataSource=[{'key': i, 'title': f'选项{i}'} for i in range(1, 10)],
    targetKeys=[2, 3, 4],
)
"""
    }
]
