### PHP源码中HashTable

#### 内存占用举例

```php
// 记录开始内存状态
$startMemory = memory_get_usage();
// 生成包含1-100000为数据元素的数组
$array = range(1, 100000);
// 获取数组占用的内存空间大小（单位字节:bytes）
echo memory_get_usage() - $startMemory, ' bytes';
```


Zend目录下的zend_alloc.c,zend_alloc.h,zend_hash.c,zend_hash.h四个文件。



HashTable包括两个主要的数据结构，
+ 其一是Bucket（桶）结构，
+ 另一个是HashTable结构。

Bucket结构是用于保存数据的容器，
而 HashTable结构则提供了对所有这些Bucket(或桶列)进行管理的机制。


php使用的是HashTable中的 `链地址法`;

典型的 hashtable 的元素顺序并不是明确固定的 : 元素在数组中的顺序通过散列函数计算随机确定的！这就导致了其实对于哈希表而言并不像数组一样存储在确定的位置访问也会有确定的位置！所以哈希表需要一种特殊的机制来记忆数据到底放在什么地方了！





#### 源码解析

Array[HashTable]主要有两个数据结构
+ Bucket
+ HashTable
>记住：HashTable和Zend_Array定义完全一样


##### bucket 结构定义(16+8+8):

```
typedef struct _Bucket {
    zend_ulong        h;//
    zend_string      *key;
    zval              val;
} Bucket;
```

如果 h 中存储的是整型的键的话， key 将设为 NULL

>与php5不同: 可以发现 zval 被直接嵌入到了 bucket 中，所以就不用单独分配空间了也节约了分配的开销。


##### hashtable 结构

```
typedef struct zeng_array {
    uint32_t          nTableSize;// 可以容纳的元素树
    uint32_t          nTableMask;
    uint32_t          nNumUsed;
    uint32_t          nNumOfElements;
    zend_long         nNextFreeElement;
    Bucket           *arData;           // 数组元素的排序
    <!-- uint32_t         *arHash;           // hashtable 查找 -->
    dtor_func_t       pDestructor;
    uint32_t          nInternalPointer;
    union {
        struct {
            ZEND_ENDIAN_LOHI_3(
                zend_uchar    flags,
                zend_uchar    nApplyCount,
                uint16_t      reserve)
        } v;
        uint32_t flags;
    } u;
} HashTable;
```

+ nNumUsed 和 nNumOfElements

>一旦 nNumUsed里面的值达到 nTableSize里面的值 PHP 就会尝试干掉所有打了 UNDEF 标记的元素来压缩 arData 数组。只有所有的 buckets 包含的数据真的达到了临界点，arData 才会真的把数组的容量扩展成原来的两倍。


arData 从不自动释放空间(除非显示声明)。所以假如你首先创建了一个包含百万条元素的数组并且之后将这些元素释放掉，数组仍然占用大量的内存。所以我们如果数组的利用率低于某一水平我们应该减少一半的 arData 容量。


##### 遍历数组的新方法：

```C
uint32_t i;
for (i = 0; i < ht->nNumUsed; ++i) {
    Bucket *b = &ht->arData[i];
    if (Z_ISUNDEF(b->val)) continue;
               // do stuff with bucket
}
```
