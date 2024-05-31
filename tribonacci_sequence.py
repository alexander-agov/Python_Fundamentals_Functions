def print_tribonacci_sequence(num):

    if num == 1 or num == 0:
        print(1)
        return
    elif num == 2:
        print("1 1")
        return
    elif num == 3:
        print ("1 1 2")
        return

    tribonacci = [1, 1, 2]
    print("1 1 2", end=" ")

    for i in range(3, num):
        next_value = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3]
        tribonacci.append(next_value)
        print(next_value, end = " ")

    print()


number = int(input())
print_tribonacci_sequence(number)



