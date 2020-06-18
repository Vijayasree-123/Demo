#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1.simple calculator
a=float(input("value of a"))
b=float(input("value of b"))
print("addition of the two numbers=",a+b)
print("substraction of the two numbers=",a-b)
print("multiplication of the two numbers=",a*b)
print("division of  the two numbers=",a/b)
print("modulus of the two numbers=",a%b)
print("exponential of the two numbers=",a**b)
print("floor division of the two numbers=",a//b)


# In[4]:


#2.simple interest
P=float(input("enter the principle amount"))
T=float(input("enter the time"))
R=float(input("enter rate of interest"))
SI=(P*T*R)/100
print("simple interest=",SI)


# In[6]:


#3.Area of circle
r=float(input("enter the radius of the circle "))
a=(22/7)*r**2
print("Area of circle is",a)


# In[7]:


#4.Area of Triangle
a=float(input("enter first side of the triangle"))
b=float(input("enter second side of the triangle"))
c=float(input("enter third side of the triangle"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("the area of the triangle is",area)


# In[8]:


#5.Celsius to fahrenheit
c=float(input("enter temperature in celsius"))
f=(c*9/5)+32
print("temperature in fahrenheit is",f)


# In[9]:


#6.Area of rectangle
l=float(input("enter the length of rectangle"))
b=float(input("enter the breadth of rectangle"))
a=l*b
print("the area of rectangle is",a)


# In[10]:


#7.Perimeter of square
s=float(input("enter the side of the square"))
a=4*s
print("Perimeter of the square is",a)


# In[11]:


#8.Circumference of a circle
r=float(input("enter the radius of the circle"))
c=2*(22/7)*r
print("circumference of the circle is",c)


# In[12]:


#9.swapping of two numbers
a=float (input("value of a"))
b=float(input("value of b"))
temp,a=a,b
b=temp
print("the value of a after swapping=",a)
print("the value of b after swapping=",b)


# In[ ]:




