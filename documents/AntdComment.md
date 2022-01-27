**children：**

　　用于传入*需要嵌套的其他评论*

**commentId：** *string*型

　　用于*设置当前评论的id信息*，主要用于方便后端数据库匹配

**authorName：** *string*型

　　设置*评论作者名称*

**authorNameHref：** *string*

　　设置*作者名称点击跳转链接*

**publishTime：** *dict*型

　　必填参数，用于*设置当前评论的发表时间*，可用的键值对参数有：

- value：*string*型，对应*评论发表时间的日期时间字符串*
- format：*string*型，用于*设置与value对应的日期时间格式字符串*，[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)，常用的有`'YYYY-MM-DD hh:mm:ss'`

**fromNow：** *bool*型，默认为`False`

　　用于设置*是否以相对时间模式显示评论发表时间距今多长时间*

**replyCounts：** *int*型，默认为`0`

　　用于*监听“添加回复”按钮被点击的次数*

**commentContent：** *string*型

　　用于*设置评论信息的正文内容*

**likesCount：** *int*型，默认为`0`

　　用于设置*当前评论的点赞次数*

**dislikesCount：** *int*型，默认为`0`

　　用于设置*当前评论的反对次数*

**action：** *string*型

　　用于设置*当前评论处于的“已点赞”/“已反对”状态*，可选的有`'liked'`与`'disliked'`

**defaultAction：** *string*型

　　用于设置*当前评论初始化时处于的“已点赞”/“已反对”状态*，可选的有`'liked'`与`'disliked'`

**avatarProps：** *dict*型

　　用于设置*当前评论作者的头像相关属性*，与`AntdAvatar`参数一致

　　