import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    duration,  # noqa: F401
    visibility_height,  # noqa: F401
    container,  # noqa: F401
    basic_callback,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '滚动一定距离后出现按钮，点击可回到顶部。'
        ),
        'iframe': True,
    },
    {
        'path': 'duration',
        'title': '设置滚动耗时',
        'description': fac.AntdParagraph(
            '设置回到顶部动作的持续时间，单位为秒。'
        ),
        'iframe': True,
    },
    {
        'path': 'visibility_height',
        'title': '设置组件出现的滚动高度阈值',
        'description': fac.AntdParagraph(
            '设置当滚动高度超过该阈值时，才会显示回到顶部按钮。',
        ),
        'iframe': True,
    },
    {
        'path': 'container',
        'title': '绑定在局部容器中',
        'description': fac.AntdParagraph(
            [
                '可使用',
                fac.AntdText('containerId', strong=True),
                '和',
                fac.AntdText('containerSelector', strong=True),
                '两种参数的方式设置绑定的局部容器，',
                fac.AntdText('containerId', strong=True),
                '接受组件的id，',
                fac.AntdText('containerSelector', strong=True),
                '接受完整的JS代码，如',
                fac.AntdText('document.querySelector("#container")', code=True),
                '。',
            ]
        ),
        'iframe': True,
    },
    {
        'path': 'basic_callback',
        'title': '基础回调',
        'description': fac.AntdParagraph(
            [
                '监听',
                fac.AntdText('BackTop', strong=True),
                '组件的点击事件。',
            ]
        ),
        'iframe': True,
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
