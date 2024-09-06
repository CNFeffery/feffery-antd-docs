import feffery_antd_components as fac
from dash.dependencies import Component
from datetime import datetime, timedelta


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            '精确日期匹配：明天',
            fac.AntdDateRangePicker(
                customCells=[
                    {
                        'year': datetime.now().year,
                        'month': datetime.now().month,
                        'date': (datetime.now() + timedelta(days=1)).day,
                        'style': {
                            'border': '1px dashed #595959',
                        },
                    }
                ]
            ),
            '年份通配：每年的本月第10天',
            fac.AntdDateRangePicker(
                customCells=[
                    {
                        'month': datetime.now().month,
                        'date': 10,
                        'style': {
                            'border': '1px dashed #595959',
                        },
                    }
                ]
            ),
            '年份+月份通配：每月的第10天',
            fac.AntdDateRangePicker(
                customCells=[
                    {
                        'date': 10,
                        'style': {
                            'border': '1px dashed #595959',
                        },
                    }
                ]
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        '精确日期匹配：明天',
        fac.AntdDateRangePicker(
            customCells=[
                {
                    'year': datetime.now().year,
                    'month': datetime.now().month,
                    'date': (datetime.now() + timedelta(days=1)).day,
                    'style': {
                        'border': '1px dashed #595959',
                    },
                }
            ]
        ),
        '年份通配：每年的本月第10天',
        fac.AntdDateRangePicker(
            customCells=[
                {
                    'month': datetime.now().month,
                    'date': 10,
                    'style': {
                        'border': '1px dashed #595959',
                    },
                }
            ]
        ),
        '年份+月份通配：每月的第10天',
        fac.AntdDateRangePicker(
            customCells=[
                {
                    'date': 10,
                    'style': {
                        'border': '1px dashed #595959',
                    },
                }
            ]
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
