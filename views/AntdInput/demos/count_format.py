import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                mode='text-area',
                showCount=True,
                placeholder='仅匹配连续的大小写字母（单词）为1个字符',
                countFormat='[a-zA-Z]+',
                style={'width': 350},
            ),
            fac.AntdInput(
                mode='text-area',
                showCount=True,
                placeholder='仅计数汉字',
                countFormat='[\u4e00-\u9fff]',
                style={'width': 350},
            ),
        ],
        direction='vertical',
        size='large',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(
            mode='text-area',
            showCount=True,
            placeholder='仅匹配连续的大小写字母（单词）为1个字符',
            countFormat='[a-zA-Z]+',
            style={'width': 350},
        ),
        fac.AntdInput(
            mode='text-area',
            showCount=True,
            placeholder='仅计数汉字',
            countFormat='[\u4e00-\u9fff]',
            style={'width': 350},
        ),
    ],
    direction='vertical',
    size='large',
)
"""
    }
]
