import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '其他'},
                {'title': 'AntdConfigProvider 参数配置'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdConfigProvider 参数配置', level=2),
        fac.AntdParagraph(
            '用于对所包裹内容的主题色、尺寸规格、禁用状态、国际化等进行统一强制设置。'
        ),
    ]
