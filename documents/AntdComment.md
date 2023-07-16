**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*需要向下嵌套的其他评论*

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**commentId：** *string*型

　　用于*设置当前评论的id信息*，便于后端数据库匹配

**authorName：** *string*型

　　用于*设置当前评论的作者名称*

**authorNameHref：** *string*型

　　用于*设置作者名称点击跳转链接*

**publishTime：** *dict*型，必填

　　用于*设置当前评论的发表时间*，可用的键值对参数有：

- **value：** *string*型，用于*设置当前评论发表日期时间字符串*
- **format：** *string*型，用于*设置与value对应的日期时间格式字符串*，[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)，常用的有`'YYYY-MM-DD hh:mm:ss'`

**fromNow：** *bool*型，默认为`False`

　　用于*设置是否以相对时间模式显示评论发表时间距今多长时间*

**showLikeDislike：** *bool*型，默认为`True`

　　用于*设置是否为当前评论渲染支持/反对按钮*

**showReply：** *bool*型，默认为`True`

　　用于*设置是否为当前评论渲染添加回复按钮*

**showDelete：** *bool*型，默认为`False`

　　用于*设置是否为当前评论渲染删除按钮*

**replyClicks：** *int*型，默认为`0`

　　用于*监听“添加回复”按钮被点击的次数*

**deleteClicks：** *int*型，默认为`0`

　　用于*监听“删除”按钮被点击的次数*

**commentContent：** *组件型*

　　用于*设置评论信息的正文内容*

**likesCount：** *int*型，默认为`0`

　　用于*设置当前评论的点赞次数*

**dislikesCount：** *int*型，默认为`0`

　　用于*设置当前评论的反对次数*

**action：** *string*型

　　用于*设置或监听当前评论处于的“已点赞”/“已反对”状态*，可选的有`'liked'`与`'disliked'`

**defaultAction：** *string*型

　　用于*设置当前评论初始化时处于的“已点赞”/“已反对”状态*，可选的有`'liked'`与`'disliked'`

**avatarProps：** *dict*型

　　用于*设置当前评论作者的头像相关属性*，与`AntdAvatar`参数一致

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题