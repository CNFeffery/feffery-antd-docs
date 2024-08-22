## `fac` Component Documentation Page English Documentation Contribution Guide

The official documentation of `fac` (`feffery-antd-components`) has added internationalization support for multiple languages, currently supporting `zh-cn` (Simplified Chinese) and `en-us` (American English). We welcome you to participate in the construction of English documentation. Below are the steps and precautions for the internationalization of various component documentation pages on the `fac` official website:

### 1 Steps

#### Step 1

`Fork` this project repository (https://github.com/CNFeffery/feffery-antd-docs), and `clone` the forked repository to your local machine.

#### Step 2

Search for the component you want to contribute to in the [issues](https://github.com/CNFeffery/feffery-antd-docs/issues) to see if there is an existing `issue` with a duplicate topic. If not, it is recommended to create a component internationalization documentation contribution `issue` with the following title format:

> [doc i18n] AntdXXX

We will review the newly created `issue` and `assign` it to the creator within the `issue` after confirmation, indicating that it has been acknowledged.

#### Step 3

The component parameter description on the right side of each page of the component documentation is automatically rendered based on the component's `__doc__` attribute. We need to prepare the corresponding English translation content in the `public/api_documents/en_us` directory of the project. It is recommended to execute `python export_api_document.py ComponentName` in the terminal at the root directory of the project, which will automatically export the `__doc__` information of the corresponding component to the corresponding `markdown` file in the `public/api_documents/en_us` directory, for example:

<p align="center"><img src="https://github.com/user-attachments/assets/888e637b-1955-4c93-8c04-2819140c223a"  /></p>

Then, you can use commonly available large language model applications to assist with the translation, and paste the completed translation back into the original `markdown` file.

#### Step 4

Refactor the `intro.py` under the `views` module corresponding to the component documentation page module, wrap the content that needs to be automatically translated between languages with `i18n`'s `translator.t()`. The `translator.t()` will automatically handle the display of the content in `intro.py` in different internationalization modes based on the global common translation relationship configured in `public/locales.json` 😉. Take `views/AntdParagraph/intro.py` as an example:

<p align="center"><img src="https://github.com/user-attachments/assets/3a6788ad-bd8c-4b7a-bb44-9d968b050da3"  /></p>

For text translations that are not defined in `public/locales.json`, please add them at the end. With the help of AI plugins such as `codeium`, you can efficiently generate automatic text translation relationships:

<p align="center"><img src="https://github.com/user-attachments/assets/b8eea88b-4d8c-4896-bf86-6a2bf52285b4"  /></p>

#### Step 5

Refactor the `demos/__init__.py` under the `views` module corresponding to the component documentation page module. Add `from functools import partial` and `from i18n import translator` in the import package section at the beginning:

<p align="center"><img src="https://github.com/user-attachments/assets/eddcd84e-3b4d-4442-80c2-cdd8c1cb24f1"  /></p>

Refactor the original `list` type `demos_config` into a function to work with `i18n.translator` for dynamic automatic translation. Based on the `partial()` transformed `t()` function inside the function (where the parameter `topic` writes the current component name, which needs to be coordinated with the corresponding theme's `ComponentName.json` in `public/topic_locales`), wrap the content of the returned content's `'title'` and `'description'` fields for translation:

> Note that for the `'description'` field that is originally a component type, please rewrite its content as a `markdown` format string, and then wrap it with `t()` for translation, for example:<br>
> <p align="center"><img src="https://github.com/user-attachments/assets/b1a5acff-7c70-4bf8-81d6-34b8f54ef2f5"  /></p>

<p align="center"><img src="https://github.com/user-attachments/assets/6ad72031-a09c-4abf-b557-87ea8d0799d0"  /></p>

#### Step 6 (Optional)

For a specific component documentation page, after following steps three to five, most of the corresponding content on the documentation website can already present an automatic internationalization translation effect, taking the `AntdParagraph` documentation page as an example:

<p align="center"><img src="https://github.com/user-attachments/assets/db32d28b-e182-4985-8301-60306ef0ffaf"  /></p>

If you need to also internationalize some example content and source code views, you can refer to the way related examples in `AntdButton`, in conjunction with `i18n` module's `get_current_locale()`:

> [basic_usage.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdButton/demos/basic_usage.py)<br> 
> [basic_callbacks.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdButton/demos/basic_callbacks.py) 

For example, for the Chinese example in `AntdParagraph` that uses the famous ancient Chinese poet *Li Bai*'s poem "Bring in the Wine," replace it with a verse by *Shakespeare* in `en-us` mode:

> [different_render_mode.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdParagraph/demos/different_render_mode.py)<br> 
> [content_ellipsis.py](https://github.com/CNFeffery/feffery-antd-docs/blob/main/views/AntdParagraph/demos/content_ellipsis.py) 

<p align="center"><img src="https://github.com/user-attachments/assets/d181a679-c035-418a-a810-9b7c0a5af598"  /></p>

#### Step 7

After debugging the relevant modifications, you can submit the code and create a new `PR` through `Github` as usual, and I will assist in merging the code 🥂. The submission `message` format [reference](https://github.com/CNFeffery/feffery-antd-docs/commit/94a701f32597379e966d48f75d8de35365e44004)

#### Step 8

Finally, don't forget to add your contribution status for the specified component in `public/contributors.json` 🎉.

Welcome to discuss any related issues with us under the current `issue`, and we look forward to your contribution 🥳.
