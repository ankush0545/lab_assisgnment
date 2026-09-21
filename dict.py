# Original dictionary
d = {"name": "Ankush", "age": 21}



def add_entry(d):
    d["course"] = "BTech"
    return d


def reassign_dict(d):
    d = {"name": "New Student", "age": 20}
    return d


print("Before:", d)

add_entry(d)
print("After add_entry():", d)

reassign_dict(d)
print("After reassign_dict():", d)