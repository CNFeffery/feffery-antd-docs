import mistune
from dash import html, dcc
from typing import List, Union
import feffery_antd_components as fac
from dash.dependencies import Component


class DocRenderer:
    """基于markdown文档渲染对应组件文档"""

    def __init__(self, paragraph_indent: int = "2rem", ignore_br: bool = False) -> None:
        self.markdown_parser = mistune.create_markdown(renderer=None)
        self.paragraph_indent = paragraph_indent
        self.ignore_br = ignore_br

    def render(self, raw_markdown: str) -> List[Component]:
        """将原始markdown字符串渲染为组件内容

        Args:
            raw_markdown (str): 输入的原始markdown字符串

        Returns:
            List[Component]: 结果渲染内容
        """

        # 从markdown内容原文解析ast数据结构
        markdown_ast = self.markdown_parser.parse(raw_markdown)[0]

        # 从ast数据中仅保留type、children、attrs、raw属性
        markdown_ast = self.__keep_attrs(
            markdown_ast, ["type", "children", "attrs", "raw"]
        )

        # 将ast数据转化为组件
        return self.__transform(markdown_ast)

    def __keep_attrs(self, node: Union[dict, list], keep_keys: List[str]) -> dict:
        """递归保留指定的键值对

        Args:
            node (Union[dict, list]): 当前传入的节点
            keep_keys (List[str]): 需要保留的键名列表

        Returns:
            dict: 处理后的结果
        """

        # 若当前节点为dict型
        if isinstance(node, dict):
            new_node = {key: value for key, value in node.items() if key in keep_keys}
            # 若当前节点存在children属性
            if new_node.get("children"):
                new_node["children"] = self.__keep_attrs(
                    new_node["children"], keep_keys
                )
            return new_node

        # 若当前节点为list型
        elif isinstance(node, list):
            return [self.__keep_attrs(item, keep_keys) for item in node]

        return node

    def __transform(self, node: Union[dict, list]) -> dict:
        """对原始的ast节点数据进行组件化转换

        Args:
            node (Union[dict, list]): 当前传入的节点

        Returns:
            dict: 转换后的结果
        """

        # 若当前节点为dict型
        if isinstance(node, dict):
            # 根据当前节点的type来进行相应的转换处理
            # 文本元素
            if node.get("type") == "text":
                return self.transform_text(node)

            # 换行元素
            elif node.get("type") == "blank_line":
                return self.transform_blank_line()

            # 段落内换行元素
            elif node.get("type") == "softbreak":
                return self.transform_softbreak()

            # 标题元素
            elif node.get("type") == "heading":
                return self.transform_heading(node)

            # 段落元素
            elif node.get("type") == "paragraph":
                return self.transform_paragraph(node)

            # 加粗元素
            elif node.get("type") == "strong":
                return self.transform_strong(node)

            # 斜体元素
            elif node.get("type") == "emphasis":
                return self.transform_emphasis(node)

            # 行内代码元素
            elif node.get("type") == "codespan":
                return self.transform_codespan(node)

            # 链接元素
            elif node.get("type") == "link":
                return self.transform_link(node)

            # 分割线元素
            elif node.get("type") == "thematic_break":
                return self.transform_thematic_break(node)

        # 若当前节点为list型
        elif isinstance(node, list):
            new_nodes = [self.__transform(item) for item in node]

            return [node for node in new_nodes if node]

        return node

    def transform_text(self, node: dict) -> Component:
        """处理普通文本的转换

        Args:
            node (dict): 当前传入的节点

        Returns:
            Component: 转换后结果
        """

        return node["raw"]

    def transform_blank_line(self) -> Component:
        """处理空行的转换

        Args:
            node (dict): 当前传入的节点

        Returns:
            Component: 转换后结果
        """

        return None if self.ignore_br else html.Br()

    def transform_softbreak(self) -> Component:
        """处理普通换行的转换

        Args:
            node (dict): 当前传入的节点

        Returns:
            Component: 转换后结果
        """

        return None if self.ignore_br else html.Br()

    def transform_heading(self, node: dict) -> Component:
        """处理标题的转换

        Args:
            node (dict): 当前传入的节点

        Returns:
            Component: 转换后结果
        """

        return fac.AntdTitle(
            [self.__transform(item) for item in node["children"]],
            level=node["attrs"]["level"],
        )

    def transform_paragraph(self, node: dict) -> Component:
        """处理段落的转换

        Args:
            node (dict): 当前传入的节点

        Returns:
            Component: 转换后结果
        """

        return html.Div(
            [self.__transform(item) for item in node["children"]],
            style={"textIndent": self.paragraph_indent},
        )

    def transform_strong(self, node: dict) -> Component:
        """处理加粗内容的转换

        Args:
            node (dict): 当前传入的节点

        Returns:
            Component: 转换后结果
        """

        return fac.AntdText(
            [self.__transform(item) for item in node["children"]], strong=True
        )

    def transform_emphasis(self, node: dict) -> Component:
        """处理斜体内容的转换

        Args:
            node (dict): 当前传入的节点

        Returns:
            Component: 转换后结果
        """

        return fac.AntdText(
            [self.__transform(item) for item in node["children"]], italic=True
        )

    def transform_codespan(self, node: dict) -> Component:
        """处理行内代码的转换

        Args:
            node (dict): 当前传入的节点

        Returns:
            Component: 转换后结果
        """

        return fac.AntdText(node["raw"], code=True)

    def transform_link(self, node: dict) -> Component:
        """处理链接的转换

        Args:
            node (dict): 当前传入的节点

        Returns:
            Component: 转换后结果
        """

        return dcc.Link(
            [self.__transform(item) for item in node["children"]],
            href=node["attrs"]["url"],
        )

    def transform_thematic_break(self, node: dict) -> Component:
        """处理分割线的转换

        Args:
            node (dict): 当前传入的节点

        Returns:
            Component: 转换后结果
        """

        return fac.AntdDivider()
