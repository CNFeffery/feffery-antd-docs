import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    basic_callbacks,  # noqa: F401，
    size,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    loading,  # noqa: F401
    custom_checked_children,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最简单的用法。'),
    },
    {
        'path': 'custom_checked_children',
        'title': '自定义开关标签',
        'description': fac.AntdParagraph(
            [
                '通过给',
                fac.AntdText('checkedChildren', strong=True),
                '和',
                fac.AntdText('unCheckedChildren', strong=True),
                '属性传入组件型参数，可以自定义开关标签。',
            ]
        ),
    },
    {
        'path': 'size',
        'title': '不同大小',
        'description': fac.AntdParagraph(
            [
                '通过',
                fac.AntdText('size', strong=True),
                '属性设置开关的尺寸，可选值为',
                fac.AntdText('small', code=True),
                '、',
                fac.AntdText('default', code=True),
                '（默认值：',
                fac.AntdText('default', code=True),
                '）。',
            ]
        ),
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                '可设置是否禁用开关。',
            ]
        ),
    },
    {
        'path': 'read_only',
        'title': '只读状态',
        'description': fac.AntdParagraph(
            [
                '可设置开关状态为只读。',
            ]
        ),
    },
    {
        'path': 'loading',
        'title': '加载中状态',
        'description': fac.AntdParagraph(
            [
                '可设置开关状态为加载中。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                '通过',
                fac.AntdText('checked', strong=True),
                '实现对开关状态切换的监听。',
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
