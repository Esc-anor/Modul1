my_dict = {'Petr': 1990, 'Nekita': 1993, 'Vladimir': 1991}
print('Dict:', my_dict)
print('Existing value:', my_dict['Petr'])
print('Not existing value:', my_dict.get('Roman'))
my_dict.update({'Sahsa': 1994, 'Anna': 1996})
a = my_dict.pop('Nekita')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print(

)
my_set = {1, 2, 3, True, 'Max', 2, 3, 0.15, 1, 'Max'}
print('Set:', my_set)
my_set.update({0.19, (1, 2, 5)})
my_set.discard('Max')
print('Modified set:', my_set)
