import feffery_antd_components as fac
from dash.dependencies import Component

def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdResult(
        title='标题示例',
        subTitle='副标题示例',
        icon=fac.AntdIcon(
            icon='antd-bulb',
            style={
                'fontSize': 60,
                'color': '#fcd53f'
                }
            )
    )
    return demo_contents               

code_string = [ 
    {
       'code':"""
fac.AntdResult(
    title='标题示例',
    subTitle='副标题示例',
    icon=fac.AntdIcon(
        icon='antd-bulb',
        style={
            'fontSize': 60,
            'color': '#fcd53f'
        }
    )
)
"""
    }
]