import feffery_antd_components as fac
import numpy as np
from dash import dcc
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdStatistic(
            id='statistic-demo',
            precision=2,
            title='XX股份实时股价',
            value=675.32,
            valueStyle={'color': '#cf1322'},
            prefix=fac.AntdIcon(icon='antd-rise'),
        ),
        dcc.Interval(id='statistic-interval-demo', n_intervals=0),
    ]
    return demo_contents


@app.callback(
    [
        Output('statistic-demo', 'value'),
        Output('statistic-demo', 'prefix'),
        Output('statistic-demo', 'valueStyle'),
    ],
    Input('statistic-interval-demo', 'n_intervals'),
    State('statistic-demo', 'value'),
)
def statistic_demo_callback(n_intervals, value):
    new_value = value + np.random.randn()

    if new_value >= value:
        return [new_value, fac.AntdIcon(icon='antd-rise'), {'color': '#cf1322'}]

    else:
        return [new_value, fac.AntdIcon(icon='antd-fall'), {'color': '#3f8600'}]


code_string = [
    {
        'code': """
fac.AntdStatistic(
    id='statistic-demo',
    precision=2,
    title='XX股份实时股价',
    value=675.32,
    valueStyle={'color': '#cf1322'},
    prefix=fac.AntdIcon(icon='antd-rise'),
),
dcc.Interval(id='statistic-interval-demo', n_intervals=0),

...

@app.callback(
    [
        Output('statistic-demo', 'value'),
        Output('statistic-demo', 'prefix'),
        Output('statistic-demo', 'valueStyle'),
    ],
    Input('statistic-interval-demo', 'n_intervals'),
    State('statistic-demo', 'value'),
)
def statistic_demo_callback(n_intervals, value):
    new_value = value + np.random.randn()

    if new_value >= value:
        return [new_value, fac.AntdIcon(icon='antd-rise'), {'color': '#cf1322'}]

    else:
        return [new_value, fac.AntdIcon(icon='antd-fall'), {'color': '#3f8600'}]
"""
    }
]
