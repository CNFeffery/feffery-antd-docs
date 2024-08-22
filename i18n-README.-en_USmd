## `fac` Component Documentation Page English Documentation Contribution Guide

The official documentation for `fac` (short for `feffery-antd-components`) has added internationalization support for multiple languages, currently supporting `zh-cn` (Simplified Chinese) and `en-us` (American English). We welcome your participation in the construction of English documentation. Below are the steps and precautions for internationalizing and multilingualizing the documentation pages for each component on the `fac` official website:

### 1 Steps

#### Step 1

`Fork` this project repository (https://github.com/CNFeffery/feffery-antd-docs), and `clone` the forked repository to your local machine.

#### Step 2

Search in [feffery-antd-docs](https://github.com/CNFeffery/feffery-antd-docs/issues) for the component you wish to contribute to, check if there is an existing `issue` with a duplicate theme. If not, it is recommended to create a component internationalization documentation contribution `issue` with the following title format:

> [doc i18n] AntdXXX

I will review the newly created `issue` and, upon confirmation, `assign` it to the creator within the `issue` to indicate confirmation.

#### Step 3

The component parameter descriptions on the right side of each page of the component documentation are automatically rendered based on the component's `__doc__` attribute. We need to prepare the corresponding English translation content in the project's `public/api_documents/en_us` directory. It is recommended to execute `python export_api_document.py ComponentName` in the terminal at the root directory of the project, which will automatically export the `__doc__` information of the corresponding component as a `markdown` file in the `public/api_documents/en_us` directory, for example:

![image](https://github.com/user-attachments/assets/888e637b-1955-4c93-8c04-2819140c223a) 

You can then use commonly available large language model applications to assist with translation, and paste the completed translation back into the original `markdown` file.

#### Step 4

Refactor the `intro.py` under the `views` module for the corresponding component documentation page module, wrap the content that needs to be automatically translated between languages with `i18n`'s `translator.t()`. The `translator.t()` will automatically handle the display of the content in `intro.py` in different internationalization modes based on the global common translation relationship configured in `public/locales.json` 😉, taking `views/AntdParagraph/intro.py` as an example:

![image](https://github.com/user-attachments/assets/3a6788ad-bd8c-4b7a-bb44-9d968b050da3) 

For text translations that are not defined in `public/locales.json`, please add them at the end. With the help of AI plugins like `codeium`, you can efficiently generate text translation relationships:

![image](https://github.com/user-attachments/assets/b8eea88b-4d8c-4896-bf86-6a2bf52285b4) 

#### Step 5

Refactor the `demos/__init__.py` under the `views` module for the corresponding component documentation page module. Add `from functools import partial` and `from i18n import translator` in the package import section at the beginning:

![image](https://github.com/user-attachments/assets/eddcd84e-3b4d-4442-80c2-cdd8c1cb24f1) 

Refactor the original `list` type `demos_config` into a function to dynamically translate automatically with `i18n.translator`. Based on the `partial()` transformed `t()` function inside the function (where the parameter `topic` writes the current component name, which needs to be coordinated with the `ComponentName.json` in the corresponding theme of `public/topic_locales`), wrap the content of the returned content's `'title'` and `'description'` fields for translation:

> Note that for the `'description'` field originally of the component type, please rewrite its content as a `markdown` format string, then wrap it with `t()` for translation, for example:
> ![image](https://github.com/user-attachments/assets/b1a5acff-7c70-4bf8-81d6-34b8f54ef2f5) 


![image](https://github.com/user-attachments/assets/6ad72031-a09c-4abf-b557-87ea8d0799d0) 

#### Step 6 (Optional)

For a specific component documentation page, after following steps three to five, most of the content on the documentation website can already present automatic internationalization translation effects. Taking the `AntdParagraph` documentation page as an example:

![image](https://github.com/user-attachments/assets/db32d28b-e182-4985-8301-60306ef0ffaf) 

If you need to internationalize and translate some example content and source code, you can refer to the way in `AntdButton` and other related examples, in conjunction with `i18n` module's `get_current_locale()`:

> [basic_usage.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdButton/demos/basic_usage.py) 
> [basic_callbacks.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdButton/demos/basic_callbacks.py) 

For example, in the Chinese example of `AntdParagraph`, which uses the famous ancient Chinese poet *Li Bai*'s poem *"Bring in the Wine"*, you can replace it with a verse by *Shakespeare* in the `en-us` mode:

> [different_render_mode.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdParagraph/demos/different_render_mode.py) 
> [content_ellipsis.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdParagraph/demos/content_ellipsis.py) 

![image](https://github.com/user-attachments/assets/d181a679-c035-418a-a810-9b7c0a5af598) 

#### Step 7

After debugging the relevant modifications, you can submit the code and create a new `PR` through `Github` as usual, and I will assist in merging the code🥂. The submission `message` format [reference](https://github.com/CNFeffery/feffery-antd-docs/commit/94a701f32597379e966d48f75d8de35365e44004) 

Welcome to discuss any related issues with us in the current `issue`, and we look forward to your contribution🥳.
