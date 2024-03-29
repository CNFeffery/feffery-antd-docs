import json
import random
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
    Output('table-row-selection-sync-selected-rows-demo', 'data'),
    Input('table-row-selection-sync-selected-rows-demo-update-data', 'nClicks'),
    prevent_initial_call=True
)
def table_row_selection_sync_selected_rows_demo_update_data(nClicks):

    return [
        {
            **{
                f'字段{i}': round(random.uniform(0, 10), 3)
                for i in range(1, 4)
            },
            'key': f'row-{row+1}'
        }
        for row in range(3)
    ]


@app.callback(
    Output('table-row-selection-sync-selected-rows-demo-output', 'children'),
    [Input('table-row-selection-sync-selected-rows-demo', 'selectedRowKeys'),
     Input('table-row-selection-sync-selected-rows-demo', 'selectedRows')]
)
def table_row_selection_sync_selected_rows_demo(selectedRowKeys, selectedRows):

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
    [Input('table-click-event-demo', 'nClicksCell'),
     Input('table-click-event-demo', 'nDoubleClicksCell')],
    [State('table-click-event-demo', 'enableCellClickListenColumns'),
     State('table-click-event-demo', 'recentlyCellClickColumn'),
     State('table-click-event-demo', 'recentlyCellClickRecord'),
     State('table-click-event-demo', 'recentlyCellDoubleClickColumn'),
     State('table-click-event-demo', 'recentlyCellDoubleClickRecord')],
    prevent_initial_call=True
)
def table_click_event_demo(nClicksCell,
                           nDoubleClicksCell,
                           enableCellClickListenColumns,
                           recentlyCellClickColumn,
                           recentlyCellClickRecord,
                           recentlyCellDoubleClickColumn,
                           recentlyCellDoubleClickRecord):

    return json.dumps(
        dict(
            enableCellClickListenColumns=enableCellClickListenColumns,
            nClicksCell=nClicksCell,
            recentlyCellClickColumn=recentlyCellClickColumn,
            recentlyCellClickRecord=recentlyCellClickRecord,
            nDoubleClicksCell=nDoubleClicksCell,
            recentlyCellDoubleClickColumn=recentlyCellDoubleClickColumn,
            recentlyCellDoubleClickRecord=recentlyCellDoubleClickRecord
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
