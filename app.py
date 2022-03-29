import os

import dash
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from config import Config
from server import app, server
from views import (
    what_is_fac,
    getting_started,
    AntdDatePicker,
    AntdDateRangePicker,
    AntdDivider,
    AntdIcon,
    AntdBackTop,
    AntdButton,
    AntdSelect,
    AntdRate,
    AntdTree,
    AntdTable,
    AntdAnchor,
    AntdSlider,
    AntdTransfer,
    AntdSteps,
    AntdMenu,
    AntdUpload,
    AntdDraggerUpload,
    AntdSpin,
    AntdInput,
    AntdTabPane,
    AntdTabs,
    AntdRow,
    AntdCol,
    AntdParagraph,
    AntdText,
    AntdTitle,
    AntdSpace,
    AntdAlert,
    AntdNotification,
    AntdMessage,
    AntdLayout,
    AntdHeader,
    AntdSider,
    AntdContent,
    AntdFooter,
    AntdPagination,
    AntdCascader,
    AntdCheckbox,
    AntdCheckboxGroup,
    AntdRadioGroup,
    AntdSwitch,
    AntdTreeSelect,
    AntdCollapse,
    AntdEmpty,
    AntdTooltip,
    AntdPopover,
    AntdStatistic,
    AntdCountdown,
    AntdTag,
    AntdDrawer,
    AntdModal,
    AntdPopconfirm,
    AntdResult,
    AntdSkeleton,
    AntdAffix,
    AntdBreadcrumb,
    AntdDropdown,
    AntdInputNumber,
    AntdTimeline,
    AntdProgress,
    AntdAvatar,
    AntdBadge,
    AntdRibbon,
    AntdTimePicker,
    AntdTimeRangePicker,
    AntdCarousel,
    AntdForm,
    AntdFormItem,
    AntdCardGrid,
    AntdCard,
    AntdMentions,
    AntdImage,
    AntdPageHeader,
    AntdCalendar,
    AntdComment,
    AntdDescriptions,
    AntdDescriptionItem,
    AntdWatermark,
    AntdPasteImage
)

app.layout = fuc.FefferyTopProgress(
    html.Div(
        [
            # 注入url监听
            dcc.Location(id='url'),

            # 注入快捷指令面板
            fuc.FefferyShortcutPanel(
                placeholder='输入你想要搜索的内容...',
                data=[
                         {
                             'id': item['props']['href'],
                             'title': item['props']['title'],
                             'handler': '() => window.open("%s")' % item['props']['href'],
                             'section': group['props']['title']
                         }
                         for group in Config.menuItems
                         for item in group['children']
                         if item['props'].get('href')
                     ] + [
                         {
                             'id': sub_item['props']['href'],
                             'title': sub_item['props']['title'],
                             'handler': '() => window.open("%s")' % sub_item['props']['href'],
                             'section': group['props']['title']
                         }
                         for group in Config.menuItems
                         for item in group['children']
                         if item['component'] == 'SubMenu'
                         for sub_item in item['children']
                     ]
            ),

            # 注入快捷添加好友悬浮卡片
            html.Div(
                [
                    fac.AntdPopover(
                        fac.AntdButton(
                            fac.AntdIcon(icon='antd-bulb'),
                            shape='circle',
                            style={
                                'zoom': '1.25',
                                'boxShadow': '0 3px 6px -4px #0000001f, 0 6px 16px #00000014, 0 9px 28px 8px #0000000d'
                            }
                        ),
                        placement='left',
                        content=[
                            fac.AntdText(
                                '微信扫码加我好友，备注【dash学习】加入学习交流群，更多灵感更快进步',
                                strong=True
                            ),
                            fac.AntdImage(
                                src=app.get_asset_url('imgs/feffery-添加好友二维码.jpg'),
                                width=250,
                                preview=False
                            )
                        ],
                        overlayStyle={
                            'width': '300px',
                            'height': '408px'
                        }
                    )
                ],
                style={
                    'position': 'fixed',
                    'right': '100px',
                    'bottom': '200px',
                    'zIndex': 99999
                }
            ),

            # 页面结构
            fac.AntdRow(
                [
                    fac.AntdCol(
                        html.Img(
                            src=app.get_asset_url(
                                'imgs/fac-logo.svg'),
                            style={
                                'height': '50px',
                                'padding': '0 10px',
                                'marginTop': '7px'
                            }
                        ),
                    ),
                    fac.AntdCol(
                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    'feffery-antd-components',
                                    strong=True,
                                    style={
                                        'fontSize': '35px'
                                    }
                                ),
                                fac.AntdText(
                                    f'v{fac.__version__}',
                                    style={
                                        'fontSize': '10px',
                                        'paddingLeft': '2px'
                                    }
                                )
                            ]
                        )
                    ),

                    fac.AntdCol(
                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    'Ctrl',
                                    keyboard=True,
                                    style={
                                        'color': '#8c8c8c'
                                    }
                                ),
                                fac.AntdText(
                                    'K',
                                    keyboard=True,
                                    style={
                                        'color': '#8c8c8c'
                                    }
                                ),
                                fac.AntdText(
                                    '唤出搜索面板',
                                    style={
                                        'color': '#8c8c8c'
                                    }
                                )
                            ],
                            style={
                                'marginLeft': '50px',
                                'marginTop': '21px'
                            }
                        ),
                        flex='auto'
                    ),

                    fac.AntdCol(
                        html.Div(
                            [
                                html.A(
                                    fac.AntdImage(
                                        alt='fac源码仓库，欢迎star',
                                        src='https://img.shields.io/github/stars/CNFeffery/feffery-antd-components?style=social',
                                        preview=False,
                                        fallback=None,
                                        style={
                                            'transform': 'translateY(0px) scale(1.25)'
                                        }
                                    ),
                                    href='https://github.com/CNFeffery/feffery-antd-components',
                                    target='_blank',
                                    style={
                                        'cursor': 'pointer'
                                    }
                                ),

                                html.A(
                                    '皖ICP备2021012734号-1',
                                    href='https://beian.miit.gov.cn/',
                                    target='_blank',
                                    style={
                                        'fontSize': '10px',
                                        'marginLeft': '50px',
                                        'color': '#494f54'
                                    }
                                )
                            ],
                            style={
                                'float': 'right',
                                'paddingRight': '20px',
                                'marginTop': '20.5px'
                            }
                        ),
                        flex='auto'
                    )
                ],
                align="middle",
                style={
                    'height': '64px',
                    'boxShadow': 'rgb(240 241 242) 0px 2px 14px',
                    'background': 'white',
                    'marginBottom': '5px'
                }
            ),

            fac.AntdRow(
                [
                    fac.AntdCol(
                        fac.AntdAffix(
                            html.Div(
                                fac.AntdMenu(
                                    id='router-menu',
                                    menuItems=Config.menuItems,
                                    mode='inline',
                                    defaultOpenKeys=[
                                        'Card', 'Descriptions', 'Form', 'Tabs', 'Grid', 'Typography', 'Layout'
                                    ],
                                    style={
                                        'height': '100%',
                                        'overflow': 'hidden auto',
                                        'paddingBottom': '50px'
                                    }
                                ),
                                style={
                                    'width': '300px',
                                    'height': '100vh',
                                    'overflowY': 'auto'
                                }
                            ),
                            offsetTop=0
                        ),
                        flex='none'
                    ),

                    fac.AntdCol(
                        html.Div(
                            id='docs-content',
                            style={
                                'backgroundColor': 'rgb(255, 255, 255)'
                            }
                        ),
                        flex='auto',
                        style={
                            'padding': '25px'
                        }
                    ),

                    fac.AntdBackTop(
                        duration=0.5
                    )
                ],
                wrap=False
            )
        ]
    ),
    listenPropsMode='exclude',
    excludeProps=Config.exclude_props,
    minimum=0.33,
    speed=800,
    debug=True
)


@app.callback(
    [Output('docs-content', 'children'),
     Output('router-menu', 'currentKey')],
    Input('url', 'pathname')
)
def render_docs_content(pathname):
    '''
    路由回调
    '''

    if pathname.startswith('/change-log-') and pathname[1:] + '.md' in os.listdir('./change logs'):
        return html.Div(
            fmc.FefferyMarkdown(
                markdownStr=open(f'./change logs/{pathname[1:]}.md', encoding='utf-8').read()
            ),
            style={
                'padding': '25px'
            }
        ), pathname.replace('/change-log-', '')

    if pathname == '/what-is-fac' or pathname == '/':
        pathname = '/what-is-fac'
        return what_is_fac.docs_content, pathname

    elif pathname == '/getting-started':
        return getting_started.docs_content, pathname

    elif pathname == '/AntdIcon':
        return AntdIcon.docs_content, pathname

    elif pathname == '/AntdButton':
        return AntdButton.docs_content, pathname

    elif pathname == '/AntdParagraph':
        return AntdParagraph.docs_content, pathname

    elif pathname == '/AntdText':
        return AntdText.docs_content, pathname

    elif pathname == '/AntdTitle':
        return AntdTitle.docs_content, pathname

    elif pathname == '/AntdDivider':
        return AntdDivider.docs_content, pathname

    elif pathname == '/AntdSpace':
        return AntdSpace.docs_content, pathname

    elif pathname == '/AntdRow':
        return AntdRow.docs_content, pathname

    elif pathname == '/AntdCol':
        return AntdCol.docs_content, pathname

    elif pathname == '/AntdLayout':
        return AntdLayout.docs_content, pathname

    elif pathname == '/AntdHeader':
        return AntdHeader.docs_content, pathname

    elif pathname == '/AntdSider':
        return AntdSider.docs_content, pathname

    elif pathname == '/AntdContent':
        return AntdContent.docs_content, pathname

    elif pathname == '/AntdFooter':
        return AntdFooter.docs_content, pathname

    elif pathname == '/AntdAffix':
        return AntdAffix.docs_content, pathname

    elif pathname == '/AntdBreadcrumb':
        return AntdBreadcrumb.docs_content, pathname

    elif pathname == '/AntdDropdown':
        return AntdDropdown.docs_content, pathname

    elif pathname == '/AntdMenu':
        return AntdMenu.docs_content, pathname

    elif pathname == '/AntdPagination':
        return AntdPagination.docs_content, pathname

    elif pathname == '/AntdSteps':
        return AntdSteps.docs_content, pathname

    elif pathname == '/AntdCascader':
        return AntdCascader.docs_content, pathname

    elif pathname == '/AntdCheckbox':
        return AntdCheckbox.docs_content, pathname

    elif pathname == '/AntdCheckboxGroup':
        return AntdCheckboxGroup.docs_content, pathname

    elif pathname == '/AntdDatePicker':
        return AntdDatePicker.docs_content, pathname

    elif pathname == '/AntdDateRangePicker':
        return AntdDateRangePicker.docs_content, pathname

    elif pathname == '/AntdInput':
        return AntdInput.docs_content, pathname

    elif pathname == '/AntdInputNumber':
        return AntdInputNumber.docs_content, pathname

    elif pathname == '/AntdRadioGroup':
        return AntdRadioGroup.docs_content, pathname

    elif pathname == '/AntdSelect':
        return AntdSelect.docs_content, pathname

    elif pathname == '/AntdRate':
        return AntdRate.docs_content, pathname

    elif pathname == '/AntdSlider':
        return AntdSlider.docs_content, pathname

    elif pathname == '/AntdSwitch':
        return AntdSwitch.docs_content, pathname

    elif pathname == '/AntdTransfer':
        return AntdTransfer.docs_content, pathname

    elif pathname == '/AntdTreeSelect':
        return AntdTreeSelect.docs_content, pathname

    elif pathname == '/AntdUpload':
        return AntdUpload.docs_content, pathname

    elif pathname == '/AntdDraggerUpload':
        return AntdDraggerUpload.docs_content, pathname

    elif pathname == '/AntdCollapse':
        return AntdCollapse.docs_content, pathname

    elif pathname == '/AntdEmpty':
        return AntdEmpty.docs_content, pathname

    elif pathname == '/AntdPopover':
        return AntdPopover.docs_content, pathname

    elif pathname == '/AntdStatistic':
        return AntdStatistic.docs_content, pathname

    elif pathname == '/AntdCountdown':
        return AntdCountdown.docs_content, pathname

    elif pathname == '/AntdTable':
        return AntdTable.docs_content, pathname

    elif pathname == '/AntdTag':
        return AntdTag.docs_content, pathname

    elif pathname == '/AntdTimeline':
        return AntdTimeline.docs_content, pathname

    elif pathname == '/AntdTooltip':
        return AntdTooltip.docs_content, pathname

    elif pathname == '/AntdTree':
        return AntdTree.docs_content, pathname

    elif pathname == '/AntdTabPane':
        return AntdTabPane.docs_content, pathname

    elif pathname == '/AntdTabs':
        return AntdTabs.docs_content, pathname

    elif pathname == '/AntdAlert':
        return AntdAlert.docs_content, pathname

    elif pathname == '/AntdDrawer':
        return AntdDrawer.docs_content, pathname

    elif pathname == '/AntdMessage':
        return AntdMessage.docs_content, pathname

    elif pathname == '/AntdModal':
        return AntdModal.docs_content, pathname

    elif pathname == '/AntdNotification':
        return AntdNotification.docs_content, pathname

    elif pathname == '/AntdResult':
        return AntdResult.docs_content, pathname

    elif pathname == '/AntdSkeleton':
        return AntdSkeleton.docs_content, pathname

    elif pathname == '/AntdSpin':
        return AntdSpin.docs_content, pathname

    elif pathname == '/AntdAnchor':
        return AntdAnchor.docs_content, pathname

    elif pathname == '/AntdBackTop':
        return AntdBackTop.docs_content, pathname

    elif pathname == '/AntdPopconfirm':
        return AntdPopconfirm.docs_content, pathname

    elif pathname == '/AntdProgress':
        return AntdProgress.docs_content, pathname

    elif pathname == '/AntdAvatar':
        return AntdAvatar.docs_content, pathname

    elif pathname == '/AntdBadge':
        return AntdBadge.docs_content, pathname

    elif pathname == '/AntdRibbon':
        return AntdRibbon.docs_content, pathname

    elif pathname == '/AntdTimePicker':
        return AntdTimePicker.docs_content, pathname

    elif pathname == '/AntdTimeRangePicker':
        return AntdTimeRangePicker.docs_content, pathname

    elif pathname == '/AntdCarousel':
        return AntdCarousel.docs_content, pathname

    elif pathname == '/AntdForm':
        return AntdForm.docs_content, pathname

    elif pathname == '/AntdFormItem':
        return AntdFormItem.docs_content, pathname

    elif pathname == '/AntdCardGrid':
        return AntdCardGrid.docs_content, pathname

    elif pathname == '/AntdCard':
        return AntdCard.docs_content, pathname

    elif pathname == '/AntdMentions':
        return AntdMentions.docs_content, pathname

    elif pathname == '/AntdImage':
        return AntdImage.docs_content, pathname

    elif pathname == '/AntdPageHeader':
        return AntdPageHeader.docs_content, pathname

    elif pathname == '/AntdCalendar':
        return AntdCalendar.docs_content, pathname

    elif pathname == '/AntdComment':
        return AntdComment.docs_content, pathname

    elif pathname == '/AntdDescriptions':
        return AntdDescriptions.docs_content, pathname

    elif pathname == '/AntdDescriptionItem':
        return AntdDescriptionItem.docs_content, pathname

    elif pathname == '/AntdWatermark':
        return AntdWatermark.docs_content, pathname

    elif pathname == '/AntdPasteImage':
        return AntdPasteImage.docs_content, pathname

    return fac.AntdResult(status='404', title='您访问的页面不存在！'), pathname


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
