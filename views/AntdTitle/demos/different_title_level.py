import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdParagraph(
            [
                fac.AntdTitle('一级标题', level=1),
                fac.AntdTitle('二级标题', level=2),
                fac.AntdTitle('三级标题', level=3),
                fac.AntdTitle('四级标题', level=4),
                fac.AntdTitle('五级标题', level=5),
            ]
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdParagraph(
            [
                fac.AntdTitle('Level1 Title', level=1),
                fac.AntdTitle('Level2 Title', level=2),
                fac.AntdTitle('Level3 Title', level=3),
                fac.AntdTitle('Level4 Title', level=4),
                fac.AntdTitle('Level5 Title', level=5),
            ]
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdParagraph(
    [
        fac.AntdTitle('一级标题', level=1),
        fac.AntdTitle('二级标题', level=2),
        fac.AntdTitle('三级标题', level=3),
        fac.AntdTitle('四级标题', level=4),
        fac.AntdTitle('五级标题', level=5)
    ]
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdParagraph(
    [
        fac.AntdTitle('Level1 Title', level=1),
        fac.AntdTitle('Level2 Title', level=2),
        fac.AntdTitle('Level3 Title', level=3),
        fac.AntdTitle('Level4 Title', level=4),
        fac.AntdTitle('Level5 Title', level=5),
    ]
)
"""
            }
        ]
