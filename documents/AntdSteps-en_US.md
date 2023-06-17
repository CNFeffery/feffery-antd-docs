**id:** *string* or *dict* type

　　Used to set the unique id information for the current component.

**key:** *string* type

　　Updates the `key` value of the current component to force a re-rendering effect.

**style:** *dict* type

　　Used to set the CSS style for the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**steps:** `list[dict]` type, required

　　Used to define the structure of each step. Each dictionary can have the following key-value pairs:

- **title:** *component type* - Used to set the title content of the current step.
- **subTitle:** *component type* - Used to set the subtitle content of the current step.
- **description:** *component type* - Used to set the description content of the current step.
- **icon:** *component type* - Used to set the icon content of the current step.

　　Here is an example:

```python
steps = [
    {
        'title': 'Step 1',
        'subTitle': '1',
        'description': 'This is step 1'
    },
    {
        'title': 'Step 2',
        'subTitle': '2',
        'description': 'This is step 2'
    },
    {
        'title': 'Step 3',
        'subTitle': '3',
        'description': 'This is step 3'
    }
]
```

**current:** *int* type, default: `0`

　　Used to set the index of the current step in the step bar. The default is `0`, which represents the first step.

**direction:** *str* type, default: `'horizontal'`

　　Used to set the display direction of the step bar. Available options are `'horizontal'` (horizontal direction) and `'vertical'` (vertical direction).

**labelPlacement:** *str* type, default: `'horizontal'`

　　Used to set the position of the title and other content for each step. Available options are `'horizontal'` (next to the icon) and `'vertical'` (below the icon).

**progressDot:** *bool* type, default: `False`

　　Used to set whether to render the step bar in a simplified dot style.

**size:** *str* type, default: `'default'`

　　Used to set the size of the step bar. Available options are `'default'` (default size) and `'small'` (mini size).

**status:** *str* type, default: `'process'`

　　Used to set the display status of the current step. Available options are `'process'`, `'wait'`, `'finish'`, and `'error'`.

**type:** *str* type, default: `'default'`

　　Used to set the overall style type of the step bar. Available options are `'default'` (default style) and `'navigation'` (navigation style).

**allowClick:** *bool* type, default: `False`

　　Used to set whether clicking on a step directly allows switching to that step.

**responsive:** *bool* type, default: `True`

　　Used to set whether to automatically switch to vertical rendering when the page width is less than 532px.