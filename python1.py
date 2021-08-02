#!/usr/bin/python3

import sys

# list = [1,2,3,4]
# it = iter(list)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

def fibonacci(n):
    a, b, counter = 0,1,0
    while True:
        if counter > n:
            return 
        yield a
        a, b = b, a+b
        counter += 1

if __name__ == "__main__":
    # myclass = MyNumbers()
    # myiter = iter(myclass)
    # # print(next(myiter))
    # # print(next(myiter))
    # # print(next(myiter))
    # # print(next(myiter))
    # # print(next(myiter))
    # for x in myiter:
    #     print(x)
    f = fibonacci(10)
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()