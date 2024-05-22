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
                            width: 20,
                            transition: 'width 0.15s'
                        }
                    }
                );
                window.dash_clientside.set_props(
                    'side-menu-container',
                    {
                        style: {
                            opacity: 0,
                            transition: 'opacity 0s'
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
                            width: 325,
                            transition: 'width 0.15s'
                        }
                    }
                );
                window.dash_clientside.set_props(
                    'side-menu-container',
                    {
                        style: {
                            opacity: 1,
                            transition: 'opacity 0.15s'
                        }
                    }
                );
            }
            return window.dash_clientside.no_update;
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
        toggleSidePropsBarVisible: (nClicks, originStyle) => {
            // 若先前处于显示状态
            if (!originStyle.display) {
                return [
                    {
                        paddingTop: 3,
                        display: 'none'
                    },
                    false,
                    Date.now().toString()
                ]
            }

            return [
                {
                    paddingTop: 3
                },
                true,
                Date.now().toString()
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
                {
                    width: 150
                },
                'antd-menu-unfold'
            ]
        },
    }
});