
def is_even(n):
    return n % 2 == 0


even_number = list(filter(is_even, map(int, input().split(' '))))
print(even_number)
