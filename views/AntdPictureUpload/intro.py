from i18n import translator
import feffery_antd_components as fac
from dash.dependencies import Component

from components import tips


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('数据录入')},
                {'title': translator.t('文件上传')},
                {'title': translator.t('AntdPictureUpload 图片上传')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdPictureUpload 图片上传'), level=2),
        fac.AntdParagraph(translator.t('专门的图片上传功能。')),
        # 上传接口示例小贴士
        tips.render(tip_type='upload api demo'),
    ]
