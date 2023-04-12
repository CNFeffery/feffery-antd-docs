import time
import dash
import random
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, ALL, MATCH

from server import app


@app.callback(
    [Output('badge-demo-1', 'count'),
     Output('badge-demo-2', 'count')],
    Input('badge-demo-generate', 'nClicks'),
    [State('badge-demo-1', 'count'),
     State('badge-demo-2', 'count')],
    prevent_initial_call=True
)
def badge_callback_demo(nClicks, count1, count2):
    return count1 + random.randint(1, 10), count2 + random.randint(1, 10)


@app.callback(
    [Output('badges-area', 'children'),
     Output('badge-click-demo-start-time', 'data')],
    Input('badge-click-demo-reset', 'nClicks'),
    prevent_initial_call=True
)
def badge_click_demo_callback1(nClicks):
    badges_count = [1] * 3 + [0] * 7
    random.shuffle(badges_count)

    return [
        [
            fac.AntdBadge(
                fac.AntdAvatar(
                    mode='image',
                    src='/assets/imgs/avatar-demo.jpg',
                    style={
                        'cursor': 'pointer'
                    }
                ),
                id={
                    'type': 'badge-click-demo',
                    'index': idx
                },
                count=c,
                dot=True,
                style={
                    'cursor': 'pointer'
                }
            )
            for idx, c in enumerate(badges_count)
        ],
        {
            'start-time': time.time()
        }
    ]


@app.callback(
    Output({'type': 'badge-click-demo', 'index': MATCH}, 'count'),
    Input({'type': 'badge-click-demo', 'index': MATCH}, 'nClicks'),
    State({'type': 'badge-click-demo', 'index': MATCH}, 'count'),
    prevent_initial_call=True
)
def badge_click_demo_callback2(nClicks, count_):
    return 0 if count_ != 0 else dash.no_update


@app.callback(
    Output('badge-click-demo-score', 'children'),
    Input({'type': 'badge-click-demo', 'index': ALL}, 'count'),
    State('badge-click-demo-start-time', 'data'),
    prevent_initial_call=True
)
def badge_click_demo_callback3(counts, start_time):
    if sum(counts) == 0:
        return fac.AntdParagraph(
            [
                fac.AntdText('你的得分：', strong=True),
                fac.AntdText('%s秒' % round(
                    time.time() - start_time['start-time'], 3))
            ]
        )
