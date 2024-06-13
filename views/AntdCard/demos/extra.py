import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCard(
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
        # 因设置了extra，extraLink将不会生效
        extraLink={
            'content': '链接示例',
            'href': 'https://zh.wikipedia.org/zh-hans/国际歌',
        },
        extra=fac.AntdButton(
            'extra示例',
            type='primary',
            href='https://zh.wikipedia.org/zh-hans/国际歌',
        ),
        style={'width': 300, 'marginBottom': 10},
    )

    return demo_contents


code_string = [
    {
        'code': """
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
    # 因设置了extra，extraLink将不会生效
    extraLink={
        'content': '链接示例',
        'href': 'https://zh.wikipedia.org/zh-hans/国际歌',
    },
    extra=fac.AntdButton(
        'extra示例',
        type='primary',
        href='https://zh.wikipedia.org/zh-hans/国际歌',
    ),
    style={'width': 300, 'marginBottom': 10},
)
"""
    }
]
