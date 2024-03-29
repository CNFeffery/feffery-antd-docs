import uuid
import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('dropdown-free-position-demo-container', 'children'),
    Input('dropdown-free-position-demo-trigger', 'contextMenuEvent'),
    prevent_initial_call=True
)
def dropdown_free_position_demo(contextMenuEvent):

    if contextMenuEvent:

        return fac.AntdDropdown(
            key=str(uuid.uuid4()),
            visible=True,
            freePosition=True,
            freePositionStyle={
                'left': contextMenuEvent['clientX'],
                'top': contextMenuEvent['clientY']
            },
            menuItems=[
                {
                    'title': f'右键菜单选项{i}',
                    'key': f'右键菜单选项{i}'
                }
                for i in range(1, 6)
            ],
            trigger='click'
        )


@app.callback(
    Output('dropdown-demo-output', 'children'),
    [Input('dropdown-demo', 'clickedKey'),
     Input('dropdown-demo', 'nClicks')],
    prevent_initial_call=True
)
def dropdown_demo_callback(clickedKey, nClicks):
    return [
        fac.AntdText('clickedKey: ', strong=True),
        fac.AntdText(clickedKey),
        fac.AntdText('　nClicks: ', strong=True),
        fac.AntdText(nClicks)
    ]
