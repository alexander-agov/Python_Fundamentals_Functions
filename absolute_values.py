number_list = input().split()
absolute_values = []
for number in number_list:
    absolute_values.append(abs(float(number)))
# absolute_values = [abs(float(number)) for number in number_list]
print(absolute_values)