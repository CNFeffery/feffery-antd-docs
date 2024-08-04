import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyStyle(
            rawStyle="""
.check-card-group-custom-style-demo .ant-pro-checkcard-content {
    padding: 5px 12px;
}
"""
        ),
        fac.AntdCheckCardGroup(
            [
                fac.AntdCheckCard(
                    f'选项{i}',
                    value=i,
                    style={
                        'width': 'auto',
                        'marginRight': 3,
                        'marginBottom': 3,
                        'borderRadius': 5,
                    },
                )
                for i in range(1, 26)
            ],
            className='check-card-group-custom-style-demo',
            defaultValue=[4, 8, 9, 15],
            multiple=True,
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': '''
[
    fuc.FefferyStyle(
        rawStyle="""
.check-card-group-custom-style-demo .ant-pro-checkcard-content {
    padding: 5px 12px;
}
"""
    ),
    fac.AntdCheckCardGroup(
        [
            fac.AntdCheckCard(
                f'选项{i}',
                value=i,
                style={
                    'width': 'auto',
                    'marginRight': 3,
                    'marginBottom': 3,
                    'borderRadius': 5,
                },
            )
            for i in range(1, 26)
        ],
        className='check-card-group-custom-style-demo',
        defaultValue=[4, 8, 9, 15],
        multiple=True,
    ),
]
'''
    }
]
