### 函数的参数和返回值可以指定类型了

### Zval结构的改变

### HashTable结构的改变

### 异常处理

PHP7中PHP5中的多数错误改成了抛出异常






### PHP 的基本构成

+ SAPI  (Server Application Programming Interface)

  >即服务器应用编程接口，实质上就是定义了一个统一的接口，它的核心就是一个结构体sapi_module_struct。SAPI提供给了外部应用跟php通信的管道，这个外部应用包括不限于Apache，httpd，liunx终端等，sapi通俗的讲就是php-cgi,php-cli,mod_php等，php就是php内核。

+ main

+ zendVM

+ Ext
