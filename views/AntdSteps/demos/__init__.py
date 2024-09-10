from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    with_more_info,  # noqa: F401
    custom_icon,  # noqa: F401
    percent,  # noqa: F401
    set_current,  # noqa: F401
    vertical,  # noqa: F401
    vertical_info,  # noqa: F401
    dot,  # noqa: F401
    sizes,  # noqa: F401
    current_status,  # noqa: F401
    navigation,  # noqa: F401
    inline,  # noqa: F401
    click_switch,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdSteps')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('基础的静态步骤条。'),
        },
        {
            'path': 'with_more_info',
            'title': t('带说明信息的步骤条'),
            'description': t('步骤条节点可额外设置副标题及描述信息。'),
        },
        {
            'path': 'custom_icon',
            'title': t('自定义图标'),
            'description': t('步骤图标可传入任意组件型内容。'),
        },
        {
            'path': 'percent',
            'title': t('当前步骤环状进度'),
            'description': t(
                '通过设置参数`percent`控制当前步骤的环状进度显示效果。'
            ),
        },
        {
            'path': 'set_current',
            'title': t('设置当前所在步骤'),
            'description': t('通过参数`current`可控制当前步骤条所在步骤。'),
        },
        {
            'path': 'vertical',
            'title': t('垂直步骤条'),
            'description': t('从上往下垂直展示步骤条信息。'),
        },
        {
            'path': 'vertical_info',
            'title': t('垂直展示步骤条信息'),
            'description': t(
                '通过参数`labelPlacement`可控制步骤条额外信息的展示形式。'
            ),
        },
        {
            'path': 'dot',
            'title': t('点状步骤条'),
            'description': t('简洁风格的点状步骤条。'),
        },
        {
            'path': 'sizes',
            'title': t('尺寸规格'),
            'description': t('不同尺寸的步骤条。'),
        },
        {
            'path': 'current_status',
            'title': t('控制当前步骤状态'),
            'description': None,
        },
        {
            'path': 'navigation',
            'title': t('导航风格步骤条'),
            'description': None,
        },
        {
            'path': 'inline',
            'title': t('内联风格步骤条'),
            'description': None,
        },
        {
            'path': 'click_switch',
            'title': t('允许点击切换步骤'),
            'description': t(
                '设置参数`allowClick=True`后可直接点击步骤进行步骤切换。'
            ),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('通过回调函数监听并控制步骤条功能。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
