import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdTable 表格'},
                {'title': '服务端数据加载模式'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdTable 表格', level=2),
        *[
            fac.AntdParagraph('表格组件适用于大数据场景的服务端数据加载模式。'),
            fac.AntdDivider(isDashed=True),
            fac.AntdParagraph(
                [
                    '本页文档展示了',
                    fac.AntdText('AntdTable', strong=True),
                    '组件基于服务端数据加载模式，对大量数据的展示需求进行性能优化，本质上是在设置参数',
                    fac.AntdText('mode="server-side"', code=True),
                    '后，通过监听',
                    fac.AntdText('AntdTable', strong=True),
                    '中翻页、排序、筛选等常见交互行为对应的监听参数变化，进而通过回调函数传递到后端进行对应数据帧的生成，并传回',
                    fac.AntdText('AntdTable', strong=True),
                    '中进行展示，相当于任意时刻下，表格中实际加载的数据只有用户所看到的当页数据',
                ],
                style={'textIndent': '2rem'},
            ),
            fac.AntdParagraph(
                [
                    fac.AntdText('注意', strong=True),
                    '，本页文档后续所有与',
                    fac.AntdText('demo_df', code=True),
                    '有关的示例中，',
                    fac.AntdText('demo_df', code=True),
                    '均为同一个',
                    fac.AntdText('pandas', strong=True),
                    '数据框，由下列代码生成：',
                ],
                style={'textIndent': '2rem', 'marginBottom': 0},
            ),
            fac.AntdCollapse(
                fmc.FefferySyntaxHighlighter(
                    showCopyButton=True,
                    showLineNumbers=True,
                    language='python',
                    codeTheme='coy-without-shadows',
                    codeString="""
import pandas as pd

# 生成演示用数据框
demo_df = (
    pd
    .DataFrame(
        {
            'id': list(range(1, 100001)),
            '字段1': np.random.choice(
                [
                    f'{s}{n}'
                    for s in list('abcdefghij')
                    for n in range(1, 10001)
                ],
                100000,
                replace=False
            ),
            '字段2': np.random.choice(
                [
                    f'类型{t}'
                    for t in range(1, 11)
                    for n in range(10000)
                ],
                100000,
                replace=False
            )
        }
    )
    # 打乱顺序
    .sample(frac=1, replace=False)
)
""",
                ),
                isOpen=False,
                title='演示用数据框生成代码',
                ghost=True,
            ),
            fac.AntdParagraph(
                [
                    '本页文档后续所有与',
                    fac.AntdText('DemoTable', code=True),
                    '有关的示例中，',
                    fac.AntdText('DemoTable', code=True),
                    '均为同一个基于',
                    fac.AntdText('peewee', strong=True),
                    '定义的',
                    fac.AntdText('ORM', strong=True),
                    '模型类，由下列代码定义：',
                ],
                style={'textIndent': '2rem', 'marginBottom': 0},
            ),
            fac.AntdCollapse(
                fmc.FefferySyntaxHighlighter(
                    showCopyButton=True,
                    showLineNumbers=True,
                    language='python',
                    codeTheme='coy-without-shadows',
                    codeString="""
from peewee import (
    SqliteDatabase,
    CharField,
    IntegerField,
    Model,
    fn
)

...

# 构造演示用数据库表模型类，基于sqlite+peewee
db = SqliteDatabase('./demo_table.db')


class DemoTable(Model):

    id = IntegerField()

    字段1 = CharField()

    字段2 = CharField()

    class Meta:

        table_name = 'demo_table'
        database = db


# 创建表格并插入示例数据
db.create_tables([DemoTable])

# 为方便调试，先检查数据表中是否已有记录，若有则跳过数据插入
with db.atomic():

    if (
        DemoTable
        .select(fn.count(DemoTable.id))
        .scalar()
    ) == 0:

        # 分批插入
        for batch in range(10):
            (
                DemoTable
                .insert_many(
                    demo_df
                    .iloc[batch*10000:(batch+1)*10000, :]
                    .to_dict('records')
                )
                .execute()
            )
""",
                ),
                isOpen=False,
                title='演示用数据库表模型生成代码',
                ghost=True,
            ),
        ],
        fac.AntdDivider(isDashed=True),
    ]
