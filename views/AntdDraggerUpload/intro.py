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
                {'title': translator.t('AntdDraggerUpload 拖拽上传')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdDraggerUpload 拖拽上传'), level=2),
        fac.AntdParagraph(translator.t('构造可拖拽或点击触发文件上传的区域。')),
        # 上传接口示例小贴士
        tips.render(tip_type='upload api demo'),
    ]
