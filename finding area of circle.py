#area of a circle
import math
r = "radius"
def area_circle(radius):
    area =math.pi*( radius ** 2)
    return area

#area of rectangle
def area_rectangle(width,length):
    area = length * width
    return area

#area of square
def area_square(width):
    area = width * width
    return area

#area of triangle
def area_triangle(height, base):
    area = 1/2 * height * base
    return area

if __name__ == "__main__":
    print("Area module")
    print("Area of a circle with a radius of 10" , area_circle(10))
    print("Area of a square 10", area_square(10))
    print("Area of a triangle 10,10", area_triangle())