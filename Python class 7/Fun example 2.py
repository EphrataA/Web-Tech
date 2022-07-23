#user input name
#name uper case
#HELLO NAME

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    #storing function in a variable
        name=str(input("enter your name: "))
        greeting = func("Hi, I am created by a function \
        passed as an argument.")
        print(greeting)

greet(shout)
greet(whisper)
 