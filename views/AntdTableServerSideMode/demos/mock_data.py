import numpy as np
import pandas as pd
from peewee import SqliteDatabase, CharField, IntegerField, Model, fn

# 生成演示用数据框
demo_df = (
    pd.DataFrame(
        {
            'id': list(range(1, 100001)),
            '字段1': np.random.choice(
                [
                    f'{s}{n}'
                    for s in list('abcdefghij')
                    for n in range(1, 10001)
                ],
                100000,
                replace=False,
            ),
            '字段2': np.random.choice(
                [f'类型{t}' for t in range(1, 11) for n in range(10000)],
                100000,
                replace=False,
            ),
        }
    )
    # 打乱顺序
    .sample(frac=1, replace=False)
)


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
    if (DemoTable.select(fn.count(DemoTable.id)).scalar()) == 0:
        # 分批插入
        for batch in range(10):
            (
                DemoTable.insert_many(
                    demo_df.iloc[
                        batch * 10000 : (batch + 1) * 10000, :
                    ].to_dict('records')
                ).execute()
            )
