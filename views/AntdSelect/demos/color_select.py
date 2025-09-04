import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider("连续型色带", innerTextOrientation="left"),
                fac.AntdSelect(
                    defaultValue="色系1",
                    options=[
                        {
                            "label": "色系1",
                            "value": "色系1",
                            "colors": ["#fff5f5", "#ff8787", "#c92a2a"],
                        },
                        {
                            "label": "色系2",
                            "value": "色系2",
                            "colors": ["#f8f0fc", "#da77f2", "#862e9c"],
                        },
                        {
                            "label": "色系3",
                            "value": "色系3",
                            "colors": ["#e7f5ff", "#4dabf7", "#1864ab"],
                        },
                    ],
                    colorsMode="sequential",
                    style={"width": "100%"},
                ),
                fac.AntdDivider("离散型色带", innerTextOrientation="left"),
                fac.AntdSelect(
                    defaultValue="色系1",
                    options=[
                        {
                            "label": "色系1",
                            "value": "色系1",
                            "colors": ["#fff5f5", "#ff8787", "#c92a2a"],
                        },
                        {
                            "label": "色系2",
                            "value": "色系2",
                            "colors": ["#f8f0fc", "#da77f2", "#862e9c"],
                        },
                        {
                            "label": "色系3",
                            "value": "色系3",
                            "colors": ["#e7f5ff", "#4dabf7", "#1864ab"],
                        },
                    ],
                    colorsMode="diverging",
                    style={"width": "100%"},
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider("Sequential colormap", innerTextOrientation="left"),
                fac.AntdSelect(
                    defaultValue="Palette 1",
                    options=[
                        {
                            "label": "Palette 1",
                            "value": "Palette 1",
                            "colors": ["#fff5f5", "#ff8787", "#c92a2a"],
                        },
                        {
                            "label": "Palette 2",
                            "value": "Palette 2",
                            "colors": ["#f8f0fc", "#da77f2", "#862e9c"],
                        },
                        {
                            "label": "Palette 3",
                            "value": "Palette 3",
                            "colors": ["#e7f5ff", "#4dabf7", "#1864ab"],
                        },
                    ],
                    colorsMode="sequential",
                    style={"width": "100%"},
                    locale="en-us",
                ),
                fac.AntdDivider("Diverging colormap", innerTextOrientation="left"),
                fac.AntdSelect(
                    defaultValue="Palette 1",
                    options=[
                        {
                            "label": "Palette 1",
                            "value": "Palette 1",
                            "colors": ["#fff5f5", "#ff8787", "#c92a2a"],
                        },
                        {
                            "label": "Palette 2",
                            "value": "Palette 2",
                            "colors": ["#f8f0fc", "#da77f2", "#862e9c"],
                        },
                        {
                            "label": "Palette 3",
                            "value": "Palette 3",
                            "colors": ["#e7f5ff", "#4dabf7", "#1864ab"],
                        },
                    ],
                    colorsMode="diverging",
                    style={"width": "100%"},
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": 350},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDivider('连续型色带', innerTextOrientation='left'),
        fac.AntdSelect(
            defaultValue='色系1',
            options=[
                {'label': '色系1','value': '色系1','colors': ['#fff5f5','#ff8787','#c92a2a']},
                {'label': '色系2','value': '色系2','colors': ['#f8f0fc','#da77f2','#862e9c']},
                {'label': '色系3','value': '色系3','colors': ['#e7f5ff','#4dabf7','#1864ab']},
            ],
            colorsMode='sequential',
            style={'width': '100%'},
        ),
        fac.AntdDivider('离散型色带', innerTextOrientation='left'),
        fac.AntdSelect(
            defaultValue='色系1',
            options=[
                {'label': '色系1','value': '色系1','colors': ['#fff5f5','#ff8787','#c92a2a']},
                {'label': '色系2','value': '色系2','colors': ['#f8f0fc','#da77f2','#862e9c']},
                {'label': '色系3','value': '色系3','colors': ['#e7f5ff','#4dabf7','#1864ab']},
            ],
            colorsMode='diverging',
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDivider('Sequential colormap', innerTextOrientation='left'),
        fac.AntdSelect(
            defaultValue='Palette 1',
            options=[
                {'label': 'Palette 1','value': 'Palette 1','colors': ['#fff5f5','#ff8787','#c92a2a']},
                {'label': 'Palette 2','value': 'Palette 2','colors': ['#f8f0fc','#da77f2','#862e9c']},
                {'label': 'Palette 3','value': 'Palette 3','colors': ['#e7f5ff','#4dabf7','#1864ab']},
            ],
            colorsMode='sequential',
            style={'width': '100%'},
            locale="en-us",
        ),
        fac.AntdDivider('Diverging colormap', innerTextOrientation='left'),
        fac.AntdSelect(
            defaultValue='Palette 1',
            options=[
                {'label': 'Palette 1','value': 'Palette 1','colors': ['#fff5f5','#ff8787','#c92a2a']},
                {'label': 'Palette 2','value': 'Palette 2','colors': ['#f8f0fc','#da77f2','#862e9c']},
                {'label': 'Palette 3','value': 'Palette 3','colors': ['#e7f5ff','#4dabf7','#1864ab']},
            ],
            colorsMode='diverging',
            style={'width': '100%'},
            locale="en-us",
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
            }
        ]
