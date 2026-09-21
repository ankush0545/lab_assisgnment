

def change_string(s: str):
    s = 'x' + s[1:]
    print(s)
    return s

s1="Hello"
if s1 != change_string(s1):
    print("Original string is modified")       
else:
    print("Original string is not modified")