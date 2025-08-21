import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
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


code_string = [
    {
        'code': '''
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
'''
    }
]
