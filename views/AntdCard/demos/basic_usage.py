import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCard(
                """
    从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
""",
                title='卡片示例',
                style={'width': 300, 'marginBottom': 10},
            ),
            fac.AntdCenter(
                fac.AntdCard(
                    """
    从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
""",
                    title='无边框卡片示例',
                    variant='borderless',
                    style={'width': 300, 'marginBottom': 10},
                ),
                style={'background': 'rgb(240, 242, 245)', 'padding': 20},
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
        fac.AntdCard(
            '''
从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
''',
            title='卡片示例',
            style={'width': 300, 'marginBottom': 10},
        ),
        fac.AntdCard(
            '''
从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
''',
            title='无边框卡片示例',
            variant='borderless',
            style={'width': 300, 'marginBottom': 10},
        ),
    ],
    direction='vertical',
)
"""
    }
]
