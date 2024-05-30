import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdPageHeader(
        fac.AntdSpace(
            [
                fac.AntdButton('按钮1'),
                fac.AntdButton('按钮2', type='primary'),
                fac.AntdSwitch(
                    checkedChildren='打开', unCheckedChildren='关闭'
                ),
                fac.AntdBadge(status='processing'),
            ]
        ),
        title='页头标题示例',
        subTitle='页头副标题示例',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdPageHeader(
    fac.AntdSpace(
        [
            fac.AntdButton('按钮1'),
            fac.AntdButton('按钮2', type='primary'),
            fac.AntdSwitch(
                checkedChildren='打开',
                unCheckedChildren='关闭'
            ),
            fac.AntdBadge(status='processing')
        ]
    ),
    title='页头标题示例',
    subTitle='页头副标题示例'
)
"""
    }
]
