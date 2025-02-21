import math

degree = float(input())
radian = math.radians(degree)
print(round(radian, 6))

height = float(input())
base1 = float(input())
base2 = float(input())
trapezoid_area = ((base1 + base2) / 2) * height
print(trapezoid_area)

num_sides = int(input())
side_length = float(input())
polygon_area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print(polygon_area)

base = float(input())
height = float(input())
parallelogram_area = base * height
print(parallelogram_area)
