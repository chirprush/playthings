from math import degrees, cos, sin

for i in range(360):
    print(i, cos(degrees(i)), sin(degrees(i)), sep=", ")
