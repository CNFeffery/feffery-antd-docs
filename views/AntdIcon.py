import re
from dash import html
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
import feffery_antd_components as fac
from dash.dependencies import Input, Output

from config import Config
from server import app

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdIcon(id, className, style, *args, **kwargs)',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5'
                    }
                ),

                fac.AntdBackTop(
                    containerId='docs-content',
                    duration=0.6
                ),

                html.Span(
                    '主要参数说明：',
                    id='主要参数说明',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5',
                        'fontWeight': 'bold',
                        'fontSize': '1.2rem'
                    }
                ),

                fmc.FefferyMarkdown(
                    markdownStr=open('documents/AntdIcon.md', encoding='utf-8').read()
                ),

                html.Div(
                    html.Span(
                        '使用示例',
                        id='使用示例',
                        style={
                            'borderLeft': '4px solid grey',
                            'padding': '3px 0 3px 10px',
                            'backgroundColor': '#f5f5f5',
                            'fontWeight': 'bold',
                            'fontSize': '1.2rem'
                        }
                    ),
                    style={
                        'marginBottom': '10px'
                    }
                ),

                html.Div(
                    [

                        fac.AntdRadioGroup(
                            id='icon-category',
                            options=[
                                {
                                    'label': 'Antd Design精选',
                                    'value': 'antd'
                                },
                                {
                                    'label': 'Material Design精选',
                                    'value': 'md'
                                },
                                {
                                    'label': 'Flat Color精选',
                                    'value': 'fc'
                                },
                                {
                                    'label': 'Devicons精选',
                                    'value': 'di'
                                },
                                {
                                    'label': 'BoxIcons精选',
                                    'value': 'bi'
                                },
                                {
                                    'label': 'Bootstrap精选',
                                    'value': 'bs'
                                },
                                {
                                    'label': 'Game Icons精选',
                                    'value': 'gi'
                                }
                            ],
                            optionType='button',
                            defaultValue='antd'
                        ),

                        fac.AntdSpin(
                            fac.AntdRow(
                                id='icon-demo',
                                style={
                                    'minHeight': '50px'
                                }
                            )
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　AntdIcon', strong=True),
                                fac.AntdText('可配合'),
                                fac.AntdText('AntdButton', strong=True),
                                fac.AntdText('、'),
                                fac.AntdText('AntdMenu', strong=True),
                                fac.AntdText('等组件使用，阅读相关文档时请留意对应图标使用示例')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                [
                    fac.AntdIcon(
                        icon=icon,
                        style={
                            'fontSize': '28px',
                            'marginRight': '5px'
                        }
                    ),
                    fac.AntdText(
                        icon,
                        copyable=True
                    )
                ]
            ),
            span=6
        )
        for icon in [
        'md-star-half',
        'md-star-border',
        'md-star',
        'md-people',
        'md-plus-one',
        'md-notifications',
        'md-pin-drop',
        'md-layers-clear',
        'md-layers',
        'md-edit-location',
        'md-tune',
        'md-transform',
        'md-timer-off',
        'md-timer',
        'md-file-upload',
        'md-file-download',
        'md-create-new-folder',
        'md-cloud-upload',
        'md-cloud-queue',
        'md-cloud-download',
        'md-cloud-done',
        'md-insert-chart',
        'md-functions',
        'md-format-quote',
        'md-attach-file',
        'md-storage',
        'md-save',
        'md-remove-circle-outline',
        'md-remove-circle',
        'md-remove',
        'md-low-priority',
        'md-link',
        'md-gesture',
        'md-forward',
        'md-flag',
        'md-drafts',
        'md-create',
        'md-content-paste',
        'md-content-cut',
        'md-content-copy',
        'md-clear',
        'md-block',
        'md-backspace',
        'md-add-box',
        'md-add',
        'md-add-circle-outline',
        'md-add-circle',
        'md-location-on',
        'md-mail-outline',
        'md-email',
        'md-not-interested',
        'md-library-books',
        'md-library-add',
        'md-equalizer',
        'md-add-alert',
        'md-visibility-off',
        'md-visibility',
        'md-verified-user',
        'md-update',
        'md-trending-up',
        'md-trending-flat',
        'md-trending-down',
        'md-translate',
        'md-toc',
        'md-timeline',
        'md-thumb-up',
        'md-thumb-down',
        'md-swap-vert',
        'md-swap-horiz',
        'md-supervisor-account',
        'md-subject',
        'md-settings',
        'md-search',
        'md-schedule',
        'md-restore',
        'md-query-builder',
        'md-power-settings-new',
        'md-opacity',
        'md-note-add',
        'md-lock-outline',
        'md-lock-open',
        'md-list',
        'md-lightbulb-outline',
        'md-launch',
        'md-label-outline',
        'md-label',
        'md-input',
        'md-info-outline',
        'md-info',
        'md-hourglass',
        'md-home',
        'md-history',
        'md-highlight-off',
        'md-help-outline',
        'md-help',
        'md-get-app',
        'md-translate',
        'md-fingerprint',
        'md-findIn-page',
        'md-favorite-border',
        'md-favorite',
        'md-extension',
        'md-explore',
        'md-exit-to-app',
        'md-event',
        'md-description',
        'md-delete-forever',
        'md-delete',
        'md-dashboard',
        'md-code',
        'md-build',
        'md-bug-report',
        'md-assignment',
        'md-assessment',
        'md-alarm-on',
        'md-alarm-off',
        'md-alarm-add',
        'md-alarm',
        'md-account-circle',
        'fc-vlc',
        'fc-view-details',
        'fc-upload',
        'fc-tree-structure',
        'fc-timeline',
        'fc-template',
        'fc-survey',
        'fc-signature',
        'fc-share',
        'fc-services',
        'fc-rules',
        'fc-questions',
        'fc-process',
        'fc-plus',
        'fc-overtime',
        'fc-organization',
        'fc-numerical-sorting21',
        'fc-numerical-sorting12',
        'fc-multiple-inputs',
        'fc-mind-map',
        'fc-menu',
        'fc-list',
        'fc-like',
        'fc-like-placeholder',
        'fc-info',
        'fc-import',
        'fc-image-file',
        'fc-idea',
        'fc-home',
        'fc-high-priority',
        'fc-low-priority',
        'fc-genealogy',
        'fc-full-trash',
        'fc-document-search',
        'fc-file',
        'fc-faq',
        'fc-export',
        'fc-empty-trash',
        'fc-download',
        'fc-document',
        'fc-deployment',
        'fc-delete-database',
        'fc-conference-call',
        'fc-database',
        'fc-data-protection',
        'fc-data-encryption',
        'fc-data-configuration',
        'fc-data-backup',
        'fc-checkmark',
        'fc-cancel',
        'fc-briefcase',
        'fc-binoculars',
        'fc-automatic',
        'fc-alphabetical-sorting-za',
        'fc-alphabetical-sorting-az',
        'fc-add-database',
        'fc-accept-database',
        'fc-about',
        'fc-radar-chart',
        'fc-scatter-chart',
        'fc-pie-chart',
        'fc-line-chart',
        'fc-flow-chart',
        'fc-doughnut-chart',
        'fc-bar-chart',
        'fc-area-chart',
        'fc-line-bar-chart',
        'fc-workflow',
        'fc-todo-list',
        'fc-synchronize',
        'fc-repair',
        'fc-statistics',
        'fc-settings',
        'fc-search',
        'fc-serial-tasks',
        'fc-safe',
        'fc-negative-dynamic',
        'fc-positive-dynamic',
        'fc-planner',
        'fc-parallel-tasks',
        'fc-org-unit',
        'fc-opened-folder',
        'fc-ok',
        'fc-inspection',
        'fc-globe',
        'fc-folder',
        'fc-electronics',
        'fc-data-sheet',
        'fc-command-line',
        'fc-calendar',
        'fc-calculator',
        'fc-bullish',
        'fc-bearish',
        'fc-bookmark',
        'fc-approval',
        'fc-advertising',
        'di-linux',
        'di-python',
        'bi-table',
        'bi-analyse',
        'bs-list-task',
        'bs-list-check',
        'bs-link',
        'bs-link-45-deg',
        'bs-envelope-open',
        'bs-envelope',
        'bs-alarm',
        'user',
        'unlock',
        'repair',
        'team',
        'sync',
        'setting',
        'send',
        'schedule',
        'save',
        'rocket',
        'reload',
        'read',
        'qrcode',
        'power-off',
        'number',
        'notification',
        'menu',
        'mail',
        'lock',
        'loading',
        'key',
        'hourglass',
        'global',
        'function',
        'import',
        'export',
        'dashboard',
        'control',
        'console-sql',
        'compass',
        'comment',
        'code',
        'cluster',
        'clear',
        'camera',
        'book',
        'catalog',
        'api',
        'alert',
        'account-book',
        'alipay',
        'alipay-circle',
        'weibo',
        'github',
        'table',
        'fall',
        'rise',
        'stock',
        'home',
        'area-chart',
        'bar-chart',
        'pie-chart',
        'box-plot',
        'dot-chart',
        'line-chart',
        'apartment',
        'app-store',
        'app-store-add',
        'bell',
        'calculator',
        'calendar',
        'database',
        'history',
        'search',
        'file-search',
        'cloud',
        'cloud-upload',
        'cloud-download',
        'cloud-server',
        'swap',
        'im-earth',
        'gi-mesh-network',
        'rollback',
        'login',
        'logout',
        'menu-fold',
        'menu-unfold',
        'full-screen',
        'full-screen-exit',
        'question-circle',
        'plus-circle',
        'minus-circle',
        'info-circle',
        'exclamation-circle',
        'close-circle',
        'check-circle',
        'clock-circle',
        'stop',
        'edit',
        'delete',
        'highlight',
        'redo',
        'undo',
        'zoom-in',
        'zoom-out',
        'sort-ascending',
        'sort-descending',
    ]
    ]
)'''),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto'
            }
        ),

        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '主要参数说明', 'href': '#主要参数说明'},
                    {
                        'title': '使用示例',
                        'href': '#使用示例',
                        'children': [
                            {'title': '基础使用', 'href': '#基础使用'}
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200
            ),
            style={
                'flex': 'none',
                'margin': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)


@app.callback(
    Output('icon-demo', 'children'),
    Input('icon-category', 'value')
)
def icon_demo_render_callback(value):
    if value == 'antd':
        return [
            fac.AntdCol(
                html.Div(
                    [
                        fac.AntdIcon(
                            icon=icon,
                            style={
                                'fontSize': '28px',
                                'marginRight': '5px'
                            }
                        ),
                        fac.AntdText(
                            icon,
                            copyable=True
                        )
                    ]
                ),
                span=6
            )
            for icon in Config.all_icons if re.findall('^md|^fc|^di|^bi|^bs|^gi', icon) == []
        ]

    else:

        return [
            fac.AntdCol(
                html.Div(
                    [
                        fac.AntdIcon(
                            icon=icon,
                            style={
                                'fontSize': '28px',
                                'marginRight': '5px'
                            }
                        ),
                        fac.AntdText(
                            icon,
                            copyable=True
                        )
                    ]
                ),
                span=6
            )
            for icon in Config.all_icons if re.findall(f'^{value}', icon) == [value]
        ]
