import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSegmentedColoring(
            id='segmented-coloring-demo2',
            size='small',
            min=-10,
            max=10,
            breakpoints=[0, 1, 2, 3, 4, 5],
            colors=['#deecf9', '#71afe5', '#2b88d8', '#0078d4', '#106ebe'],
        ),
        fac.AntdParagraph(
            [
                fac.AntdText('breakpoints: ', strong=True),
                fac.AntdText(id='segmented-coloring-demo2-output'),
            ]
        ),
    ]

    return demo_contents


@app.callback(
    Output('segmented-coloring-demo2-output', 'children'),
    Input('segmented-coloring-demo2', 'breakpoints'),
)
def segmented_coloring_demo2_callback(breakpoints):
    return str(breakpoints)


code_string = [
    {
        'code': """
fac.AntdSegmentedColoring(
    id='segmented-coloring-demo2',
    size='small',
    min=-10,
    max=10,
    breakpoints=[0, 1, 2, 3, 4, 5],
    colors=["#deecf9", "#71afe5",
            "#2b88d8", "#0078d4",
            "#106ebe"]
),

fac.AntdParagraph(
    [
        fac.AntdText('breakpoints: ', strong=True),
        fac.AntdText(
            id='segmented-coloring-demo2-output'
        )
    ]
)

...

@app.callback(
    Output('segmented-coloring-demo2-output', 'children'),
    Input('segmented-coloring-demo2', 'breakpoints')
)
def segmented_coloring_demo2_callback(breakpoints):
    return str(breakpoints)
"""
    }
]
