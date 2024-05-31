sequence = input().split()
min_number = min(list(map(int, sequence)))
max_number = max(list(map(int, sequence)))
sum_numbers = sum(list(map(int, sequence)))

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
