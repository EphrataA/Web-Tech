list_of_names = ['alex','dave','abel','hanna']
list_of_nick_name = ['al','d','ab','h']


for single_element,single_nick_name in zip(list_of_names,list_of_nick_name):
    print(f'{list_of_names[single_element]} nickname is {list_of_nick_name}')