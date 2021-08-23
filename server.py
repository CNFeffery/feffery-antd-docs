import dash

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True
)

app.title = 'feffery-antd-components在线文档'

server = app.server
