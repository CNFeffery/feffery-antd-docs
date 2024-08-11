import numpy as np
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {'title': '示例字段1', 'dataIndex': '示例字段1', 'width': '100'},
            {'title': '示例字段2', 'dataIndex': '示例字段2', 'width': '100'},
            {'title': '示例字段3', 'dataIndex': '示例字段3', 'width': '100'},
        ],
        data=[
            {
                '示例字段1': i,
                '示例字段2': i,
                '示例字段3': round(np.random.rand(), 3),
            }
            for i in range(10)
        ],
        bordered=True,
        conditionalStyleFuncs={
            '示例字段1': """
(record, index) => {
    if ( index % 2 === 1 ) {
        return {
            style: {
                backgroundColor: "#ebfbee"
            }
        }
    }
}
""",
            '示例字段2': """
(record, index) => {
    if ( index % 2 === 1 ) {
        return {
            style: {
                color: "red"
            }
        }
    }
}
""",
            '示例字段3': """
(record, index) => {
    if ( record['示例字段3'] <= 0.5 ) {
        return {
            style: {
                background: `linear-gradient(90deg, rgb(61, 153, 112) 0%, rgb(61, 153, 112) ${record['示例字段3']*100}%, white ${record['示例字段3']*100}%, white 100%)`,
                backgroundClip: 'padding-box'
            }
        };
    }
    return {
        style: {
            background: `linear-gradient(90deg, rgb(255, 65, 54) 0%, rgb(255, 65, 54) ${record['示例字段3']*100}%, white ${record['示例字段3']*100}%, white 100%)`,
            backgroundClip: 'padding-box'
        }
    };
}
""",
        },
    )

    return demo_contents


code_string = [
    {
        'code': '''
fac.AntdTable(
    columns=[
        {'title': '示例字段1', 'dataIndex': '示例字段1', 'width': '100'},
        {'title': '示例字段2', 'dataIndex': '示例字段2', 'width': '100'},
        {'title': '示例字段3', 'dataIndex': '示例字段3', 'width': '100'},
    ],
    data=[
        {
            '示例字段1': i,
            '示例字段2': i,
            '示例字段3': round(np.random.rand(), 3),
        }
        for i in range(10)
    ],
    bordered=True,
    conditionalStyleFuncs={
        '示例字段1': """
(record, index) => {
    if ( index % 2 === 1 ) {
        return {
            style: {
                backgroundColor: "#ebfbee"
            }
        }
    }
}
""",
        '示例字段2': """
(record, index) => {
    if ( index % 2 === 1 ) {
        return {
            style: {
                color: "red"
            }
        }
    }
}
""",
        '示例字段3': """
(record, index) => {
    if ( record['示例字段3'] <= 0.5 ) {
        return {
            style: {
                background: `linear-gradient(90deg, rgb(61, 153, 112) 0%, rgb(61, 153, 112) ${record['示例字段3']*100}%, white ${record['示例字段3']*100}%, white 100%)`,
                backgroundClip: 'padding-box'
            }
        };
    }
    return {
        style: {
            background: `linear-gradient(90deg, rgb(255, 65, 54) 0%, rgb(255, 65, 54) ${record['示例字段3']*100}%, white ${record['示例字段3']*100}%, white 100%)`,
            backgroundClip: 'padding-box'
        }
    };
}
""",
    },
)
'''
    }
]
