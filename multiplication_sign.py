def determine_product_sign(num1, num2, num3):
    negativesCount = 0
    if num1 < 0:
        negativesCount += 1
    if num2 < 0:
        negativesCount += 1
    if num3 < 0:
        negativesCount += 1
    if negativesCount % 2 == 0 and num1 * num2 * num3 !=0:
        return "positive"
    elif negativesCount % 2 != 0 and num1 * num2 * num3 != 0:
        return "negative"
    else:
        return "zero"


num1 = int(input())
num2 = int(input())
num3 = int(input())
product_sign = determine_product_sign(num1, num2, num3)
print(product_sign)

