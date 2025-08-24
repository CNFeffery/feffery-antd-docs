import feffery_antd_components as fac
import numpy as np
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        # 构造演示用例相关内容
        demo_contents = fac.AntdTable(
            columns=[
                {"title": "示例字段1", "dataIndex": "示例字段1", "width": "100"},
                {"title": "示例字段2", "dataIndex": "示例字段2", "width": "100"},
                {"title": "示例字段3", "dataIndex": "示例字段3", "width": "100"},
            ],
            data=[
                {
                    "示例字段1": i,
                    "示例字段2": i,
                    "示例字段3": round(np.random.rand(), 3),
                }
                for i in range(10)
            ],
            bordered=True,
            conditionalStyleFuncs={
                "示例字段1": """
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
                "示例字段2": """
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
                "示例字段3": """
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

    elif current_locale == "en-us":
        # construct demo contents (dataIndex translated too)
        demo_contents = fac.AntdTable(
            columns=[
                {
                    "title": "Example Field 1",
                    "dataIndex": "Example Field 1",
                    "width": "100",
                },
                {
                    "title": "Example Field 2",
                    "dataIndex": "Example Field 2",
                    "width": "100",
                },
                {
                    "title": "Example Field 3",
                    "dataIndex": "Example Field 3",
                    "width": "100",
                },
            ],
            data=[
                {
                    "Example Field 1": i,
                    "Example Field 2": i,
                    "Example Field 3": round(np.random.rand(), 3),
                }
                for i in range(10)
            ],
            bordered=True,
            conditionalStyleFuncs={
                "Example Field 1": """
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
                "Example Field 2": """
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
                "Example Field 3": """
(record, index) => {
    if ( record['Example Field 3'] <= 0.5 ) {
        return {
            style: {
                background: `linear-gradient(90deg, rgb(61, 153, 112) 0%, rgb(61, 153, 112) ${record['Example Field 3']*100}%, white ${record['Example Field 3']*100}%, white 100%)`,
                backgroundClip: 'padding-box'
            }
        };
    }
    return {
        style: {
            background: `linear-gradient(90deg, rgb(255, 65, 54) 0%, rgb(255, 65, 54) ${record['Example Field 3']*100}%, white ${record['Example Field 3']*100}%, white 100%)`,
            backgroundClip: 'padding-box'
        }
    };
}
""",
            },
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": '''
import numpy as np
fac.AntdTable(
    columns=[
        {"title": "示例字段1", "dataIndex": "示例字段1", "width": "100"},
        {"title": "示例字段2", "dataIndex": "示例字段2", "width": "100"},
        {"title": "示例字段3", "dataIndex": "示例字段3", "width": "100"},
    ],
    data=[
        {"示例字段1": i, "示例字段2": i, "示例字段3": round(np.random.rand(), 3)}
        for i in range(10)
    ],
    bordered=True,
    conditionalStyleFuncs={{
        "示例字段1": """
(record, index) => {
    if ( index % 2 === 1 ) {
        return { style: { backgroundColor: "#ebfbee" } }
    }
}
""",
        "示例字段2": """
(record, index) => {
    if ( index % 2 === 1 ) {
        return { style: { color: "red" } }
    }
}
""",
        "示例字段3": """
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
    }},
)
'''
            }
        ]

    elif current_locale == "en-us":
        return [
            {
                "code": '''
import numpy as np
fac.AntdTable(
    columns=[
        {"title": "Example Field 1", "dataIndex": "Example Field 1", "width": "100"},
        {"title": "Example Field 2", "dataIndex": "Example Field 2", "width": "100"},
        {"title": "Example Field 3", "dataIndex": "Example Field 3", "width": "100"},
    ],
    data=[
        {"Example Field 1": i, "Example Field 2": i, "Example Field 3": round(np.random.rand(), 3)}
        for i in range(10)
    ],
    bordered=True,
    conditionalStyleFuncs={{
        "Example Field 1": """
(record, index) => {
    if ( index % 2 === 1 ) {
        return { style: { backgroundColor: "#ebfbee" } }
    }
}
""",
        "Example Field 2": """
(record, index) => {
    if ( index % 2 === 1 ) {
        return { style: { color: "red" } }
    }
}
""",
        "Example Field 3": """
(record, index) => {
    if ( record['Example Field 3'] <= 0.5 ) {
        return {
            style: {
                background: `linear-gradient(90deg, rgb(61, 153, 112) 0%, rgb(61, 153, 112) ${record['Example Field 3']*100}%, white ${record['Example Field 3']*100}%, white 100%)`,
                backgroundClip: 'padding-box'
            }
        };
    }
    return {
        style: {
            background: `linear-gradient(90deg, rgb(255, 65, 54) 0%, rgb(255, 65, 54) ${record['Example Field 3']*100}%, white ${record['Example Field 3']*100}%, white 100%)`,
            backgroundClip: 'padding-box'
        }
    };
}
""",
    }},
)
'''
            }
        ]
