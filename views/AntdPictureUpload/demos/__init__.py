import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    disabled,  # noqa: F401
    editable,  # noqa: F401
    confirm_before_delete,  # noqa: F401
    icons_visible,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('点击触发图片文件上传功能。'),
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('disabled=True', code=True),
                '开启禁用状态。',
            ]
        ),
    },
    {
        'path': 'editable',
        'title': '图片编辑功能',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('editable=True', code=True),
                '后，可配合参数',
                fac.AntdText('editConfig', code=True),
                '进行图片编辑相关功能的配置。',
            ]
        ),
    },
    {
        'path': 'confirm_before_delete',
        'title': '删除前确认',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('confirmBeforeDelete=True', code=True),
                '为已上传文件记录的删除操作添加二次确认功能。',
            ]
        ),
    },
    {
        'path': 'icons_visible',
        'title': '预览及删除图标的显隐',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('showPreviewIcon', code=True),
                '、',
                fac.AntdText('showRemoveIcon', code=True),
                '控制已上传图片记录预览及删除图标的显隐。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': None,
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
