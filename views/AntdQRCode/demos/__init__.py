from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    qrcode_icon,  # noqa: F401
    icon_size,  # noqa: F401
    border,  # noqa: F401
    qrcode_status,  # noqa: F401
    custom_render_type,  # noqa: F401
    custom_color,  # noqa: F401
    custom_size,  # noqa: F401
    error_level,  # noqa: F401
    download_qrcode,  # noqa: F401
    high_usage,  # noqa: F401
    auto_spin,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdQRCode')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('基本用法。'),
        },
        {
            'path': 'qrcode_icon',
            'title': t('带图片的例子'),
            'description': t('带图片的二维码。'),
        },
        {
            'path': 'icon_size',
            'title': t('二维码中图片大小'),
            'description': t('通过设置`iconSize`调整二维码中图片的大小。'),
        },
        {
            'path': 'border',
            'title': t('边框'),
            'description': t('通过设置`bordered`显示或隐藏边框。'),
        },
        {
            'path': 'qrcode_status',
            'title': t('不同的状态'),
            'description': t('通过参数`status`控制二维码的状态。'),
        },
        {
            'path': 'custom_render_type',
            'title': t('自定义渲染类型'),
            'description': t('通过参数`type`控制二维码的渲染类型。'),
        },
        {
            'path': 'custom_color',
            'title': t('自定义颜色'),
            'description': t(
                '通过参数`color`和`bgColor`来控制二维码的颜色和背景色。'
            ),
        },
        {
            'path': 'custom_size',
            'title': t('自定义尺寸'),
            'description': t('自定义尺寸。'),
        },
        {
            'path': 'error_level',
            'title': t('纠错比例'),
            'description': t('通过设置`errorLevel`调整不同的容错等级。'),
        },
        {
            'path': 'download_qrcode',
            'title': t('下载二维码'),
            'description': t('下载二维码的简单实现。'),
        },
        {
            'path': 'auto_spin',
            'title': t('自动进入加载中状态'),
            'description': t(
                '通过设置`autoSpin`控制在`value`处于回调更新中时，是否自动切换为`loading`状态。'
            ),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t(
                "监听当前“点击刷新”按钮累计点击次数，仅在`status`为`'expired'`时有效。"
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
