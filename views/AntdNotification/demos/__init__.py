import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    type,  # noqa: F401
    placement,  # noqa: F401
    duration,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '通知提醒框的常规使用方式是通过回调向某个容器输出，每一次输出都会触发一条新的通知提醒框的新增。'
        ),
    },
    {
        'path': 'type',
        'title': '通知类型',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('共有五种类型'),
                fac.AntdText('default', code=True),
                fac.AntdText('、'),
                fac.AntdText('info', code=True),
                fac.AntdText('、'),
                fac.AntdText('success', code=True),
                fac.AntdText('、'),
                fac.AntdText('warning', code=True),
                fac.AntdText('、'),
                fac.AntdText('error', code=True),
                fac.AntdText('。'),
            ]
        ),
    },
    {
        'path': 'placement',
        'title': '弹出位置',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('使用'),
                fac.AntdText('placement', code=True),
                fac.AntdText(
                    '可以配置通知从上面、下面、左上角、右上角、左下角、右下角弹出。'
                ),
            ]
        ),
    },
    {
        'path': 'duration',
        'title': '修改延时',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置参数'),
                fac.AntdText('duration', code=True),
                fac.AntdText('控制全局通知提醒的显示时间，默认为'),
                fac.AntdText('4.5', code=True),
                fac.AntdText('秒。'),
            ]
        ),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
