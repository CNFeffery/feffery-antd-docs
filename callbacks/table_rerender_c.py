import json
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('table-rerender-button-demo-output', 'children'),
    Input('table-rerender-button-demo', 'nClicksButton'),
    [State('table-rerender-button-demo', 'clickedContent'),
     State('table-rerender-button-demo', 'clickedCustom'),
     State('table-rerender-button-demo', 'recentlyButtonClickedDataIndex'),
     State('table-rerender-button-demo', 'recentlyButtonClickedRow')],
    prevent_initial_call=True
)
def table_rerender_button_demo(nClicksButton,
                               clickedContent,
                               clickedCustom,
                               recentlyButtonClickedDataIndex,
                               recentlyButtonClickedRow):

    return json.dumps(
        dict(
            nClicksButton=nClicksButton,
            clickedContent=clickedContent,
            clickedCustom=clickedCustom,
            recentlyButtonClickedDataIndex=recentlyButtonClickedDataIndex,
            recentlyButtonClickedRow=recentlyButtonClickedRow
        ),
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    Output('table-rerender-checkbox-demo-output', 'children'),
    [Input('table-rerender-checkbox-demo', 'recentlyCheckedLabel'),
     Input('table-rerender-checkbox-demo', 'recentlyCheckedDataIndex'),
     Input('table-rerender-checkbox-demo', 'recentlyCheckedStatus'),
     Input('table-rerender-checkbox-demo', 'recentlyCheckedRow')],
    prevent_initial_call=True
)
def table_rerender_checkbox_demo(recentlyCheckedLabel,
                                 recentlyCheckedDataIndex,
                                 recentlyCheckedStatus,
                                 recentlyCheckedRow):

    return json.dumps(
        dict(
            recentlyCheckedLabel=recentlyCheckedLabel,
            recentlyCheckedDataIndex=recentlyCheckedDataIndex,
            recentlyCheckedStatus=recentlyCheckedStatus,
            recentlyCheckedRow=recentlyCheckedRow
        ),
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    Output('table-rerender-switch-demo-output', 'children'),
    [Input('table-rerender-switch-demo', 'recentlySwitchDataIndex'),
     Input('table-rerender-switch-demo', 'recentlySwitchStatus'),
     Input('table-rerender-switch-demo', 'recentlySwitchRow')],
    prevent_initial_call=True
)
def table_rerender_switch_demo(recentlySwitchDataIndex,
                               recentlySwitchStatus,
                               recentlySwitchRow):

    return json.dumps(
        dict(
            recentlySwitchDataIndex=recentlySwitchDataIndex,
            recentlySwitchStatus=recentlySwitchStatus,
            recentlySwitchRow=recentlySwitchRow
        ),
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    Output('table-rerender-dropdown-demo-output', 'children'),
    Input('table-rerender-dropdown-demo', 'nClicksDropdownItem'),
    [State('table-rerender-dropdown-demo', 'recentlyClickedDropdownItemTitle'),
     State('table-rerender-dropdown-demo',
           'recentlyDropdownItemClickedDataIndex'),
     State('table-rerender-dropdown-demo', 'recentlyDropdownItemClickedRow')],
    prevent_initial_call=True
)
def table_rerender_dropdown_demo(nClicksDropdownItem,
                                 recentlyClickedDropdownItemTitle,
                                 recentlyDropdownItemClickedDataIndex,
                                 recentlyDropdownItemClickedRow):

    return json.dumps(
        dict(
            nClicksDropdownItem=nClicksDropdownItem,
            recentlyClickedDropdownItemTitle=recentlyClickedDropdownItemTitle,
            recentlyDropdownItemClickedDataIndex=recentlyDropdownItemClickedDataIndex,
            recentlyDropdownItemClickedRow=recentlyDropdownItemClickedRow
        ),
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    Output('table-rerender-select-demo-output', 'children'),
    [Input('table-rerender-select-demo', 'recentlySelectRow'),
     Input('table-rerender-select-demo', 'recentlySelectDataIndex'),
     Input('table-rerender-select-demo', 'recentlySelectValue')],
    prevent_initial_call=True
)
def table_rerender_select_demo(recentlySelectRow,
                               recentlySelectDataIndex,
                               recentlySelectValue):

    return json.dumps(
        dict(
            recentlySelectRow=recentlySelectRow,
            recentlySelectDataIndex=recentlySelectDataIndex,
            recentlySelectValue=recentlySelectValue
        ),
        indent=4,
        ensure_ascii=False
    )
