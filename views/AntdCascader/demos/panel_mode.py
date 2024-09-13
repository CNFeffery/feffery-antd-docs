import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdCascader(
            panelMode=True,
            options=[
                {
                    'label': '四川省',
                    'key': '四川省',
                    'value': '四川省',
                    'children': [
                        {
                            'label': '成都市',
                            'key': '成都市',
                            'value': '成都市',
                        },
                        {
                            'label': '广安市',
                            'key': '广安市',
                            'value': '广安市',
                        },
                    ],
                },
                {
                    'label': '重庆市',
                    'key': '重庆市',
                    'value': '重庆市',
                    'children': [
                        {
                            'label': '渝中区',
                            'key': '渝中区',
                            'value': '渝中区',
                            'children': [
                                {
                                    'label': '解放碑街道',
                                    'key': '解放碑街道',
                                    'value': '解放碑街道',
                                }
                            ],
                        },
                        {
                            'label': '渝北区',
                            'key': '渝北区',
                            'value': '渝北区',
                        },
                    ],
                },
            ],
            placeholder='请选择',
            multiple=True,
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdCascader(
            panelMode=True,
            options=[
                {
                    'label': 'Sichuan Province',
                    'key': 'Sichuan Province',
                    'value': 'Sichuan Province',
                    'children': [
                        {
                            'label': 'Chengdu City',
                            'key': 'Chengdu City',
                            'value': 'Chengdu City',
                        },
                        {
                            'label': "Guang'an City",
                            'key': "Guang'an City",
                            'value': "Guang'an City",
                        },
                    ],
                },
                {
                    'label': 'Chongqing Municipality',
                    'key': 'Chongqing Municipality',
                    'value': 'Chongqing Municipality',
                    'children': [
                        {
                            'label': 'Yuzhong District',
                            'key': 'Yuzhong District',
                            'value': 'Yuzhong District',
                            'children': [
                                {
                                    'label': 'Jiefangbei Sub-district',
                                    'key': 'Jiefangbei Sub-district',
                                    'value': 'Jiefangbei Sub-district',
                                }
                            ],
                        },
                        {
                            'label': 'Yubei District',
                            'key': 'Yubei District',
                            'value': 'Yubei District',
                        },
                    ],
                },
            ],
            placeholder='Please select',
            multiple=True,
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdCascader(
    panelMode=True,
    options=[
        {
            'label': '四川省',
            'key': '四川省',
            'value': '四川省',
            'children': [
                {
                    'label': '成都市',
                    'key': '成都市',
                    'value': '成都市',
                },
                {
                    'label': '广安市',
                    'key': '广安市',
                    'value': '广安市',
                },
            ],
        },
        {
            'label': '重庆市',
            'key': '重庆市',
            'value': '重庆市',
            'children': [
                {
                    'label': '渝中区',
                    'key': '渝中区',
                    'value': '渝中区',
                    'children': [
                        {
                            'label': '解放碑街道',
                            'key': '解放碑街道',
                            'value': '解放碑街道',
                        }
                    ],
                },
                {
                    'label': '渝北区',
                    'key': '渝北区',
                    'value': '渝北区',
                },
            ],
        },
    ],
    placeholder='请选择',
    multiple=True,
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdCascader(
    panelMode=True,
    options=[
        {
            'label': 'Sichuan Province',
            'key': 'Sichuan Province',
            'value': 'Sichuan Province',
            'children': [
                {
                    'label': 'Chengdu City',
                    'key': 'Chengdu City',
                    'value': 'Chengdu City',
                },
                {
                    'label': "Guang'an City",
                    'key': "Guang'an City",
                    'value': "Guang'an City",
                },
            ],
        },
        {
            'label': 'Chongqing Municipality',
            'key': 'Chongqing Municipality',
            'value': 'Chongqing Municipality',
            'children': [
                {
                    'label': 'Yuzhong District',
                    'key': 'Yuzhong District',
                    'value': 'Yuzhong District',
                    'children': [
                        {
                            'label': 'Jiefangbei Sub-district',
                            'key': 'Jiefangbei Sub-district',
                            'value': 'Jiefangbei Sub-district',
                        }
                    ],
                },
                {
                    'label': 'Yubei District',
                    'key': 'Yubei District',
                    'value': 'Yubei District',
                },
            ],
        },
    ],
    placeholder='Please select',
    multiple=True,
)
"""
            }
        ]
