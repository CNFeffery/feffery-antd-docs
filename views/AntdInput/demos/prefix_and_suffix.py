import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                prefix=fac.AntdIcon(icon='antd-user'),
                placeholder='请输入用户名',
            ),
            fac.AntdInput(
                suffix=fac.AntdIcon(icon='antd-lock'),
                placeholder='请输入密码',
            ),
            fac.AntdInput(
                prefix=fac.AntdIcon(icon='antd-user'),
                mode='password',
                placeholder='请输入密码',
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(
            prefix=fac.AntdIcon(icon='antd-user'),
            placeholder='请输入用户名',
        ),
        fac.AntdInput(
            suffix=fac.AntdIcon(icon='antd-lock'),
            placeholder='请输入密码',
        ),
        fac.AntdInput(
            prefix=fac.AntdIcon(icon='antd-user'),
            mode='password',
            placeholder='请输入密码',
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
    }
]
