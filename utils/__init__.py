import os
import re
import mistune
from flask import request
from mistune.core import BlockState
from dash.dependencies import Component
from mistune.renderers.markdown import MarkdownRenderer

# 国际化
from i18n import translator

markdown_parser = mistune.create_markdown(renderer='ast')
markdown_renderer = MarkdownRenderer()


def parse_component_props(component: Component) -> str:
    """解析转换指定组件的参数说明"""

    # 获取当前国际化语种
    current_locale = request.cookies.get(translator.cookie_name, 'zh-cn')

    if current_locale == 'zh-cn':
        raw_docstring = component.__doc__ + '\n'
    elif current_locale == 'en-us':
        # 检查目标英文文档文件是否存在
        if f'{component.__name__}.md' in os.listdir(
            './public/api_documents/en_us'
        ):
            with open(
                './public/api_documents/en_us/{}.md'.format(component.__name__),
                encoding='utf-8',
            ) as f:
                raw_docstring = f.read()
        else:
            raw_docstring = component.__doc__ + '\n'

    # 去除开头多余内容
    raw_docstring = re.sub(
        '^.*?Keyword arguments\:',
        '',
        raw_docstring,
        flags=re.S,
    )

    raw_docstring_parts = markdown_parser.parse(raw_docstring)[0]

    # 剔除无关属性说明
    for i, part in enumerate(raw_docstring_parts):
        if part['type'] == 'list':
            raw_docstring_parts[i]['children'] = [
                item
                for item in part['children']
                if not re.match(
                    '^loading_state',
                    item['children'][0]['children'][0].get('raw', ''),
                )
            ]

    # 还原markdown内容
    raw_docstring = markdown_renderer(raw_docstring_parts, state=BlockState())

    # 修正多级列表换行显示
    raw_docstring = raw_docstring.replace(':\n', ':\n\n')

    if current_locale == 'zh-cn':
        # 修正默认值说明行
        raw_docstring = raw_docstring.replace('默认值：', '，默认值：')

        # 移除末端英文句号
        raw_docstring = raw_docstring.replace('.\n', '\n')

        # 替换过长的英文类型描述
        raw_docstring = raw_docstring.replace(
            'a list of or a singular dash component', '单个或多个组件'
        )
        raw_docstring = raw_docstring.replace(
            ' is a dict with keys:', '是支持下列键值对的字典：'
        )
        raw_docstring = raw_docstring.replace(
            'a value equal to: ', '可选项有：'
        )

    return raw_docstring


def generate_shortcut_panel_data(raw_menu_data: list) -> list:
    """基于侧边菜单栏生成快捷搜索面板所需数据结构"""

    data = []
    for level1 in raw_menu_data:
        if level1['component'] == 'ItemGroup':
            for level2 in level1['children']:
                if level2['component'] == 'Item':
                    data.append(
                        {
                            'id': level2['props']['key'],
                            'title': level2['props']['title'],
                            'section': level1['props']['title'],
                            'handler': '() => window.open("{}")'.format(
                                level2['props']['href']
                            ),
                        }
                    )

                elif level2['component'] == 'SubMenu':
                    for level3 in level2['children']:
                        if level3['component'] == 'Item':
                            data.append(
                                {
                                    'id': level3['props']['key'],
                                    'title': level3['props']['title'],
                                    'section': '{} / {}'.format(
                                        level1['props']['title'],
                                        level2['props']['title'],
                                    ),
                                    'handler': '() => window.open("{}")'.format(
                                        level3['props']['href']
                                    ),
                                }
                            )
                        elif level3['component'] == 'SubMenu':
                            for level4 in level3['children']:
                                if level3['props']['title'].startswith(
                                    'AntdTable'
                                ):
                                    data.append(
                                        {
                                            'id': level4['props']['key'],
                                            'title': translator.t(
                                                'AntdTable 表格：'
                                            )
                                            + level4['props']['title'],
                                            'section': '{} / {} / {}'.format(
                                                level1['props']['title'],
                                                level2['props']['title'],
                                                level3['props']['title'],
                                            ),
                                            'handler': '() => window.open("{}")'.format(
                                                level4['props']['href']
                                            ),
                                        }
                                    )
                                else:
                                    data.append(
                                        {
                                            'id': level4['props']['key'],
                                            'title': level4['props']['title'],
                                            'section': '{} / {} / {}'.format(
                                                level1['props']['title'],
                                                level2['props']['title'],
                                                level3['props']['title'],
                                            ),
                                            'handler': '() => window.open("{}")'.format(
                                                level4['props']['href']
                                            ),
                                        }
                                    )

    return data
