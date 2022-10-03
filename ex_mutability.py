"""
Module ex_mutability
contains an example of how mutable and immutable
objects are passed as arguments to a function
"""

def func_mutability(a, b):
    a = 10
    b[0] = 10
    print("in function -------------------------------")
    print("value 'a' is: {} and id: {}".format(a,id(a)))
    print("value 'b' is: {} and id: {}".format(b,id(b)))
    print("out function ------------------------------")

# x is integer / immutable
x = 5
# y is list / mutable
y = [5]
print("value 'x' is: {} and id: {}".format(x,id(x)))
print("value 'y' is: {} and id: {}".format(y,id(y)))
func_mutability(x, y)
print("value 'x' is: {} and id: {}".format(x,id(x)))
print("value 'y' is: {} and id: {}".format(y,id(y)))
