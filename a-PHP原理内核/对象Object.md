PHP的对象是一种复合型的数据，使用一种 `zend_object_value` 的结构体来存放。

```
typedef struct _zend_object_value {
    zend_object_handle handle;  //  unsigned int类型，EG(objects_store).object_buckets的索引
    zend_object_handlers *handlers;
} zend_object_value;
```
