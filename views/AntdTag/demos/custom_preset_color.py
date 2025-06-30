import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('使用示例', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    fac.AntdTag(content=i, style=generate_tag_colors(i))
                    for i in [
                        '#8039d6',
                        '#d63987',
                        'rgb(63 215 121)',
                        'rgb(60, 150, 231)',
                        'rgb(198 143 22 / 100%)',
                        'rgba(231, 76, 60, 1)',
                    ]
                ],
                wrap=True,
            ),
            fac.AntdDivider('请选择颜色', innerTextOrientation='left'),
            fac.AntdColorPicker(
                id='tag-color-picker-demo',
                placement='top',
                showText=True,
            ),
            fac.AntdTag(
                content='自定义标签',
                id='tag-color-picker-tag-demo',
            ),
        ],
        direction='vertical',
        style={
            'width': '100%',
        },
    )

    return demo_contents


def generate_tag_colors(font_color):
    """
    根据给定的字体颜色生成适合的标签颜色。
    注：在浅色字体情况下表现不好。

    参数:
    font_color (str): 字体颜色，接受HEX、RGB、HSB格式。

    返回:
    适用于Dash style属性的字典，包含字体颜色、背景颜色、边框颜色。
    """
    import colorsys

    def hex_to_rgb(hex_code):
        if hex_code.startswith('#'):
            hex_code = hex_code.lstrip('#')

        r = int(hex_code[:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)

        return r, g, b

    if '#' in font_color:
        rgb_color = hex_to_rgb(font_color)
        _h, _l, _s = colorsys.rgb_to_hls(*rgb_color)
    elif 'rgb' in font_color:
        rgb = (
            font_color.split('(')[1]
            .split(')')[0]
            .split(',' if ',' in font_color else ' ')[:3]
        )
        r, g, b = (
            int(rgb[0]),
            int(rgb[1]),
            int(rgb[2].split('/')[0]) if '/' in rgb[2] else int(rgb[2]),
        )
        _h, _l, _s = colorsys.rgb_to_hls(r, g, b)
    elif 'hsb' in font_color:
        hsb = (
            font_color.split('(')[1]
            .split(')')[0]
            .split(',' if ',' in font_color else ' ')[:3]
        )
        __h, __s, __b = (
            float(int(hsb[0].strip()) / 360),
            float(hsb[1].strip().replace('%', '')) / 100.0
            if '%' in hsb[1]
            else float(hsb[1].strip()),
            float(hsb[2].strip().replace('%', '')) / 100.0
            if '%' in hsb[1]
            else float(hsb[1].strip()),
        )

        r, g, b = colorsys.hsv_to_rgb(__h, __s, __b)
        _h, _l, _s = colorsys.rgb_to_hls(r, g, b)
        # 转换为hsl格式供web使用
        font_color = f'hsl({_h * 360}, {_s * 100.0:.2f}%, {_l * 100.0:.2f}%)'
    else:
        return None

    background_hsl = f'hsl({_h * 360:.0f}, 100%, 95%)'
    border_hsl = f'hsl({_h * 360:.0f}, 100%, 70%)'

    return {
        'color': font_color,
        'background-color': background_hsl,
        'border-color': border_hsl,
    }


@app.callback(
    Output('tag-color-picker-tag-demo', 'style'),
    Input('tag-color-picker-demo', 'value'),
)
def callback_func(value):
    value = value or '#1677ff'

    return generate_tag_colors(value)


code_string = [
    {
        'code': '''
fac.AntdSpace(
    [
        fac.AntdDivider('使用示例', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                fac.AntdTag(content=i, style=generate_tag_colors(i))
                for i in [
                    '#8039d6',
                    '#d63987',
                    'rgb(63 215 121)',
                    'rgb(60, 150, 231)',
                    'rgb(198 143 22 / 100%)',
                    'rgba(231, 76, 60, 1)',
                ]
            ],
            wrap=True,
        ),
        fac.AntdDivider('请选择颜色', innerTextOrientation='left'),
        fac.AntdColorPicker(
            id='tag-color-picker-demo',
            placement='top',
            showText=True,
        ),
        fac.AntdTag(
            content='自定义标签',
            id='tag-color-picker-tag-demo',
        ),
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)


def generate_tag_colors(font_color):
    """
    根据给定的字体颜色生成适合的标签颜色。
    注：在浅色字体情况下表现不好。

    参数:
    font_color (str): 字体颜色，接受HEX、RGB、HSB格式。

    返回:
    适用于Dash style属性的字典，包含字体颜色、背景颜色、边框颜色。
    """
    import colorsys
    def hex_to_rgb(hex_code):
        if hex_code.startswith('#'):
            hex_code = hex_code.lstrip('#')

        r = int(hex_code[:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)

        return r, g, b

    if '#' in font_color:
        rgb_color = hex_to_rgb(font_color)
        _h, _l, _s = colorsys.rgb_to_hls(*rgb_color)
    elif 'rgb' in font_color:
        rgb = (
            font_color.split('(')[1]
            .split(')')[0]
            .split(',' if ',' in font_color else ' ')[:3]
        )
        r, g, b = (
            int(rgb[0]),
            int(rgb[1]),
            int(rgb[2].split('/')[0]) if '/' in rgb[2] else int(rgb[2]),
        )
        _h, _l, _s = colorsys.rgb_to_hls(r, g, b)
    elif 'hsb' in font_color:
        hsb = (
            font_color.split('(')[1]
            .split(')')[0]
            .split(',' if ',' in font_color else ' ')[:3]
        )
        __h, __s, __b = (
            float(int(hsb[0].strip()) / 360),
            float(hsb[1].strip().replace('%', '')) / 100.0
            if '%' in hsb[1]
            else float(hsb[1].strip()),
            float(hsb[2].strip().replace('%', '')) / 100.0
            if '%' in hsb[1]
            else float(hsb[1].strip()),
        )

        r, g, b = colorsys.hsv_to_rgb(__h, __s, __b)
        _h, _l, _s = colorsys.rgb_to_hls(r, g, b)
        # 转换为hsl格式供web使用
        font_color = f'hsl({_h*360}, {_s*100.0:.2f}%, {_l*100.0:.2f}%)'
    else:
        return None

    background_hsl = f'hsl({_h*360:.0f}, 100%, 95%)'
    border_hsl = f'hsl({_h*360:.0f}, 100%, 70%)'

    return {
        'color': font_color,
        'background-color': background_hsl,
        'border-color': border_hsl,
    }


@app.callback(
    Output('tag-color-picker-tag-demo', 'style'),
    Input('tag-color-picker-demo', 'value'),
)
def callback_func(value):
    value = value or '#1677ff'

    return generate_tag_colors(value)

'''
    }
]
