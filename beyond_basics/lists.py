"""
Using zip builtin function to iterate multiple lists.

If one list is bigger than other, it will iterate only through the smaller one size.
"""
list_1 = ['a', 'b', 'c', 'd', 'e', 'f']
list_2 = [1, 2, 3]

for item_list_1, item_list_2 in zip(list_1, list_2):
    print("Item list 1: %s refers to Item list 2: %s" % (item_list_1, item_list_2))