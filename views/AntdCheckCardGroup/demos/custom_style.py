import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fuc.FefferyStyle(
                rawStyle="""
.check-card-group-custom-style-demo .ant-pro-checkcard-content {
    padding: 5px 12px;
}
"""
            ),
            fac.AntdCheckCardGroup(
                [
                    fac.AntdCheckCard(
                        f'选项{i}',
                        value=i,
                        style={
                            'width': 'auto',
                            'marginRight': 3,
                            'marginBottom': 3,
                            'borderRadius': 5,
                        },
                    )
                    for i in range(1, 26)
                ],
                className='check-card-group-custom-style-demo',
                defaultValue=[4, 8, 9, 15],
                multiple=True,
            ),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fuc.FefferyStyle(
                rawStyle="""
.check-card-group-custom-style-demo .ant-pro-checkcard-content {
    padding: 5px 12px;
}
"""
            ),
            fac.AntdCheckCardGroup(
                [
                    fac.AntdCheckCard(
                        f'Option{i}',
                        value=i,
                        style={
                            'width': 'auto',
                            'marginRight': 3,
                            'marginBottom': 3,
                            'borderRadius': 5,
                        },
                    )
                    for i in range(1, 26)
                ],
                className='check-card-group-custom-style-demo',
                defaultValue=[4, 8, 9, 15],
                multiple=True,
            ),
        ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': '''
[
    fuc.FefferyStyle(
        rawStyle="""
.check-card-group-custom-style-demo .ant-pro-checkcard-content {
    padding: 5px 12px;
}
"""
    ),
    fac.AntdCheckCardGroup(
        [
            fac.AntdCheckCard(
                f'选项{i}',
                value=i,
                style={
                    'width': 'auto',
                    'marginRight': 3,
                    'marginBottom': 3,
                    'borderRadius': 5,
                },
            )
            for i in range(1, 26)
        ],
        className='check-card-group-custom-style-demo',
        defaultValue=[4, 8, 9, 15],
        multiple=True,
    ),
]
'''
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': '''
[
    fuc.FefferyStyle(
        rawStyle="""
.check-card-group-custom-style-demo .ant-pro-checkcard-content {
    padding: 5px 12px;
}
"""
    ),
    fac.AntdCheckCardGroup(
        [
            fac.AntdCheckCard(
                f'Option{i}',
                value=i,
                style={
                    'width': 'auto',
                    'marginRight': 3,
                    'marginBottom': 3,
                    'borderRadius': 5,
                },
            )
            for i in range(1, 26)
        ],
        className='check-card-group-custom-style-demo',
        defaultValue=[4, 8, 9, 15],
        multiple=True,
    ),
]
'''
            }
        ]
