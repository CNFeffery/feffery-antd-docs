import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdSpace(
                [
                    fac.AntdButton(
                        'Execute js',
                        clickExecuteJsString='alert("Execute js example")',
                    ),
                    fac.AntdButton(
                        'Open modal',
                        clickExecuteJsString='dash_clientside.set_props("button-click-execute-js-modal", {"visible": true})',
                    ),
                ],
                wrap=True,
            ),
            # example modal
            fac.AntdModal(
                'This is an example modal',
                id='button-click-execute-js-modal',
                title='Example modal',
            ),
        ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdSpace(
        [
            fac.AntdButton(
                'Execute js',
                clickExecuteJsString='alert("Execute js example")',
            ),
            fac.AntdButton(
                'Open modal',
                clickExecuteJsString='dash_clientside.set_props("button-click-execute-js-modal", {"visible": true})',
            ),
        ],
        wrap=True,
    ),
    # example modal
    fac.AntdModal(
        'This is an example modal',
        id='button-click-execute-js-modal',
        title='Example modal',
    ),
]
"""
            }
        ]
