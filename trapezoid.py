#******************************************************************************
# trapezoid.py
#******************************************************************************
# Name: Simon Mei
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):NONE
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import math

def f_of_x(x):
    if x<0:
        return (1+x)*math.cos(math.pi*x)
    else:
        return (1-x)*math.cos(math.pi*x)

a=float(input('a value: '))
b=float(input('b value: '))
n=int(input('N value: '))
d_x=(b-a)/n

area=(f_of_x(b)+f_of_x(a))/2

for i in range(1,n):
    a1=a+i*d_x
    a2=f_of_x(a1)
    area+=a2
    
area*=d_x
print(area)
