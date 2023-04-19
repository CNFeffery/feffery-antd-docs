window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        handleSideMenuCollapse: (nClicks, oldStyle) => {
            if (nClicks) {
                if (oldStyle.width === '325px') {
                    return [
                        {
                            'width': 20,
                            'height': '100vh',
                            'transition': 'width 0.2s',
                            'borderRight': '1px solid rgb(240, 240, 240)',
                            'paddingRight': 20
                        },
                        'antd-arrow-right'
                    ]
                }
                return [
                    {
                        'width': '325px',
                        'height': '100vh',
                        'transition': 'width 0.2s',
                        'borderRight': '1px solid rgb(240, 240, 240)',
                        'paddingRight': 20
                    },
                    'antd-arrow-left'
                ]
            }
            return window.dash_clientside.no_update;
        },
        handleSidePropsCollapse: (nClicks, sidePropsWidth, oldStyle) => {
            if (window.dash_clientside.callback_context.triggered[0]) {
                if (window.dash_clientside.callback_context.triggered[0]['prop_id'] === 'fold-side-props.nClicks' && nClicks) {
                    if (oldStyle.width !== 0) {
                        return [
                            {
                                'width': 0,
                                'height': '100vh',
                                'padding': '0 10px',
                                'position': 'relative',
                                'background': '#f2f3f5',
                                'transition': 'width 0.15s ease'
                            },
                            'antd-arrow-left'
                        ]
                    }
                    return [
                        {
                            'width': sidePropsWidth || 500,
                            'height': '100vh',
                            'padding': '0 20px',
                            'position': 'relative',
                            'background': '#f2f3f5',
                            'transition': 'width 0.4s ease'
                        },
                        'antd-arrow-right'
                    ]
                } else if (window.dash_clientside.callback_context.triggered[0]['prop_id'] === 'side-props-width.data' && sidePropsWidth) {
                    return [
                        {
                            'width': sidePropsWidth,
                            'height': '100vh',
                            'padding': '0 20px',
                            'position': 'relative',
                            'background': '#f2f3f5',
                            'transition': 'width 0.15s ease'
                        },
                        'antd-arrow-right'
                    ]
                }
            }

            return window.dash_clientside.no_update;
        },
        handleSidePropsResize: (nClicksPlus, nClicksMinus, data) => {
            data = data || 500
            if (window.dash_clientside.callback_context.triggered[0]['prop_id'] === 'side-props-width-plus.nClicks' && nClicksPlus) {
                return [
                    data + 50,
                    data + 50 >= 700,
                    data + 50 <= 400
                ]
            } else if (window.dash_clientside.callback_context.triggered[0]['prop_id'] === 'side-props-width-minus.nClicks' && nClicksMinus) {
                return [
                    data - 50,
                    data - 50 >= 700,
                    data - 50 <= 400
                ]
            }

            return [
                data,
                data >= 700,
                data <= 400
            ];
        }
    }
});