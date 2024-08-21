from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component

from config import AppConfig

# 国际化
from i18n import translator


def render(component: Component, section_name: str = None) -> Component:
    """渲染当页文档贡献者头像"""

    # 尝试获取当前组件更多文档贡献者信息
    contributors = [
        'CNFeffery',
        *(
            # 根据组件名称或章节名称获取贡献者信息
            (
                AppConfig.doc_contributors['components'].get(section_name)
                if section_name
                else AppConfig.doc_contributors['components'].get(
                    component.__name__
                )
            )
            or []
        ),
    ]

    return fac.AntdFlex(
        [
            fac.AntdText(translator.t('当页文档贡献者'), type='secondary'),
            fac.AntdSpace(
                [
                    fac.AntdTooltip(
                        html.A(
                            fac.AntdAvatar(
                                mode='image',
                                src=AppConfig.doc_contributors['contributors'][
                                    contributor
                                ]['avatar'],
                                size=36,
                            ),
                            href=AppConfig.doc_contributors['contributors'][
                                contributor
                            ]['url'],
                            target='_blank',
                        ),
                        title=contributor,
                    )
                    for contributor in contributors
                ],
                size=5,
            ),
        ],
        vertical=True,
        gap='small',
        style={
            'width': '100%',
            'paddingBottom': 8,
            'marginTop': 8,
            'marginBottom': 8,
        },
    )
