import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdSwitch(
                        id='tabs-animation-demo-inkBarAnimated',
                        checked=True,
                        checkedChildren='True',
                        unCheckedChildren='False',
                    ),
                    label='inkBarAnimated',
                ),
                fac.AntdFormItem(
                    fac.AntdSwitch(
                        id='tabs-animation-demo-tabPaneAnimated',
                        checked=False,
                        checkedChildren='True',
                        unCheckedChildren='False',
                    ),
                    label='tabPaneAnimated',
                ),
            ],
            layout='inline',
        ),
        fac.AntdTabs(
            id='tabs-animation-demo',
            items=[
                {
                    'key': f'标签页{i}',
                    'label': f'标签页{i}',
                    'children': fac.AntdCenter(
                        f'这是标签页{i}的内容示例',
                        style={
                            'fontSize': 18,
                            'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                            'height': 200,
                        },
                    ),
                }
                for i in range(1, 6)
            ],
        ),
    ]

    return demo_contents


app.clientside_callback(
    """(inkBarAnimated, tabPaneAnimated) => [inkBarAnimated, tabPaneAnimated]""",
    [
        Output('tabs-animation-demo', 'inkBarAnimated'),
        Output('tabs-animation-demo', 'tabPaneAnimated'),
    ],
    [
        Input('tabs-animation-demo-inkBarAnimated', 'checked'),
        Input('tabs-animation-demo-tabPaneAnimated', 'checked'),
    ],
)

code_string = [
    {
        'code': '''
[
    fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdSwitch(
                    id='tabs-animation-demo-inkBarAnimated',
                    checked=True,
                    checkedChildren='True',
                    unCheckedChildren='False',
                ),
                label='inkBarAnimated',
            ),
            fac.AntdFormItem(
                fac.AntdSwitch(
                    id='tabs-animation-demo-tabPaneAnimated',
                    checked=False,
                    checkedChildren='True',
                    unCheckedChildren='False',
                ),
                label='tabPaneAnimated',
            ),
        ],
        layout='inline',
    ),
    fac.AntdTabs(
        id='tabs-animation-demo',
        items=[
            {
                'key': f'标签页{i}',
                'label': f'标签页{i}',
                'children': fac.AntdCenter(
                    f'这是标签页{i}的内容示例',
                    style={
                        'fontSize': 18,
                        'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                        'height': 200,
                    },
                ),
            }
            for i in range(1, 6)
        ],
    ),
]

...

app.clientside_callback(
    """(inkBarAnimated, tabPaneAnimated) => [inkBarAnimated, tabPaneAnimated]""",
    [
        Output('tabs-animation-demo', 'inkBarAnimated'),
        Output('tabs-animation-demo', 'tabPaneAnimated'),
    ],
    [
        Input('tabs-animation-demo-inkBarAnimated', 'checked'),
        Input('tabs-animation-demo-tabPaneAnimated', 'checked'),
    ],
)
'''
    }
]
