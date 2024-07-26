def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def calculator(x,y,func):
    return func(x,y)

print(calculator(2,3,multiply))

# the above thing is known as higher order functions
# higher order function is a function that can work with another functions
# in above case calculator is higher order function