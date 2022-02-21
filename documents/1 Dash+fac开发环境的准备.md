　　`Dash`与`fac`的安装非常简单，这里建议大家养成好习惯，使用**虚拟环境**来构建我们开发`Dash`使用到的环境，以使用`conda`作为环境管理软件为例，执行下列控制台命令我们来创建一个`Python`版本为`3.7`，名称为`dash-dev-demo`的环境，其中临时使用到国内上海交大的`conda`镜像源：

```bash
conda create -n dash-dev-demo python=3.7 -c https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main -y
```

　　使用`conda activate dash-dev-demo`激活我们刚刚创建的环境之后，再执行以下控制台命令（这里我们使用豆瓣镜像源来加速），就可以完成`Dash`+`fac`环境的搭建啦😀：

```bash
pip install dash feffery-antd-components -i https://pypi.douban.com/simple/
```

　　在`Python`中执行下列语句可以分别查看`Dash`与`feffery-antd-components`的版本：

```python
>>> import dash
>>> print('Dash版本：%s' % dash.__version__)
Dash版本：2.1.0
```

```python
>>> # 我们按照规范以fac为别名导入feffery-antd-components
>>> import feffery_antd_components as fac
>>> print('fac版本：%s' % fac.__version__)
fac版本：0.1.0-rc2
```

　　至此我们就完成了`Dash`+`fac`基础开发环境的搭建😋！