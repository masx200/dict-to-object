# dict-to-object

把 python 字典转换成一个对象,可以使用`.x`和`['x']`来访问对象的属性

# 使用方法

```python
from dict_to_obj import dict_to_obj
obj1 = dict_to_obj({'a': 1, 'b': {"w": []}})
print(obj1)
print(obj1.a)
print(obj1.b.w)
print(obj1['a'])
print(obj1['b']['w'])

```

# 实现原理

把字典的键和值拷贝到新的对象上,并且递归转换字典和列表
