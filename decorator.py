
def my_decorator(func):
    def wrapper():
        print("Function run Initialized.")
        func()
        print("Function run completed.")
    return wrapper

@my_decorator
def  square(num=9):
    print(num**2)


square()  
