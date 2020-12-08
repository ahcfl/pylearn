### 16.1. 今日目标
### 16.2.【了解】框架概念

* 静态资源：不是经常变化的资源、往往是固定不变的资源
* 动态资源：经常变化的资源
* 模板文件：提供了一个显示的模板，显示的内容不同，但是结构是一样的
* 服务器的作用：
  * 1）接受客户端请求
  * 2）响应客户端请求
  * 3）调用应用框架获取

### 16.3.【应用】miniWeb框架构建基本构建

* 思路：

  * 判断请求的资源路径是 是否是 .py 结尾
  * 如果 .py 结尾，——> 显示动态内容
  * 如果.html 结尾，——> 显示静态内容

* 核心代码：

  ```python
      # index.py
      if file_path.endswith(".py"):
      # 2. 让.py 显示的内容和.html显示的内容区别开开
          response_body = "This is index Show! %s" % time.ctime()
          # 调用 utils 模块的 create_http_response 函数，拼接响应协议
          response_data = utils.create_http_response("200 OK", response_body.encode())
  
      # index.html
      else:
      ....
  ```


### 16.4.【应用】miniWeb框架构建-动态显示

* 思路：
  * 首先必须是 .py 结尾的文件
  * 判断请求的资源路径，并且根据资源路径不同设置 不同的 response_body
  * 当请求的资源路径不存在，返回 404 错误
* 核心代码：

```python
# 3. 判断请求的资源路径，根据不同的路径显示不同的额内容
        if file_path == "/index.py":
            response_body = "This is index show!"
            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.create_http_response("200 OK", response_body.encode())

        elif file_path == "/center.py":
            response_body = "This is center show!"
            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.create_http_response("200 OK", response_body.encode())


        elif file_path == "/gettime.py":
            response_body = "helloworld! %s" % time.ctime()
            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.create_http_response("200 OK", response_body.encode())

        else:
            response_body = "Sorry Page Not Found ! 404"
            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.create_http_response("404 Not Found", response_body.encode())

```



### 16.5.【应用】路由列表（django）

* 实现步骤：

  * 创建 urls 模块，模块的作用提供一个路由字典

    > 字典保存路径和函数的对应关系

    * 导入函数的模块 from application import funs

    * route_dict

      > ```
      > # 定义路由字典
      > route_dict = {
      > 
      >     '/index.py': funs.index,
      >     '/center.py': funs.center,
      >     '/gettime.py': funs.gettime
      > 
      > }
      > ```

  * 创建 funs 模块， 提供了具体的功能对应的函数

    > 定义路径对应的函数
    >
    > ```
    > import time
    > 
    > def index():
    >     """ 处理 index.py 请求 """
    >     return "This is index show!--funs"
    > 
    > 
    > def center():
    >     """ 处理 index.py 请求 """
    >     return "This is center show!"
    > 
    > 
    > def gettime():
    >     """ 处理 index.py 请求 """
    >     return "This is gettime show! %s " % time.ctime()
    > ```

  * 修改app文件中 动态显示的判断部分

    > 1. 判断 路径 是否在 路由字典中     key in 字典
    > 2. 如果在字典中，根据key(请求路径) 取出 对应的函数的引用
    > 3. 执行函数，获取函数的返回值，然后赋值 给 response_body

    ```
    if file_path in urls.route_dict:
    
                # 根据key值，去urls.route_dict中，获取值（函数引用）
                func = urls.route_dict[file_path]
                # 根据路由字典，获取函数的引用，执行该函数，返回执行的结果，
                # 保存到 response_body 变量中
                response_body = func()
                # 调用 utils 模块的 create_http_response 函数，拼接响应协议
                response_data = utils.create_http_response("200 OK", response_body.encode())
    
            else:
            ....
            ....
    ```


### 16.6.【应用】路由装饰器(flask)

* 修改urls模块

  > route_dict = {  }

* 修改funs模块

  * 导入 from application import urls 

  * 创建装饰器工厂,并且把路径添加到字典中（创建路由字典）

    > ```
    > def route(path):
    >     # path 向装饰器内部传递的参数   path   /index.py
    >     # 装饰器
    >     # 字典
    >     # {"index.py":index函数引用}
    >     def function_out(func):    #func   index函数的引用
    >         # 2-----
    >         urls.route_dict[path] = func
    >         # print("装饰[%s]" % path)
    > 
    >         # 装饰器内层函数
    >         def function_in():
    >             # 调用原函数并且执行
    >             return func()
    > 
    >         return function_in
    > 
    >     return function_out
    > ```

  * 装饰函数

    > ```
    > @route("/center.py")
    > def center():
    >     """ 处理 index.py 请求 """
    >     return "This is center show!"
    > ```

* 在 app模块中导入 funs 模块

  > 此时funs 模块中的函数被加载，加载的同时被装饰（就会向字典中添加路由信息）

### 16.7.【应用】模板替换

* 思路

  * 拷贝资源（templates）到工程下

  * 修改 funs模块中的 index 和 center函数

  * 在函数中读取对应的文件

    > with open("templates/index.html") as file:
    >
    > ​	content = file.read()

  * 使用正则替换网页中的内容 {%content%} ---> helloworld!

  * 返回替换后的内容

    > return content

### 16.8.【应用】<选股系统-股票信息>数据加载_1

* 创建并导入数据到数据库

  * 创建数据库  create database stock_db charset=utf8
  * 使用数据库 use stock_db
  * 导入数据库（先客户端登录）
  * 准备脚本文件
  * 导入脚本   source stock_db.sql

* 修改index函数

  * 连接数据库，获取数据

    * 导入模块

    * 建立连接

    * 创建游标

    * 使用游标执行sql

    * 获取查询的结果

      > data_from_mysql = str(cur.fetchall())

    * 关闭资源

      > 先关闭游标，在关闭连接

  * 替换为查询的数据

    > content = re.sub("{%content%}",data_from_mysql,content)

### 16.9.【应用】<选股系统-股票信息>数据加载_2

* 思路：

  * 把查询的数据进行遍历，并且拼接html格式的文本

    > <tr></tr>  表示一行   　<td></td> 一列

  * 替换为拼接后的字符串

    > content = re.sub("{%content%}",data_from_myql,content)

  * 注意：

    > %s %s %s   ---> line        # line 是一个元组

### 16.10.【应用】<选股系统-个人中心>数据加载

* 思路：

  * 关联查询

    > select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info i, focus f where i.id = f.id

  * 把查询的数据进行遍历，并且拼接html格式的文本

    > <tr></tr>  表示一行   　<td></td> 一列

  * 替换为拼接后的字符串

    > content = re.sub("{%content%}",data_from_myql,content)

### 16.11. 总结