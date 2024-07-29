# to raise an exception we use "raise" keyword
# for i in range(10):
#     if i==4:
#         raise TypeError("I made it")
#     print(i)

class MyError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)

for i in range(10):
    if i==4:
        raise MyError("I made it")
    print(i)