import re
import dash

from config import DeployConfig, AppConfig


class CustomDash(dash.Dash):
    '''
    自定义Dash实例，用于改造默认的CDN访问行为
    '''

    def interpolate_index(self, **kwargs):

        scripts = kwargs.pop('scripts')

        # 提取scripts中部分符合条件的外部js资源
        external_scripts = re.findall(
            '(<script src="http.*?"></script>)',
            scripts
        )

        # 将原有的script标签内容替换为带备用地址错误切换的版本
        for external_script in external_scripts:
            scripts = scripts.replace(
                external_script,
                '''<script src="{}" onerror='this.remove(); let fallbackScript = document.createElement("script"); fallbackScript.src = "{}"; document.querySelector("head").prepend(fallbackScript);'></script>'''.format(
                    re.findall('"(.*?)"', external_script)[0]
                    .replace('https://unpkg.com/', 'https://npm.onmicrosoft.cn/'),
                    re.findall('"(.*?)"', external_script)[0]
                )
            )

        scripts = (
            '''
<script>
const requiredModules = {};
{}
</script>
'''.format(
                str(DeployConfig.cdn_modules),
                open('./public/handleModulesLoadError.js', encoding='utf-8')
                .read()
            ) +
            scripts
        )

        return super(CustomDash, self).interpolate_index(scripts=scripts, **kwargs)


app = CustomDash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    extra_hot_reload_paths=[
        './documents',
        './change_logs'
    ],
    compress=True
)

app.title = AppConfig.title

server = app.server
