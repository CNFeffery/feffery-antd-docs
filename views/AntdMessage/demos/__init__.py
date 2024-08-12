import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    type,  # noqa: F401
    duration,  # noqa: F401
    top,  # noqa: F401
    max_count,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '全局提示的常规使用方式是通过回调向某个容器输出，每一次输出都会触发一条新的全局提示的新增。'
        ),
    },
    {
        'path': 'type',
        'title': '提示类型',
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
        'path': 'duration',
        'title': '修改延时',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置参数'),
                fac.AntdText('duration', code=True),
                fac.AntdText('控制全局提示的显示时间，默认为'),
                fac.AntdText('3', code=True),
                fac.AntdText('秒。'),
            ]
        ),
    },
    {
        'path': 'top',
        'title': '顶端最小距离',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置参数'),
                fac.AntdText('top', code=True),
                fac.AntdText('控制全局提示的顶端最小距离。'),
            ]
        ),
    },
    {
        'path': 'max_count',
        'title': '提示消息数量',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置参数'),
                fac.AntdText('maxCount', code=True),
                fac.AntdText('控制同屏最大消息数。'),
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
