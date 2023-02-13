import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('input-demo-output', 'children'),
    [Input(f'input-{mode}-mode-demo', 'value')
     for mode in ['default', 'search', 'text-area', 'password']]
)
def input_mode_demo(*value_list):

    return fac.AntdSpace(
        [
            fac.AntdText(
                f'{mode}模式value：{value_list[i]}'
            )
            for i, mode in enumerate(
                ['default', 'search', 'text-area', 'password']
            )
        ],
        direction='vertical'
    )


@app.callback(
    Output('input-debounce-demo-output', 'children'),
    Input('input-debounce-demo', 'debounceValue')
)
def input_debounce_demo(debounceValue):

    return f'debounceValue: {debounceValue}'


@app.callback(
    Output('input-enter-demo-output', 'children'),
    Input('input-enter-demo', 'nSubmit')
)
def input_enter_dmeo(nSubmit):

    return f'nSubmit: {nSubmit}'


@app.callback(
    Output('input-search-demo-output', 'children'),
    Input('input-search-demo', 'nClicksSearch')
)
def input_search_dmeo(nClicksSearch):

    return f'nClicksSearch: {nClicksSearch}'
