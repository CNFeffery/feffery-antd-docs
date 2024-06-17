import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDraggerUpload(
        apiUrl='/upload/',
        fileMaxSize=1,
        fileTypes=['csv', 'txt'],
        text='请上传.csv或.txt文件',
        hint='点击或拖拽文件至此处进行上传',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    fileTypes=['csv', 'txt'],
    text='请上传.csv或.txt文件',
    hint='点击或拖拽文件至此处进行上传',
)
"""
    }
]
