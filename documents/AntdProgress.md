**type：** *string*型，默认为`'line'`

　　用于设置*进度条类型*，可选的有`'line'`（条形）、`'circle'`（环形）及`'dashboard'`（仪表盘型）

**size：** *string*型，默认为`'default'`

　　用于设置*进度条尺寸大小*，可选的有`'default'`与`'small'`

**percent：** *int*或*float*型，默认为`0`

　　用于设置进度条对应的*百分比*，取值在`0`到`100`之间，当设置为`100`时进度条会自动渲染为*完成状态*

**format：** *dict*型

　　用于自定义*百分比数值格式*，可用的键值对有：

- prefix：*string*型，用于设置百分比数值*前缀文字*
- suffix：*string*型，用于设置百分比数值*后缀文字*，默认为`'%'`
- content：*string*型，用于直接设置要显示的实际内容，用于替代原有的百分比数值

**status：** *string*型

　　仅当`type='line'`时有效，用于自定义*进度条状态*，可选的有`'success'`、`'exception'`、`'normal'`及`'active'`，其中`'active'`仅线型进度条可用

**showInfo：** *bool*型，默认为`True`

　　用于设置*是否显示进度百分比数值及状态图标*

**strokeColor：** *string*或*dict*型

　　用于设置*进度条颜色*，当传入*string*型时，接受*css合法色彩值*；当传入*dict*型时，可通过键值对`from`、`to`分别传入*css合法色彩值*用于实现*渐变色*进度条

**strokeLinecap：** *string*型，默认为`'round'`

　　用于设置*进度条的线型*，可选的有`'round'`与`'square'`

**width：** *int*型，默认为`132`

　　当`type='circle'`或`type='dashboard'`时，用于设置*画布像素宽度*

**strokeWidth：** *int*型

　　用于设置*进度条宽度*，针对不同`type`的进度条单位不同，当`type='line'`时，代表像素宽度，默认为`10`；当`type='circle'`或`type='dashboard'`时，代表其占`width`值的**百分比**，默认为`6`

**trailColor：** *string*型

　　用于设置*未满100%剩余进度条部分的颜色*

**gapDegree：** *int*型，默认为`75`

　　针对`type='dashboard'`模式，用于设置*仪表盘进度条的缺口部分弧度（单位：度）*，取值应在`0`到`295`之间

**gapPosition：** *string*型，默认为`'bottom'`

　　针对`type='dashboard'`模式，用于设置*仪表盘进度条缺口方位*，可选的有`'top'`、`'bottom'`、`'left'`与`'right'`

**steps：** *int*型

　　针对`type='line'`模式，用于设置*进度条的分段数量*