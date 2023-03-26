from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('config-provider-primary-color-demo', 'primaryColor'),
    Input('config-provider-primary-color', 'color')
)
def config_provider_primary_color_demo(color):

    return color


@app.callback(
    Output('config-provider-component-disabled-demo', 'componentDisabled'),
    Input('config-provider-component-disabled', 'checked')
)
def config_provider_component_disabled_demo(checked):

    return checked


@app.callback(
    Output('config-provider-component-size-demo', 'componentSize'),
    Input('config-provider-component-size', 'value'),
    prevent_initial_call=True
)
def config_provider_component_size_demo(value):

    return value


@app.callback(
    Output('config-provider-locale-demo', 'locale'),
    Input('config-provider-locale', 'value'),
    prevent_initial_call=True
)
def config_provider_locale_demo(value):

    return value
