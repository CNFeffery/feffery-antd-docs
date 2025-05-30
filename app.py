import re
import os
import dash
import time
from flask import request
from dash import html, dcc
from datetime import datetime
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State, MATCH, ClientsideFunction

import views
from server import app, server  # noqa: F401
from components import page_header, side_menu, changelog_render
from config import AppConfig
from utils import generate_shortcut_panel_data
import views.AntdTableServerSideMode
import views.advanced_usage
import views.getting_started
import views.what_is_fac

# 国际化
from i18n import translator

# 记录应用最近启动时间
boot_datetime = datetime.now().strftime('%Y-%m-%d')


def render_layout():
    return fuc.FefferyTopProgress(
        [
            # 根容器url监听
            fuc.FefferyLocation(id='root-url'),
            # 全局状态存储
            fac.Fragment(
                [
                    # 国际化语种
                    fuc.FefferyCookie(
                        id='global-locale',
                        expires=3600 * 24 * 365,
                        cookieKey=translator.cookie_name,
                    )
                ]
            ),
            # 全局页面重载
            fuc.FefferyReload(id='global-reload'),
            # 国际化初始自动判断
            fuc.FefferyExecuteJs(
                jsString="""
// 初始化语种自动赋值策略
if ( !document.cookie.includes('dash-i18n=') ) {
    if ( !navigator.language.startsWith('zh-') ) {
        window.dash_clientside.set_props('global-locale', { value: 'en-us' })
    }
}
                """
            ),
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
                            style={'position': 'fixed'},
                        ),
                        id='global-spin-center',
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
                        manual=True,
                    ),
                ]
            ),
        ],
        listenPropsMode='include',
        includeProps=[
            'doc-layout-container.children',
        ],
        minimum=0.33,
    )


# 动态layout
app.layout = render_layout


@app.callback(
    Output('root-container', 'children'),
    Input('root-url', 'pathname'),
    [
        State('root-url', 'trigger'),
        State('root-url', 'search'),
    ],
    prevent_initial_call=True,
)
def root_router(pathname, trigger, search):
    """根节点路由控制"""

    current_locale = request.cookies.get(translator.cookie_name)

    # 赋值默认国际化语种
    current_locale = current_locale or 'zh-cn'

    if pathname.startswith('/~demo/'):
        time.sleep(0.5)

        try:
            # 尝试提取单体示例对应的类别、路径信息
            demo_type, demo_path = pathname.split('/')[2:4]

            return [
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
                    style={'padding': 0 if 'padding=no' in search else 50},
                ),
            ]

        except (ValueError, AttributeError):
            return fac.AntdCenter(
                fac.AntdResult(
                    status='404',
                    title=fac.AntdParagraph(
                        [
                            translator.t('演示示例不存在，'),
                            html.A(translator.t('回到首页'), href='/'),
                        ]
                    ),
                ),
                style={'height': 'calc(100vh - 200px)'},
            )

    # 动态路由切换时，阻止页面重复加载
    if trigger in ['pushstate', 'popstate']:
        return dash.no_update

    return [
        # 控制非正式发布模式下的文档页初始化通知提示
        (
            None
            if AppConfig.is_release
            else fac.AntdNotification(
                type='info',
                message='提示信息',
                placement='bottomRight',
                description=(
                    translator.t(
                        '当前文档网站尚未正式发布，相关文档持续补充建设中。（最近更新时间：{}）'
                    ).format(boot_datetime)
                ),
            )
        ),
        # 悬浮按钮组功能
        fac.AntdFloatButtonGroup(
            [
                fac.AntdFloatButton(
                    icon=fac.AntdIcon(icon='antd-bug'),
                    tooltip=translator.t('问题反馈'),
                    href=AppConfig.library_repo + '/issues/new',
                ),
                fac.AntdFloatButton(
                    id='open-preferences-modal',
                    icon=fac.AntdIcon(icon='antd-setting'),
                    tooltip=translator.t('偏好设置'),
                ),
            ],
            shape='square',
            style={'right': 100, 'bottom': 100},
        ),
        # 注入偏好设置模态框
        fac.AntdModal(
            fac.AntdSpace(
                [
                    fac.AntdFormItem(
                        fac.AntdRadioGroup(
                            id='preferences-search-panel-open-mode',
                            options=[
                                {
                                    'label': translator.t('新页面'),
                                    'value': 'new',
                                },
                                {
                                    'label': translator.t('当前页'),
                                    'value': 'current',
                                },
                            ],
                            defaultValue='new',
                            persistence=True,
                        ),
                        label=translator.t('搜索面板跳转方式'),
                        style={'margin': 0},
                    )
                ],
                style={'paddingTop': 15},
            ),
            id='preferences-modal',
            title=fac.AntdSpace(
                [
                    fac.AntdIcon(icon='antd-setting'),
                    translator.t('偏好设置'),
                ]
            ),
        ),
        # 注入快捷搜索面板
        fuc.FefferyShortcutPanel(
            id='global-search-panel',
            placeholder=translator.t('输入你想要搜索的组件...'),
            data=generate_shortcut_panel_data(AppConfig.side_menu_items()),
            panelStyles={'accentColor': '#1890ff', 'zIndex': 99999},
            locale=('zh' if current_locale == 'zh-cn' else 'en'),
        ),
        # 文档页面容器url监听
        dcc.Location(id='doc-layout-url'),
        # 页首
        page_header.render(locale=current_locale),
        # 主体区域
        fac.AntdRow(
            [
                # 侧边菜单
                side_menu.render(locale=current_locale),
                # 内容区域
                fac.AntdCol(
                    id='doc-layout-container',
                    flex='auto',
                    style={'width': 0, 'padding': '0 0 0 30px'},
                ),
            ],
            wrap=False,
        ),
    ]


@app.callback(
    Output('doc-layout-container', 'children'),
    Input('doc-layout-url', 'pathname'),
    running=[
        (Output('global-spin-center', 'spinning'), True, False),
    ],
    prevent_initial_call=True,
)
def doc_layout_router(pathname):
    """路由控制"""

    time.sleep(0.5)

    # 404页面
    doc_layout = fac.AntdResult(
        status='404',
        title=translator.t('您访问的页面不存在或还在建设中'),
        style={'height': 'calc(100vh - 65px)'},
    )

    # 处理针对非常规单页组件的路由请求
    if pathname in ['/what-is-fac', '/']:
        doc_layout = views.what_is_fac.render()

    elif pathname == '/getting-started':
        doc_layout = views.getting_started.render()

    elif pathname == '/advanced-classname':
        doc_layout = views.advanced_usage.advanced_classname.render()

    elif pathname == '/popup-container':
        doc_layout = views.advanced_usage.popup_container.render()

    elif pathname == '/internationalization':
        doc_layout = views.advanced_usage.internationalization.render()

    elif pathname == '/prop-persistence':
        doc_layout = views.advanced_usage.prop_persistence.render()

    elif pathname == '/use-key-to-refresh':
        doc_layout = views.advanced_usage.use_key_to_refresh.render()

    elif pathname == '/batch-props-values':
        doc_layout = views.advanced_usage.batch_props_values.render()

    elif pathname == '/import-alias':
        doc_layout = views.advanced_usage.import_alias.render()

    elif pathname in [
        '/AntdTable-basic',
        '/AntdTable-advanced',
        '/AntdTable-server-side-mode',
        '/AntdTable-rerender',
    ]:
        if pathname == '/AntdTable-basic':
            doc_layout = views.AntdTableBasic.render()
        elif pathname == '/AntdTable-advanced':
            doc_layout = views.AntdTableAdvanced.render()
        elif pathname == '/AntdTable-server-side-mode':
            doc_layout = views.AntdTableServerSideMode.render()
        elif pathname == '/AntdTable-rerender':
            doc_layout = views.AntdTableRerender.render()

    elif pathname.startswith('/changelog'):
        # 尝试提取命中的版本号
        match_version = pathname.split('-')[-1]
        # 检查提取的版本号对应更新日志是否存在
        if match_version + '.md' in os.listdir('changelogs'):
            doc_layout = changelog_render.render(version=match_version)

    # 提取当前views下合法格式页面模块
    valid_views = [
        '/' + name
        for name in dir(views)
        if not name.startswith('__') and name != 'advanced_usage'
    ]

    # 检测当前pathname是否符合单页组件文档页面模块
    if pathname in valid_views:
        doc_layout = getattr(views, pathname.replace('/', '')).render()

    return doc_layout


app.clientside_callback(
    # 控制侧边菜单栏的展开/收起
    ClientsideFunction(
        namespace='clientside', function_name='toggleSideMenuVisible'
    ),
    Input('toggle-side-menu', 'nClicks'),
    State('toggle-side-menu-icon', 'icon'),
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

    elif pathname.startswith('/changelog-'):
        # 尝试提取命中的版本号
        match_version = pathname.split('-')[-1]
        # 检查提取的版本号对应更新日志是否存在
        if match_version + '.md' in os.listdir('changelogs'):
            return [[re.sub('\.\d+$', '', match_version) + '.x版本'], pathname]

    return [None, pathname]


app.clientside_callback(
    # 处理侧边菜单栏自动滚动到当前菜单项位置
    ClientsideFunction(
        namespace='clientside', function_name='handleMenuTargetScoll'
    ),
    Input('doc-layout-url', 'pathname'),
)


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
    [
        Input('side-props-search-bar-toggle', 'nClicks'),
        Input('doc-layout-listen-esc-press', 'pressedCounts'),
    ],
    State('side-props-search-bar', 'style'),
    State('side-props-search-bar-keyword', 'focusing'),
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

app.clientside_callback(
    # 文档页点击回到顶部按钮，自动清除url中的hash
    """(nClicks) => {
        window.location.hash = '';
    }""",
    Input('doc-layout-back-top', 'nClicks'),
)

app.clientside_callback(
    # 控制点击触发的搜索面板展开
    '(n_clicks) => true',
    Output('global-search-panel', 'open'),
    Input('open-global-search-panel', 'n_clicks'),
    prevent_initial_call=True,
)

app.clientside_callback(
    # 打开偏好设置模态框
    '(nClicks) => true',
    Output('preferences-modal', 'visible'),
    Input('open-preferences-modal', 'nClicks'),
    prevent_initial_call=True,
)


app.clientside_callback(
    # 调整搜索面板新页面打开方式
    """(value, origin) => {

    return origin.map(
        (item) => {
            return {
                ...item,
                handler: (
                    value === 'new' ?
                    item.handler.replace('window.location.replace', 'window.open') :
                    item.handler.replace('window.open', 'window.location.replace')
                ),
            }
        }
    )
}""",
    Output('global-search-panel', 'data'),
    Input('preferences-search-panel-open-mode', 'value'),
    State('global-search-panel', 'data'),
)


if __name__ == '__main__':
    app.run(debug=True)
