import json
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('table-row-selection-demo-output', 'children'),
    [Input('table-row-selection-demo', 'selectedRowKeys'),
     Input('table-row-selection-demo', 'selectedRows')],
    prevent_initial_call=True
)
def table_row_selection_demo(selectedRowKeys, selectedRows):

    return json.dumps(
        dict(
            selectedRowKeys=selectedRowKeys,
            selectedRows=selectedRows
        ),
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    Output('table-sort-demo-output', 'children'),
    Input('table-sort-demo', 'sorter'),
    prevent_initial_call=True
)
def table_sort_demo(sorter):

    return json.dumps(
        sorter,
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    Output('table-filter-demo-output', 'children'),
    Input('table-filter-demo', 'filter'),
    prevent_initial_call=True
)
def table_filter_demo(filter_):

    return json.dumps(
        filter_,
        indent=4,
        ensure_ascii=False
    )


@app.callback(
    Output('table-click-event-demo-output', 'children'),
    Input('table-click-event-demo', 'nClicksCell'),
    [State('table-click-event-demo', 'enableCellClickListenColumns'),
     State('table-click-event-demo', 'recentlyCellClickColumn'),
     State('table-click-event-demo', 'recentlyCellClickRecord')],
    prevent_initial_call=True
)
def table_click_event_demo(nClicksCell,
                           enableCellClickListenColumns,
                           recentlyCellClickColumn,
                           recentlyCellClickRecord):

    return json.dumps(
        dict(
            nClicksCell=nClicksCell,
            enableCellClickListenColumns=enableCellClickListenColumns,
            recentlyCellClickColumn=recentlyCellClickColumn,
            recentlyCellClickRecord=recentlyCellClickRecord
        ),
        indent=4,
        ensure_ascii=False
    )


# 为方便演示，这里使用浏览器端回调
app.clientside_callback(
    '''( recentlyMouseEnterColumnDataIndex,
         recentlyMouseEnterRowKey,
         recentlyMouseEnterRow ) => {
        return JSON.stringify(
            {
                recentlyMouseEnterColumnDataIndex,
                recentlyMouseEnterRowKey,
                recentlyMouseEnterRow
            },
            null,
            4
        );
    }''',
    Output('table-hover-event-demo-output', 'children'),
    [Input('table-hover-event-demo', 'recentlyMouseEnterColumnDataIndex'),
     Input('table-hover-event-demo', 'recentlyMouseEnterRowKey'),
     Input('table-hover-event-demo', 'recentlyMouseEnterRow')],
    prevent_initial_call=True
)
