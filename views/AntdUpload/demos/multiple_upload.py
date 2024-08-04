import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdUpload(
        apiUrl='/upload/',
        fileMaxSize=1,
        multiple=True,
        buttonContent='点击上传多个文件',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    multiple=True,
    buttonContent='点击上传多个文件',
)
"""
    }
]
