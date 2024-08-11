import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdPictureUpload(
        apiUrl='/upload/',
        fileMaxSize=1,
        buttonContent='点击上传图片',
        defaultFileList=[
            {
                'name': 'feffery-添加好友二维码.jpg',
                'status': 'done',
                'url': '/assets/imgs/index/feffery-添加好友二维码.jpg',
            }
            for i in range(1, 6)
        ],
        confirmBeforeDelete=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdPictureUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    buttonContent='点击上传图片',
    defaultFileList=[
        {
            'name': 'feffery-添加好友二维码.jpg',
            'status': 'done',
            'url': '/assets/imgs/index/feffery-添加好友二维码.jpg',
        }
        for i in range(1, 6)
    ],
    confirmBeforeDelete=True,
)
"""
    }
]
