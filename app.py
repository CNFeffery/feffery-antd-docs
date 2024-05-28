import dash
import time
import uuid
from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State, MATCH, ClientsideFunction

import views
from server import app
from components import page_header, side_menu
from config import AppConfig
from utils import generate_shortcut_panel_data


def render_layout():
    return fuc.FefferyTopProgress(
        [
            # 根容器url监听
            fuc.FefferyLocation(id='root-url'),
            # 页面根容器
            html.Div(
                id='root-container',
            ),
            # 辅助内容
            fac.Fragment(
                [
                    # 内容区刷新辅助动画锚点
                    fac.AntdSpin(
                        html.Div(
                            id='global-spin-center',
                            style={'position': 'fixed'},
                        ),
                        indicator=fuc.FefferyExtraSpinner(
                            type='guard',
                            color='#1890ff',
                            style={
                                'position': 'fixed',
                                'top': '50%',
                                'left': '50%',
                                'width': 100,
                                'height': 100,
                                'transform': 'translate(-50%, -50%)',
                                'zIndex': 999,
                            },
                        ),
                    ),
                ]
            ),
        ],
        listenPropsMode='include',
        includeProps=[
            'root-container.children',
            'doc-layout-container.children',
        ],
        minimum=0.33,
    )


# 动态layout
app.layout = render_layout


@app.callback(
    [Output('root-container', 'children'), Output('global-spin-center', 'key')],
    Input('root-url', 'pathname'),
    State('root-url', 'trigger'),
)
def root_router(pathname, trigger):
    """根节点路由控制"""

    if pathname.startswith('/~demo/'):
        time.sleep(0.5)

        try:
            # 尝试提取单体示例对应的类别、路径信息
            demo_type, demo_path = pathname.split('/')[2:4]

            return [
                [
                    fuc.FefferyStyle(
                        rawStyle="""
/* 隐藏debug模式工具图标 */
.dash-debug-menu,
.dash-debug-menu__outer--closed {
    display: none;
}
"""
                    ),
                    html.Div(
                        getattr(
                            getattr(views, demo_type).demos, demo_path
                        ).render(),
                        style={'padding': 50},
                    ),
                ],
                str(uuid.uuid4()),
            ]

        except ValueError:
            return [
                fac.AntdCenter(
                    fac.AntdResult(status='404', title='演示示例不存在'),
                    style={'height': '100vh'},
                ),
                str(uuid.uuid4()),
            ]

    # 动态路由切换时，阻止页面重复加载
    if trigger == 'pushstate':
        return dash.no_update

    return [
        [
            # 注入快捷搜索面板
            fuc.FefferyShortcutPanel(
                placeholder='输入你想要搜索的组件...',
                data=generate_shortcut_panel_data(AppConfig.side_menu_items),
                panelStyles={'accentColor': '#1890ff', 'zIndex': 99999},
            ),
            # 文档页面容器url监听
            dcc.Location(id='doc-layout-url'),
            # 页首
            page_header.render(),
            # 主体区域
            fac.AntdRow(
                [
                    # 侧边菜单
                    side_menu.render(),
                    # 内容区域
                    fac.AntdCol(
                        id='doc-layout-container',
                        flex='auto',
                        style={'width': 0, 'padding': '0 0 0 30px'},
                    ),
                ],
                wrap=False,
            ),
        ],
        str(uuid.uuid4()),
    ]


@app.callback(
    [
        Output('doc-layout-container', 'children'),
        Output('global-spin-center', 'key', allow_duplicate=True),
    ],
    Input('doc-layout-url', 'pathname'),
    prevent_initial_call=True,
)
def doc_layout_router(pathname):
    """路由控制"""

    time.sleep(0.5)

    # 404页面
    doc_layout = fac.AntdResult(
        status='404',
        title='您访问的页面不存在或还在建设中',
        style={'height': 'calc(100vh - 65px)'},
    )

    # 提取当前views下合法格式页面模块
    valid_views = [
        '/' + name for name in dir(views) if not name.startswith('__')
    ]

    # 检测当前pathname是否符合单页组件文档页面模块
    if pathname in valid_views:
        doc_layout = getattr(views, pathname.replace('/', '')).render()

    return [doc_layout, str(uuid.uuid4())]


app.clientside_callback(
    # 控制侧边菜单栏的展开/收起
    ClientsideFunction(
        namespace='clientside', function_name='toggleSideMenuVisible'
    ),
    Output('toggle-side-menu', 'id'),
    Input('toggle-side-menu', 'nClicks'),
    State('toggle-side-menu-icon', 'icon'),
    prevent_initial_call=True,
)


@app.callback(
    [Output('side-menu', 'openKeys'), Output('side-menu', 'currentKey')],
    Input('doc-layout-url', 'pathname'),
)
def update_side_menu_state(pathname):
    """处理pathname变动时，对侧边菜单栏相关状态的更新"""

    if pathname == '/':
        pathname = '/what-is-fac'

    if AppConfig.side_menu_expand_keys.get(pathname):
        return [AppConfig.side_menu_expand_keys[pathname], pathname]

    return [None, pathname]


app.clientside_callback(
    # 侧边参数栏展开/收起控制
    ClientsideFunction(
        namespace='clientside', function_name='toggleSidePropsVisible'
    ),
    Output('side-props', 'style'),
    Output('toggle-side-props-visible-icon', 'icon'),
    Input('toggle-side-props-visible', 'nClicks'),
    State('toggle-side-props-visible-icon', 'icon'),
    prevent_initial_call=True,
)


app.clientside_callback(
    # 侧边参数栏关键词搜索框展开/收起控制
    ClientsideFunction(
        namespace='clientside', function_name='toggleSidePropsBarVisible'
    ),
    [
        Output('side-props-search-bar', 'style'),
        Output('side-props-search-bar-keyword', 'autoFocus'),
        Output('side-props-search-bar-keyword', 'key'),
        Output('side-props-search-bar-keyword', 'value'),
        Output('side-props-search-bar-keyword', 'debounceValue'),
    ],
    Input('side-props-search-bar-toggle', 'nClicks'),
    State('side-props-search-bar', 'style'),
    prevent_initial_call=True,
)

app.clientside_callback(
    # 侧边参数栏关键词搜索
    ClientsideFunction(
        namespace='clientside', function_name='updateSidePropsMarkdownKeywords'
    ),
    Output('side-props-markdown', 'searchKeyword'),
    Input('side-props-search-bar-keyword', 'debounceValue'),
    prevent_initial_call=True,
)

app.clientside_callback(
    # 基于模式匹配，控制示例代码框的展开/收起
    ClientsideFunction(
        namespace='clientside', function_name='toggleDemoCodeVisible'
    ),
    Output({'type': 'demo-code', 'index': MATCH}, 'style'),
    Input({'type': 'demo-code-toggle', 'index': MATCH}, 'nClicks'),
    State({'type': 'demo-code', 'index': MATCH}, 'style'),
    prevent_initial_call=True,
)

app.clientside_callback(
    # 侧边页面目录展开/收起控制
    ClientsideFunction(
        namespace='clientside', function_name='toggleDocAnchorVisible'
    ),
    Output('doc-anchor-col', 'style'),
    Output('toggle-doc-anchor-visible-icon', 'icon'),
    Input('toggle-doc-anchor-visible', 'nClicks'),
    State('toggle-doc-anchor-visible-icon', 'icon'),
    prevent_initial_call=True,
)

app.clientside_callback(
    # 小屏幕下侧边菜单自动折叠
    ClientsideFunction(
        namespace='clientside', function_name='smallScreenAutoCollapseSide'
    ),
    Output('toggle-side-menu', 'nClicks'),
    Output('toggle-side-props-visible', 'nClicks'),
    Input('doc-layout-responsive', 'responsive'),
    State('toggle-side-menu', 'nClicks'),
    State('toggle-side-props-visible', 'nClicks'),
    State('toggle-side-menu-icon', 'icon'),
    State('toggle-side-props-visible-icon', 'icon'),
    prevent_initial_call=True,
)

app.clientside_callback(
    # 小屏幕下优化页首
    ClientsideFunction(
        namespace='clientside', function_name='smallScreenUpdateHeader'
    ),
    Output('doc-layout-header-standard-col1', 'style'),
    Output('doc-layout-header-standard-col2', 'style'),
    Output('doc-layout-header-standard-col3', 'style'),
    Input('page-header-responsive', 'responsive'),
    prevent_initial_call=True,
)

app.clientside_callback(
    # 控制侧边参数栏关键词搜索滚动切换
    ClientsideFunction(
        namespace='clientside', function_name='handleSidePropsSearchScroll'
    ),
    Output('side-props-markdown-search-status', 'data'),
    Input('side-props-search-bar-keyword', 'nSubmit'),
    Input('side-props-markdown', 'searchKeyword'),
    State('side-props-markdown-search-status', 'data'),
    prevent_initial_call=True,
)

if __name__ == '__main__':
    app.run(debug=True)
