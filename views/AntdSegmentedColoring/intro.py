from i18n import translator
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('数据录入')},
                {'title': translator.t('AntdSegmentedColoring 分段着色')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdSegmentedColoring 分段着色'), level=2),
        fac.AntdParagraph(
            translator.t(
                '用于配合数据可视化进行分段着色控制，或作为静态的图例进行展示。'
            )
        ),
    ]
