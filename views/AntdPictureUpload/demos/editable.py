import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdPictureUpload(
        apiUrl='/upload/',
        fileMaxSize=1,
        buttonContent='点击上传图片',
        editable=True,
        editConfig={
            'grid': True,
            'rotate': True,
            'modalTitle': '图片编辑窗口标题示例',
            'modalWidth': 600,
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdPictureUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    buttonContent='点击上传图片',
    editable=True,
    editConfig={
        'grid': True,
        'rotate': True,
        'modalTitle': '图片编辑窗口标题示例',
        'modalWidth': 600,
    },
)
"""
    }
]
