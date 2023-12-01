from PIL import Image
from math import sqrt

image = Image.open("sky.png")

r = 0
g = 0
b = 0

count = 0

for pixel in image.getdata():
    r += pixel[0] / 255
    g += pixel[1] / 255
    b += pixel[2] / 255
    count += 1

r /= count
g /= count
b /= count

# By calculus, one can prove that the closest (by the Euclidean metric) gray
# color will be the average of the three color channels
avg = (r + g + b) / 3

print("Sky color:", (r, g, b))
print("Closest gray:", (avg, avg, avg))
print("Distance:", sqrt((r - avg) ** 2 + (g - avg) ** 2 + (b - avg) ** 2))
