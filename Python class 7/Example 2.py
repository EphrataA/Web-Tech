def announce(f):
    def wrapper(name):
        print("About to run the function")
        name=name.upper()
        f(name)
        print("Done running the function")
    return wrapper

@announce
def hello_func(*name):
    for single in name:
       print(f'hello {name}')

hello_func('hanna','abel','robert','alex')