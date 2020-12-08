### 2.1.学习目标
### 2.2. 常用命令-数据流、管道

* 数据流

  * 输入流
  * 输出流
  * 标准的错误输出流

* 重定向：改变数据的流向（一般重定向到文件中）

  `>` 重定向

  `>>` 以追加的方式重定向

* 管道： 一个命令的输出作为另外一个命令的输入去使用

  `|`       指令1 | 指令2           * 指令1必须要有输出

### 2.3. [难点]常用命令-建立链接

* linux中连接文件有两种：软链接   硬链接

  * 软链接： 相当于快捷方式，通过软链接可以修改源文件的内容

    > ln -s 源文件  连接文件

  * 硬链接：一个文件有多个名字，通过硬链接可以修改源文件的内容

    > ln 源文件  连接文件


### 2.4. [难点]常用命令-建立链接2

* 删除软硬链接查看对源文件的影响

  > 删除软硬链接，对源文件都没有影响

* 删除源文件查看对链接文件的影响

  > 删除源文件，软链接不可用
  >
  > 删除源文件，如果文件还有多个硬链接，则无影响

* 区别：

  * 软链接可以指向一个不存在的文件，硬链接不可以
  * 可以对目录创建软链接，不可以对目录创建硬链接™

### 2.5. 常用命令-文件搜索

* 在文本内部搜索 grep

  * grep 内部搜索

    > grep ‘内容’ 文件路径
    >
    > -n   查看结果的行数
    >
    > -i    忽略大小写
    >
    > -v   取反

  * grep 正则搜索

    > grep  '^a' 文件路径     搜索以a开头的行

* 在计算机中搜索文件 find

  > find  目标的目录 选项  条件

  * 按照名称搜索 -name

    find ./ -name test.txt

    find ./ -name '*.txt'   所有的文本文件

    > `*` 任意一个或多个字符
    >
    > ? 任意一个字符
    >
    > []  范围     [12]

  * 按照大小搜索 -size

    > find ./ -size +30M      大于30M
    >
    > Find ./ -size -20M      小于20M
    >
    > find ./ -size +15M  -size -30M    大于15M小于30M

### 2.6. [重、难点]常用命令-归档和压缩(1)

* 归档和解档

  * tar -cvf 归档的文件名.tar  文件1  文件2...
  * tar -xvf 档案文件名

  > 选项f必须放到最后

* 归档+压缩 和 解压+解档

  * 归档+压缩

    > tar -zcvf 归档的文件名.tar.gz  文件1  文件2...

  * 解压+解档

    > tar -zxvf 归档的文件名.tar.gz
    >
    > 如果需要指定解档的目录：tar -zxvf 归档的文件名.tar.gz -C 要解压解档到的目录

### 2.7. [重、难点]常用命令-归档和压缩(2)

* zip      压缩

  压缩目录:zip -r xxx.zip 目录

* unzip  解压缩

  unzip xxx.zip 解压

  unzip -d xxx xxx.zip 指定解压目录为xxx

### 2.8. [重点]常用命令-文件权限

* 文件权限的构成

  9个字母，3组（拥有者权限u,  组权限g, 其他用户权限o）           所有用户权限a

* 每一组权限可选的权限有：

  r  可读   w 可写  x 可执行（文件：文件可以直接运行，绿色,  目录：表示这个目录可以打开）  - 没有权限

### 2.9. [重点]常用命令-权限修改

* 权限修改指令： chmod

  * 字母法

    用户： u g  o  a

    权限设置： +（增加）、 -（撤销） 、=（设置）

    具体权限： r   w  x 

    用法： chmod 用户+具体权限 文件名

  * 数字法

    r - 4   w-2    x-1    `-` -0

    三位权限数字：第一位文件拥有者权限   第二位 同组用户权限  第三位 其他用户权限

    chmod 权限数字 文件路径

### 2.10. [重点]常用命令-用户管理

* 切换用户

  * 临时:  sudo 命令

  * 永久：

    >  su 用户名   输入用户名对应的密码
    >
    >  sudo -s     输入的的当前用户的密码

* passwd 修改密码

  passwd 表示修改当前用户的密码

  passwd xxx    修改xxx用户的密码

* exit

  * exit 如果没有用户在栈中，直接退出终端
  * 如果多次切换用户，退出到上次登录的用户

* who

  * 用来查看当前系统登录了哪些用户

    -q  统计用户数

    -u  显示最后一次操作据现在的时间

### 2.11. 常用命令-关机、重启

* 关机shutdown
  * shutdown 15:50 指定 在 15：50关机
  * shutdown +20    20分钟以后关机
  * shutdown -h now
* 重启 reboot

### 2.12. 软件安装与卸载

* linux 软件安装的三种方式

  > 源代码包安装     deb包安装      apt-get方式

* apt-get方式安装软件

  * 配置软件源   修改 /etc/apt/source.list
  * 更新软件源    sudo apt-get update
  * 安装软件:　sudo apt-get install 软件包名称
  * 卸载软件： sudo apt-get remove 软件包名称

### 2.13. [重点]ssh远程登录

* 服务器端安装 ssh  server

  > ```
  > sudo apt-get install openssh-server
  > ```

* 客户端登录

  > ssh  服务器用户名@服务器地址

  ssh  demo@192.168.150.112   --> 123

### 2.14. [重点]scp远程拷贝

* scp的作用：可以上传或者下载文件

  * 上传： scp  本地路径   服务器用户@服务器ip:服务器路径

    > scp  ./logo.png demo@192.168.150.112:/home/demo/python20/test/logo.png

  * 下载： scp   服务器用户@服务器ip:服务器路径 本地路径  

    > scp  demo@192.168.150.112:/home/demo/python20/test/logo.png  ./logo.png 

  * 如果操作的是目录使用`scp -r`

### 2.15. [重、难点]编辑器vim介绍

* 三种模式：命令模式（移动光标、复制、删除）   输入模式（编辑文件）  末行模式（保存文件、查找替换）
* 三种模式转换：打开文件默认是命令模式 ——a\i\o--->输入模式--->esc---命令模式---:--> 末行模式

### 2.16. [重、难点]编辑器vim操作

* 创建文件： vi 文件名 ——> i 进入编辑模式-->编辑文件--->esc 到命令模式--->:进入末行模式-->wq保存并退出
* vi编辑器进入输入模式：
  * i 光标前插入  I 行首插入
  * a光标后， A行尾
  * o 光标下一行产生新行  O 光标上一行产生新行
* 进入命令模式：任何模式下按esc

### 2.17. 实战:《系统性能定时监控》-介绍

* psutil 获取服务器的硬件信息

  * cpu的核心数  psutil.cpu_count()

  * cpu的使用率  psutil.cpu_percent(interval=0.5)

  * 内存信息    psutil.virtual_memory() 

  * 内存的使用率 psutil.virtual_memory().percent

  * 硬盘的分区信息：psutil.disk_partitions()

  * 硬盘的指定路径的硬盘信息：psutil.disk_usage("/")

  * 硬盘的使用率：psutil.disk_usage("/").percent

  * 网络数据信息：

    > 收到的字节数：psutil.net_io_counters().bytes_recv
    >
    > 发送的字节数：psutil.net_io_counters().bytes_sent

### 2.18. 实战:《系统性能定时监控》-基础

思路：

> 1、导入模块
>
> 2、定义变量保存cpu信息、内存信息、硬盘信息、网络信息
>
> 3、拼接要显示的字符串（格式化的字符串拼接）
>
> 4、保存信息到文件中

```python
# 1、导入模块
import psutil
import datetime
# 2、定义变量保存CPU的使用率
cpu_per = psutil.cpu_percent(interval=0.5)

# 3、定义变量保存内存信息
memory_info = psutil.virtual_memory()

# 4、定义变量保存硬盘的信息
disk_info = psutil.disk_usage("/")

# 5、定义变量保存网络的信息
net_info = psutil.net_io_counters()

# 获取系统当前时间
current_time = datetime.datetime.now().strftime("%F %T")

# 6、拼接字符串显示
log_str = "|-------------------|------------|-------------|-------------|----------------------------|\n"
log_str += "|      监控时间      |  CPU使用率  |   内存使用率  |   硬盘使用率  |          网络收发量          |\n"
log_str += "|                   | (共%d核CPU)  |  (总计%dG内存) | (总计%dG硬盘)|                            |\n" % (psutil.cpu_count(logical=False), memory_info.total/1024/1024/1024, disk_info.total/1024/1024/1024)
log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
log_str += "|%s|    %s%%   |    %s%%    |    %s%%    |   收:%s/发:%s  |\n" % (current_time, cpu_per, memory_info.percent, disk_info.percent, net_info.bytes_recv, net_info.bytes_sent)
log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
print(log_str)

# 7、保存监控信息到日志文件
# a --> 以**读写**方式打开文件。如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入 
f = open("log.txt", "a")
f.write(log_str + "\n\n")
f.close()
```

* 获取当前时间：`current_time = datetime.datetime.now().strftime("%F %T")`



### 2.19. 实战:《系统性能定时监控》-升级版

* 定义了linux_monitor() 实现监控

```python
def linux_monitor(time):
    """定义函数，实现硬件信息的获取"""
    # 2、定义变量保存CPU的使用率
    cpu_per = psutil.cpu_percent(interval=time)

    # 3、定义变量保存内存信息
    memory_info = psutil.virtual_memory()

    # 4、定义变量保存硬盘的信息
    disk_info = psutil.disk_usage("/")

    # 5、定义变量保存网络的信息
    net_info = psutil.net_io_counters()

    # 获取系统当前时间
    current_time = datetime.datetime.now().strftime("%F %T")

    # 6、拼接字符串显示
    log_str = "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|      监控时间      |  CPU使用率  |   内存使用率  |   硬盘使用率  |          网络收发量          |\n"
    log_str += "|                   | (共%d核CPU)  |  (总计%dG内存) | (总计%dG硬盘)|                            |\n" % (
    psutil.cpu_count(logical=False), memory_info.total / 1024 / 1024 / 1024, disk_info.total / 1024 / 1024 / 1024)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|%s|    %s%%   |    %s%%    |    %s%%    |   收:%s/发:%s  |\n" % (
    current_time, cpu_per, memory_info.percent, disk_info.percent, net_info.bytes_recv, net_info.bytes_sent)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    print(log_str)

    # 7、保存监控信息到日志文件
    f = open("log.txt", "a")
    f.write(log_str + "\n\n")
    f.close()
```



* main() 启动定时监控

```python

def main():
    """程序的入口"""
    while True:
        linux_monitor(5)
```



### 终端方式运行

* 第一步，文件增加 可执行权限  `chmod u+x xxxx.py`

* 第二步，告诉终端代码使用 python解释器执行

  > #!/home/demo/.Envs/1-basics-python3/bin/python3

* 第三步， 进入虚拟环境运行

  > workon 1-basics-python3

* 第四步，./xxxx.py



### 2.20. 知识点总结