import dash

app = dash.Dash(
    __name__,
    external_stylesheets=[
        'https://cdn.staticfile.org/twitter-bootstrap/4.5.2/css/bootstrap.min.css'
    ],
    suppress_callback_exceptions=True,
    routes_pathname_prefix='/feffery-antd-docs/'
)

app.title = 'feffery-antd-components说明文档'

server = app.server
