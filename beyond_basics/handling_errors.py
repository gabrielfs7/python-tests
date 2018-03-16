"""

Try catching exception in Python

"""
try:
    a = 1
    b = "2"
    print(a + b)
except TypeError as error:
    print("Ops... Got an TypeError here! {0}".format(error))

try:
    print(c)
except NameError as error:
    print("Ops... Got an NameError here! {0} ".format(error))

"""

Can catch more than one Exception or generic ones.
 
"""
try:
    print(a / 0)
    print(c)
    print(a + b)
except (NameError, TypeError) as error:
    print("Ops... Got NameError or TypeError here! {0}".format(error))
except Exception as error:
    print("Ops... Got an Exception here! %s {0}".format(error) % type(error))