from dash import html
import feffery_markdown_components as fmc


def render(version: str):
    """渲染更新日志页面"""

    with open('./changelogs/{}.md'.format(version), 'r', encoding='utf-8') as f:
        changelog = f.read()

    return html.Div(
        fmc.FefferyMarkdown(markdownStr=changelog),
        style={'padding': '50px 4vw'},
    )
