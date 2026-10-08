import os
import copy
import re
from string import Formatter
from functools import wraps
from flask import request, has_request_context
from dash.development.base_component import Component
from feffery_dash_utils.i18n_utils import Translator


def get_current_locale() -> str:
    """获取当前国际化语种，缺省或无效 Cookie 使用中文。"""
    locale = (
        request.cookies.get('dash-i18n', 'zh-cn')
        if has_request_context()
        else 'zh-cn'
    )
    return locale if locale in ('zh-cn', 'en-us') else 'zh-cn'


translator = Translator(
    translations=[
        # 全局无主题文案
        './public/locales.json',
        # 各组件文档主题文案
        *[
            os.path.join('./public/topic_locales', path)
            for path in sorted(os.listdir('./public/topic_locales'))
            if path.endswith('.json')
        ],
    ],
    get_current_locale=get_current_locale,
)

# 只转换展示属性，保留 id、key、value、回调数据及源代码。
DISPLAY_PROPS = frozenset(
    {
        'children',
        'title',
        'label',
        'description',
        'message',
        'content',
        'placeholder',
        'tooltip',
        'subTitle',
        'okText',
        'cancelText',
        'text',
        'commentContent',
        'authorName',
        'beforeIcon',
        'afterIcon',
        'searchPlaceholder',
        'notFoundContent',
        'emptyDescription',
        'checkedChildren',
        'unCheckedChildren',
        'addonBefore',
        'addonAfter',
        'prefix',
        'suffix',
        'help',
        'extra',
        'footer',
        'header',
        'ribbon',
        'confirmText',
        'resetText',
        'unit',
        'suffixText',
        'prefixText',
        'alt',
        'checkedContent',
        'unCheckedContent',
        'buttonContent',
        'hint',
        'failedTooltipInfo',
        'loadingOkText',
        'titleTooltip',
        'tooltips',
        'tooltipPrefix',
        'tooltipSuffix',
        'modalTitle',
        'pending',
        'operations',
        'titles',
    }
)
STRUCTURED_PROPS = frozenset(
    {
        'items',
        'options',
        'treeData',
        'menuItems',
        'linkDict',
        'columns',
        'dataSource',
        'tabs',
        'steps',
        'links',
        'titlePopoverInfo',
    }
)
OPAQUE_PROPS = frozenset(
    {
        'id',
        'key',
        'name',
        'value',
        'defaultValue',
        'selectedKeys',
        'checkedKeys',
        'expandedKeys',
        'checkedValue',
        'selectedRowKeys',
        'style',
        'styles',
        'className',
        'classNames',
        'codeString',
        'jsString',
        'batchPropsValues',
        'batchPropsNames',
        'data',
        'record',
        'selectedRows',
        'formValues',
        'initialValues',
        'href',
        'src',
        'uploadId',
        'dataIndex',
        'targetId',
        'parent',
        'defaultActiveKey',
        'disabledTabKeys',
        'url',
        'image',
        'fallback',
        'rule',
        'countFormat',
    }
)


def _compile_templates():
    templates = []
    for source, translations in translator.translations['demo_templates'][
        'zh-cn'
    ].items():
        pattern = []
        for literal, field, _, _ in Formatter().parse(source):
            pattern.append(re.escape(literal))
            if field is not None:
                pattern.append('(.*?)')
        templates.append(
            (re.compile(''.join(pattern), re.S), translations['en-us'])
        )
    # Prefer specific templates over broad ones such as “节点{0}”.
    return sorted(
        templates, key=lambda item: len(item[0].pattern), reverse=True
    )


_visible_templates = _compile_templates()


def rich_text_source(value):
    """将简单富文本段落映射为稳定的 Markdown 翻译键。"""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        parts = [rich_text_source(item) for item in value]
        return (
            ''.join(parts) if all(part is not None for part in parts) else None
        )
    if isinstance(value, Component) and value._type == 'AntdText':
        text = rich_text_source(getattr(value, 'children', ''))
        if text is None:
            return None
        for prop, marker in [('code', '`'), ('strong', '**'), ('italic', '*')]:
            if getattr(value, prop, False):
                text = marker + text + marker
        return text
    return None


def translate_visible_text(value: str) -> str:
    """翻译示例中的显示文案，运行时不请求任何外部翻译服务。"""
    if get_current_locale() != 'en-us':
        return value
    contents = translator.translations['demo_text']['zh-cn']
    if value in contents:
        return contents[value]['en-us']
    if not re.search(r'[\u3400-\u9fff]', value):
        return value
    if '```' in value:
        return value
    for phrase in ('示例内容', '内容示例', '选择卡片示例'):
        count, remainder = divmod(len(value), len(phrase))
        if count and not remainder and value == phrase * count:
            return (contents[phrase]['en-us'] + ' ') * count
    for pattern, target in _visible_templates:
        match = pattern.fullmatch(value)
        if match:
            # 动态片段可能来自用户输入或回调数据，只翻译模板本身。
            return target.format(*match.groups())

    def translate_fragment(match):
        source = match.group()
        if source in contents:
            return contents[source]['en-us']
        for phrase in ('示例内容', '内容示例', '选择卡片示例'):
            count, remainder = divmod(len(source), len(phrase))
            if count and not remainder and source == phrase * count:
                return (contents[phrase]['en-us'] + ' ') * count
        # 处理 join() 产生的演示文案，各片段仍使用静态翻译资源。
        return re.sub(
            r'[\u3400-\u9fff]+|[，。；：！？、]',
            lambda part: contents.get(part.group(), {}).get(
                'en-us',
                {
                    '，': ', ',
                    '。': '. ',
                    '；': '; ',
                    '：': ': ',
                    '！': '!',
                    '？': '?',
                    '、': ', ',
                }.get(part.group(), part.group()),
            ),
            source,
        )

    # f-string 的静态中文片段，如“点击次数：”，也从同一资源提取。
    return re.sub(
        r'[\u3400-\u9fff][\u3400-\u9fff，。；：！？、（）]*',
        translate_fragment,
        value,
    )


def _localize_options(value):
    if isinstance(value, list):
        value = [
            {'label': translate_visible_text(item), 'value': item}
            if isinstance(item, str) and translate_visible_text(item) != item
            else item
            for item in value
        ]
    return localize_component(value, display=False)


def localize_component(value, display=True):
    """复制并翻译组件树中的展示字段，不修改原始组件或业务数据。"""
    if get_current_locale() != 'en-us':
        return value
    if isinstance(value, Component):
        result = copy.copy(value)
        if value._type == 'AntdParagraph' and hasattr(value, 'children'):
            source = rich_text_source(value.children)
            contents = translator.translations.get('advanced_usage', {}).get(
                'zh-cn', {}
            )
            if source in contents:
                from utils.doc_renderer import MarkdownRenderer

                rendered = MarkdownRenderer().render(contents[source]['en-us'])
                result.children = rendered[0].children
                return result
        for prop in value._prop_names:
            if prop not in OPAQUE_PROPS and hasattr(value, prop):
                original = getattr(value, prop)
                if prop == 'options' and value._type in {
                    'AntdSelect',
                    'AntdRadioGroup',
                    'AntdCheckboxGroup',
                    'AntdSegmented',
                }:
                    setattr(result, prop, _localize_options(original))
                    continue
                setattr(
                    result,
                    prop,
                    localize_component(original, prop in DISPLAY_PROPS),
                )
        return result
    if isinstance(value, (list, tuple)):
        result = [localize_component(item, display) for item in value]
        return tuple(result) if isinstance(value, tuple) else result
    if isinstance(value, dict):
        return {
            key: item
            if key in OPAQUE_PROPS
            else localize_component(item, key in DISPLAY_PROPS)
            for key, item in value.items()
        }
    if display and isinstance(value, str):
        return translate_visible_text(value)
    return value


def localized_output(function):
    """为渲染函数添加示例文案翻译。"""

    @wraps(function)
    def wrapped(*args, **kwargs):
        return localize_component(function(*args, **kwargs))

    return wrapped


def localized_callback(properties):
    """只翻译回调的展示属性输出，其他输出保持原样。"""

    def decorate(function):
        @wraps(function)
        def wrapped(*args, **kwargs):
            result = function(*args, **kwargs)
            if len(properties) == 1:
                prop = properties[0]
                if prop == 'options' and get_current_locale() == 'en-us':
                    return _localize_options(result)
                return (
                    localize_component(result, prop in DISPLAY_PROPS)
                    if prop in DISPLAY_PROPS | STRUCTURED_PROPS
                    else result
                )
            if not isinstance(result, (list, tuple)) or len(result) != len(
                properties
            ):
                return result
            values = [
                _localize_options(item)
                if prop == 'options' and get_current_locale() == 'en-us'
                else localize_component(item, prop in DISPLAY_PROPS)
                if prop in DISPLAY_PROPS | STRUCTURED_PROPS
                else item
                for prop, item in zip(properties, result)
            ]
            return tuple(values) if isinstance(result, tuple) else values

        return wrapped

    return decorate
