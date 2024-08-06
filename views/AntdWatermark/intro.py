import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdWatermark 水印'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdWatermark 水印', level=2),
        fac.AntdParagraph('用于在指定内容上叠加水印内容。'),
    ]
