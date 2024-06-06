import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('尝试搜索"香蕉"', innerTextOrientation='left'),
            fac.AntdSelect(
                placeholder='search label',
                optionFilterProp='label',
                options=[
                    {
                        'label': '香蕉',
                        'value': 'banana',
                    },
                    {
                        'label': '苹果',
                        'value': 'apple',
                    },
                    {
                        'label': '西瓜',
                        'value': 'watermelon',
                    },
                    {
                        'label': '草莓',
                        'value': 'strawberry',
                    },
                    {
                        'label': '葡萄',
                        'value': 'grape',
                    },
                ],
                style={'width': '100%'},
            ),
            fac.AntdDivider('尝试搜索"banana"', innerTextOrientation='left'),
            fac.AntdSelect(
                placeholder='search value',
                optionFilterProp='value',
                options=[
                    {
                        'label': '香蕉',
                        'value': 'banana',
                    },
                    {
                        'label': '苹果',
                        'value': 'apple',
                    },
                    {
                        'label': '西瓜',
                        'value': 'watermelon',
                    },
                    {
                        'label': '草莓',
                        'value': 'strawberry',
                    },
                    {
                        'label': '葡萄',
                        'value': 'grape',
                    },
                ],
                style={'width': '100%'},
            ),
            fac.AntdDivider('尝试搜索"banana"', innerTextOrientation='left'),
            fac.AntdText('针对组件型label，只可搜索value'),
            fac.AntdSelect(
                placeholder='search value in component label options',
                optionFilterProp='value',
                options=[
                    {
                        'label': fac.AntdText('香蕉', strong=True),
                        'value': 'banana',
                    },
                    {
                        'label': fac.AntdText('苹果', strong=True),
                        'value': 'apple',
                    },
                    {
                        'label': fac.AntdText('西瓜', strong=True),
                        'value': 'watermelon',
                    },
                    {
                        'label': fac.AntdText('草莓', strong=True),
                        'value': 'strawberry',
                    },
                    {
                        'label': fac.AntdText('葡萄', strong=True),
                        'value': 'grape',
                    },
                ],
                style={'width': '100%'},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
        [
            fac.AntdDivider('尝试搜索"香蕉"', innerTextOrientation='left'),
            fac.AntdSelect(
                placeholder='search label',
                optionFilterProp='label',
                options=[
                    {
                        'label': '香蕉',
                        'value': 'banana',
                    },
                    {
                        'label': '苹果',
                        'value': 'apple',
                    },
                    {
                        'label': '西瓜',
                        'value': 'watermelon',
                    },
                    {
                        'label': '草莓',
                        'value': 'strawberry',
                    },
                    {
                        'label': '葡萄',
                        'value': 'grape',
                    },
                ],
                style={'width': '100%'},
            ),
            fac.AntdDivider('尝试搜索"banana"', innerTextOrientation='left'),
            fac.AntdSelect(
                placeholder='search value',
                optionFilterProp='value',
                options=[
                    {
                        'label': '香蕉',
                        'value': 'banana',
                    },
                    {
                        'label': '苹果',
                        'value': 'apple',
                    },
                    {
                        'label': '西瓜',
                        'value': 'watermelon',
                    },
                    {
                        'label': '草莓',
                        'value': 'strawberry',
                    },
                    {
                        'label': '葡萄',
                        'value': 'grape',
                    },
                ],
                style={'width': '100%'},
            ),
            fac.AntdDivider('针对组件型label，只可搜索"value"', innerTextOrientation='left'),
            fac.AntdSelect(
                placeholder='search component label',
                optionFilterProp='value',
                options=[
                    {
                        'label': fac.AntdText('香蕉', strong=True),
                        'value': 'banana',
                    },
                    {
                        'label': fac.AntdText('苹果', strong=True),
                        'value': 'apple',
                    },
                    {
                        'label': fac.AntdText('西瓜', strong=True),
                        'value': 'watermelon',
                    },
                    {
                        'label': fac.AntdText('草莓', strong=True),
                        'value': 'strawberry',
                    },
                    {
                        'label': fac.AntdText('葡萄', strong=True),
                        'value': 'grape',
                    },
                ],
                style={'width': '100%'},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )
"""
    }
]
