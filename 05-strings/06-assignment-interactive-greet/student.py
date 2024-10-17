def interactive_greet():
    name = input("What is your name? ") 
    print(greet(name))

def greet(name):
    return f"Hello, {name}!"