from functools import partial
import feffery_antd_components as fac
from dash.dependencies import Component

from utils.doc_renderer import MarkdownRenderer

# 国际化
from i18n import translator

markdown_renderer = MarkdownRenderer()


def render(component: Component) -> Component:
    """渲染当前组件演示用例"""
    t = partial(translator.t, locale_topic='AntdCol')
    return fac.AntdParagraph(
        markdown_renderer.render(
            t(
                '注：**AntdCol**使用需配合**AntdRow**，请前往[AntdRow文档页](/AntdRow)查看具体使用示例。'
            )
        ),
        style={'paddingBottom': 'calc(100vh - 550px)'},
    )
