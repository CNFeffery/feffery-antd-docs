默认模式下，`options`参数通过`children`字段进行自由嵌套，以构造任意树形结构，其中各节点合法参数说明如下：

- label (string; required):

  当前节点标题内容

- key (string; optional):

  当前节点唯一识别id

- value (string or number; required):

  当前节点唯一值

- children (list; optional):

  为当前节点定义子节点

- disabled (boolean; default False):

  是否禁用当前节点