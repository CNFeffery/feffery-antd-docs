from dash import html
import feffery_antd_components as fac

from config import AppConfig


def render():
    """渲染侧边导航菜单"""

    return fac.AntdCol(
        fac.AntdAffix(
            html.Div(
                [
                    html.Div(
                        fac.AntdMenu(
                            id='side-menu',
                            menuItems=AppConfig.side_menu_items,
                            menuItemKeyToTitle={
                                **{
                                    '/' + value.split(' ')[0]: fac.AntdRow(
                                        [
                                            fac.AntdCol(value),
                                            fac.AntdCol(
                                                fac.AntdTooltip(
                                                    fac.AntdTag(
                                                        content=fac.AntdIcon(
                                                            icon='antd-app-store-add'
                                                        ),
                                                        color='green',
                                                    ),
                                                    title='0.3.x版本新增组件',
                                                    placement='right',
                                                )
                                            ),
                                        ],
                                        justify='space-between',
                                        wrap=False,
                                    )
                                    for value in [
                                        'AntdFloatButton 悬浮按钮',
                                        'AntdCenter 居中',
                                        'AntdFlex 弹性布局',
                                        'AntdColorPicker 颜色选择',
                                        'AntdCheckableTag 可选择标签',
                                        'AntdImageGroup 图片组合',
                                        'AntdQRCode 二维码',
                                        'AntdTour 漫游式引导',
                                        'Fragment 空节点',
                                    ]
                                },
                                **{
                                    '/' + value.split(' ')[0]: fac.AntdRow(
                                        [
                                            fac.AntdCol(value),
                                            fac.AntdCol(
                                                fac.AntdTooltip(
                                                    fac.AntdTag(
                                                        content=fac.AntdIcon(
                                                            icon='antd-experiment'
                                                        ),
                                                        color='blue',
                                                    ),
                                                    title='实验性质组件',
                                                    placement='right',
                                                )
                                            ),
                                        ],
                                        justify='space-between',
                                        wrap=False,
                                    )
                                    for value in [
                                        'AntdDraggablePanel 可拖拽面板',
                                        'AntdEditorLayout 编辑器布局',
                                    ]
                                },
                            },
                            mode='inline',
                            style={'borderRight': 'none'},
                        ),
                        id='side-menu-container',
                        style={'transition': 'opacity 0.15s'},
                    ),
                    fac.AntdButton(
                        fac.AntdIcon(
                            id='toggle-side-menu-icon', icon='antd-arrow-left'
                        ),
                        id='toggle-side-menu',
                        type='text',
                        shape='circle',
                        style={
                            'position': 'absolute',
                            'zIndex': 999,
                            'top': '10px',
                            'right': '-15px',
                            'background': 'white',
                            'boxShadow': '0 4px 10px 0 rgba(0,0,0,.1)',
                        },
                    ),
                ],
                className='hidden-scroll-bar',
                style={
                    'height': 'calc(100vh - 64px)',
                    'borderRight': '1px solid #e9ecef',
                    'overflowY': 'auto',
                },
            ),
            id='side-menu-affix',
            offsetTop=64.1,
            style={'width': 325, 'transition': 'width 0.15s'},
        ),
        flex='none',
    )
