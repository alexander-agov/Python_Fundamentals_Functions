import math


def closest_point_to_center ():
    x1 = float ( input () )
    y1 = float ( input () )
    x2 = float ( input () )
    y2 = float ( input () )

    distance1 = math.sqrt (x1 * x1 + y1 * y1)
    distance2 = math.sqrt (x2 * x2 + y2 * y2)

    if distance1 <= distance2:
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")


closest_point_to_center()