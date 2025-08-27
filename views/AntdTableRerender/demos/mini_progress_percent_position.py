import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSpace(
                    [
                        'align:',
                        fac.AntdRadioGroup(
                            id='table-mini-progress-percent-position-demo-align',
                            options=['start', 'center', 'end'],
                            value='end',
                        ),
                    ]
                ),
                fac.AntdSpace(
                    [
                        'type:',
                        fac.AntdRadioGroup(
                            id='table-mini-progress-percent-position-demo-type',
                            options=['inner', 'outer'],
                            value='inner',
                        ),
                    ]
                ),
                fac.AntdTable(
                    id='table-mini-progress-percent-position-demo',
                    columns=[
                        {
                            'dataIndex': 'mini-progress示例',
                            'title': 'mini-progress示例',
                            'renderOptions': {
                                'renderType': 'mini-progress',
                                'progressShowPercent': True,
                                'progressPercentPosition': {
                                    'align': 'end',
                                    'type': 'inner',
                                },
                            },
                        },
                    ],
                    data=[{'mini-progress示例': x} for x in [0, 0.66, 1]],
                    bordered=True,
                ),
            ],
            direction='vertical',
            size='small',
            style={'width': '100%'},
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSpace(
                    [
                        'align:',
                        fac.AntdRadioGroup(
                            id='table-mini-progress-percent-position-demo-align',
                            options=['start', 'center', 'end'],
                            value='end',
                        ),
                    ]
                ),
                fac.AntdSpace(
                    [
                        'type:',
                        fac.AntdRadioGroup(
                            id='table-mini-progress-percent-position-demo-type',
                            options=['inner', 'outer'],
                            value='inner',
                        ),
                    ]
                ),
                fac.AntdTable(
                    id='table-mini-progress-percent-position-demo',
                    locale='en-us',
                    columns=[
                        {
                            'dataIndex': 'mini-progress Example',
                            'title': 'mini-progress Example',
                            'renderOptions': {
                                'renderType': 'mini-progress',
                                'progressShowPercent': True,
                                'progressPercentPosition': {
                                    'align': 'end',
                                    'type': 'inner',
                                },
                            },
                        },
                    ],
                    data=[{'mini-progress Example': x} for x in [0, 0.66, 1]],
                    bordered=True,
                ),
            ],
            direction='vertical',
            size='small',
            style={'width': '100%'},
        )

    return demo_contents


app.clientside_callback(
    """
(align, type) => {
    return [
        {
            'dataIndex': 'mini-progress示例',
            'title': 'mini-progress示例',
            'renderOptions': {
                'renderType': 'mini-progress',
                'progressShowPercent': true,
                'progressPercentPosition': {
                    'align': align,
                    'type': type,
                },
            },
        },
    ];
}
""",
    Output('table-mini-progress-percent-position-demo', 'columns'),
    [
        Input('table-mini-progress-percent-position-demo-align', 'value'),
        Input('table-mini-progress-percent-position-demo-type', 'value'),
    ],
    prevent_initial_call=True,
)


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                'align:',
                fac.AntdRadioGroup(
                    id='table-mini-progress-percent-position-demo-align',
                    options=['start', 'center', 'end'],
                    value='end',
                ),
            ]
        ),
        fac.AntdSpace(
            [
                'type:',
                fac.AntdRadioGroup(
                    id='table-mini-progress-percent-position-demo-type',
                    options=['inner', 'outer'],
                    value='inner',
                ),
            ]
        ),
        fac.AntdTable(
            id='table-mini-progress-percent-position-demo',
            columns=[
                {
                    'dataIndex': 'mini-progress示例',
                    'title': 'mini-progress示例',
                    'renderOptions': {
                        'renderType': 'mini-progress',
                        'progressShowPercent': True,
                        'progressPercentPosition': {
                            'align': 'end',
                            'type': 'inner',
                        },
                    },
                },
            ],
            data=[{'mini-progress示例': x} for x in [0, 0.66, 1]],
            bordered=True,
        ),
    ],
    direction='vertical',
    size='small',
    style={'width': '100%'},
)

...

app.clientside_callback(
    \"""
(align, type) => {
    return [
        {
            'dataIndex': 'mini-progress示例',
            'title': 'mini-progress示例',
            'renderOptions': {
                'renderType': 'mini-progress',
                'progressShowPercent': true,
                'progressPercentPosition': {
                    'align': align,
                    'type': type,
                },
            },
        },
    ];
}
\""",
    Output('table-mini-progress-percent-position-demo', 'columns'),
    [
        Input('table-mini-progress-percent-position-demo-align', 'value'),
        Input('table-mini-progress-percent-position-demo-type', 'value'),
    ],
    prevent_initial_call=True,
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                'align:',
                fac.AntdRadioGroup(
                    id='table-mini-progress-percent-position-demo-align',
                    options=['start', 'center', 'end'],
                    value='end',
                ),
            ]
        ),
        fac.AntdSpace(
            [
                'type:',
                fac.AntdRadioGroup(
                    id='table-mini-progress-percent-position-demo-type',
                    options=['inner', 'outer'],
                    value='inner',
                ),
            ]
        ),
        fac.AntdTable(
            id='table-mini-progress-percent-position-demo',
            locale="en-us",
            columns=[
                {
                    'dataIndex': 'mini-progress Example',
                    'title': 'mini-progress Example',
                    'renderOptions': {
                        'renderType': 'mini-progress',
                        'progressShowPercent': True,
                        'progressPercentPosition': {
                            'align': 'end',
                            'type': 'inner',
                        },
                    },
                },
            ],
            data=[{'mini-progress Example': x} for x in [0, 0.66, 1]],
            bordered=True,
        ),
    ],
    direction='vertical',
    size='small',
    style={'width': '100%'},
)

...

app.clientside_callback(
    \"""
(align, type) => {
    return [
        {
            'dataIndex': 'mini-progress Example',
            'title': 'mini-progress Example',
            'renderOptions': {
                'renderType': 'mini-progress',
                'progressShowPercent': true,
                'progressPercentPosition': {
                    'align': align,
                    'type': type,
                },
            },
        },
    ];
}
\""",
    Output('table-mini-progress-percent-position-demo', 'columns'),
    [
        Input('table-mini-progress-percent-position-demo-align', 'value'),
        Input('table-mini-progress-percent-position-demo-type', 'value'),
    ],
    prevent_initial_call=True,
)
"""
            }
        ]
