

- children (a list of or a singular dash component, string or number; optional):
    当前悬浮按钮组内悬浮按钮.

- id (string; optional):
    组件唯一id.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- description (a list of or a singular dash component, string or number; optional):
    描述内容.

- icon (a list of or a singular dash component, string or number; optional):
    图标元素.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- open (boolean; optional):
    设置或监听当前悬浮按钮组展开状态.

- shape (a value equal to: 'circle', 'square'; default 'circle'):
    内部各悬浮按钮形状，可选项有`'circle'`、`'square'`  默认值：`'circle'`.

- style (dict; optional):
    当前组件css样式.

- tooltip (a list of or a singular dash component, string or number; optional):
    气泡卡片内容.

- trigger (a value equal to: 'click', 'hover'; optional):
    菜单展开模式触发方式，可选项有`'click'`、`'hover'`.

- type (a value equal to: 'default', 'primary'; default 'default'):
    按钮类型，可选项有`'default'`、`'primary'`  默认值：`'default'`.