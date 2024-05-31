import math

def calculate_distance(x, y):
    return math.sqrt(x * x + y * y)


def calculate_distance_four(x1, y1, x2, y2):
    return math.sqrt ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) )


def print_line(x1, y1, x2, y2):
    if (calculate_distance(x1, y1) <= calculate_distance(x2, y2)):
        print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

length1 = calculate_distance_four(x1, y1, x2, y2)
length2 = calculate_distance_four(x3, y3, x4, y4)

if length1 >= length2:
    print_line(x1, y1, x2, y2)
else:
    print_line(x3, y3, x4, y4)
