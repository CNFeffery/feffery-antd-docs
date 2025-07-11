from dash import html
from functools import partial
import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import translator
from utils.doc_renderer import MarkdownRenderer

md_renderer = MarkdownRenderer()


def render() -> Component:
    """渲染“版本迁移指南”文档页"""

    t = partial(translator.t, locale_topic='version_migration_guide')

    return html.Div(
        [
            fac.AntdBackTop(),
            html.Div(
                [
                    fac.AntdTitle(
                        t('从0.3到0.4版本'), id='从0.3到0.4版本', level=2
                    ),
                    fac.AntdParagraph(
                        md_renderer.render(
                            t(
                                '`fac`从`0.3`版本迁移到`0.4`版本，除了新增的大量功能外，还需要注意少量组件的参数调整情况，具体如下：'
                            )
                        ),
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdTitle(t('AntdCard移除bordered参数'), level=4),
                    fac.AntdParagraph(
                        md_renderer.render(
                            t(
                                "跟随底层`Antd`框架的变化，`AntdCard`移除了`bordered`参数，请改为设置`variant='borderless'`代替。"
                            )
                        ),
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdTitle(
                        t(
                            '部分组件xxxStyle、xxxClassName格式参数重构到styles、classNames参数中'
                        ),
                        level=4,
                    ),
                    fac.AntdParagraph(
                        md_renderer.render(
                            t(
                                '跟随底层`Antd`框架的变化，相关参数重构至语义化结构参数`styles`、`classNames`对应字段中，具体涉及组件及参数见[0.4.0更新日志](/changelog-0.4.0)中的**变化**章节。'
                            )
                        ),
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdTitle(
                        t('AntdAvatarGroup部分参数重构到max参数中'),
                        level=4,
                    ),
                    fac.AntdParagraph(
                        md_renderer.render(
                            t(
                                '跟随底层`Antd`框架的变化，AntdAvatarGroup部分参数重构至`max`参数中，具体涉及组件及参数见[0.4.0更新日志](/changelog-0.4.0)中的**变化**章节。'
                            )
                        ),
                        style={'textIndent': '2rem'},
                    ),
                ],
                style={'flex': 'auto'},
            ),
            html.Div(
                fac.AntdAnchor(
                    linkDict=[
                        {
                            'title': t('从0.3到0.4版本'),
                            'href': '#从0.3到0.4版本',
                        },
                    ],
                    offsetTop=65,
                ),
                style={'flex': 'none'},
            ),
        ],
        style={'display': 'flex', 'padding': 25},
    )
