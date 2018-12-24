## CPU Affinity (CPU亲合力)

[https://www.cnblogs.com/dongzhiquan/archive/2012/02/15/2353274.html]

[https://blog.csdn.net/Adam040606/article/details/52972439]

>`CPU亲合力` 就是指在Linux系统中能够将一个或多个进程绑定到一个或多个处理器上运行.

一个进程的CPU亲合力掩码决定了该进程将在哪个或哪几个CPU上运行.在一个多处理器系统中,设置CPU亲合力的掩码可能会获得更好的性能.


`cpumask`:某一位为1则表示某进程可以运行在该位所代表的cpu上.

一个CPU的亲合力掩码用一个cpu_set_t结构体来表示一个CPU集合,下面的几个宏分别对这个掩码集进行操作:
   ·CPU_ZERO() 清空一个集合
   ·CPU_SET()与CPU_CLR()分别对将一个给定的CPU号加到一个集合或者从一个集合中去掉.
   ·CPU_ISSET()检查一个CPU号是否在这个集合中.

下面两个函数就是用来设置获取线程CPU亲和力状态:
+ `·sched_setaffinity(pid_t pid, unsigned int cpusetsize, cpu_set_t *mask)`
     该函数设置进程为pid的这个进程,让它运行在mask所设定的CPU上.如果pid的值为0,则表示指定的是当前进程,使当前进程运行在mask所设定的那些CPU上.第二个参数cpusetsize是mask所指定的数的长度.通常设定为sizeof(cpu_set_t).如果当前pid所指定的进程此时没有运行在mask所指定的任意一个CPU上,则该指定的进程会从其它CPU上迁移到mask的指定的一个CPU上运行.

+ `·sched_getaffinity(pid_t pid, unsigned int cpusetsize, cpu_set_t *mask)`

     该函数获得pid所指示的进程的CPU位掩码,并将该掩码返回到mask所指向的结构中.即获得指定pid当前可以运行在哪些CPU上.同样,如果pid的值为0.也表示的是当前进程.



## cpumask
