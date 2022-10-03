"""
Module ex_im-mu_table
contains example of an exception of immutable and mutable object
"""

list_1 = [1, 2, 3]
tuple_1 = ("Holberton", list_1)
print("tuple_1 : {} and id: {}".format(tuple_1, id(tuple_1)))
# modify element of tuple_1
list_1[0] = 5
# id should be the same for exception
print("tuple_1 : {} and id: {}".format(tuple_1, id(tuple_1)))
