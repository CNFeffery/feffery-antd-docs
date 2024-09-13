import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSwitch(
                    id='cascader-demo-search_keyword_switch',
                    checked=True,
                    checkedChildren='label mode',
                    unCheckedChildren='value mode',
                ),
                fac.AntdCascader(
                    id='cascader-demo-search_keyword',
                    options=[
                        {
                            'label': 'Sichuan Province',
                            'key': 'Sichuan Province',
                            'value': 'scs',
                            'children': [
                                {
                                    'label': 'Chengdu City',
                                    'key': 'Chengdu City',
                                    'value': 'cds',
                                },
                                {
                                    'label': "Guang'an City",
                                    'key': "Guang'an City",
                                    'value': 'gas',
                                },
                            ],
                        },
                        {
                            'label': 'Chongqing Municipality',
                            'key': 'Chongqing Municipality',
                            'value': 'cqs',
                            'children': [
                                {
                                    'label': 'Yuzhong District',
                                    'key': 'Yuzhong District',
                                    'value': 'yzq',
                                    'children': [
                                        {
                                            'label': 'Jiefangbei Sub-district',
                                            'key': 'Jiefangbei Sub-district',
                                            'value': 'jfbjd',
                                        }
                                    ],
                                },
                                {
                                    'label': 'Yubei District',
                                    'key': 'Yubei District',
                                    'value': 'ybq',
                                },
                            ],
                        },
                    ],
                    placeholder='Please select',
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdSwitch(
            id='cascader-demo-search_keyword_switch',
            checked=True,
            checkedChildren='label mode',
            unCheckedChildren='value mode',
        ),
        fac.AntdCascader(
            id='cascader-demo-search_keyword',
            options=[
                {
                    'label': 'Sichuan Province',
                    'key': 'Sichuan Province',
                    'value': 'scs',
                    'children': [
                        {
                            'label': 'Chengdu City',
                            'key': 'Chengdu City',
                            'value': 'cds',
                        },
                        {
                            'label': "Guang'an City",
                            'key': "Guang'an City",
                            'value': 'gas',
                        },
                    ],
                },
                {
                    'label': 'Chongqing Municipality',
                    'key': 'Chongqing Municipality',
                    'value': 'cqs',
                    'children': [
                        {
                            'label': 'Yuzhong District',
                            'key': 'Yuzhong District',
                            'value': 'yzq',
                            'children': [
                                {
                                    'label': 'Jiefangbei Sub-district',
                                    'key': 'Jiefangbei Sub-district',
                                    'value': 'jfbjd',
                                }
                            ],
                        },
                        {
                            'label': 'Yubei District',
                            'key': 'Yubei District',
                            'value': 'ybq',
                        },
                    ],
                },
            ],
            placeholder='Please select',
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
