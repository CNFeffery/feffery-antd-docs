- id (string; optional):
  Component unique id.

- key (string; optional):
  Update the `key` value of the current component to force a re-render of the current component.

- className (string | dict; optional):
  CSS class name of the current component, supports [dynamic css](/advanced-classname).

- name (string; optional):
  Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
  Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

- disabled (boolean; default False):
  Whether to disable the current component. Default: `False`.

- autoFocus (boolean; default False):
  Whether to automatically gain focus. Default: `False`.

- checked (boolean; optional):
  Listen to or set whether the current switch is on.

- checkedChildren (a list of or a singular dash component, string or number; optional):
  Component type, embedded content when in the “on” state.

- unCheckedChildren (a list of or a singular dash component, string or number; optional):
  Component type, embedded content when in the “off” state.

- size (a value equal to: 'default', 'small'; default 'default'):
  Current component size specification. Options are `'small'`, `'middle'`. Default: `'default'`.

- loading (boolean; default False):
  Whether to render a loading state. Default: `False`.

- readOnly (boolean; default False):
  Whether to render as read-only. Default: `False`.

- batchPropsNames (list of strings; optional):
  Several property names that need to be included in [batch property listening](/batch-props-values).

- batchPropsValues (dict; optional):
  Listen to several property values specified in `batchPropsNames`.

- data-_ (string; optional):
  Wildcard attributes in `data-_` format.

- aria-_ (string; optional):
  Wildcard attributes in `aria-_` format.

- loading_state (dict; optional)

  `loading_state` is a dict with keys:

  - is_loading (boolean; optional):
    Determines if the component is loading or not.

  - prop_name (string; optional):
    Holds which property is loading.

  - component_name (string; optional):
    Holds the name of the component that is loading.

- persistence (boolean | string | number; optional):
  Whether to enable [prop persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'checked's; optional):
  Several property names for which the persistence feature is enabled. Options are `'checked'`. Default: `['checked']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
  Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence)
  Default: `'local'`.
