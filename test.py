from dict_to_obj import dict_to_obj
obj1 = dict_to_obj({'a': 1, 'b': {"w": []}})
print(obj1)
print(obj1.a)
print(obj1.b.w)
print(obj1['a'])
print(obj1['b']['w'])
