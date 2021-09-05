import dash
import dash_html_components as html
import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('table-demo-output', 'children'),
    [Input('table-demo', 'currentData'),
     Input('table-demo', 'recentlyChangedRow'),
     Input('table-demo', 'sorter'),
     Input('table-demo', 'filter'),
     Input('table-demo', 'pagination')],
    prevent_initial_call=True
)
def table_callback_demo(currentData,
                        recentlyChangedRow,
                        sorter,
                        filter,
                        pagination):
    import time
    time.sleep(1)

    ctx = dash.callback_context

    return [
        fac.AntdTitle('本次回调由{}所触发'.format(ctx.triggered[0]['prop_id'].split('.')[-1]), level=3),
        fac.AntdDivider(),

        fac.AntdTitle('currentData：', level=5),
        html.Pre(str(currentData)),

        fac.AntdTitle('recentlyChangedRow：', level=5),
        html.Pre(str(recentlyChangedRow)),

        fac.AntdTitle('sorter：', level=5),
        html.Pre(str(sorter)),

        fac.AntdTitle('filter：', level=5),
        html.Pre(str(filter)),

        fac.AntdTitle('pagination：', level=5),
        html.Pre(str(pagination))
    ]
