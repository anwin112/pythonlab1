
#1(1) Declare a python datatype list and do the following:
#(a) Write a Python program to sum all the items of the list.
#(b) Write a Python program to multiply all the items.
#(c) Write a Python program to get the largest number from a list.
#(d) Write a Python program to get the smallest number from a list.

l1=[1,2,3,4,5]
sum=0
#a
for i in range(0,len(l1)):
    sum+=l1[i]
print("the sum of digits is",sum)

#b
mul=1
for i in range(0,len(l1)):
    mul*=l1[i]
print("the product of digits is",mul)

#c
l1.sort()
print("largest element is",l1[-1])

#d
print("smallest element is",l1[0])