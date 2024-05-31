def get_result(type_is):
    if type_is == "int":
        number = int(input())
        return number * 2
    elif type_is == "real":
        number = float(input())
        result = number * 1.5
        return f'{result:.2f}'
    elif type_is == "string":
        text = input()
        return f"${text}$"


any_type = input()
print(get_result(any_type))
