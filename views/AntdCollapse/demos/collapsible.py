import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCollapse(
                fac.AntdParagraph('内容示例' * 20),
                title='collapsible="header"',
                collapsible='header',
                isOpen=False,
                style={'width': 300},
            ),
            fac.AntdCollapse(
                fac.AntdParagraph('内容示例' * 20),
                title='collapsible="disabled"',
                collapsible='disabled',
                isOpen=False,
                style={'width': 300},
            ),
            fac.AntdCollapse(
                fac.AntdParagraph('内容示例' * 20),
                title='collapsible="icon"',
                collapsible='icon',
                isOpen=False,
                style={'width': 300},
            ),
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdCollapse(
            fac.AntdParagraph('内容示例' * 20),
            title='collapsible="header"',
            collapsible='header',
            isOpen=False,
            style={'width': 300},
        ),
        fac.AntdCollapse(
            fac.AntdParagraph('内容示例' * 20),
            title='collapsible="disabled"',
            collapsible='disabled',
            isOpen=False,
            style={'width': 300},
        ),
        fac.AntdCollapse(
            fac.AntdParagraph('内容示例' * 20),
            title='collapsible="icon"',
            collapsible='icon',
            isOpen=False,
            style={'width': 300},
        ),
    ],
    direction='vertical',
)
"""
    }
]
