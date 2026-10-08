from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    render_footer,  # noqa: F401
    custom_footer_button,  # noqa: F401
    width,  # noqa: F401
    responsive_width,  # noqa: F401
    centered,  # noqa: F401
    loading,  # noqa: F401
    confirm_loading,  # noqa: F401
    basic_callbacks,  # noqa: F401
    prevent_close,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdModal')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('常规的通过回调触发对话框的弹出。'),
        },
        {
            'path': 'render_footer',
            'title': t('渲染底部操作区'),
            'description': t(
                '设置参数`renderFooter=True`后，会在对话框底部渲染自带的操作按钮。'
            ),
        },
        {
            'path': 'custom_footer_button',
            'title': t('调整底部操作按钮'),
            'description': t(
                '通过相关的一系列参数对底部操作区的取消、确认按钮进行自定义调整。'
            ),
        },
        {
            'path': 'width',
            'title': t('控制对话框宽度'),
            'description': t('通过参数`width`控制对话框宽度。'),
        },
        {
            'path': 'responsive_width',
            'title': t('响应式对话框宽度'),
            'description': t(
                '参数`width`支持传入字典型，以设置不同页面宽度断点下的响应式对话框宽度。'
            ),
        },
        {
            'path': 'centered',
            'title': t('垂直居中'),
            'description': t(
                '设置参数`centered=True`后，对话框将垂直居中显示。'
            ),
        },
        {
            'path': 'loading',
            'title': t('加载中状态'),
            'description': t(
                '设置参数`loading=True`为对话框内容区开启加载中状态。'
            ),
        },
        {
            'path': 'confirm_loading',
            'title': t('确认按钮加载中状态'),
            'description': t(
                '设置参数`confirmAutoSpin=True`后，确认按钮每次被点击后都会自动进入加载中状态，此特性适合配合具有一定计算耗时的回调函数，回调完成后通过更新参数`confirmLoading=False`来还原确认按钮的状态。'
            ),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('通过回调函数监听对话框常用事件。'),
        },
        {
            'path': 'prevent_close',
            'title': t('阻止默认关闭行为'),
            'description': t(
                '设置参数`preventClose=True`后，对话框将不会被用户手动操作关闭，可基于此实现模态框关闭二次确认。'
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
