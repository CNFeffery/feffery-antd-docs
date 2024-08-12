import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    layout,  # noqa: F401
    flex_layout,  # noqa: F401
    label_align_left,  # noqa: F401
    label_wrap,  # noqa: F401
    required,  # noqa: F401
    tooltip,  # noqa: F401
    validate_status,  # noqa: F401
    batch_help,  # noqa: F401
    batch_validate_status,  # noqa: F401
    batch_value,  # noqa: F401
    callback_control_validate,  # noqa: F401
    callback_listen_values,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('常规居中与行内居中。'),
    },
    {
        'path': 'layout',
        'title': '其他布局方式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('layout', code=True),
                '控制表单布局方式。',
            ]
        ),
    },
    {
        'path': 'flex_layout',
        'title': '基于flex布局分配宽度',
        'description': fac.AntdParagraph(
            [
                '基于参数',
                fac.AntdText('labelCol', code=True),
                '、',
                fac.AntdText('wrapperCol', code=True),
                '的',
                fac.AntdText('flex', code=True),
                '子参数，实现对表单标签、控件部分宽度的更灵活分配。',
            ]
        ),
    },
    {
        'path': 'label_align_left',
        'title': '表单项标签左对齐',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('labelAlign', code=True),
                '控制表单项标签对齐方式。',
            ]
        ),
    },
    {
        'path': 'label_wrap',
        'title': '表单项标签超长换行',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('labelWrap', code=True),
                '控制表单项标签是否超长换行。',
            ]
        ),
    },
    {
        'path': 'required',
        'title': '表单项添加必填标识',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('required', code=True),
                '控制表单项标签是否额外添加必填标识。',
            ]
        ),
    },
    {
        'path': 'tooltip',
        'title': '表单项额外提示信息',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('tooltip', code=True),
                '为表单项标签添加额外提示信息。',
            ]
        ),
    },
    {
        'path': 'validate_status',
        'title': '校验状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('validateStatus', code=True),
                '为表单项设置不同的校验状态。',
            ]
        ),
    },
    {
        'path': 'batch_help',
        'title': '批量控制帮助信息',
        'description': fac.AntdParagraph(
            [
                '为具有有效',
                fac.AntdText('id', code=True),
                '的表单设置参数',
                fac.AntdText('enableBatchControl=True', code=True),
                '后，可通过参数',
                fac.AntdText('helps', code=True),
                '批量控制内部各表单项的帮助信息。',
            ]
        ),
    },
    {
        'path': 'batch_validate_status',
        'title': '批量控制校验状态',
        'description': fac.AntdParagraph(
            [
                '为具有有效',
                fac.AntdText('id', code=True),
                '的表单设置参数',
                fac.AntdText('enableBatchControl=True', code=True),
                '后，可通过参数',
                fac.AntdText('validateStatuses', code=True),
                '批量控制内部各表单项的校验状态。',
            ]
        ),
    },
    {
        'path': 'batch_value',
        'title': '批量控制校验状态',
        'description': fac.AntdParagraph(
            [
                '为具有有效',
                fac.AntdText('id', code=True),
                '的表单设置参数',
                fac.AntdText('enableBatchControl=True', code=True),
                '后，可通过参数',
                fac.AntdText('values', code=True),
                '批量控制内部各表单项的值。',
            ]
        ),
    },
    {
        'path': 'callback_control_validate',
        'title': '回调控制表单验证',
        'description': fac.AntdParagraph(
            '配合回调函数，对表单中的各个表单项进行精细化的验证控制。'
        ),
    },
    {
        'path': 'callback_listen_values',
        'title': '回调批量监听表单值',
        'description': fac.AntdParagraph(
            '配合回调函数，对开启批量值控制的表单值进行快捷监听。'
        ),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
