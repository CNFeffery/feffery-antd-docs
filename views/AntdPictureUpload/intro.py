import feffery_antd_components as fac
from dash.dependencies import Component

from components import tips


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': '文件上传'},
                {'title': 'AntdPictureUpload 图片上传'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdPictureUpload 图片上传', level=2),
        fac.AntdParagraph('专门的图片上传功能。'),
        # 上传接口示例小贴士
        tips.render(tip_type='upload api demo'),
    ]
