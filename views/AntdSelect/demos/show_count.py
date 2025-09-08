import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdInput(mode="text-area", showCount=True, style={"width": 350}),
                fac.AntdInput(
                    mode="text-area",
                    maxLength=10,
                    showCount=True,
                    placeholder="设置maxLength后，字符数将显示上限",
                    style={"width": 350},
                ),
            ],
            direction="vertical",
            size="large",
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdInput(mode="text-area", showCount=True, style={"width": 350}),
                fac.AntdInput(
                    mode="text-area",
                    maxLength=10,
                    showCount=True,
                    placeholder="When maxLength is set, the counter shows the limit",
                    style={"width": 350},
                ),
            ],
            direction="vertical",
            size="large",
        )

    return demo_contents


def code_string() -> list:
    current_locale = get_current_locale()
    if current_locale == "zh-cn":
        return [
            {
                "code": """fac.AntdSpace(
    [
        fac.AntdInput(
            mode='text-area',
            showCount=True,
            style={'width': 350},
        ),
        fac.AntdInput(
            mode='text-area',
            maxLength=10,
            showCount=True,
            placeholder='设置maxLength后，字符数将显示上限',
            style={'width': 350},
        ),
    ],
    direction='vertical',
    size='large',
)"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """fac.AntdSpace(
            [
                fac.AntdInput(mode="text-area", showCount=True, style={"width": 350}),
                fac.AntdInput(
                    mode="text-area",
                    maxLength=10,
                    showCount=True,
                    placeholder="When maxLength is set, the counter shows the limit",
                    style={"width": 350},
                ),
            ],
            direction="vertical",
            size="large",
        )"""
            }
        ]
