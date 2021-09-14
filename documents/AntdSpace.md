**children：**

　　用于传入需要规整对齐的各个*子元素组件*

**align：** *string*型

　　用于设置内部嵌套组件的*对齐方式*，可选的有`'start'`、`'end'`、`'center'`、`'baseline'`

**direction：** *string*型，默认为`'horizontal'`

　　用于设置内部组件*排列方向*，可选的有`'vertical'`（竖直排列）及`'horizontal'`（水平排列）

**size：** *string*或*int*型，默认为`'small'`

　　用于设置内部排列组件的*间隔大小*，可选的有`'small'`、`'middle'`、`'large'`，或传入*int*型代表像素单位间隔

**addSplitLine：** *bool*型，默认为`False`

　　用于设置是否为内部排列的各个组件之间*添加分隔线*

**wrap：** *bool*型，默认为`False`

　　仅在**水平排列模式**时可用，用于设置是否在内部排列的组件宽度溢出时*自动换行*

