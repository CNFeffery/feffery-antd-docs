- **id:** String or dict type

  　　Used to *set the unique ID information for the current component*.

  **style:** Dict type

  　　Used to *set the CSS style for the current component*.

  **className:** String type

  　　Used to *set the CSS class name for the current component*.

  **children:** Component type

  　　Used to pass *nested child elements*.

  **tab:** String type

  　　Used to *set the tab title displayed in the current tab page*.

  **key:** String type

  　　Used to *set the unique ID information for the current tab page*.

  **disabled:** Boolean type, default is `False`

  　　Used to *set whether the current tab page is disabled*.

  **closable:** Boolean type, default is `True`

  　　Used when the parent `AntdTabs` is set with the parameter `type='editable-card'`. It is used to *set whether the close button is rendered for the current tab panel*.

  **titleSideInfoPopover:** Dict type

  　　Used to *set a popover with additional information on the right side of the tab panel title*. Available key-value parameters are:

  - **title:** String type, used to *set the title of the information popover*.
  - **content:** String type, used to *set the content of the information popover*.