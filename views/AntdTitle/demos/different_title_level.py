import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

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

    return demo_contents


code_string = [
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
