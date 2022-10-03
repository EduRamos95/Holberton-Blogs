"""
Module ex_immutable
contains example of a immutable object
"""

tuple_1 = (1, 2, 3)
print("tuple_1 : {} and id: {}".format(tuple_1, id(tuple_1)))
tuple_1 = list(tuple_1)
# modify tuple_1
tuple_1[0] = 5
# id should'nt be the same
tuple_1 = tuple(tuple_1)
print("tuple_1 : {} and id: {}".format(tuple_1, id(tuple_1)))
