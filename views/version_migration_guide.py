from dash import html
from functools import partial
import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import translator, get_current_locale
from utils.doc_renderer import MarkdownRenderer

md_renderer = MarkdownRenderer()


def render() -> Component:
    """渲染“版本迁移指南”文档页"""

    t = partial(translator.t, locale_topic='version_migration_guide')
    current_locale = get_current_locale()

    return html.Div(
        [
            fac.AntdBackTop(),
            html.Div(
                [
                    # fac.AntdTitle(t('环境搭建'), id='环境搭建', level=3),
                    # fac.AntdParagraph(
                    #     md_renderer.render(
                    #         t(
                    #             '在基于**Dash**和**fac**进行应用开发之前，我们需要先搭建好所需的环境，推荐使用**conda**或**mamba**作为环境管理工具，这里以Python 3.10版本为例，在终端执行下列命令进行相关环境的创建及激活：'
                    #         )
                    #     ),
                    #     style={'textIndent': '2rem'},
                    # ),
                ],
                style={'flex': 'auto'},
            ),
            html.Div(
                fac.AntdAnchor(
                    linkDict=[
                        {'title': t('环境搭建'), 'href': '#环境搭建'},
                        {'title': t('构建示例应用'), 'href': '#构建示例应用'},
                        *(
                            [
                                {'title': '拓展阅读', 'href': '#拓展阅读'},
                                {
                                    'title': '更多dash专业知识',
                                    'href': '#更多dash专业知识',
                                },
                            ]
                            if current_locale == 'zh-cn'
                            else []
                        ),
                    ],
                    offsetTop=65,
                ),
                style={'flex': 'none'},
            ),
        ],
        style={'display': 'flex', 'padding': 25},
    )
