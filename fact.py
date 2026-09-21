
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

num=int(input("Enter a number: ")) 
print("The factorial of", num, "is:", fact(num))