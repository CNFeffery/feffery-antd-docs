import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('添加末尾幽灵节点', innerTextOrientation='left'),
            fac.AntdTimeline(
                items=[
                    {'content': '训练数据导入'},
                    {'content': '模型训练'},
                    {'content': '模型持久化'},
                    {'content': '模型发布'},
                ],
                pending='处理中',
            ),
            fac.AntdDivider('自定义幽灵节点图标', innerTextOrientation='left'),
            fac.AntdTimeline(
                items=[
                    {'content': '训练数据导入'},
                    {'content': '模型训练'},
                    {'content': '模型持久化'},
                    {'content': '模型发布'},
                ],
                pending='处理中',
                # 使用fuc.FefferyMotion组件为fac.AntdIcon组件添加动画效果
                pendingDot=fuc.FefferyMotion(
                    fac.AntdIcon(
                        icon='antd-hourglass',
                    ),
                    animate={
                        'transform': 'rotate(180deg)',
                    },
                    transition={
                        'repeat': 'infinity',
                        'duration': 1,
                        'type': 'spring',
                    },
                ),
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
        fac.AntdDivider('添加末尾幽灵节点', innerTextOrientation='left'),
        fac.AntdTimeline(
            items=[
                {'content': '训练数据导入'},
                {'content': '模型训练'},
                {'content': '模型持久化'},
                {'content': '模型发布'},
            ],
            pending='处理中',
        ),
        fac.AntdDivider('自定义幽灵节点图标', innerTextOrientation='left'),
        fac.AntdTimeline(
            items=[
                {'content': '训练数据导入'},
                {'content': '模型训练'},
                {'content': '模型持久化'},
                {'content': '模型发布'},
            ],
            pending='处理中',
            # 使用fuc.FefferyMotion组件为fac.AntdIcon组件添加动画效果
            pendingDot=fuc.FefferyMotion(
                fac.AntdIcon(
                    icon='antd-hourglass',
                ),
                animate={
                    'transform': 'rotate(180deg)',
                },
                transition={
                    'repeat': 'infinity',
                    'duration': 1,
                    'type': 'spring',
                },
            ),
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
