from i18n import translator
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('数据展示')},
                {'title': translator.t('描述列表')},
                {'title': translator.t('AntdDescriptionItem 描述列表子项')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('AntdDescriptionItem 描述列表子项'), level=2
        ),
        fac.AntdParagraph(translator.t('在描述列表中构建单个描述列表子项。')),
    ]
