import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                'mode="right"（默认）', innerTextOrientation='left'
            ),
            fac.AntdTimeline(
                items=[
                    {'label': '1小时前', 'content': '训练数据导入'},
                    {'label': '58分钟前', 'content': '模型训练'},
                    {'label': '9分钟前', 'content': '模型持久化'},
                    {'label': '1分钟前', 'content': '模型发布'},
                ],
                pending='处理中',
            ),
            fac.AntdDivider('mode="alternate"', innerTextOrientation='left'),
            fac.AntdTimeline(
                items=[
                    {'label': '1小时前', 'content': '训练数据导入'},
                    {'label': '58分钟前', 'content': '模型训练'},
                    {'label': '9分钟前', 'content': '模型持久化'},
                    {'label': '1分钟前', 'content': '模型发布'},
                ],
                pending='处理中',
                mode='alternate',
            ),
            fac.AntdDivider('mode="right"', innerTextOrientation='left'),
            fac.AntdTimeline(
                items=[
                    {'label': '1小时前', 'content': '训练数据导入'},
                    {'label': '58分钟前', 'content': '模型训练'},
                    {'label': '9分钟前', 'content': '模型持久化'},
                    {'label': '1分钟前', 'content': '模型发布'},
                ],
                pending='处理中',
                mode='right',
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
        fac.AntdDivider(
            'mode="right"（默认）',
            innerTextOrientation='left'
        ),
        fac.AntdTimeline(
            items=[
                {
                    'label': '1小时前',
                    'content': '训练数据导入'
                },
                {
                    'label': '58分钟前',
                    'content': '模型训练'
                },
                {
                    'label': '9分钟前',
                    'content': '模型持久化'
                },
                {
                    'label': '1分钟前',
                    'content': '模型发布'
                }
            ],
            pending='处理中'
        ),

        fac.AntdDivider(
            'mode="alternate"',
            innerTextOrientation='left'
        ),
        fac.AntdTimeline(
            items=[
                {
                    'label': '1小时前',
                    'content': '训练数据导入'
                },
                {
                    'label': '58分钟前',
                    'content': '模型训练'
                },
                {
                    'label': '9分钟前',
                    'content': '模型持久化'
                },
                {
                    'label': '1分钟前',
                    'content': '模型发布'
                }
            ],
            pending='处理中',
            mode='alternate'
        ),

        fac.AntdDivider(
            'mode="right"',
            innerTextOrientation='left'
        ),
        fac.AntdTimeline(
            items=[
                {
                    'label': '1小时前',
                    'content': '训练数据导入'
                },
                {
                    'label': '58分钟前',
                    'content': '模型训练'
                },
                {
                    'label': '9分钟前',
                    'content': '模型持久化'
                },
                {
                    'label': '1分钟前',
                    'content': '模型发布'
                }
            ],
            pending='处理中',
            mode='right'
        )
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)
"""
    }
]
