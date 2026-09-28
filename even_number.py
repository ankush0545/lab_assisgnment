def even_numbers(limit):
    for num in range(2, limit + 1, 2):
        yield num


for num in even_numbers(10):
    print(num)