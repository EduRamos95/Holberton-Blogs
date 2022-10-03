"""
Module ex_mutable
contains example of a mutable object
"""

list_1 = [1, 2, 3]
print("list_1 : {} and id: {}".format(list_1, id(list_1)))
# modify list_1
list_1[0] = 5
# id should be the same
print("list_1 : {} and id: {}".format(list_1, id(list_1)))
