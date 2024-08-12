import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    render_footer,  # noqa: F401
    custom_footer_button,  # noqa: F401
    width,  # noqa: F401
    centered,  # noqa: F401
    loading,  # noqa: F401
    confirm_loading,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('常规的通过回调触发对话框的弹出。'),
    },
    {
        'path': 'render_footer',
        'title': '渲染底部操作区',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('renderFooter=True', code=True),
                '后，会在对话框底部渲染自带的操作按钮。',
            ]
        ),
    },
    {
        'path': 'custom_footer_button',
        'title': '调整底部操作按钮',
        'description': fac.AntdParagraph(
            '通过相关的一系列参数对底部操作区的取消、确认按钮进行自定义调整。'
        ),
    },
    {
        'path': 'width',
        'title': '控制对话框宽度',
        'description': fac.AntdParagraph(
            ['通过参数', fac.AntdText('width', code=True), '控制对话框宽度。']
        ),
    },
    {
        'path': 'centered',
        'title': '垂直居中',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('centered=True', code=True),
                '后，对话框将垂直居中显示。',
            ]
        ),
    },
    {
        'path': 'loading',
        'title': '加载中状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('loading=True', code=True),
                '为对话框内容区开启加载中状态。',
            ]
        ),
    },
    {
        'path': 'confirm_loading',
        'title': '确认按钮加载中状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('confirmAutoSpin=True', code=True),
                '后，确认按钮每次被点击后都会自动进入加载中状态，此特性适合配合具有一定计算耗时的回调函数，回调完成后通过更新参数',
                fac.AntdText('confirmLoading=False', code=True),
                '来还愿确认按钮的状态。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('通过回调函数监听对话框常用事件。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
