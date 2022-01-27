from flask import request
from datetime import datetime
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('comment-demo', 'children'),
    Input('comment-demo-submit', 'nClicks'),
    [State('comment-demo-input', 'value'),
     State('comment-demo', 'children')],
    prevent_initial_call=True
)
def comment_demo_add_children_callback(nClicks, value, children):
    if value:
        return children + [
            fac.AntdComment(
                authorName=request.remote_addr,
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss'
                },
                commentContent=value
            )
        ] if children else [
            fac.AntdComment(
                authorName=request.remote_addr,
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss'
                },
                commentContent=value
            )
        ]

    else:
        return children
