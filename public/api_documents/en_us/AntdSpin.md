- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- wrapperClassName (string | dict; optional):
    CSS class name for the outer container.

- spinning (boolean; default False):
    Whether the component is loading.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
    Size of the default loading icon. Supported values: `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- delay (number; optional):
    Delay in milliseconds before showing the loading indicator. Default: `0`.

- text (string; optional):
    Loading indicator text.

- fullscreen (boolean; default False):
    Whether fullscreen mode is enabled. Default: `False`.

- debug (boolean; default False):
    Whether debug mode logs `prop` information to the developer console on each animation load. Default: `False`.

- listenPropsMode (a value equal to: 'default', 'exclude', 'include'; default 'default'):
    Monitoring mode. Supported values: `'default'`, `'exclude'`, `'include'`. Default: `'default'`.

- excludeProps (list of strings; optional):
    Callback targets excluded from monitoring when `listenPropsMode='exclude'`, in the form `['组件id1.组件属性1', '组件id2.组件属性2', ...]` (component ID and property name pairs).

- includeProps (list of strings; optional):
    Callback targets included in monitoring when `listenPropsMode='include'`, in the form `['组件id1.组件属性1', '组件id2.组件属性2', ...]` (component ID and property name pairs).

- indicator (a list of or a singular dash component, string or number; optional):
    Custom loading icon. Supports components.

- manual (boolean; default False):
    Whether spinning is controlled manually through `spinning`, independently of callbacks involving child elements. Default: `False`.

- percent (number | a value equal to: 'auto'; optional):
    Circular loading progress: a number from 0 to 100 for actual progress, or `'auto'` for an estimated progress indicator that continues indefinitely.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
