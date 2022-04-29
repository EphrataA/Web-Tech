name = input('please insert your name:')
age = int(input('please insert your age:'))
age_res = 18

if age>age_res:
    print('your ID will be printed')
elif age<age_res:
     print(f'come back after {age_res-age} years')