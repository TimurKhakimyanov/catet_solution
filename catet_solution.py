#code to calculate the lengths of the legs and the hypotenuse of a triangle
#values are entered in order a then b then C
#if the value is unknown and you need to find it, enter 0 instead
#July 2020 

#код для вычисления катетов и гипотенузы прямоугольного треугольника
#значения вводятся в порядке а потом b потом с
#если значение неизвестно и его и нужно найти вместо него вводится 0
#Июль 2020 год 


from math import sqrt
a = 0
b = 0
c = 0


a = int(input())
b = int(input())
c = int(input())

if a == 0:
    c = c*c
    b = b*b
    a = c - b
    a = pow(a,0.5)
    print("катет а равен" , a)
if b == 0:
    c = c*c
    a = a*a
    b = c - a
    b = pow(b,0.5)
    print("катет b равен" , b)
if c == 0:
    a = a*a
    b = b*b
    c = a + b
    c = pow(c,0.5)
    print ("гипотенуза с равна" , c)
    
