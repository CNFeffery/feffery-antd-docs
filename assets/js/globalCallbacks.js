// 改造console.error()以隐藏无关痛痒的警告信息
const originalConsoleError = console.error;
console.error = function (...args) {
    // 检查args中是否包含需要过滤的内容
    const shouldFilter = args.some(arg => typeof arg === 'string' && arg.includes('Warning:'));

    if (!shouldFilter) {
        originalConsoleError.apply(console, args);
    }
};

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        toggleSideMenuVisible: (nClicks, originIcon) => {
            if (originIcon === 'antd-arrow-left') {
                window.dash_clientside.set_props(
                    'toggle-side-menu-icon',
                    {
                        icon: 'antd-arrow-right'
                    }
                );
                window.dash_clientside.set_props(
                    'side-menu-affix',
                    {
                        style: {
                            width: 20
                        }
                    }
                );
                window.dash_clientside.set_props(
                    'side-menu-container',
                    {
                        style: {
                            opacity: 0
                        }
                    }
                );
            } else {
                window.dash_clientside.set_props(
                    'toggle-side-menu-icon',
                    {
                        icon: 'antd-arrow-left'
                    }
                );
                window.dash_clientside.set_props(
                    'side-menu-affix',
                    {
                        style: {
                            width: 325
                        }
                    }
                );
                window.dash_clientside.set_props(
                    'side-menu-container',
                    {
                        style: {
                            opacity: 1
                        }
                    }
                );
            }
        },
        handleMenuTargetScoll: (pathname) => {

            // 处理侧边菜单项滚动
            setTimeout(() => {
                // 查找当前页面中name为pathname的元素
                let scrollTarget = document.getElementsByName(pathname)
                if (scrollTarget.length > 0) {
                    // 滚动到该元素
                    scrollTarget[0].scrollIntoView({ behavior: "smooth" });
                }
            }, 1000)

        },
        toggleSidePropsVisible: (nClicks, originIcon) => {
            // 若先前处于显示状态
            if (originIcon === 'antd-arrow-right') {
                return [
                    {
                        width: 20
                    },
                    'antd-arrow-left'
                ]
            }

            return [
                {
                    width: 500
                },
                'antd-arrow-right'
            ]
        },
        toggleSidePropsBarVisible: (nClicks, pressedCounts, originStyle, focusing) => {
            // 若先前聚焦于搜索框内，且本次回调由esc键点按触发，隐藏搜索框
            if (window.dash_clientside.callback_context.triggered_id === 'doc-layout-listen-esc-press') {
                if (focusing) {
                    return [
                        {
                            paddingTop: 3,
                            display: 'none'
                        },
                        false,
                        Date.now().toString(),
                        null,
                        null
                    ]
                } else {
                    return window.dash_clientside.no_update;
                }
            }
            // 若先前处于显示状态
            if (!originStyle.display) {
                return [
                    {
                        paddingTop: 3,
                        display: 'none'
                    },
                    false,
                    Date.now().toString(),
                    null,
                    null
                ]
            }

            return [
                {
                    paddingTop: 3
                },
                true,
                Date.now().toString(),
                null,
                null
            ]
        },
        updateSidePropsMarkdownKeywords: (value) => value || null,
        toggleDemoCodeVisible: (nClicks, originStyle) => {
            // 若先前处于显示状态
            if (!originStyle?.display) {
                return {
                    display: 'none'
                }
            }
            return null;
        },
        toggleDocAnchorVisible: (nClicks, originIcon) => {
            // 若先前处于显示状态
            if (originIcon === 'antd-menu-unfold') {
                return [
                    {
                        width: 0,
                        display: 'none'
                    },
                    'antd-menu-fold'
                ]
            }

            return [
                {},
                'antd-menu-unfold'
            ]
        },
        smallScreenAutoCollapseSide: (responsive, nClicksLeft, nClicksRight, iconLeft, iconRight) => {
            // 满足较小屏幕尺寸规格要求
            if (!responsive?.lg) {
                return [
                    // 根据先前的导航菜单折叠状态，选择要更新的新状态
                    iconLeft === 'antd-arrow-left' ? (nClicksLeft || 0) + 1 : window.dash_clientside.no_update,
                    // 根据先前的侧边参数栏折叠状态，选择要更新的新状态
                    iconRight === 'antd-arrow-right' ? (nClicksRight || 0) + 1 : window.dash_clientside.no_update,
                    { display: 'none' },
                    { display: 'none' },
                    {}
                ]
            }
            return [
                window.dash_clientside.no_update,
                window.dash_clientside.no_update,
                {},
                {},
                { display: 'none' }
            ];
        },
        smallScreenUpdateHeader: (responsive) => {
            // 满足较小屏幕尺寸规格要求
            if (!responsive?.lg) {
                return [
                    { display: 'none' },
                    { display: 'none' },
                    {}
                ]
            }
            return [
                {},
                {},
                { display: 'none' }
            ];
        },
        handleSidePropsSearchScroll: (nSubmit, searchKeyword, status) => {
            // 若本次回调由关键词更新触发
            if (window.dash_clientside.callback_context.triggered_id === 'side-props-markdown') {
                // 延时执行，提升稳定性
                setTimeout(() => {
                    // 尝试提取有效的关键词节点数量
                    let highlightTargets = document.getElementsByClassName('side-props-keyword-highlight')

                    if (highlightTargets.length > 0) {
                        // 临时更新第一个关键词的样式
                        highlightTargets[0].style.color = 'red'
                        // 率先滚动到第一个关键词命中处
                        let targetsContainer = document.getElementById('side-props-markdown-container')
                        targetsContainer.scrollTo({
                            top: highlightTargets[0].offsetTop - 73,
                            behavior: 'smooth'
                        })
                        window.dash_clientside.set_props(
                            'side-props-markdown-search-status',
                            {
                                data: {
                                    total: highlightTargets.length,
                                    current: 0
                                }
                            }
                        )
                    } else {
                        window.dash_clientside.set_props(
                            'side-props-markdown-search-status',
                            {
                                data: null
                            }
                        )
                    }
                }, 500)
            } else if (window.dash_clientside.callback_context.triggered_id === 'side-props-search-bar-keyword') {
                // 若当前关键词搜索结果状态有效
                if (status) {
                    // 计算下一个目标关键词下标
                    let nextIndex;
                    if (status.current < status.total - 1) {
                        nextIndex = status.current + 1
                    } else {
                        nextIndex = 0
                    }
                    let highlightTargets = document.getElementsByClassName('side-props-keyword-highlight')
                    // 还原前一个关键词的样式
                    highlightTargets[status.current].style.color = null;
                    // 临时更新下一个关键词的样式
                    highlightTargets[nextIndex].style.color = 'red'
                    let targetsContainer = document.getElementById('side-props-markdown-container')
                    targetsContainer.scrollTo({
                        top: highlightTargets[nextIndex].offsetTop - 73,
                        behavior: 'smooth'
                    })
                    // 更新状态
                    window.dash_clientside.set_props(
                        'side-props-markdown-search-status',
                        {
                            data: {
                                total: highlightTargets.length,
                                current: nextIndex
                            }
                        }
                    )
                }
            }
            return window.dash_clientside.no_update;
        }
    }
});