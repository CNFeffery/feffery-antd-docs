import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTimeline(
                items=[
                    {
                        'content': '负责人：张三',
                        'icon': fac.AntdAvatar(
                            mode='image',
                            src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                        ),
                    },
                    {
                        'content': '训练数据导入',
                        'icon': fac.AntdIcon(
                            icon='md-cloud-upload', style={'fontSize': '18px'}
                        ),
                    },
                    {
                        'content': '模型训练',
                        'icon': fac.AntdIcon(
                            icon='antd-clock-circle', style={'fontSize': '18px'}
                        ),
                    },
                    {
                        'content': '模型持久化',
                        'icon': fac.AntdIcon(
                            icon='fc-accept-database',
                            style={'fontSize': '18px'},
                        ),
                    },
                    {
                        'content': '模型发布',
                        'icon': fac.AntdIcon(
                            icon='md-cloud-done', style={'fontSize': '18px'}
                        ),
                    },
                ]
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
                    'content': '负责人：张三',
                    'icon': fac.AntdAvatar(
                        mode='image',
                        src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                    ),
                },
                {
                    'content': '训练数据导入',
                    'icon': fac.AntdIcon(
                        icon='md-cloud-upload',
                        style={
                            'fontSize': '18px'
                        }
                    )
                },
                {
                    'content': '模型训练',
                    'icon': fac.AntdIcon(
                        icon='antd-clock-circle',
                        style={
                            'fontSize': '18px'
                        }
                    )
                },
                {
                    'content': '模型持久化',
                    'icon': fac.AntdIcon(
                        icon='fc-accept-database',
                        style={
                            'fontSize': '18px'
                        }
                    )
                },
                {
                    'content': '模型发布',
                    'icon': fac.AntdIcon(
                        icon='md-cloud-done',
                        style={
                            'fontSize': '18px'
                        }
                    )
                }
            ]
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
