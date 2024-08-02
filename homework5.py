immutable_var = 1, 'String', True
print(immutable_var)
print(type(immutable_var))
#immutable_var [2] = False # immutable_var - Кортеж так же, как и список, является коллекцией, но в отличие от него он неизменяем.(<class 'tuple'>)
#чтобы immutable_var стал списком необходимо все значения взять в квадратные скобки и тогда ему присвоится <class 'list'>
mutable_list = [5, 'apple', False]
print(type(mutable_list))
mutable_list[0] = 6
mutable_list[1] = 'peach'
mutable_list.append(0.5)
mutable_list.extend(['string', True])
mutable_list.remove('string')
print(mutable_list)
print('apple' in mutable_list)