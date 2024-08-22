## `fac` 组件文档页英文文档贡献指南

`fac`（`feffery-antd-components`）官网文档已新增国际化多语种切换功能，目前支持的语种有`zh-cn`（简体中文）、`en-us`（美国英语），欢迎一起参与英文文档建设，下面是针对`fac`官网中各个组件文档页进行国际化多语种改造的步骤及注意事项：

### 1 步骤

#### 第一步

`fork`本项目仓库（ https://github.com/CNFeffery/feffery-antd-docs ），并`clone`已`fork`的仓库到本地。

#### 第二步

在[issues](https://github.com/CNFeffery/feffery-antd-docs/issues)中查找自己想要进行贡献的组件，是否已存在重复主题的`issue`，若无，推荐按照下列标题格式创建组件国际化文档贡献`issue`：

> [doc i18n] AntdXXX

我们会查看相关新建`issue`，并在确认后在`issue`内`assign`给创建者，表示已确认。

#### 第三步

每页组件文档右侧边中的组件参数说明，是基于组件的`__doc__`属性自动渲染的，我们需要在项目的`public/api_documents/en_us`目录下准备对应的英文翻译内容，推荐在项目根目录终端执行`python export_api_document.py 组件名`，会自动将对应组件的`__doc__`信息导出为`public/api_documents/en_us`目录下相应的`markdown`文件，譬如：

<p align="center"><img src="https://github.com/user-attachments/assets/888e637b-1955-4c93-8c04-2819140c223a" /></p>

接着可以基于常用的大语言模型类应用辅助翻译，将翻译完成后的内容粘贴回原`markdown`文件即可。

#### 第四步

重构`views`模块下对应组件文档页模块的`intro.py`，使用`i18n`中的`translator.t()`对需要自动语种转化的内容进行包裹，`translator.t()`会基于`public/locales.json`中配置的全局通用翻译对照关系，自动处理`intro.py`中相关内容在不同国际化模式下的内容显示 😉，以`views/AntdParagraph/intro.py`为例：

<p align="center"><img src="https://github.com/user-attachments/assets/3a6788ad-bd8c-4b7a-bb44-9d968b050da3" /></p>

对于未在`public/locales.json`中定义过的文案翻译关系，请在末尾进行补充，借助`codeium`等 AI 插件，可以高效的实现文案翻译关系的自动生成：

<p align="center"><img src="https://github.com/user-attachments/assets/b8eea88b-4d8c-4896-bf86-6a2bf52285b4" /></p>

#### 第五步

重构`views`模块下对应组件文档页模块的`demos/__init__.py`，开头导包部分新增`from functools import partial`和`from i18n import translator`：

<p align="center"><img src="https://github.com/user-attachments/assets/eddcd84e-3b4d-4442-80c2-cdd8c1cb24f1" /></p>

重构原本`list`类型的`demos_config`为函数，从而配合`i18n.translator`进行动态自动翻译，基于函数内部通过`partial()`改造的`t()`函数（其中参数`topic`写入当前组件名，需配合`public/topic_locales`中对应主题的`组件名.json`），对返回内容中的`'title'`、`'description'`字段内容进行包裹翻译：

> 注意，针对原本为组件型的`'description'`字段，请将其内容改写为`markdown`格式字符串，再使用`t()`进行包裹，譬如：<br>
> <p align="center"><img src="https://github.com/user-attachments/assets/b1a5acff-7c70-4bf8-81d6-34b8f54ef2f5" /></p>

<p align="center"><img src="https://github.com/user-attachments/assets/6ad72031-a09c-4abf-b557-87ea8d0799d0" /></p>

#### 第六步（可选的）

针对某个组件文档页，通过第三步到第五步的操作后，文档网站中对应的绝大部分内容已经可以呈现出自动国际化翻译效果，以`AntdParagraph`文档页为例：

<p align="center"><img src="https://github.com/user-attachments/assets/db32d28b-e182-4985-8301-60306ef0ffaf" /></p>

如果你需要对部分示例内容及源码查看也进行国际化转换，可以参考譬如`AntdButton`中相关示例的方式，配合`i18n`模块中的`get_current_locale()`：

> [basic_usage.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdButton/demos/basic_usage.py)<br>
> [basic_callbacks.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdButton/demos/basic_callbacks.py)

譬如针对`AntdParagraph`的中文示例中使用到中国古代著名诗人*李白*所著的《将进酒》，在`en-us`模式下替换为*莎士比亚*的诗句：

> [different_render_mode.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdParagraph/demos/different_render_mode.py)<br>
> [content_ellipsis.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdParagraph/demos/content_ellipsis.py)

<p align="center"><img src="https://github.com/user-attachments/assets/d181a679-c035-418a-a810-9b7c0a5af598" /></p>

#### 第七步

在相关修改内容调试完成后，通过`Github`进行常规的代码提交及新建`PR`操作即可，我会协助完成代码的合并 🥂，提交`message`格式[参考](https://github.com/CNFeffery/feffery-antd-docs/commit/94a701f32597379e966d48f75d8de35365e44004)

#### 第八步

最后别忘记在`public/contributors.json`中添加上你对指定组件的贡献状态🎉。

相关问题欢迎在当前`issue`下与我们展开讨论，期待你的贡献 🥳。
