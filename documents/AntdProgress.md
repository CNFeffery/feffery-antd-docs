**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**type：** *string*型，默认为`'line'`

　　用于*设置进度条类型*，可选的有`'line'`、`'circle'`、`'dashboard'`

**size：** *string*型，默认为`'default'`

　　用于*设置进度条的尺寸规格*，可选的有`'default'`、`'small'`

**percent：** *int*或*float*型，默认为`0`

　　用于*设置进度条对应的百分比*，取值应在0到100之间

**format：** *dict*型

　　用于*配置百分比文字内容*，可用的键值对参数有：

- **prefix：** *string*型，默认为`''`，用于*设置进度条百分比文字内容的前缀文字*
- **suffix：** *string*型，默认为`'%'`，用于*设置进度条百分比文字内容的后缀文字*
- **content：** *组件型*，用于*强制覆盖原有的百分比文字内容*

**status：** *string*型

　　用于*强制设置进度条的状态类型*，可选的有`'success'`、`'exception'`、`'normal'`、`'active'`，其中`'active'`仅`'line'`型进度条可用

**showInfo：** *bool*型，默认为`True`

　　用于*设置是否显示进度数值或状态图标*

**strokeColor：** *string*或*dict*型

　　用于*设置进度条颜色*，当传入*dict*型输入时可设置渐变色，可用的键值对参数有：

- **from：** *string*型，用于*设置进度条起始颜色*
- **to：** *string*型，用于*设置进度条终点颜色*

**strokeLinecap：** *string*型，默认为`'round'`

　　用于*设置进度条线型*，同`css`中的`stroke-linecap`属性，可选的有`'round'`、`'butt'`、`'square'`

**strokeWidth：** *int*型

　　用于*设置进度条像素线宽*

**trailColor：** *string*型

　　用于*设置进度条未完成部分的颜色*，默认无颜色

**width：** *int*型，默认为`132`

　　当`type`为`'circle'`和`'dashboard'`时可用，用于*设置画布像素宽度*

**gapDegree：** *int*型，默认为`75`

　　当`type`为`'dashboard'`时可用，用于*设置仪表盘进度条的缺口角度*，取值应在0到295之间

**gapPosition：** *string*型，默认为`'bottom'`

　　当`type`为`'dashboard'`时可用，用于*设置仪表盘缺口方向*，可选的有`'left'`、`'top'`、`'right'`、`'bottom'`

**steps：** *int*型

　　当`type`为`'line'`时可用，用于*设置分段进度条的分段数量*



