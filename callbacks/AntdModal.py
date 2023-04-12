import time
import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('modal-basic-demo', 'visible'),
    Input('modal-basic-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_basic_demo(nClicks):

    return True


@app.callback(
    Output('modal-footer-demo', 'visible'),
    Input('modal-footer-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_footer_demo(nClicks):

    return True


@app.callback(
    Output('modal-custom-button-demo', 'visible'),
    Input('modal-custom-button-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_custom_button_demo(nClicks):

    return True


@app.callback(
    Output('modal-width-demo', 'visible'),
    Input('modal-width-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_width_demo(nClicks):

    return True


@app.callback(
    Output('modal-centered-demo', 'visible'),
    Input('modal-centered-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_centered_demo(nClicks):

    return True


@app.callback(
    Output('modal-loading-demo', 'visible'),
    Input('modal-loading-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_loading_demo(nClicks):

    return True


@app.callback(
    Output('modal-loading-demo', 'confirmLoading'),
    Input('modal-loading-demo', 'okCounts'),
    prevent_initial_call=True
)
def modal_loading_reset(okCounts):

    time.sleep(2)

    return False


@app.callback(
    Output('modal-callback-demo', 'visible'),
    Input('modal-callback-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_callback_demo(nClicks):

    return True


@app.callback(
    Output('modal-callback-demo-output', 'children'),
    [Input('modal-callback-demo', 'okCounts'),
     Input('modal-callback-demo', 'cancelCounts'),
     Input('modal-callback-demo', 'closeCounts')],
    prevent_initial_call=True
)
def handle_modal_callback_demo(okCounts, cancelCounts, closeCounts):

    return json.dumps(
        dict(
            okCounts=okCounts,
            cancelCounts=cancelCounts,
            closeCounts=closeCounts
        ),
        indent=4,
        ensure_ascii=False
    )
