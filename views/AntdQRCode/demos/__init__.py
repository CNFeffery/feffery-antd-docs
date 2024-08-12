import feffery_antd_components as fac
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

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('基本用法。'),
    },
    {
        'path': 'qrcode_icon',
        'title': '带图片的例子',
        'description': fac.AntdParagraph('带图片的二维码。'),
    },
    {
        'path': 'icon_size',
        'title': '二维码中图片大小',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('iconSize', code=True),
                fac.AntdText('调整二维码中图片的大小。'),
            ]
        ),
    },
    {
        'path': 'border',
        'title': '边框',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('bordered', code=True),
                fac.AntdText('显示或隐藏边框。'),
            ]
        ),
    },
    {
        'path': 'qrcode_status',
        'title': '不同的状态',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('可以通过'),
                fac.AntdText('status', code=True),
                fac.AntdText('的值控制二维码的状态，提供了'),
                fac.AntdText('active', code=True),
                fac.AntdText('、'),
                fac.AntdText('expired', code=True),
                fac.AntdText('、'),
                fac.AntdText('loading', code=True),
                fac.AntdText('、'),
                fac.AntdText('scanned', code=True),
                fac.AntdText('四个值。'),
            ]
        ),
    },
    {
        'path': 'custom_render_type',
        'title': '自定义渲染类型',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('type', code=True),
                fac.AntdText('自定义渲染结果，提供'),
                fac.AntdText('canvas', code=True),
                fac.AntdText('和'),
                fac.AntdText('svg', code=True),
                fac.AntdText('两个选项。'),
            ]
        ),
    },
    {
        'path': 'custom_color',
        'title': '自定义颜色',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('color', code=True),
                fac.AntdText('自定义二维码颜色，通过设置'),
                fac.AntdText('bgColor', code=True),
                fac.AntdText('自定义背景颜色。'),
            ]
        ),
    },
    {
        'path': 'custom_size',
        'title': '自定义尺寸',
        'description': fac.AntdParagraph('自定义尺寸。'),
    },
    {
        'path': 'error_level',
        'title': '纠错比例',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('errorLevel', code=True),
                fac.AntdText('调整不同的容错等级。'),
            ]
        ),
    },
    {
        'path': 'download_qrcode',
        'title': '下载二维码',
        'description': fac.AntdParagraph('下载二维码的简单实现。'),
    },
    {
        'path': 'auto_spin',
        'title': '自动进入加载中状态',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置'),
                fac.AntdText('autoSpin', code=True),
                fac.AntdText('控制在'),
                fac.AntdText('value', code=True),
                fac.AntdText('处于回调更新中时，是否自动切换为'),
                fac.AntdText('loading', code=True),
                fac.AntdText('状态。'),
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('监听当前"点击刷新"按钮累计点击次数，仅在'),
                fac.AntdText('status', code=True),
                fac.AntdText('为'),
                fac.AntdText("'expired'", code=True),
                fac.AntdText('时有效。'),
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
