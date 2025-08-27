import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdQRCode 二维码'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdQRCode 二维码', level=2),
        fac.AntdParagraph(
            '能够将文本转换生成二维码的组件，支持自定义配色和 Logo 配置。'
        ),
    ]
