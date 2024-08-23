from dash import html
import feffery_markdown_components as fmc

from i18n import get_current_locale


def render(version: str):
    """渲染更新日志页面"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        with open(
            './changelogs/{}.md'.format(version), 'r', encoding='utf-8'
        ) as f:
            changelog = f.read()
    elif current_locale == 'en-us':
        with open(
            './changelogs/en_us/{}.md'.format(version), 'r', encoding='utf-8'
        ) as f:
            changelog = f.read()

    return html.Div(
        fmc.FefferyMarkdown(markdownStr=changelog),
        style={'padding': '50px 4vw'},
    )
