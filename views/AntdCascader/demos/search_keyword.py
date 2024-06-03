import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSwitch(
                id='cascader-demo-search_keyword_switch',
                checked=True,
                checkedChildren='label模式',
                unCheckedChildren='value模式',
            ),
            fac.AntdCascader(
                id='cascader-demo-search_keyword',
                options=[
                    {
                        'label': '四川省',
                        'key': '四川省',
                        'value': 'scs',
                        'children': [
                            {
                                'label': '成都市',
                                'key': '成都市',
                                'value': 'cds',
                            },
                            {
                                'label': '广安市',
                                'key': '广安市',
                                'value': 'gas',
                            },
                        ],
                    },
                    {
                        'label': '重庆市',
                        'key': '重庆市',
                        'value': 'cqs',
                        'children': [
                            {
                                'label': '渝中区',
                                'key': '渝中区',
                                'value': 'yzq',
                                'children': [
                                    {
                                        'label': '解放碑街道',
                                        'key': '解放碑街道',
                                        'value': 'jfbjd',
                                    }
                                ],
                            },
                            {
                                'label': '渝北区',
                                'key': '渝北区',
                                'value': 'ybq',
                            },
                        ],
                    },
                ],
                placeholder='请选择',
                multiple=True,
            ),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('cascader-demo-search_keyword', 'optionFilterProp'),
    Input('cascader-demo-search_keyword_switch', 'checked'),
)
def cascader_search_keyword(checked):
    if checked:
        return 'label'
    return 'value'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSwitch(
            id='cascader-demo-search_keyword_switch',
            checked=True,
            checkedChildren='label',
            unCheckedChildren='value',
        ),
        fac.AntdCascader(
            id='cascader-demo-search_keyword',
            options=[
                {
                    'label': '四川省',
                    'key': '四川省',
                    'value': 'scs',
                    'children': [
                        {
                            'label': '成都市',
                            'key': '成都市',
                            'value': 'cds',
                        },
                        {
                            'label': '广安市',
                            'key': '广安市',
                            'value': 'gas',
                        },
                    ],
                },
                {
                    'label': '重庆市',
                    'key': '重庆市',
                    'value': 'cqs',
                    'children': [
                        {
                            'label': '渝中区',
                            'key': '渝中区',
                            'value': 'yzq',
                            'children': [
                                {
                                    'label': '解放碑街道',
                                    'key': '解放碑街道',
                                    'value': 'jfbjd',
                                }
                            ],
                        },
                        {
                            'label': '渝北区',
                            'key': '渝北区',
                            'value': 'ybq',
                        },
                    ],
                },
            ],
            placeholder='请选择',
            multiple=True,
        ),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('cascader-demo-search_keyword', 'optionFilterProp'),
    Input('cascader-demo-search_keyword_switch', 'checked'),
)
def cascader_search_keyword(checked):
    if checked:
        return 'label'
    return 'value'
"""
    }
]
