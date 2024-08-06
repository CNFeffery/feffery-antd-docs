import feffery_antd_components as fac
from dash.dependencies import Component
from dash.dependencies import Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdButton(
                    '开始引导', type='primary', id='start-tour-demo-1'
                ),
                fac.AntdDivider(),
                fac.AntdSpace(
                    [
                        fac.AntdButton('上传', id='upload-btn-tour-demo-1'),
                        fac.AntdButton(
                            '保存', type='primary', id='save-btn-tour-demo-1'
                        ),
                        fac.AntdButton('···', id='more-btn-tour-demo-1'),
                    ]
                ),
                fac.AntdTour(
                    steps=[
                        {
                            'title': '欢迎',
                            'description': '欢迎使用 fac.AntdTour 组件！',
                            # 可配置封面图，可传入多个Dash组件
                            'cover': fac.AntdImage(
                                src='assets/imgs/fac-logo.svg',
                                preview=False,
                                height=100,
                                width=100,
                            ),
                        },
                        {
                            'title': '上传文件',
                            'description': '点击此按钮上传文件',
                            'targetId': 'upload-btn-tour-demo-1',
                        },
                        {
                            'title': '保存文件',
                            'description': '点击此按钮保存文件',
                            'targetId': 'save-btn-tour-demo-1',
                        },
                        {
                            'title': '更多功能',
                            'description': '点击此按钮查看更多功能',
                            'targetId': 'more-btn-tour-demo-1',
                        },
                    ],
                    id='tour-demo-1',
                ),
            ],
            direction='vertical',
        )
    ]

    return demo_contents


@app.callback(
    [
        Output('tour-demo-1', 'current'),
        Output('tour-demo-1', 'open'),
    ],
    Input('start-tour-demo-1', 'nClicks'),
    prevent_initial_call=True,
)
def start_tour_demo(nClicks):
    # 清空Tour step序号回归0，并打开Tour
    return 0, True


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdButton(
            '开始引导', type='primary', id='start-tour-demo-1'
        ),
        fac.AntdDivider(),
        fac.AntdSpace(
            [
                fac.AntdButton('上传', id='upload-btn-tour-demo-1'),
                fac.AntdButton(
                    '保存', type='primary', id='save-btn-tour-demo-1'
                ),
                fac.AntdButton('···', id='more-btn-tour-demo-1'),
            ]
        ),
        fac.AntdTour(
            steps=[
                {
                    'title': '欢迎',
                    'description': '欢迎使用 Feffery Antd Tour 组件！',
                    # 可配置封面图，可传入多个Dash组件
                    'cover': fac.AntdImage(
                        src='assets/imgs/fac-logo.svg',
                        preview=False,
                        height=100,
                        width=100,
                    ),
                },
                {
                    'title': '上传文件',
                    'description': '点击此按钮上传文件',
                    'targetId': 'upload-btn-tour-demo-1',
                },
                {
                    'title': '保存文件',
                    'description': '点击此按钮保存文件',
                    'targetId': 'save-btn-tour-demo-1',
                },
                {
                    'title': '更多功能',
                    'description': '点击此按钮查看更多功能',
                    'targetId': 'more-btn-tour-demo-1',
                },
            ],
            id='tour-demo-1',
        ),
    ],
    direction='vertical',
)


@app.callback(
    [
        Output('tour-demo-1', 'current'),
        Output('tour-demo-1', 'open'),
    ],
    Input('start-tour-demo-1', 'nClicks'),
    prevent_initial_call=True,
)
def start_tour_demo-1(nClicks):
    # 清空Tour step序号回归0，并打开Tour
    return 0, True
"""
    }
]
