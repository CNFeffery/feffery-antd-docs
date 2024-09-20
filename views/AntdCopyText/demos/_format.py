import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdFormItem(
                fac.AntdCopyText(
                    text='field1\tfield2\tfield3\nvalue1\tvalue2\tvalue3',
                    beforeIcon=fac.AntdButton('点我复制'),
                    afterIcon=fac.AntdButton('复制成功'),
                ),
                label='text/plain',
            ),
            fac.AntdFormItem(
                fac.AntdCopyText(
                    text='<a href="http://fac.feffery.tech/" >demo link</ a>',
                    beforeIcon=fac.AntdButton('点我复制'),
                    afterIcon=fac.AntdButton('复制成功'),
                    format='text/html',
                ),
                label='text/html',
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
                text='field1\\tfield2\\tfield3\\nvalue1\\tvalue2\\tvalue3',
                beforeIcon=fac.AntdButton('点我复制'),
                afterIcon=fac.AntdButton('复制成功'),
            ),
            label='text/plain',
        ),
        fac.AntdFormItem(
            fac.AntdCopyText(
                text='<a href="http://fac.feffery.tech/" >demo link</ a>',
                beforeIcon=fac.AntdButton('点我复制'),
                afterIcon=fac.AntdButton('复制成功'),
                format='text/html',
            ),
            label='text/html',
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
