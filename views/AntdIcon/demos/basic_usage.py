import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component

from config import DemosConfig


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRow(
        [
            fac.AntdCol(
                fac.AntdSpace(
                    [
                        # 懒加载优化
                        fuc.FefferyLazyLoad(
                            fac.AntdIcon(icon=icon, style={'fontSize': 26}),
                            height=44,
                        ),
                        fac.AntdText(
                            icon,
                            copyable=True,
                            style={'borderBottom': '1px dashed #e1dfdd'},
                        ),
                    ],
                    direction='vertical',
                    size=0,
                    style={
                        'display': 'flex',
                        'alignItems': 'center',
                        'justifyContent': 'center',
                        'marginBottom': '5px',
                    },
                ),
                # 响应式显示优化
                xs=24,
                sm=12,
                md=12,
                lg=12,
                xl=8,
                xxl=6,
            )
            for icon in DemosConfig.all_icons
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdRow(
    [
        fac.AntdCol(
            fac.AntdSpace(
                [
                    # 懒加载优化
                    fuc.FefferyLazyLoad(
                        fac.AntdIcon(icon=icon, style={'fontSize': 26}),
                        height=44,
                    ),
                    fac.AntdText(
                        icon,
                        copyable=True,
                        style={'borderBottom': '1px dashed #e1dfdd'},
                    ),
                ],
                direction='vertical',
                size=0,
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center',
                    'marginBottom': '5px',
                },
            ),
            # 响应式显示优化
            xs=24,
            sm=12,
            md=12,
            lg=12,
            xl=8,
            xxl=6,
        )
        for icon in DemosConfig.all_icons
    ]
)
"""
    }
]
