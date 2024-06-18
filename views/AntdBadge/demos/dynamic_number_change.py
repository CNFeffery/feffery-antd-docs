import random
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdButton(
                '计数随机递增', id='badge-demo-generate', type='primary'
            ),
            fac.AntdBadge(
                fac.AntdAvatar(
                    mode='image',
                    src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                ),
                id='badge-demo-1',
                count=6,
            ),
            fac.AntdBadge(
                fac.AntdAvatar(
                    mode='image',
                    src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                ),
                id='badge-demo-2',
                count=0,
                dot=True,
            ),
        ],
        size=20,
    )

    return demo_contents


@app.callback(
    [Output('badge-demo-1', 'count'), Output('badge-demo-2', 'count')],
    Input('badge-demo-generate', 'nClicks'),
    [State('badge-demo-1', 'count'), State('badge-demo-2', 'count')],
    prevent_initial_call=True,
)
def badge_callback_demo(nClicks, count1, count2):
    return count1 + random.randint(1, 10), count2 + random.randint(1, 10)


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdButton(
            '计数随机递增', id='badge-demo-generate', type='primary'
        ),
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
            ),
            id='badge-demo-1',
            count=6,
        ),
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
            ),
            id='badge-demo-2',
            count=0,
            dot=True,
        ),
    ],
    size=20,
)

...

@app.callback(
    [Output('badge-demo-1', 'count'), Output('badge-demo-2', 'count')],
    Input('badge-demo-generate', 'nClicks'),
    [State('badge-demo-1', 'count'), State('badge-demo-2', 'count')],
    prevent_initial_call=True,
)
def badge_callback_demo(nClicks, count1, count2):
    return count1 + random.randint(1, 10), count2 + random.randint(1, 10)
"""
    }
]
