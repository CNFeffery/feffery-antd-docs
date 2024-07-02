import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTimeline(
                items=[
                    {'label': '1小时前', 'content': '训练数据导入'},
                    {'label': '58分钟前', 'content': '模型训练'},
                    {
                        'label': fac.AntdTag(content='9分钟前'),
                        'content': '模型持久化',
                    },
                    {
                        'label': fac.AntdTag(content='1分钟前'),
                        'content': '模型发布',
                    },
                ],
                pending='处理中',
            )
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
                {
                    'label': '1小时前',
                    'content': '训练数据导入'
                },
                {
                    'label': '58分钟前',
                    'content': '模型训练'
                },
                {
                    'label': fac.AntdTag(content='9分钟前'),
                    'content': '模型持久化',
                },
                {
                    'label': fac.AntdTag(content='1分钟前'),
                    'content': '模型发布',
                },
            ],
            pending='处理中'
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
