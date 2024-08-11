import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdRadioGroup(
                id='transfer-multiple-mode-search-demo-switch-mode',
                options=[
                    {'label': mode, 'value': mode}
                    for mode in ['case-insensitive', 'case-sensitive', 'regex']
                ],
                defaultValue='case-insensitive',
                optionType='button',
            ),
            fac.AntdTransfer(
                id='transfer-multiple-mode-search-demo',
                dataSource=[
                    {'key': i, 'title': f'选项{i}'} for i in list('AbCdEf')
                ],
                targetKeys=[],
                showSearch=True,
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('transfer-multiple-mode-search-demo', 'optionFilterMode'),
    Input('transfer-multiple-mode-search-demo-switch-mode', 'value'),
)
def transfer_multiple_mode_search_demo(value):
    return value


code_string = [
    {
        'code': """

"""
    }
]
