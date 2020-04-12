#python_version == '3.7.4'
import math
def check_valid (triangle): 
    triangle = sorted(triangle)
    a,b,c= (triangle[0]),(triangle[1]),(triangle[2])
    if a>0 and b>0 and c>0 and a+b > c:
        return("True")
    else:
        return("False")
def is_right_triangle(triangle):
    triangle = sorted(triangle)
    a,b,c= (triangle[0]),(triangle[1]),(triangle[2])
    if (a**2)+(b**2)==(c**2) or (b**2)+(c**2)==(a**2) or (a**2)+(c**2)==(b**2):
        return ("True")
    else:
        return ("False")
def perimeter (triangle):
    a,b,c= (triangle[0]),(triangle[1]),(triangle[2])
    Sum = a+b+c
    return (Sum)
def area (triangle):
    a,b,c= (triangle[0]),(triangle[1]),(triangle[2])
    p = (a+b+c)/2
    T = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return (T)





