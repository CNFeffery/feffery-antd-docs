import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCascader(
        placeholder='请选择',
        optionsMode='flat',
        options=[
            {'value': '1', 'label': '节点1', 'key': '1'},
            *[
                {
                    'value': f'1-{i}',
                    'label': f'节点1-{i}',
                    'key': f'1-{i}',
                    'parent': '1',
                }
                for i in range(1, 4)
            ],
            {'value': '2', 'label': '节点2', 'key': '2'},
            {'value': '2-1', 'label': '节点2-1', 'key': '2-1', 'parent': '2'},
            {'value': '2-2', 'label': '节点2-2', 'key': '2-2', 'parent': '2'},
            *[
                {
                    'value': f'2-2-{i}',
                    'label': f'节点2-2-{i}',
                    'key': f'2-2-{i}',
                    'parent': '2-2',
                }
                for i in range(1, 4)
            ],
        ],
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdCascader(
    placeholder='请选择',
    optionsMode='flat',
    options=[
        {
            'value': '1',
            'label': '节点1',
            'key': '1'
        },
        *[
            {
                'value': f'1-{i}',
                'label': f'节点1-{i}',
                'key': f'1-{i}',
                'parent': '1'
            }
            for i in range(1, 4)
        ],
        {
            'value': '2',
            'label': '节点2',
            'key': '2'
        },
        {
            'value': '2-1',
            'label': '节点2-1',
            'key': '2-1',
            'parent': '2'
        },
        {
            'value': '2-2',
            'label': '节点2-2',
            'key': '2-2',
            'parent': '2'
        },
        *[
            {
                'value': f'2-2-{i}',
                'label': f'节点2-2-{i}',
                'key': f'2-2-{i}',
                'parent': '2-2'
            }
            for i in range(1, 4)
        ],
    ]
)
"""
    }
]
