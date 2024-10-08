import dash
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdSteps(
                id='steps-demo',
                steps=[{'title': f'步骤{i}'} for i in range(5)],
                direction='horizontal',
                type='navigation',
                allowClick=True,
            ),
            fac.AntdDivider(isDashed=True),
            fac.AntdButton('下一步', id='steps-demo-go-next', type='primary'),
            fac.AntdDivider(direction='vertical'),
            fac.AntdButton('上一步', id='steps-demo-go-last', type='primary'),
            fac.AntdDivider(direction='vertical'),
            fac.AntdButton('重置', id='steps-demo-restart', type='primary'),
            fac.AntdDivider(isDashed=True),
            fac.AntdText(id='steps-demo-current'),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdSteps(
                id='steps-demo',
                steps=[{'title': f'Step {i}'} for i in range(5)],
                direction='horizontal',
                type='navigation',
                allowClick=True,
            ),
            fac.AntdDivider(isDashed=True),
            fac.AntdButton('Next', id='steps-demo-go-next', type='primary'),
            fac.AntdDivider(direction='vertical'),
            fac.AntdButton('Last', id='steps-demo-go-last', type='primary'),
            fac.AntdDivider(direction='vertical'),
            fac.AntdButton('Restart', id='steps-demo-restart', type='primary'),
            fac.AntdDivider(isDashed=True),
            fac.AntdText(id='steps-demo-current'),
        ]

    return demo_contents


@app.callback(
    Output('steps-demo', 'current'),
    [
        Input('steps-demo-go-next', 'nClicks'),
        Input('steps-demo-go-last', 'nClicks'),
        Input('steps-demo-restart', 'nClicks'),
    ],
    State('steps-demo', 'current'),
    prevent_initial_call=True,
)
def steps_callback_demo_part1(go_next, go_last, restart, current):
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'].startswith('steps-demo-go-next'):
        return current + 1

    elif ctx.triggered[0]['prop_id'].startswith('steps-demo-go-last'):
        return max(current - 1, 0)

    else:
        return 0


@app.callback(
    Output('steps-demo-current', 'children'),
    Input('steps-demo', 'current'),
    prevent_initial_call=True,
)
def steps_callback_demo_part2(current):
    current_locale = get_current_locale()
    if current_locale == 'zh-cn':
        return f'当前步骤为：步骤{current}'

    elif current_locale == 'en-us':
        return f'Current step is: Step {current}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdSteps(
        id='steps-demo',
        steps=[{'title': f'步骤{i}'} for i in range(5)],
        direction='horizontal',
        type='navigation',
        allowClick=True,
    ),
    fac.AntdDivider(isDashed=True),
    fac.AntdButton('下一步', id='steps-demo-go-next', type='primary'),
    fac.AntdDivider(direction='vertical'),
    fac.AntdButton('上一步', id='steps-demo-go-last', type='primary'),
    fac.AntdDivider(direction='vertical'),
    fac.AntdButton('重置', id='steps-demo-restart', type='primary'),
    fac.AntdDivider(isDashed=True),
    fac.AntdText(id='steps-demo-current'),
]

...

@app.callback(
    Output('steps-demo', 'current'),
    [
        Input('steps-demo-go-next', 'nClicks'),
        Input('steps-demo-go-last', 'nClicks'),
        Input('steps-demo-restart', 'nClicks'),
    ],
    State('steps-demo', 'current'),
    prevent_initial_call=True,
)
def steps_callback_demo_part1(go_next, go_last, restart, current):
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'].startswith('steps-demo-go-next'):
        return current + 1

    elif ctx.triggered[0]['prop_id'].startswith('steps-demo-go-last'):
        return max(current - 1, 0)

    else:
        return 0


@app.callback(
    Output('steps-demo-current', 'children'),
    Input('steps-demo', 'current'),
    prevent_initial_call=True,
)
def steps_callback_demo_part2(current):
    return f'当前步骤为：步骤{current}'
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdSteps(
        id='steps-demo',
        steps=[{'title': f'Step {i}'} for i in range(5)],
        direction='horizontal',
        type='navigation',
        allowClick=True,
    ),
    fac.AntdDivider(isDashed=True),
    fac.AntdButton('Next', id='steps-demo-go-next', type='primary'),
    fac.AntdDivider(direction='vertical'),
    fac.AntdButton('Last', id='steps-demo-go-last', type='primary'),
    fac.AntdDivider(direction='vertical'),
    fac.AntdButton('Restart', id='steps-demo-restart', type='primary'),
    fac.AntdDivider(isDashed=True),
    fac.AntdText(id='steps-demo-current'),
]

...

@app.callback(
    Output('steps-demo', 'current'),
    [
        Input('steps-demo-go-next', 'nClicks'),
        Input('steps-demo-go-last', 'nClicks'),
        Input('steps-demo-restart', 'nClicks'),
    ],
    State('steps-demo', 'current'),
    prevent_initial_call=True,
)
def steps_callback_demo_part1(go_next, go_last, restart, current):
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'].startswith('steps-demo-go-next'):
        return current + 1

    elif ctx.triggered[0]['prop_id'].startswith('steps-demo-go-last'):
        return max(current - 1, 0)

    else:
        return 0


@app.callback(
    Output('steps-demo-current', 'children'),
    Input('steps-demo', 'current'),
    prevent_initial_call=True,
)
def steps_callback_demo_part2(current):
    return f'Current step is: Step {current}'
"""
            }
        ]
