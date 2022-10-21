# ndarray 对象

NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。

创建一个 ndarray 对象只需要调用 array 函数即可：

```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

参数说明：

| 名称   | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| object | 数组或嵌套的数列                                             |
| dtype  | 数组元素的数据类型，可选                                     |
| copy   | 对象是否需要复制，可选                                       |
| order  | 创建数组的样式，C 为行方向，F 为列方向，A 为任意方向（默认） |
| subok  | 默认返回一个与基类类型一致的数组                             |
| ndmin  | 指定生成数组的最小维度                                       |

Example:

```python
import numpy as np
np.array([1, 2, 3], dtype = complex)  # [1.+0.j 2.+0.j 3.+0.j]
np.array([1, 2, 3], ndmin =  2)       # [[1 2 3]]
```

# 数据类型 dtype 对象

numpy 支持的数据类型比 python 内置的类型多得多，基本可以和 C 对应上，常见类型有：

- bool\_ 布尔类型
- int\_ 默认的整数类型
- int8 字节（-128 to 127）
- int16 整数整数（-32768 to 32767）
- int32 int64
- unit8 16 32 64
- float\_ float64 的简写
- float16 32 64
- complex\_ complex128 的简写，128 位复数
- complex64 128

Example:

```python
import numpy as np
# 使用标量类型
dt = np.dtype(np.int32)  # print(dt) int32
# # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')      # print(dt) int32

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)  # [('abc', 21, 50.0), ('xyz', 18, 75.0)]
```

每个内建类型都有一个唯一定义它的字符代码，如下：

| 字符 | 对应类型              |
| :--- | :-------------------- |
| b    | 布尔型                |
| i    | (有符号) 整型         |
| u    | 无符号整型 integer    |
| f    | 浮点型                |
| c    | 复数浮点型            |
| m    | timedelta（时间间隔） |
| M    | datetime（日期时间）  |
| O    | (Python) 对象         |
| S, a | (byte-)字符串         |
| U    | Unicode               |
| V    | 原始数据 (void)       |

# 数组属性

numpy数组的维数称为 `秩(rank)`，秩就是轴的数量，即数组的维度，一维数组的秩为1，二维数组的秩为2，以此类推。

每一个线性的数组称为是一个 `轴(axis`，也就是维度。比如说，二维数组相当于是两个一维数组，其中第一个一维数组中的每个元素又是一个一维数组。所以一维数组就是轴，第一个轴相当于底层数组，第二个轴就是底层数组里的数组。而秩是轴的数量，也就是数组的维度数。

| 属性             | 说明                                                         |
| :--------------- | :----------------------------------------------------------- |
| ndarray.ndim     | 秩，即轴的数量或维度的数量                                   |
| ndarray.shape    | 数组的维度，对于矩阵，n 行 m 列                              |
| ndarray.size     | 数组元素的总个数，相当于 .shape 中 n*m 的值                  |
| ndarray.dtype    | ndarray 对象的元素类型                                       |
| ndarray.itemsize | ndarray 对象中每个元素的大小，以字节为单位                   |
| ndarray.flags    | ndarray 对象的内存信息                                       |
| ndarray.real     | ndarray元素的实部                                            |
| ndarray.imag     | ndarray 元素的虚部                                           |
| ndarray.data     | 包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。 |

其中 `ndarray.shape`较为常用：

```python
import numpy as np  
a = np.array([[1,2,3],[4,5,6]])   # [2,3] 2表示，第一个数组有两个元素。  3表示，这两个元素（数组），内有三个元素。

# 调整数组大小
a.shape = (3,2)

# 结果为
[[1 2]
 [3 4]
 [5 6]]
# 也可以通过reshape来调整数组大小
b = a.reshape(3,2)  
```

# 创建数组

**numpy.empty**

numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：

```python
numpy.empty(shape, dtype = float, order = 'C')
```

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| shape | 数组形状                                                     |
| dtype | 数据类型，可选                                               |
| order | 有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。 |

Example

```python
import numpy as np  
np.empty([3,2], dtype = int) 

#结果为，数组元素为随机值，因为未初始化
[[4611686018427387904                   0]
 [4611686018427387904                   0]
 [                  4                   0]]
```

**numpy.zeros**

创建指定大小的数组，数组元素以 0 来填充：

```python
numpy.zeros(shape, dtype = float, order = 'C')
```

Example

```python
import numpy as np
 
# 默认为浮点数
x = np.zeros(5) 
print(x)
 
# 设置类型为整数
y = np.zeros((5,), dtype = int) 
print(y)
 
# 自定义类型
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(z)


结果依次为：
[0. 0. 0. 0. 0.]
[0 0 0 0 0]
[[(0, 0) (0, 0)]
 [(0, 0) (0, 0)]]
```

**numpy.ones**

创建指定形状的数组，数组元素以 1 来填充:

```python
numpy.ones(shape, dtype = None, order = 'C')
```

同样默认为浮点数。

## 从已有数组中创建

**numpy.asarray**

numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个，比 numpy.array 少两个。

```
numpy.asarray(a, dtype = None, order = None)
```

**numpy.frombuffer**

numpy.frombuffer 用于实现动态数组。

numpy.frombuffer 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象。

```
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
```

## 从数值范围创建

**numpy.arange**

numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：

```
numpy.arange(start, stop, step, dtype)
```

根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray。

参数说明：

| 参数    | 描述                                                         |
| :------ | :----------------------------------------------------------- |
| `start` | 起始值，默认为`0`                                            |
| `stop`  | 终止值（不包含）                                             |
| `step`  | 步长，默认为`1`                                              |
| `dtype` | 返回`ndarray`的数据类型，如果没有提供，则会使用输入数据的类型。 |

**numpy.linspace**

numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：

```
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
```

**numpy.logspace**

numpy.logspace 函数用于创建一个于等比数列。格式如下：

```
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
```

base 参数意思是取对数的时候 log 的下标。

# 切片和索引

ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。

ndarray 数组可以基于 0 - n 的下标进行索引，切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组。

**切片**

```python
import numpy as np
 
a = np.arange(10)
slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2   
print (a[s])   # [2  4  6]

# 等价操作，通过切片参数: start:stop:step
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)       # [2  4  6]
```

冒号 **:** 的解释：如果只放置一个参数，如 **[2]**，将返回与该索引相对应的单个元素。如果为 **[2:]**，表示从该索引开始以后的所有项都将被提取。如果使用了两个参数，如 **[2:7]**，那么则提取两个索引(不包括停止索引)之间的项。

切片还可以包括**省略号 …**，来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的 ndarray。

Example

```python
import numpy as np
 
arr = np.arange(24).reshape((2, 3, 4))
 
print arr[1, ...]               # 等价于 arr[1, :, :]
print arr[..., 1]               # 等价于 arr[:, :, 1]
print (a[...,1:])               # 第2列及剩下的所有元素
```

**索引**

ndarray 数组可以基于 0 - n 的下标进行索引，此外，数组可以由整数数组索引、布尔索引及花式索引。
