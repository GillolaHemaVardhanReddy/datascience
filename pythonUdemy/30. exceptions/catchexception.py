# syntax for try except else finally
errorName = ""
try:
    # something that might cause an exception
    pass
except errorName as errmsg:
    # do this if there were an exception with given error name 1
    pass
except errorName as errmsg:
    # do this if there were an exception with given error name 2
    pass
else:
    # do this if there were no exceptions
    pass
finally:
    # do this no matte what happens
    pass

# SOLUTIONS:

# FileNotFound
try:
    with open("a_file.txt") as file:
        file.read()
except FileNotFoundError as errmsg:
    print("there was an error: ",errmsg)

# KeyError
try:
    x = {1:"h",2:"m"}
    print(x[4])
except KeyError as errmsg:
    print(f"error is : {errmsg} is not a key")
else:
    print("we are safe there is no error")
finally:
    print("Yo i will run anyways")

# IndexError
# f = [1,2,3]
# print(f[6])

# TypeError
# text = "abc"
# print(text+5)