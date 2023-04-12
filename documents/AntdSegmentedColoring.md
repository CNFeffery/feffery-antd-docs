**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**breakpoints：** `list[int]`型，必填

　　用于*设置或监听当前的各分段断点值*

**colors：** `list[string]`型，必填

　　用于*设置与断点各区间一一对应的色彩值*，`color`数组长度应为`breakpoints`数组长度-1

**controls：** *bool*型，默认为`True`

　　用于*设置是否在每个数字输入框右侧内部添加辅助快捷增减按钮*

**keyboard：** *bool*型，默认为`True`

　　用于*设置是否允许通过键盘上下键调整各个数字输入框的数值*

**min：** *int*、*float*或*string*型

　　用于*设置数字输入框的合法数值下限*，默认无限制

**max：** *int*、*float*或*string*型

　　用于*设置数字输入框的合法数值上限*，默认为限制

**step：** *int*、*float*或*string*型

　　用于*设置数字输入框的增减步长*

**precision：** *int*型

　　用于*设置数字输入框的数值精度即小数位数*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**size：** *string*型，默认为`'middle'`

　　用于*设置当前组件的尺寸规格*，可选项有`'small'`、`'middle'`和`'large'`

**bordered：** *bool*型，默认为`True`

　　用于*设置是否渲染边框*

**placeholder：** *string*型

　　用于*设置为各输入框统一设置空白输入下的填充说明文字*

**readOnly：** *bool*型

　　用于*设置是否以只读模式进行展示*

**pureLegend：** *bool*型，默认为`False`

　　用于*设置是否开启纯图例模式*

**inputNumberStyle：** *dict*型

　　用于*统一为数字输入框设置css样式*

**colorBlockStyle：** *dict*型

　　用于*统一为色块设置css样式*

**colorBlockPosition：** *string*型

　　用于*设置色块相对于数字输入框的位置*，可选的有`'left'`、`'right'`

**pureLegendLabelStyle：** *dict*型

　　当`pureLegend=True`时，用于*设置图例文字的css样式*