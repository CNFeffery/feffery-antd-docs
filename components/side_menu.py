from dash import html
import feffery_antd_components as fac

from config import AppConfig


def render(locale: str = 'zh-cn'):
    """渲染侧边导航菜单"""

    return fac.AntdCol(
        fac.AntdAffix(
            html.Div(
                [
                    html.Div(
                        fac.AntdMenu(
                            id='side-menu',
                            menuItems=AppConfig.side_menu_items(),
                            mode='inline',
                            inlineIndent=12,
                            style={'borderRight': 'none'},
                        ),
                        id='side-menu-container',
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
            style={
                'width': 325,
            },
        ),
        flex='none',
    )
