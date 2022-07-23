# # request number of registered user
# # input student name and age

# name = str(input('insert your name'))
# age= int(input('insert age'))

# #positional args
# #keyword args
# #default args
# 

# def display(user_name:str,user_age:int):
#     print(f'hello{user_name} and age is:{user_age}')

#     display(name,user_age = age)

#1, displayname uppercase
#2, caculate age
#3, avg mark
#4, pass/fail
#introduction
#function user log in
#cost


def greet(*names):
    """ this function greets all the person in the names tuple."""
    # names is tuple with arguments
    for name in names:
        print("hello", name)

greet("racheal","monica","phoebe","chandler","joey","ross")