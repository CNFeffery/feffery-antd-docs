import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTimeline(
                items=[
                    {'content': '训练数据导入'},
                    {'content': '模型训练'},
                    {'content': '模型持久化'},
                    {'content': '模型发布'},
                ],
                pending='处理中',
                reverse=True,
            ),
        ],
        direction='vertical',
        style={
            'width': '100%',
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdTimeline(
            items=[
                {'content': '训练数据导入'},
                {'content': '模型训练'},
                {'content': '模型持久化'},
                {'content': '模型发布'},
            ],
            pending='处理中',
            reverse=True,
        ),
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)
"""
    }
]
