def my_decorator(func):
    def wrapper():
        print("Function run Initialized.")
        func()
        print("Function run completed.")
    return wrapper

@my_decorator
def double_result(num=5):
    print(num*2)    

double_result()