import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdSpace(
            [
                fac.AntdCompact(
                    [
                        fac.AntdInput(
                            placeholder='请输入', style={'width': 150}
                        ),
                        fac.AntdSelect(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}',
                                }
                                for i in range(1, 4)
                            ],
                            defaultValue='选项1',
                            style={'width': 80},
                        ),
                    ]
                ),
                fac.AntdCompact(
                    [
                        fac.AntdInput(
                            placeholder='请输入', style={'width': '100%'}
                        ),
                        fac.AntdSelect(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}',
                                }
                                for i in range(1, 4)
                            ],
                            defaultValue='选项1',
                            style={'width': 80},
                        ),
                    ],
                    style={'width': '100%'},
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdCompact(
                    [
                        fac.AntdInput(
                            placeholder='Please enter', style={'width': 150}
                        ),
                        fac.AntdSelect(
                            options=[
                                {
                                    'label': f'option{i}',
                                    'value': f'option{i}',
                                }
                                for i in range(1, 4)
                            ],
                            defaultValue='option1',
                            style={'width': 100},
                        ),
                    ]
                ),
                fac.AntdCompact(
                    [
                        fac.AntdInput(
                            placeholder='Please enter', style={'width': '100%'}
                        ),
                        fac.AntdSelect(
                            options=[
                                {
                                    'label': f'option{i}',
                                    'value': f'option{i}',
                                }
                                for i in range(1, 4)
                            ],
                            defaultValue='option1',
                            style={'width': 100},
                        ),
                    ],
                    style={'width': '100%'},
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdCompact(
            [
                fac.AntdInput(placeholder='请输入', style={'width': 150}),
                fac.AntdSelect(
                    options=[
                        {
                            'label': f'选项{i}',
                            'value': f'选项{i}',
                        }
                        for i in range(1, 4)
                    ],
                    defaultValue='选项1',
                    style={'width': 80},
                ),
            ]
        ),
        fac.AntdCompact(
            [
                fac.AntdInput(
                    placeholder='请输入', style={'width': '100%'}
                ),
                fac.AntdSelect(
                    options=[
                        {
                            'label': f'选项{i}',
                            'value': f'选项{i}',
                        }
                        for i in range(1, 4)
                    ],
                    defaultValue='选项1',
                    style={'width': 80},
                ),
            ],
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdCompact(
            [
                fac.AntdInput(
                    placeholder='Please enter', style={'width': 150}
                ),
                fac.AntdSelect(
                    options=[
                        {
                            'label': f'option{i}',
                            'value': f'option{i}',
                        }
                        for i in range(1, 4)
                    ],
                    defaultValue='option1',
                    style={'width': 100},
                ),
            ]
        ),
        fac.AntdCompact(
            [
                fac.AntdInput(
                    placeholder='Please enter', style={'width': '100%'}
                ),
                fac.AntdSelect(
                    options=[
                        {
                            'label': f'option{i}',
                            'value': f'option{i}',
                        }
                        for i in range(1, 4)
                    ],
                    defaultValue='option1',
                    style={'width': 100},
                ),
            ],
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
