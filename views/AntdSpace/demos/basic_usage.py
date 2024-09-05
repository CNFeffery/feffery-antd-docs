from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdDivider('水平方向（默认）', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '50px',
                            'width': '50px',
                        }
                    )
                ]
                * 3
            ),
            fac.AntdDivider('竖直方向', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '50px',
                            'width': '50px',
                        }
                    )
                ]
                * 3,
                direction='vertical',
            ),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdDivider('Horizontal', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '50px',
                            'width': '50px',
                        }
                    )
                ]
                * 3
            ),
            fac.AntdDivider('Vertical', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '50px',
                            'width': '50px',
                        }
                    )
                ]
                * 3,
                direction='vertical',
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
    fac.AntdDivider('水平方向（默认）', innerTextOrientation='left'),
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            )
        ]
        * 3
    ),
    fac.AntdDivider('竖直方向', innerTextOrientation='left'),
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            )
        ]
        * 3,
        direction='vertical',
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
    fac.AntdDivider('Horizontal', innerTextOrientation='left'),
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            )
        ]
        * 3
    ),
    fac.AntdDivider('Vertical', innerTextOrientation='left'),
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            )
        ]
        * 3,
        direction='vertical',
    ),
]
"""
            }
        ]
