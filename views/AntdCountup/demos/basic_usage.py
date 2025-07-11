import feffery_antd_components as fac
from dash.dependencies import Component
from datetime import datetime, timedelta


def render() -> Component:
    """渲染当前演示用例"""

    start_time = datetime.now() - timedelta(seconds=2 * 24 * 60 * 60 + 30)

    # 构造演示用例相关内容
    demo_contents = fac.AntdRow(
        [
            fac.AntdCol(
                fac.AntdCountup(
                    title='Countup',
                    value=start_time.strftime('%Y-%m-%d %H:%M:%S:%f'),
                ),
                span=12,
            ),
            fac.AntdCol(
                fac.AntdCountup(
                    title='Million Seconds',
                    value=start_time.strftime('%Y-%m-%d %H:%M:%S:%f'),
                    format='HH:mm:ss:SSS',
                ),
                span=12,
            ),
            fac.AntdCol(
                fac.AntdCountup(
                    title='Day Level',
                    value=start_time.strftime('%Y-%m-%d %H:%M:%S:%f'),
                    format='D 天 H 时 m 分 s 秒',
                ),
                span=24,
            ),
        ],
        gutter=16,
    )

    return demo_contents


code_string = [
    {
        'code': """
start_time = datetime.now() - timedelta(seconds=2 * 24 * 60 * 60 + 30)

...

fac.AntdRow(
    [
        fac.AntdCol(
            fac.AntdCountup(
                title='Countup',
                value=start_time.strftime('%Y-%m-%d %H:%M:%S:%f'),
            ),
            span=12,
        ),
        fac.AntdCol(
            fac.AntdCountup(
                title='Million Seconds',
                value=start_time.strftime('%Y-%m-%d %H:%M:%S:%f'),
                format='HH:mm:ss:SSS',
            ),
            span=12,
        ),
        fac.AntdCol(
            fac.AntdCountup(
                title='Day Level',
                value=start_time.strftime('%Y-%m-%d %H:%M:%S:%f'),
                format='D 天 H 时 m 分 s 秒',
            ),
            span=24,
        ),
    ],
    gutter=16,
)
"""
    }
]
