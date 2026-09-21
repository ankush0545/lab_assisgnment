
def remove_lst(lst:list):

    return lst[0:len(lst)-1]

lst=[1, 2, 3, 4, 5]
if lst != remove_lst(lst):
    print("Original list is modified")
else:
    print("Original list is not modified")
