from dash import dcc
import feffery_antd_components as fac
from dash.dependencies import Component


def render(component: Component) -> Component:
    """渲染当前组件演示用例"""

    return fac.AntdParagraph(
        [
            '注：',
            fac.AntdText('AntdFormItem', strong=True),
            '使用需配合',
            fac.AntdText('AntdForm', strong=True),
            '，请前往',
            dcc.Link('AntdForm文档页', href='/AntdForm'),
            '查看具体使用示例。',
        ],
        style={'paddingBottom': 'calc(100vh - 550px)'},
    )
