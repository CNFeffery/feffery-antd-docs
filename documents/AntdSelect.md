**placeholder：** *string*型

　　用于设置空白输入下的填充说明文字

**options：** *list*型，必填，无默认值

　　用于设置下拉选择区域每个选项的信息，常规组织方式与分组组织方式所需的格式参考下面，其中对于每个选项，`'label'`设置对应选项的显示文字，`'value'`设置对应选项被选中后对应的返回值（*string*或*int*型），`'disabled'`设置对应选项是否处于*不可选择*状态，`'colors'`用于开启*色带渲染*模式（传入由`css`中合法色彩输入所组成的列表）；对于分组，`'group'`用于设置组名，`'options'`传入若干常规组织方式下的多个选项所构成的列表：

```python
# 常规组织方式
options = [
    {'label': '中国', 'value': '中国'},
    {'label': '美国', 'value': '美国'},
    {'label': '俄罗斯', 'value': '俄罗斯'},
    {'label': '德国', 'value': '德国', 'disabled': True},
    {'label': '加拿大', 'value': '加拿大'}
]

# 分组组织方式
options = [
    {
        'group': '亚洲',
        'options': [
            {'label': '中国', 'value': '中国'}
        ]
    },
    {
        'group': '北美洲',
        'options': [
            {'label': '美国', 'value': '美国'},
            {'label': '加拿大', 'value': '加拿大'}
        ]
    },
    {
        'group': '欧洲',
        'options': [
            {'label': '俄罗斯', 'value': '俄罗斯'},
            {'label': '德国', 'value': '德国'}
        ]
    }
]
```

**mode：** *string*型或*None*，默认为`None`

　　用于设置下拉选择模式，可选项有`'multiple'`（多选）、`'tags'`（自由新增模式）、`None`（单选）

**colorsMode：** *string*型，默认为`'sequential'`

　　用于设置具体的*色带渲染模式*，可选的有`'sequential'`（连续色带）及`'diverging'`（离散色带）

**colorsNameWidth：** *int*型，默认为`40`

　　用于设置*色带渲染*模式下，色带前`label`部分的像素宽度

**defaultValue：** *list*型、string型或*list*型

　　用于设置默认被选中的单个选项的`'value'`值，或多个选项的`'value'`值构成的列表

**maxTagCount：** *int*型，默认为5

　　用于限定已选择选项在输入框内*最多存放*的数量，超出部分会省略为*数字记号*

**listHeight：** *int*型，默认为256

　　用于设置下拉选择框的最大*像素高度*，超出部分则需使用滑轮滑动浏览

**placement：** *str*型，默认为`'bottomLeft'`

　　用于设置*悬浮层展开方位*，可选的有`'bottomLeft'`、`'bottomRight'`、`'topLeft'`及`'topRight'`

**status：** *str型*

　　用于*手动设置组件的校验状态*，可选的有`'error'`和`'warning'`

**optionFilterProp：** *string*型，默认为`'value'`

　　用于*设置基于输入框内输入内容进行搜索的目标字段*，可选的有`'value'`、`'label'`

**value：** *list*型、string型或*list*型

　　用于在回调中捕获用户选的单个选项的`'value'`值，或多个选项的`'value'`值构成的列表



