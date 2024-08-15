import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdButton(
                    '执行js', clickExecuteJsString='alert("执行js示例")'
                ),
                fac.AntdButton(
                    '打开模态框',
                    clickExecuteJsString='dash_clientside.set_props("button-click-execute-js-modal", {"visible": true})',
                ),
            ],
            wrap=True,
        ),
        # 示例模态框
        fac.AntdModal(
            '这是一个示例模态框',
            id='button-click-execute-js-modal',
            title='示例模态框',
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdSpace(
        [
            fac.AntdButton(
                '执行js', clickExecuteJsString='alert("执行js示例")'
            ),
            fac.AntdButton(
                '打开模态框',
                clickExecuteJsString='dash_clientside.set_props("button-click-execute-js-modal", {"visible": true})',
            ),
        ],
        wrap=True,
    ),
    # 示例模态框
    fac.AntdModal(
        '这是一个示例模态框',
        id='button-click-execute-js-modal',
        title='示例模态框',
    ),
]
"""
    }
]
