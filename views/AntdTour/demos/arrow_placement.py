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
                    '开始placement引导',
                    type='primary',
                    id='start-placement-tour-demo',
                ),
                fac.AntdButton(
                    '开始arrow引导', type='primary', id='start-arrow-tour-demo'
                ),
                fac.AntdDivider(),
                fac.AntdSpace(
                    [
                        fac.AntdButton(i, id=f'placement-{i}-btn-tour-demo')
                        for i in [
                            'center',
                            'left',
                            'leftTop',
                            'leftBottom',
                            'right',
                            'rightTop',
                            'rightBottom',
                            'top',
                            'topLeft',
                            'topRight',
                            'bottom',
                            'bottomLeft',
                            'bottomRight',
                            'arrowPointAtCenter',
                            'arrowIsFalse',
                        ]
                    ],
                    wrap=True,
                ),
                fac.AntdDivider(),
                fac.AntdSpace(
                    [
                        fac.AntdButton(i, id=f'arrow-{index}-btn-tour-demo')
                        for index, i in enumerate(
                            [
                                '有箭头',
                                '无箭头',
                                '箭头指向元素中心',
                                '箭头不指向元素中心',
                            ]
                        )
                    ],
                    wrap=True,
                ),
                fac.AntdTour(
                    # 全局配置placement为center，即所有步骤的弹框默认位置为居中
                    placement='center',
                    # 全局配置arrow为pointAtCenter: False，即所有步骤的弹框箭头不需要指向元素中心
                    arrow={'pointAtCenter': False},
                    steps=[
                        {
                            'title': i,
                            'description': f'弹框相对元素位置：{i}',
                            'targetId': f'placement-{i}-btn-tour-demo',
                            # 单独配置不同step的placement，优先级高于全局placement
                            'placement': i,
                        }
                        for i in [
                            'center',
                            'left',
                            'leftTop',
                            'leftBottom',
                            'right',
                            'rightTop',
                            'rightBottom',
                            'top',
                            'topLeft',
                            'topRight',
                            'bottom',
                            'bottomLeft',
                            'bottomRight',
                        ]
                    ],
                    id='tour-demo',
                ),
                fac.AntdTour(
                    placement='topRight',
                    # 全局配置arrow为True
                    arrow=True,
                    steps=[
                        {
                            'title': k,
                            'description': f'{k}的弹框示例',
                            'targetId': f'arrow-{index}-btn-tour-demo',
                            # 单独配置不同step的arrow，优先级高于全局arrow
                            'arrow': v,
                        }
                        for index, (k, v) in enumerate(
                            {
                                '有箭头': True,
                                '无箭头': False,
                                '箭头指向元素中心': {'pointAtCenter': True},
                                '箭头不指向元素中心': {'pointAtCenter': False},
                            }.items()
                        )
                    ],
                    id='arrow-tour-demo',
                ),
            ],
            direction='vertical',
        )
    ]

    return demo_contents


@app.callback(
    [
        Output('placement-tour-demo', 'current'),
        Output('placement-tour-demo', 'open'),
    ],
    Input('start-placement-tour-demo', 'nClicks'),
    prevent_initial_call=True,
)
def start_placement_tour_demo(nClicks):
    # 清空Tour step序号回归0，并打开Tour
    return 0, True


@app.callback(
    [
        Output('arrow-tour-demo', 'current'),
        Output('arrow-tour-demo', 'open'),
    ],
    Input('start-arrow-tour-demo', 'nClicks'),
    prevent_initial_call=True,
)
def start_arrow_tour_demo(nClicks):
    # 清空Tour step序号回归0，并打开Tour
    return 0, True


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdButton(
            '开始placement引导',
            type='primary',
            id='start-placement-tour-demo',
        ),
        fac.AntdButton(
            '开始arrow引导', type='primary', id='start-arrow-tour-demo'
        ),
        fac.AntdDivider(),
        fac.AntdSpace(
            [
                fac.AntdButton(i, id=f'placement-{i}-btn-tour-demo')
                for i in [
                    'center',
                    'left',
                    'leftTop',
                    'leftBottom',
                    'right',
                    'rightTop',
                    'rightBottom',
                    'top',
                    'topLeft',
                    'topRight',
                    'bottom',
                    'bottomLeft',
                    'bottomRight',
                    'arrowPointAtCenter',
                    'arrowIsFalse',
                ]
            ],
            wrap=True,
        ),
        fac.AntdDivider(),
        fac.AntdSpace(
            [
                fac.AntdButton(i, id=f'arrow-{index}-btn-tour-demo')
                for index, i in enumerate(
                    [
                        '有箭头',
                        '无箭头',
                        '箭头指向元素中心',
                        '箭头不指向元素中心',
                    ]
                )
            ],
            wrap=True,
        ),
        fac.AntdTour(
            # 全局配置placement为center，即所有步骤的弹框默认位置为居中
            placement='center',
            # 全局配置arrow为pointAtCenter: False，即所有步骤的弹框箭头不需要指向元素中心
            arrow={'pointAtCenter': False},
            steps=[
                {
                    'title': i,
                    'description': f'弹框相对元素位置：{i}',
                    'targetId': f'placement-{i}-btn-tour-demo',
                    # 单独配置不同step的placement，优先级高于全局placement
                    'placement': i,
                }
                for i in [
                    'center',
                    'left',
                    'leftTop',
                    'leftBottom',
                    'right',
                    'rightTop',
                    'rightBottom',
                    'top',
                    'topLeft',
                    'topRight',
                    'bottom',
                    'bottomLeft',
                    'bottomRight',
                ]
            ],
            id='tour-demo',
        ),
        fac.AntdTour(
            placement='topRight',
            # 全局配置arrow为True
            arrow=True,
            steps=[
                {
                    'title': k,
                    'description': f'{k}的弹框示例',
                    'targetId': f'arrow-{index}-btn-tour-demo',
                    # 单独配置不同step的arrow，优先级高于全局arrow
                    'arrow': v,
                }
                for index, (k, v) in enumerate(
                    {
                        '有箭头': True,
                        '无箭头': False,
                        '箭头指向元素中心': {'pointAtCenter': True},
                        '箭头不指向元素中心': {'pointAtCenter': False},
                    }.items()
                )
            ],
            id='arrow-tour-demo',
        ),
    ],
    direction='vertical',
)


@app.callback(
    [
        Output('placement-tour-demo', 'current'),
        Output('placement-tour-demo', 'open'),
    ],
    Input('start-placement-tour-demo', 'nClicks'),
    prevent_initial_call=True,
)
def start_placement_tour_demo(nClicks):
    # 清空Tour step序号回归0，并打开Tour
    return 0, True


@app.callback(
    [
        Output('arrow-tour-demo', 'current'),
        Output('arrow-tour-demo', 'open'),
    ],
    Input('start-arrow-tour-demo', 'nClicks'),
    prevent_initial_call=True,
)
def start_arrow_tour_demo(nClicks):
    # 清空Tour step序号回归0，并打开Tour
    return 0, True

"""
    }
]
