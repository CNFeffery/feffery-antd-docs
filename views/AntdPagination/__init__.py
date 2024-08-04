import feffery_antd_components as fac
from dash.dependencies import Component

from . import intro, demos
from components import doc_layout


def render() -> Component:
    return doc_layout.render(
        component=fac.AntdPagination,
        intro=intro.render(),
        demos=demos.render(component=fac.AntdPagination),
        catalog=demos.demos_config,
    )
