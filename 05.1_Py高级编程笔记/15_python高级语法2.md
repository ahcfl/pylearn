### 15.1. 今日目标
### 15.2.【理解】import导入模块路径问题

* 存在的问题：当我们把模块文件放到工程文件夹的外部的文件，发现无法正常引入模块

* 原因： 外部的文件夹的路径，没有放到环境变量中

* 查看环境变量

  > 1. 导入 sys模块
  > 2. sys.path 查看环境变量  返回值是列表

* 把自己写的模块的路径加入到环境变量中

  * sys.path.append("自己的路径")     # 加入环境变量的末位
  * sys.path.insert(0, "自己的路径")    # 加入到环境变量的开头位置

### 15.3.【理解】import的reload加载问题

* import 导入模块后，如果模块被修改，此时再次 import 不起作用

  > import 自动防止重复包含

* 强制重新加载一次模块

  reload() 函数

  > 1. from imp import reload
  > 2. reload(要重新加载的模块)

### 15.4.【了解】from...import的私有化问题

* 私有化： 模块中的一些变量不希望被其他模块导入，可以使用私有化解决

* 私有化使用的前提：必须使用 “ from xxx import *  “

* 用法： 在模块中，把变量前增加一个下划线 `_变量名`

* 注意：如果使用其他的方式导入模块，私有化将无效

  > from xxx import _私有变量
  >
  > print(_私有变量)    不会报错

### 15.5.【记忆】import和from...import的区别

* 区别
  * 写法：
    * import          模块名.变量/函数/类
    * from ... import *          变量名/函数/类
  * 底层的区别：
    * import         直接引用了源模块的 变量/函数/类
    * from ... import *　　拷贝源模块的　变量/函数/类　到当前自己类

### 15.6.【理解】可变参数的拆包问题

* 可变参数 *args  **kwargs  默认会封包过程
* 如果想要这种单数继续传递到下一个函数，传递的时候 func(*args,**kwargs)

### 15.7.【理解】单继承中super()

* super() 使用的时候，传递参数的时候，self 不用传递

* super() 调用顺序，按照 mro顺序来完成

  > `Grandson.__mro__`  是一个元组
  >
  > 当在类中使用 super() 在  mro列表中找到当前类的下一个元素，调用该元素的方法 

### 15.8.【理解】多继承和MRO顺序

* 多继承中 super()  执行顺序，严格执行 MRO顺序表

* MRO顺序表：

  * 类名.mro()
  * `类名.__mro__`

* 注意：

  > 当在类中使用 super() 在  mro列表中找到当前类的下一个元素，调用该元素的方法 
  >
  > 多继承中，不建议使用类名 直接调用父类的方法

### 15.9.【记忆】property基本使用

* @property 的特点： 让我们通过对象.方法名的方式可以调用方法

* 语法格式：

  @proerty

  def xxx(self):

  ​	pass

* 注意：

  > @property 装饰的方法，只能有一个参数self

### 15.10.【记忆】property其他使用方式

* 经典类： @property 一种方式

* 新式类：

  * @property 

    > goods.price    获取价格的方法

  * @xxx.setter

    > goods.price = xxx

  * @xxx.deleter

    > del goods.price    ---> @xxx.delete 装饰的方法

### 15.11.【了解】property作为类属性

* 定义 property 对象的类属性

  > xxx =property(参数1，参数2，参数3，参数4)
  >
  >     #　第一个参数，当我们　foo.BAR 自动调用第一个参数的方法
  >     #  第二个参数，当我们　foo.BAR = 100,自动调用第二个参数的方法
  >     #  第三个参数，当我们　del foo.BAR ,自动调用第三个参数的方法
  >     #  第四个参数，当我们　Foo.BAR.__doc__,自动获取第四个参数的内容 

* 使用
  * 对象.xxx    获取值
  * 对象.xxx = 100   设置值
  * del 对象.xxx        调用第三个参数方法 
  * `类.xxx.__doc__  `  获取第四个参数的内容

### 15.12.【记忆】魔法属性和方法-1

* 魔术属性

  * `__doc__`   获取描述信息
    * 获取类的  `类名.__doc__`
    * 获取方法的描述 `对象.方法名.__doc__`
  * `__module__` 获取所属的模块(`对象名.__module__`)  直接改文件 获取的__main__
  * `__class__` 获取对象所属的类 `对象名.__class__`

* 魔术方法

  - `__init__` 初始化方法  `类名() 自动调用`
  - `__del__ ` 删除对象的时候，会调用  `del 对象`


### 15.13.【记忆】魔法属性和方法-2

* 魔术属性`__dict__` 获取对象或者类的信息
  * 获取对象信息 `对象名.__dict__`对象的实例属性信息
  * 获取类的信息`类名.__dict__` 模块、类描述、对象方法...
* 魔术方法
  * `__call__() `  当使用 对象名() 会调用该方法
  * `__str__()` 打印对象的会调用 print(obj)    str方法一定要return，而且return 一定字符串内容
  * 用字典的书写格式操作对象的方法
    * `__getitem__ `  对象['xxx']
    * `__setitem__ ` 对象['xx'] = xxx
    * `__delitem__ ` del 对象['xx']  

### 15.14.【理解】with管理上下文方式一

* 上下文：以 with open 来说，打开文件在上文      关闭文件在下文

* 上下文管理器：

  * `__enter__ ` 上文方法
  * `__exit__` 下文方法

* 自定义一个满足满足上下文管理器的 类

  ```python
  """
  类：  MyFile()
  类方法：
      1. __enter__()  上文方法
      2. __exit__()   下文方法
      3. __init__()   方法，接收参数并且初始化
  
  
  with MyFile('hello.txt', 'r') as file:
      file.read()
  
  """
  
  
  class MyFile(object):
  
      # 1. __enter__()  上文方法
      def __enter__(self):
          print("进入上文....")
          # 1，打开文件
          self.file = open(self.file_name, self.file_model)
          # 2，返回打开的文件资源
          return self.file
  
      # 2. __exit__()   下文方法
      def __exit__(self, exc_type, exc_val, exc_tb):
          print("进入下文....")
          # 关闭文件资源
          self.file.close()
  
      # 3. __init__()   方法，接收参数并且初始化
      def __init__(self, file_name, file_model):
          # 保存文件名和文件打开模式，到实例属性中
          self.file_name = file_name
          self.file_model = file_model
  
  
  if __name__ == '__main__':
  
      with MyFile("hello.txt", "r") as file:
          # 开始读取文件
          file_data = file.read()
          print(file_data)
  ```


### 15.15.【理解】with管理上下文方式二

* 通过装饰器 @ contextmanager 实现上下文管理

  * 装饰器

  * 待装饰的函数

    myopen()   分拆成上文和下文，使用yield 分拆

    ```python
    def myopen(file_name,file_model):
    
        print("进入上文")
        # 1.打开文件
        file = open(file_name,file_model)
        # 2.返回资源
        yield file
        print("进入下文")
        # 下文
        # 3. 关闭资源
        file.close()
    ```

* 装饰的过程：

  * 导入模块 from contextlib import contextmanager

  * 第二步：

    > @contextmanager
    > def myopen(file_name,file_model):
    >
    > ...

### 15.16. 总结