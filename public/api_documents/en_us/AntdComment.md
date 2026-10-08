- id (string; optional):
    Unique identifier for the component.

- children (a list of or a singular dash component, string or number; optional):
    Nested comment components.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- commentId (string; optional):
    Unique comment ID, for example for matching database records.

- authorName (string; optional):
    Comment author's display name.

- authorNameHref (string; optional):
    Link associated with the comment author's name.

- publishTime (dict; required):
    Required. Publication date/time settings.

    `publishTime` is a dict with keys:

    - value (string; required):
        Required. Date/time string.

    - format (string; optional):
        Format matching the date/time string.

- fromNow (boolean; default False):
    Whether to display publication time as relative time.

- showLikeDislike (boolean; default True):
    Whether to show the like/dislike buttons. Default: `True`.

- showReply (boolean; default True):
    Whether to show the reply button. Default: `True`.

- showDelete (boolean; default False):
    Whether to show the delete button. Default: `False`.

- replyClicks (number; default 0):
    Cumulative number of reply button clicks. Default: `0`.

- deleteClicks (number; default 0):
    Cumulative number of delete button clicks. Default: `0`.

- commentContent (a list of or a singular dash component, string or number; optional):
    Comment body content. Supports components.

- likesCount (number; default 0):
    Monitor or set the like count.

- dislikesCount (number; default 0):
    Monitor or set the dislike count.

- action (a value equal to: 'liked', 'disliked', 'default'; optional):
    Monitor or set the comment's like/dislike status. Supported values: `'liked'`, `'disliked'`, `'default'`. Default: `'default'`.

- defaultAction (a value equal to: 'liked', 'disliked', 'default'; optional):
    Initial comment like/dislike status. Supported values: `'liked'`, `'disliked'`, `'default'`.

- avatarProps (dict; optional):
    Comment author avatar settings, as in `AntdAvatar`.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
    Anchoring strategy for the related popup layer. Options are `'parent'`, `'body'`. Default: `'body'`.

- batchPropsNames (list of strings; optional):
    Property names to include in [batch property monitoring](/batch-props-values).

- batchPropsValues (dict; optional):
    Values of the properties specified by `batchPropsNames`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading.
