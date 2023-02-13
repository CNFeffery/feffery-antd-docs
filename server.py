import dash


class CustomDash(dash.Dash):

    def interpolate_index(self, **kwargs):
        # scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'https://unpkg.zhimg.com/')
        # scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'http://npm.elemecdn.com/')
        # scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'https://fastly.jsdelivr.net/npm/')

        scripts = kwargs.pop('scripts')

        return super(CustomDash, self).interpolate_index(scripts=scripts, **kwargs)


app = CustomDash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    extra_hot_reload_paths=[
        './documents'
    ],
    compress=True,
    assets_ignore='dark.css'
)

app.title = 'feffery-antd-components在线文档'

server = app.server
