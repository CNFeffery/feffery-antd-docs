"""Apply documented, version-specific corrections without changing FAC itself."""

import json
import re
from pathlib import Path

import feffery_antd_components as fac

CORRECTIONS = json.loads(
    (
        Path(__file__).resolve().parents[1]
        / 'public/api_documents/docstring_corrections.json'
    ).read_text(encoding='utf-8')
)


def get_component_docstring(component):
    document = component.__doc__
    if fac.__version__ != CORRECTIONS['fac_version']:
        return document
    for prop, correction in (
        CORRECTIONS['corrections'].get(component.__name__, {}).items()
    ):
        pattern = re.compile(
            rf'(?m)(^    - {re.escape(prop)} \([^\n]+\):\n)'
            r'        \S[^\n]*(?:\n        \S[^\n]*)*'
        )
        document, count = pattern.subn(
            lambda match: match[1] + '        ' + correction['zh-cn'], document
        )
        if count != 1:
            raise ValueError(
                f'Cannot apply documented correction: {component.__name__}.{prop}'
            )
    return document
