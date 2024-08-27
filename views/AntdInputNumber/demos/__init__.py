from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    sizes,  # noqa: F401
    variant,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    status,  # noqa: F401
    addon,  # noqa: F401
    prefix,  # noqa: F401
    suffix,  # noqa: F401
    limit_min_max,  # noqa: F401
    step,  # noqa: F401
    precision,  # noqa: F401
    string_mode,  # noqa: F401
    basic_callbacks,  # noqa: F401
    debounce_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': None,
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': '通过参数`size`控制数值输入框的尺寸规格。',
    },
    {
        'path': 'variant',
        'title': '形态变体',
        'description': '通过参数`variant`控制数值输入框的形态变体。',
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': '设置参数`disabled=True`禁用当前组件。',
    },
    {
        'path': 'read_only',
        'title': '只读状态',
        'description': '通过参数`readOnly`控制数值输入框是否呈现只读状态。',
    },
    {
        'path': 'status',
        'title': '强制渲染校验状态',
        'description': '通过参数`status`控制数值输入框强制渲染校验状态。',
    },
    {
        'path': 'addon',
        'title': '添加前后置额外元素',
        'description': None,
    },
    {
        'path': 'prefix',
        'title': '添加内嵌前缀元素',
        'description': None,
    },
    {
        'path': 'suffix',
        'title': '添加内嵌后缀元素',
        'description': None,
    },
    {
        'path': 'limit_min_max',
        'title': '限制上下限',
        'description': None,
    },
    {
        'path': 'step',
        'title': '控制步长',
        'description': None,
    },
    {
        'path': 'precision',
        'title': '控制精度',
        'description': None,
    },
    {
        'path': 'string_mode',
        'title': '高精度模式',
        'description': '针对超高精度数值的输入场景，通过设置参数`stringMode=True`后，数值将以字符串形式进行监听，从而确保数值精度不丢失。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': None,
    },
    {
        'path': 'debounce_callbacks',
        'title': '防抖回调监听',
        'description': '通过监听施加了防抖效果的输入值，以避免回调函数过于频繁的被触发。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
