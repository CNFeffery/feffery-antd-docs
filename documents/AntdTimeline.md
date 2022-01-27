**item：** *list*型

　　用于设置*按顺序定义时间轴节点*的数据结构，每个元素为*dict*型，可用的键值对参数有：

- content：*string*型，用于设置当前节点的*内容信息*
- color：*string*型，用于设置*节点颜色*，来表示节点的不同状态，推荐的配色有`'blue'`（表示正在进行或默认状态）、`'green'`（表示已完成状态）、`'red'`（表示警告或错误状态）、`'grey'`（表示为完成或失效状态），也可自行定义`css`合法色彩字符串
- icon：*string*型，用于设置*时间轴节点图标*，同`AntdIcon`的`icon`参数，不设置时默认为圆圈
- iconStyle：*dict*型，用于设置*节点图标的css样式*
- contentStyle：*dict*型，用于设置*content文字的css样式*
- label：*string*型，用于设置*节点标题内容*

**mode：** *string*型，默认为`'right'`

　　用于设置*节点内容相对于时间轴的位置方式*，可选的有`'left'`、`'alternate'`和`'right'`

**pending：** *string*型

　　用于设置*在时间轴末端要添加的“加载中”状态中幽灵节点对应的文字内容*，不设置则不会渲染该节点

**reverse：** *bool*型，默认为`False`

　　用于设置*时间轴的节点顺序是否按照从下往上的顺序排列*