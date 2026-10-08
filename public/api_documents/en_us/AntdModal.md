- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - mask (dict; optional):
        CSS styles for the mask element.

    - content (dict; optional):
        CSS styles for the container element.

    - wrapper (dict; optional):
        CSS styles for the wrapper element.

    - header (dict; optional):
        CSS styles for the header element.

    - body (dict; optional):
        CSS styles for the body element.

    - footer (dict; optional):
        CSS styles for the footer element.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - mask (string; optional):
        CSS class name for the mask element.

    - content (string; optional):
        CSS class name for the container element.

    - wrapper (string; optional):
        CSS class name for the wrapper element.

    - header (string; optional):
        CSS class name for the header element.

    - body (string; optional):
        CSS class name for the body element.

    - footer (string; optional):
        CSS class name for the footer element.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- visible (boolean; default False):
    Monitor or set dialog visibility. Default: `False`.

- title (a list of or a singular dash component, string or number; optional):
    Title content. Supports components.

- loadingTitle (a list of or a singular dash component, string or number; optional):
    Title content in the loading state. Supports components.

- renderFooter (boolean; default False):
    Whether to render footer action buttons. Default: `False`.

- okText (a list of or a singular dash component, string or number; optional):
    Confirm button content. Supports components.

- okButtonProps (dict; optional):
    Confirm button settings.

    `okButtonProps` is a dict with keys:

    - size (a value equal to: 'small', 'middle', 'large'; optional):
        Button size specification, options include `'small'`, `'middle'`, `'large'`. Default value: `'middle'`.

    - type (a value equal to: 'primary', 'ghost', 'dashed', 'link', 'text', 'default'; optional):
        Button type, options include `'default'`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`. Default value: `'default'`.

    - danger (boolean; optional):
        Whether the button displays a danger style. Default value: `False`.

    - disabled (boolean; optional):
        Whether the button presents a disabled state. Default value: `False`.

    - shape (a value equal to: 'circle', 'round'; optional):
        The shape of the button, with options `'default'`, `'circle'`, `'round'`. Default value: `'default'`.

    - style (dict; optional):
        Button CSS style.

    - className (string; optional):
        Button CSS class name.

- cancelText (a list of or a singular dash component, string or number; optional):
    Cancel button content. Supports components.

- cancelButtonProps (dict; optional):
    Cancel button settings.

    `cancelButtonProps` is a dict with keys:

    - size (a value equal to: 'small', 'middle', 'large'; optional):
        Button size specification, options include `'small'`, `'middle'`, `'large'`. Default value: `'middle'`.

    - type (a value equal to: 'primary', 'ghost', 'dashed', 'link', 'text', 'default'; optional):
        Button type, options include `'default'`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`. Default value: `'default'`.

    - danger (boolean; optional):
        Whether the button displays a danger style. Default value: `False`.

    - disabled (boolean; optional):
        Whether the button presents a disabled state. Default value: `False`.

    - shape (a value equal to: 'circle', 'round'; optional):
        The shape of the button, with options `'default'`, `'circle'`, `'round'`. Default value: `'default'`.

    - style (dict; optional):
        Button CSS style.

    - className (string; optional):
        Button CSS class name.

- width (dict; default 520):
    Dialog width in pixels. Default: `520`.

    `width` is a number | string | dict with keys:

    - xs (number | string; optional):
        Responsive breakpoint for viewport widths below 576px.

    - sm (number | string; optional):
        Responsive breakpoint for viewport widths of at least 576px.

    - md (number | string; optional):
        Responsive breakpoint for viewport widths of at least 768px.

    - lg (number | string; optional):
        Responsive breakpoint for viewport widths of at least 992px.

    - xl (number | string; optional):
        Responsive breakpoint for viewport widths of at least 1200px.

    - xxl (number | string; optional):
        Responsive breakpoint for viewport widths of at least 1600px.

- centered (boolean; default False):
    Whether to center the dialog vertically. Default: `False`.

- keyboard (boolean; default True):
    Whether the Escape key closes the dialog. Default: `True`.

- closable (boolean; default True):
    Whether to show the close button in the upper-right corner. Default: `True`.

- mask (boolean; default True):
    Whether to show the background mask. Default: `True`.

- maskClosable (boolean; default True):
    Whether clicking the mask closes the dialog. Default: `True`.

- okClickClose (boolean; default True):
    Whether clicking Confirm closes the dialog. Default: `True`.

- preventClose (boolean; default False):
    Whether to block automatic dialog closing through the close icon, mask, Cancel button, or Escape key. Default: `False`.

- zIndex (number; default 1000):
    Modal z-index. Default: `1000`.

- okCounts (number; default 0):
    Cumulative number of Confirm button clicks. Default: `0`.

- cancelCounts (number; default 0):
    Cumulative number of Cancel button clicks. Default: `0`.

- closeCounts (number; default 0):
    Cumulative number of close button clicks. Default: `0`.

- confirmAutoSpin (boolean; default False):
    Whether each confirmation click automatically sets `confirmLoading=True`. Default: `False`.

- loadingOkText (a list of or a singular dash component, string or number; optional):
    Confirm button content when `confirmLoading=True`. Supports components.

- confirmLoading (boolean; default False):
    Whether the footer confirmation button is loading. Default: `False`.

- transitionType (a value equal to: 'none', 'fade', 'zoom', 'zoom-big', 'zoom-big-fast', 'slide-up', 'slide-down', 'slide-left', 'slide-right', 'move-up', 'move-down', 'move-left', 'move-right'; default 'zoom'):
    Modal show/hide animation. Supported values: `'none'`, `'fade'`, `'zoom'`, `'zoom-big'`, `'zoom-big-fast'`, `'slide-up'`, `'slide-down'`, `'slide-left'`, `'slide-right'`, `'move-up'`, `'move-down'`, `'move-left'`, `'move-right'`. Default: `'zoom'`.

- forceRender (boolean; default False):
    Whether to render modal content before the modal is first shown. Default: `False`.

- destroyOnClose (boolean; default True):
    Whether to destroy modal content after closing. Default: `True`.

- loading (boolean; default False):
    Whether to show the entire component as loading. Default: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
