import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdSteps(
            steps=[
                {
                    'title': f'步骤{i + 1}的title',
                    'subTitle': f'步骤{i + 1}的subTitle',
                    'description': f'步骤{i + 1}的description',
                }
                for i in range(3)
            ],
            type='navigation',
            current=2,
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSteps(
            steps=[
                {
                    'title': f'Step {i + 1} title',
                    'subTitle': f'Step {i + 1} subTitle',
                    'description': f'Step {i + 1} description',
                }
                for i in range(3)
            ],
            type='navigation',
            current=2,
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}的title',
            'subTitle': f'步骤{i + 1}的subTitle',
            'description': f'步骤{i + 1}的description',
        }
        for i in range(3)
    ],
    type='navigation',
    current=2,
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSteps(
    steps=[
        {
            'title': f'Step {i + 1} title',
            'subTitle': f'Step {i + 1} subTitle',
            'description': f'Step {i + 1} description',
        }
        for i in range(3)
    ],
    type='navigation',
    current=2,
)
"""
            }
        ]
