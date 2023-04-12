import numpy as np
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    [Output('statistic-demo', 'value'),
     Output('statistic-demo', 'prefix'),
     Output('statistic-demo', 'valueStyle')],
    Input('statistic-interval-demo', 'n_intervals'),
    State('statistic-demo', 'value')
)
def statistic_demo_callback(n_intervals, value):
    new_value = value + np.random.randn()

    if new_value >= value:
        return [
            new_value,
            fac.AntdIcon(
                icon='antd-rise'
            ),
            {
                'color': '#cf1322'
            }
        ]

    else:
        return [
            new_value,
            fac.AntdIcon(
                icon='antd-fall'
            ),
            {
                'color': '#3f8600'
            }
        ]
