import json
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染“属性批量监听”文档页"""

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(duration=0.3),
                    fac.AntdBreadcrumb(
                        items=[{'title': '进阶使用'}, {'title': '批量属性监听'}]
                    ),
                    fac.AntdDivider(isDashed=True),
                    fac.AntdParagraph(
                        [
                            fac.AntdText('fac', strong=True),
                            '中针对部分组件，提供了',
                            fac.AntdText('批量属性监听', strong=True),
                            '支持，通过参数',
                            fac.AntdText('batchPropsNames', code=True),
                            '声明的若干属性，可以在回调函数编排时，仅通过属性',
                            fac.AntdText('batchPropsValues', strong=True),
                            '进行监听和使用，以下方同时开启了节点选择、节点勾选、可拖拽、节点收藏等功能的树组件为例：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdSpace(
                        [
                            fac.AntdTree(
                                id='batch-props-values-demo',
                                treeData=[
                                    {
                                        'title': '四川省',
                                        'key': '四川省',
                                        'children': [
                                            {
                                                'title': '成都市',
                                                'key': '成都市',
                                            },
                                            {
                                                'title': '广安市',
                                                'key': '广安市',
                                            },
                                        ],
                                    },
                                    {
                                        'title': '重庆市',
                                        'key': '重庆市',
                                        'children': [
                                            {
                                                'title': '渝中区',
                                                'key': '渝中区',
                                                'children': [
                                                    {
                                                        'title': '解放碑街道',
                                                        'key': '解放碑街道',
                                                    }
                                                ],
                                            },
                                            {
                                                'title': '渝北区',
                                                'key': '渝北区',
                                            },
                                        ],
                                    },
                                ],
                                selectable=True,
                                checkable=True,
                                enableNodeFavorites=True,
                                draggable=True,
                                batchPropsNames=[
                                    'expandedKeys',
                                    'selectedKeys',
                                    'checkedKeys',
                                    'halfCheckedKeys',
                                    'draggedNodeKey',
                                    'clickedContextMenu',
                                    'favoritedKeys',
                                ],
                            ),
                            html.Pre(id='batch-props-values-demo-output'),
                        ],
                        direction='vertical',
                        style={'width': '100%'},
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
fac.AntdSpace(
    [
        fac.AntdTree(
            id='batch-props-values-demo',
            treeData=[
                {
                    'title': '四川省',
                    'key': '四川省',
                    'children': [
                        {
                            'title': '成都市',
                            'key': '成都市'
                        },
                        {
                            'title': '广安市',
                            'key': '广安市'
                        }
                    ]
                },
                {
                    'title': '重庆市',
                    'key': '重庆市',
                    'children': [
                        {
                            'title': '渝中区',
                            'key': '渝中区',
                            'children': [
                                {
                                    'title': '解放碑街道',
                                    'key': '解放碑街道'
                                }
                            ]
                        },
                        {
                            'title': '渝北区',
                            'key': '渝北区'
                        }
                    ]
                }
            ],
            selectable=True,
            checkable=True,
            enableNodeFavorites=True,
            draggable=True,
            batchPropsNames=[
                'expandedKeys',
                'selectedKeys',
                'checkedKeys',
                'halfCheckedKeys',
                'draggedNodeKey',
                'clickedContextMenu',
                'favoritedKeys'
            ]
        ),
        html.Pre(id='batch-props-values-demo-output')
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)

...

import json

...

@app.callback(
    Output('batch-props-values-demo-output', 'children'),
    Input('batch-props-values-demo', 'batchPropsValues')
)
def batch_props_values_demo(batchPropsValues):

    return json.dumps(
        dict(
            batchPropsValues=batchPropsValues
        ),
        indent=4,
        ensure_ascii=False
    )
""",
                    ),
                    html.Div(style={'height': '100px'}),
                ],
                style={'flex': 'auto', 'padding': '25px'},
            )
        ],
        style={'display': 'flex', 'paddingRight': 40},
    )


@app.callback(
    Output('batch-props-values-demo-output', 'children'),
    Input('batch-props-values-demo', 'batchPropsValues'),
)
def batch_props_values_demo(batchPropsValues):
    return json.dumps(
        dict(batchPropsValues=batchPropsValues), indent=4, ensure_ascii=False
    )
