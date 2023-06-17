**id:** *string* or *dict*

　　Used to set the *unique id information* of the current component.

**key:** *string*

　　Updates the `key` value of the current component to force a re-render.

**style:** *dict*

　　Used to set the *CSS style* of the current component.

**className:** *string* or *dict*

　　Used to set the *CSS class name* of the current component, supporting [dynamic CSS](/advanced-classname).

**children:** *component*

　　Used to pass *nested child elements*.

**locale:** *string*, default is `'zh-cn'`

　　Used to *set the language for functional text of the current component*. Options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**commentId:** *string*

　　Used to *set the id information of the current comment* for backend database matching.

**authorName:** *string*

　　Used to *set the author name of the current comment*.

**authorNameHref:** *string*

　　Used to *set the hyperlink for the author name*.

**publishTime:** *dict*, required

　　Used to *set the publishing time of the current comment*. Available key-value parameters are:

- **value:** *string*, used to *set the date and time string of the comment publishing time*.
- **format:** *string*, used to *set the format string corresponding to the value*. [Reference](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/). Common formats include `'YYYY-MM-DD hh:mm:ss'`.

**fromNow:** *bool*, default is `False`

　　Used to *set whether to display the comment publishing time as relative time*.

**showLikeDislike:** *bool*, default is `True`

　　Used to *set whether to render the support/dislike buttons for the current comment*.

**showReply:** *bool*, default is `True`

　　Used to *set whether to render the "add reply" button for the current comment*.

**showDelete:** *bool*, default is `False`

　　Used to *set whether to render the delete button for the current comment*.

**replyCounts:** *int*, default is `0`

　　Used to *listen to the number of times the "add reply" button is clicked*.

**deleteClicks:** *int*, default is `0`

　　Used to *listen to the number of times the "delete" button is clicked*.

**commentContent:** *component*

　　Used to *set the body content of the comment*.

**likesCount:** *int*, default is `0`

　　Used to *set the number of likes for the current comment*.

**dislikesCount:** *int*, default is `0`

　　Used to *set the number of dislikes for the current comment*.

**action:** *string*

　　Used to *set or listen to the "liked"/"disliked" state of the current comment*. Options are `'liked'` and `'disliked'`.

**defaultAction:** *string*

　　Used to *set the initial "liked"/"disliked" state of the current comment*. Options are `'liked'` and `'disliked'`.

**avatarProps:** *dict*

　　Used to *set the avatar-related properties of the current comment author*, consistent with `AntdAvatar` parameters.

**popupContainer:** *string*, default is `'body'`

　　Used to *set the reference container type for the floating elements related to the current component*. Options are `'body'` (page root node as reference) and `'parent'` (parent container of the current element as reference). When the component is inside a scrollable container, setting `popupContainer='parent'` can solve the issue of the floating layer not scrolling with the content.