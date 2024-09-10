import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdFlex(
            [
                fac.AntdFlex(
                    [
                        fac.AntdTitle('计算任务xxx', level=4),
                        fac.AntdText(
                            '这是计算任务xxx的描述信息balabalabala',
                            type='secondary',
                        ),
                    ],
                    vertical=True,
                ),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}',
                            'description': f'这是步骤{i + 1}的描述',
                        }
                        for i in range(3)
                    ],
                    type='inline',
                    style={'height': 50},
                ),
            ],
            justify='space-between',
            align='flex-end',
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdFlex(
            [
                fac.AntdFlex(
                    [
                        fac.AntdTitle('Compute task xxx', level=4),
                        fac.AntdText(
                            'This is the description of compute task xxx',
                            type='secondary',
                        ),
                    ],
                    vertical=True,
                ),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'Step {i + 1}',
                            'description': f'This is the description of step {i + 1}',
                        }
                        for i in range(3)
                    ],
                    type='inline',
                    style={'height': 50},
                ),
            ],
            justify='space-between',
            align='flex-end',
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdFlex(
    [
        fac.AntdFlex(
            [
                fac.AntdTitle('计算任务xxx', level=4),
                fac.AntdText(
                    '这是计算任务xxx的描述信息balabalabala',
                    type='secondary',
                ),
            ],
            vertical=True,
        ),
        fac.AntdSteps(
            steps=[
                {
                    'title': f'步骤{i + 1}',
                    'description': f'这是步骤{i + 1}的描述',
                }
                for i in range(3)
            ],
            type='inline',
            style={'height': 50},
        ),
    ],
    justify='space-between',
    align='flex-end',
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdFlex(
    [
        fac.AntdFlex(
            [
                fac.AntdTitle('Compute task xxx', level=4),
                fac.AntdText(
                    'This is the description of compute task xxx',
                    type='secondary',
                ),
            ],
            vertical=True,
        ),
        fac.AntdSteps(
            steps=[
                {
                    'title': f'Step {i + 1}',
                    'description': f'This is the description of step {i + 1}',
                }
                for i in range(3)
            ],
            type='inline',
            style={'height': 50},
        ),
    ],
    justify='space-between',
    align='flex-end',
)
"""
            }
        ]
