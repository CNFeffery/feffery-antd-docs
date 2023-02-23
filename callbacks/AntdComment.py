import dash
import uuid
from datetime import datetime
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, ALL

from server import app


@app.callback(
    [Output('comment-demo', 'children'),
     Output('comment-demo-input', 'value')],
    [Input('comment-demo-submit', 'nClicks'),
     Input({'type': 'comment-demo-children', 'index': ALL}, 'deleteClicks')],
    [State('comment-demo-input', 'value'),
     State('comment-demo', 'children')],
    prevent_initial_call=True
)
def comment_demo_add_children_callback(nClicks, deleteClicks, value, children):
    # 本次回调由子回复删除功能触发
    if 'deleteClicks' in dash.callback_context.triggered[0]['prop_id']:
        triggerIndex = eval(dash.callback_context.triggered[0]['prop_id'].replace(
            '.deleteClicks', ''))['index']

        return [
            child for child in children if child['props']['id']['index'] != triggerIndex
        ], dash.no_update

    if value:
        return children + [
            fac.AntdComment(
                id={
                    'type': 'comment-demo-children',
                    'index': str(uuid.uuid4())
                },
                authorName='dash学习者',
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss'
                },
                commentContent=value,
                showReply=False,
                showDelete=True
            )
        ] if children else [
            fac.AntdComment(
                id={
                    'type': 'comment-demo-children',
                    'index': str(uuid.uuid4())
                },
                authorName='dash学习者',
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss'
                },
                commentContent=value,
                showReply=False,
                showDelete=True
            )
        ], None

    else:
        return children, None
