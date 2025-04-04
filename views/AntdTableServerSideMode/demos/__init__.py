from dash.dependencies import Component

from . import (
    pandas_pagination,  # noqa: F401
    pandas_pagination_single_sort,  # noqa: F401
    pandas_pagination_multiple_sort,  # noqa: F401
    pandas_pagination_filter,  # noqa: F401
    database_pagination,  # noqa: F401
    database_pagination_single_sort,  # noqa: F401
    database_pagination_multiple_sort,  # noqa: F401
    database_pagination_filter,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'pandas_pagination',
        'title': '翻页驱动',
        'description': '此例展示了在服务端数据加载模式下，针对**pandas**数据框，联动表格翻页相关事件实现远程数据加载。',
        'group': 'pandas示例',
    },
    {
        'path': 'pandas_pagination_single_sort',
        'title': '翻页+单字段排序驱动',
        'description': '此例展示了在服务端数据加载模式下，针对**pandas**数据框，联动表格翻页+单字段排序相关事件实现远程数据加载。',
        'group': 'pandas示例',
    },
    {
        'path': 'pandas_pagination_multiple_sort',
        'title': '翻页+组合排序驱动',
        'description': '此例展示了在服务端数据加载模式下，针对**pandas**多字段组合排序相关事件实现远程数据加载。',
        'group': 'pandas示例',
    },
    {
        'path': 'pandas_pagination_filter',
        'title': '翻页+筛选驱动',
        'description': '此例展示了在服务端数据加载模式下，针对**pandas**数据框，联动表格翻页+字段筛选相关事件实现远程数据加载。',
        'group': 'pandas示例',
    },
    {
        'path': 'database_pagination',
        'title': '翻页驱动',
        'description': '此例展示了在服务端数据加载模式下，针对数据库表格，联动表格翻页相关事件实现远程数据加载。',
        'group': '数据库示例',
    },
    {
        'path': 'database_pagination_single_sort',
        'title': '翻页+单字段排序驱动',
        'description': '此例展示了在服务端数据加载模式下，针对数据库表格，联动表格翻页+单字段排序相关事件实现远程数据加载。',
        'group': '数据库示例',
    },
    {
        'path': 'database_pagination_multiple_sort',
        'title': '翻页+组合排序驱动',
        'description': '此例展示了在服务端数据加载模式下，针对数据库表格，联动表格翻页+多字段组合排序相关事件实现远程数据加载。',
        'group': '数据库示例',
    },
    {
        'path': 'database_pagination_filter',
        'title': '翻页+筛选驱动',
        'description': '此例展示了在服务端数据加载模式下，针对数据库表格，联动表格翻页+字段筛选相关事件实现远程数据加载。',
        'group': '数据库示例',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
