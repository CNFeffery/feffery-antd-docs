import feffery_antd_components as fac
from dash.dependencies import Component

from . import intro, demos
from components import doc_layout


def render() -> Component:
    return doc_layout.render(
        component=fac.AntdAnchor,
        intro=intro.render(),
        demos=demos.render(component=fac.AntdAnchor),
        catalog=demos.demos_config,
    )
