import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdCheckbox(
            id='checkbox-demo-client-side',
            label='全选',
            style={'marginRight': '8px'},
        ),
        fac.AntdCheckboxGroup(
            id='checkbox-group-demo-client-side',
            options=[
                {'label': f'选项{i}', 'value': f'选项{i}'} for i in range(5)
            ],
        ),
    ]

    return demo_contents


app.clientside_callback(
    """(checked, value, options) => {
        let ctx = dash_clientside.callback_context;
        value = value || []
        if ( ctx?.triggered[0].prop_id === 'checkbox-group-demo-client-side.value' ) {
            return [
                value.length === options.length ? true : false,
                value,
                value.length > 0 && value.length < options.length ? true : false
            ]
        } else if ( ctx?.triggered[0].prop_id === 'checkbox-demo-client-side.checked' ) {
            return [
                checked,
                checked ? options.map(item => item.value) : [],
                !checked && value.length > 0 && value.length < options.length ? true : false
            ]
        }
        return dash_clientside.no_update;
    }""",
    [
        Output('checkbox-demo-client-side', 'checked'),
        Output('checkbox-group-demo-client-side', 'value'),
        Output('checkbox-demo-client-side', 'indeterminate'),
    ],
    [
        Input('checkbox-demo-client-side', 'checked'),
        Input('checkbox-group-demo-client-side', 'value'),
    ],
    State('checkbox-group-demo-client-side', 'options'),
    prevent_initial_call=True,
)

code_string = [
    {
        'code': '''
[
    fac.AntdCheckbox(
        id='checkbox-demo-client-side',
        label='全选',
        style={'marginRight': '8px'},
    ),
    fac.AntdCheckboxGroup(
        id='checkbox-group-demo-client-side',
        options=[
            {'label': f'选项{i}', 'value': f'选项{i}'} for i in range(5)
        ],
    ),
]

...

app.clientside_callback(
    """(checked, value, options) => {
        let ctx = dash_clientside.callback_context;
        value = value || []
        if ( ctx?.triggered[0].prop_id === 'checkbox-group-demo-client-side.value' ) {
            return [
                value.length === options.length ? true : false,
                value,
                value.length > 0 && value.length < options.length ? true : false
            ]
        } else if ( ctx?.triggered[0].prop_id === 'checkbox-demo-client-side.checked' ) {
            return [
                checked,
                checked ? options.map(item => item.value) : [],
                !checked && value.length > 0 && value.length < options.length ? true : false
            ]
        }
        return dash_clientside.no_update;
    }""",
    [
        Output('checkbox-demo-client-side', 'checked'),
        Output('checkbox-group-demo-client-side', 'value'),
        Output('checkbox-demo-client-side', 'indeterminate'),
    ],
    [
        Input('checkbox-demo-client-side', 'checked'),
        Input('checkbox-group-demo-client-side', 'value'),
    ],
    State('checkbox-group-demo-client-side', 'options'),
    prevent_initial_call=True,
)
'''
    }
]
