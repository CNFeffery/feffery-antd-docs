from typing import List
from pathlib import Path
import feffery_antd_components as fac
from i18n import get_current_locale
from utils.api_doc_sources import get_component_docstring


def get_components_docs(components: List[str]) -> str:
    """从components列表中提取合法的组件docstring"""

    components = list(dict.fromkeys(components))
    english = get_current_locale() == 'en-us'
    docs_directory = (
        Path(__file__).resolve().parents[1] / 'public/api_documents/en_us'
    )

    output = ''

    if 'all' in components:
        components = [
            attr
            for attr in dir(fac)
            if attr.startswith('Antd') or attr == 'Fragment'
        ]

    for component in components:
        if hasattr(fac, component):
            target = getattr(fac, component)
            document = (
                get_component_docstring(target)
                if isinstance(target, type)
                else target.__doc__
            )
            translated_path = docs_directory / f'{component}.md'
            if english and translated_path.is_file():
                document = translated_path.read_text(encoding='utf-8')
            output += f"""
# {'Component: ' if english else '组件名称：'}{component}

# {'Component properties' if english else '组件参数文档'}

{document}


"""

    return output
