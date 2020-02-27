# dict-to-object

把 python 字典转换成一个对象

# 使用方法

```python
from dict_to_obj import dicttoobj
obj1=dicttoobj({'a':1,'b':{"w":[]}})
obj1.a
obj1.b.w
obj1['a']
obj1['b']['w']
```
# 实现原理

把字典的键和值拷贝到新的对象上,并且递归转换字典和列表