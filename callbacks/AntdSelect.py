import time
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('select-demo1-output', 'children'),
    Input('select-demo1', 'value'),
)
def select_demo1(value):

    return f'value: {value}'


@app.callback(
    Output('select-demo2-output', 'children'),
    Input('select-demo2', 'value'),
)
def select_demo2(value):

    return f'value: {value}'


@app.callback(
    Output('select-search-value-demo-output', 'children'),
    Input('select-search-value-demo', 'searchValue')
)
def select_search_value_demo(searchValue):

    return f'searchValue: {searchValue}'


@app.callback(
    Output('select-debounce-search-value-demo-output', 'children'),
    Input('select-debounce-search-value-demo', 'debounceSearchValue')
)
def select_debounce_search_value_demo(debounceSearchValue):

    return f'debounceSearchValue: {debounceSearchValue}'


@app.callback(
    Output('select-auto-spin-remote-load-options', 'options'),
    Input('select-auto-spin-remote-load-options', 'debounceSearchValue')
)
def select_auto_spin_remote_load_options_demo(debounceSearchValue):

    if debounceSearchValue:

        time.sleep(1)

        return [
            {
                'label': f'{debounceSearchValue}模拟选项{i}',
                'value': f'{debounceSearchValue}模拟选项{i}'
            }
            for i in range(1, 6)
        ]

    return []
