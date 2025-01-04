from typing import List
import feffery_antd_components as fac


def get_components_docs(components: List[str]) -> str:
    """从components列表中提取合法的组件docstring"""

    components = list(set(components))

    output = ''

    if 'all' in components:
        components = [
            attr
            for attr in dir(fac)
            if attr.startswith('Antd') or attr == 'Fragment'
        ]

    for component in components:
        if hasattr(fac, component):
            output += f"""
# 组件名称：{component}

# 组件参数文档

{getattr(fac, component).__doc__}


"""

    return output
