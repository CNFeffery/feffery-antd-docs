from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    disabled,  # noqa: F401
    list_max_length,  # noqa: F401
    file_types,  # noqa: F401
    multiple_upload,  # noqa: F401
    directory_upload,  # noqa: F401
    failed_tooltip,  # noqa: F401
    confirm_before_delete,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '点击目标区域或拖拽文件至目标区域触发文件上传功能。',
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': '设置参数`disabled=True`开启禁用状态。',
    },
    {
        'path': 'list_max_length',
        'title': '限制上传列表记录数量',
        'description': '通过参数`fileListMaxLength`限制上传列表中的文件上传记录最大数量。',
    },
    {
        'path': 'file_types',
        'title': '限制上传文件类型',
        'description': '通过参数`fileTypes`限制可上传的文件类型。',
    },
    {
        'path': 'multiple_upload',
        'title': '多文件上传',
        'description': '设置参数`multiple=True`后可一次性上传多个文件。',
    },
    {
        'path': 'directory_upload',
        'title': '文件夹上传',
        'description': '设置参数`directory=True`后可选择文件夹进行内部文件的批量上传。',
    },
    {
        'path': 'failed_tooltip',
        'title': '自定义失败文件提示',
        'description': '设置参数`failedTooltipInfo`进行上传失败文件的错误提示信息自定义。',
    },
    {
        'path': 'confirm_before_delete',
        'title': '删除前确认',
        'description': '设置参数`confirmBeforeDelete=True`为已上传文件记录的删除操作添加二次确认功能。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': None,
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
