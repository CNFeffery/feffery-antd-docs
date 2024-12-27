import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': align,
                'dataIndex': align,
                'headerAlign': align,
            }
            for align in ['left', 'center', 'right']
        ],
        data=[{align: 999 for align in ['left', 'center', 'right']}] * 3,
        bordered=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': align,
            'dataIndex': align,
            'headerAlign': align,
        }
        for align in ['left', 'center', 'right']
    ],
    data=[{align: 999 for align in ['left', 'center', 'right']}] * 3,
    bordered=True,
)
"""
    }
]
