# add = 777

# def make_pizza(size, *toppings):
#     """打印顾客点的所有配料"""
#     print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- "+topping)


# def build_profile(first, last, **user_info):
#     # global add
#     print(add)
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# # make_pizza(16, "pepperoni")
# # make_pizza(12, "mushrooms", "green peppers", "extra cheese")
# user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
# print(user_profile)
# print(add)

class revealAccess:
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val

    def __set__(self, obj, val):
        print("updating", self.name)
        self.val = val

class MyClass:
    x = revealAccess(10, 'val "x"')
    y = 5

m = MyClass()
print(m.x)
m.x = 20
print(m.x)
print(m.y)


