import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdFormItem(
                fac.AntdCopyText(
                    text='test',
                    beforeIcon=fac.AntdButton('点我复制'),
                    afterIcon=fac.AntdButton('复制成功'),
                    tooltips=False,
                ),
                label='关闭提示',
            ),
            fac.AntdFormItem(
                fac.AntdCopyText(
                    text='test',
                    beforeIcon=fac.AntdButton('点我复制'),
                    afterIcon=fac.AntdButton('复制成功'),
                    tooltips=['请点击复制', '搞定！'],
                ),
                label='自定义提示',
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdFormItem(
            fac.AntdCopyText(
                text='test',
                beforeIcon=fac.AntdButton('点我复制'),
                afterIcon=fac.AntdButton('复制成功'),
                tooltips=False,
            ),
            label='关闭提示',
        ),
        fac.AntdFormItem(
            fac.AntdCopyText(
                text='test',
                beforeIcon=fac.AntdButton('点我复制'),
                afterIcon=fac.AntdButton('复制成功'),
                tooltips=['请点击复制', '搞定！'],
            ),
            label='自定义提示',
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
